import pya
import math
import photonics as p
import label as L
import GaPSiNOx_250_constants as c
import DFG_250_structures as s

from importlib import reload
reload(s)
reload(c)
reload(p)
reload(L)

path = 'C:/Users/adlogan/Dropbox/Projects/Frequency Conversion/Lumerical/Projects/Photonics Design/GaP on SiN/GaP on SiN with HSQ/GaPSiNOx250_SHG1_2020_11_20/'
path_test = path + 'Devices/'
path_array = path + 'Arrays/'

filename_full = 'GaPSiNOx250_SHG1'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

top = layout.create_cell("top")

marker = layout.create_cell("marker")

Q_vis = ['16K','80K']
Q_tel = ['45K','200K']
Q_shg_nir = ['18K','56K']
Q_shg_tel = ['50K','160K']

ring_mod = {'SR003_R7770_W940':range(-40,40,4)}#[0]}#
cp_Q = {'SR003_R7770_W940':[(a,b) for a in Q_shg_tel for b in Q_shg_nir]}

cp_Q_single = {'1550TE':[(a,) for a in Q_tel], '637TM':[(a,) for a in Q_vis]}
rep_single = 5
single_type = ['1550TE','637TM']


gr_types = ['1550TE','775TM','637TM']
gr_shapes = ['ell']

for shape in p.marker(origin, c.scale, c.res)[0]:
	marker.shapes(GaP).insert(shape)

digits = L.label_gen(c.text_spec['h'], c.text_spec['t'], c.text_spec['res'])

digit_cells = {}

for handle in digits:
  digit_cells[handle] = layout.create_cell(handle)
  for shape in digits[handle]:
    digit_cells[handle].shapes(GaP).insert(shape)
	

grating_cells = {}

for lambda_type in gr_types:
	grating_cells[lambda_type] = {}
	for shape_type in gr_shapes:
		filename = 'grating_' + lambda_type + '_' + shape_type
		gr_path = [lambda_type]
		gr_shape_path = [shape_type]
		if lambda_type in c.wg_spec:
			wg_path = [lambda_type]
		else:
			wg_path = ['Multi']
		
		grating = s.gr_from_spec(origin,wg_path,gr_path,gr_shape_path)
		
		grating_cells[lambda_type][shape_type] = layout.create_cell(filename)
		
		for shape in grating[0]:
			grating_cells[lambda_type][shape_type].shapes(GaP).insert(shape)
            
		
		grating_cells[lambda_type][shape_type].write(path_test + filename + '.gds')

cp_ring_cells = {}
cp_ring_cell_pts = {}

for ring_type in ring_mod:
	cp_ring_cells[ring_type] = {}
	cp_ring_cell_pts[ring_type] = {}
	ring_path = ['SHG',ring_type]
	wg_path = [['1550TE'],['775TM']]
	layout_path = ['cp_ring','SHG',ring_type]
	layout_cp_path = [['std','1550TE'],['std','775TM']]
	for cp_type in cp_Q[ring_type]:
		cp_ring_cells[ring_type][cp_type] = {}
		cp_ring_cell_pts[ring_type][cp_type] = {}
		ring_cp_path = [['1550TE',cp_type[0]],['775TM',cp_type[1]]]
		for mod_type in ring_mod[ring_type]:
			filename = 'cpring_' + ring_type + '_ir' + cp_type[0] + '_vis' + cp_type[1] + '_w' + str(mod_type)
			cp_ring_cells[ring_type][cp_type][mod_type] = layout.create_cell(filename)
			
			current_cell = cp_ring_cells[ring_type][cp_type][mod_type]
			
			w_mod = {'w':mod_type}
			
			(shapes,cp_pts,pt_marker,pt_label_1,pt_label_2) = s.coupled_ring_from_spec(origin, ring_path, w_mod, ring_cp_path, wg_path, layout_path, layout_cp_path)
			
			for shape in shapes:
				current_cell.shapes(GaP).insert(shape)
			
			
			current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
			
			L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.ring_spec['SHG'][ring_type]['label'], pt_label_1[0])
			
			if 'in' in c.layout_spec['cp_ring']['SHG'][ring_type]['cp']['std']['1550TE']:
				current_cell.insert(pya.CellInstArray(grating_cells['1550TE']['ell'].cell_index(), pya.Trans(cp_pts[0][0][1],False,cp_pts[0][0][0].x,cp_pts[0][0][0].y)))
			if 'out' in c.layout_spec['cp_ring']['SHG'][ring_type]['cp']['std']['1550TE']:
				current_cell.insert(pya.CellInstArray(grating_cells['1550TE']['ell'].cell_index(), pya.Trans(cp_pts[0][1][1],False,cp_pts[0][1][0].x,cp_pts[0][1][0].y)))
			if 'in' in c.layout_spec['cp_ring']['SHG'][ring_type]['cp']['std']['775TM']:
				current_cell.insert(pya.CellInstArray(grating_cells['775TM']['ell'].cell_index(), pya.Trans(cp_pts[1][0][1],False,cp_pts[1][0][0].x,cp_pts[1][0][0].y)))
			if 'out' in c.layout_spec['cp_ring']['SHG'][ring_type]['cp']['std']['775TM']:
				current_cell.insert(pya.CellInstArray(grating_cells['775TM']['ell'].cell_index(), pya.Trans(cp_pts[1][1][1],False,cp_pts[1][1][0].x,cp_pts[1][1][0].y)))
			
			cp_ring_cell_pts[ring_type][cp_type][mod_type] = pt_label_2[0]
			
			current_cell.write(path_test + filename + '.gds')
			

cp_ring_single_cells = {}
cp_ring_single_cell_pts = {}


for ring_type in single_type:
	cp_ring_single_cells[ring_type] = {}
	cp_ring_single_cell_pts[ring_type] = {}
	ring_path = [ring_type,'lr_v1']
	wg_path = [[ring_type]]
	layout_path = ['cp_ring',ring_type,'lr_v1']
	layout_cp_path = [['std',ring_type]]
	for cp_type in cp_Q_single[ring_type]:
		cp_ring_single_cells[ring_type][cp_type] = {}
		cp_ring_single_cell_pts[ring_type][cp_type] = {}
		ring_cp_path = [[ring_type,cp_type[0]]]
		for mod_type in range(1):
			filename = 'cpring_' + ring_type + '_c' + cp_type[0] + '_w' + str(mod_type)
			cp_ring_single_cells[ring_type][cp_type][mod_type] = layout.create_cell(filename)
			
			current_cell = cp_ring_single_cells[ring_type][cp_type][mod_type]
			
			w_mod = {'w':mod_type}
			
			(shapes,cp_pts,pt_marker,pt_label_1,pt_label_2) = s.coupled_ring_from_spec(origin, ring_path, w_mod, ring_cp_path, wg_path, layout_path, layout_cp_path)
			
			for shape in shapes:
				current_cell.shapes(GaP).insert(shape)
			
			
			current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
			
			L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.ring_spec[ring_type]['lr_v1']['label'], pt_label_1[0])
			
			if 'in' in c.layout_spec['cp_ring'][ring_type]['lr_v1']['cp']['std'][ring_type]:
				current_cell.insert(pya.CellInstArray(grating_cells[ring_type]['ell'].cell_index(), pya.Trans(cp_pts[0][0][1],False,cp_pts[0][0][0].x,cp_pts[0][0][0].y)))
			if 'out' in c.layout_spec['cp_ring'][ring_type]['lr_v1']['cp']['std'][ring_type]:
				current_cell.insert(pya.CellInstArray(grating_cells[ring_type]['ell'].cell_index(), pya.Trans(cp_pts[0][1][1],False,cp_pts[0][1][0].x,cp_pts[0][1][0].y)))
			
			cp_ring_single_cell_pts[ring_type][cp_type][mod_type] = pt_label_2[0]
			
			current_cell.write(path_test + filename + '.gds')


gtest_cells = {}
gtest_cell_pts = {}

for lambda_type in gr_types:
	if lambda_type not in gtest_cells:
		gtest_cells[lambda_type] = {}
		gtest_cell_pts[lambda_type] = {}
	
	if lambda_type in c.wg_spec:
		wg_path = [lambda_type]
	else:
		wg_path = ['Multi']
	
	gr_path = [lambda_type]
	layout_path = ['gtest',lambda_type]
	
	for shape_type in gr_shapes:
		filename = 'gtest_' + lambda_type + '_' + shape_type
		gr_shape_path = [shape_type]
		
		gtest_cells[lambda_type][shape_type] = layout.create_cell(filename)
		
		current_cell = gtest_cells[lambda_type][shape_type]
		
		(gtest_shapes, pt_gr_in, pt_gr_out, pt_label) = s.gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path, 2)

		for shape in gtest_shapes:
			current_cell.shapes(GaP).insert(shape)

		current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
		current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(pt_gr_out[1],False,pt_gr_out[0].x,pt_gr_out[0].y)))
		
		gtest_cell_pts[lambda_type][shape_type] = pt_label[0]
				
		current_cell.write(path_test + filename + '.gds')
		
	
	
	# filename = 'gtest_' + lambda_type + '_hyb'
	# gr_shape_path = ['ell']
		
	# gtest_cells[lambda_type]['hyb'] = layout.create_cell(filename)
		
	# current_cell = gtest_cells[lambda_type]['hyb']
		
	# (gtest_shapes, pt_gr_in, pt_gr_out, pt_label) = s.gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path, 2)

	# for shape in gtest_shapes:
		# current_cell.shapes(GaP).insert(shape)

	# current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['str'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
	# current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_out[1],False,pt_gr_out[0].x,pt_gr_out[0].y)))
		
	# gtest_cell_pts[lambda_type]['hyb'] = pt_label[0]
				
	# current_cell.write(path_test + filename + '.gds')	



cp_ring_array_cells = {}
cp_label = {b:{a:str(cp_Q[b].index(a)) for a in cp_Q[b]} for b in cp_Q}



for ring_type in cp_ring_cells:
	cp_ring_array_cells[ring_type] = {}
	
	for cp_type in cp_ring_cells[ring_type]:
		filename = 'array_cp_ring_' + ring_type + '_ir' + cp_type[0] + '_nir' + cp_type[1]
		cp_ring_array_cells[ring_type][cp_type] = layout.create_cell(filename)
		
		current_array = cp_ring_array_cells[ring_type][cp_type]
		x_num = c.array_spec['cp_ring']['SHG'][ring_type]['std']['x_num']
		
		for dy in range(math.floor(len(cp_ring_cells[ring_type][cp_type])/x_num)):
			for dx in range(x_num):
				array_trans = pya.Trans(0,False,dx*c.array_spec['cp_ring']['SHG'][ring_type]['std']['x'][0]  + dy*c.array_spec['cp_ring']['SHG'][ring_type]['std']['y'][0],dx*c.array_spec['cp_ring']['SHG'][ring_type]['std']['x'][1]  + dy*c.array_spec['cp_ring']['SHG'][ring_type]['std']['y'][1])
				
				mod_type = ring_mod[ring_type][dx + dy*x_num]
				
				current_array.insert(pya.CellInstArray(cp_ring_cells[ring_type][cp_type][mod_type].cell_index(), array_trans))
				
				label = cp_label[ring_type][cp_type] + str(dy) + str(dx)
				
				L.label_insert(current_array, digit_cells, c.text_spec['d'], label, array_trans.trans(cp_ring_cell_pts[ring_type][cp_type][mod_type]))
		
		current_array.write(path_array + filename + '.gds')
		top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))


cp_ring_single_array_cells = {}
cp_label_single = {b:{a:str(cp_Q_single[b].index(a)) for a in cp_Q_single[b]} for b in cp_Q_single}

for ring_type in cp_ring_single_cells:
	cp_ring_single_array_cells[ring_type] = {}
	
	for cp_type in cp_ring_single_cells[ring_type]:
		filename = 'array_cp_ring_' + ring_type + '_c' + cp_type[0]
		cp_ring_single_array_cells[ring_type][cp_type] = layout.create_cell(filename)
		
		current_array = cp_ring_single_array_cells[ring_type][cp_type]
		x_num = c.array_spec['cp_ring'][ring_type]['lr_v1']['std']['x_num']
		
		for dy in range(math.floor(rep_single/x_num)):
			for dx in range(x_num):
				array_trans = pya.Trans(0,False,dx*c.array_spec['cp_ring'][ring_type]['lr_v1']['std']['x'][0]  + dy*c.array_spec['cp_ring'][ring_type]['lr_v1']['std']['y'][0],dx*c.array_spec['cp_ring'][ring_type]['lr_v1']['std']['x'][1]  + dy*c.array_spec['cp_ring'][ring_type]['lr_v1']['std']['y'][1])
				
				mod_type = 0
				
				current_array.insert(pya.CellInstArray(cp_ring_single_cells[ring_type][cp_type][mod_type].cell_index(), array_trans))
				
				label = cp_label_single[ring_type][cp_type] + str(dy) + str(dx)
				
				L.label_insert(current_array, digit_cells, c.text_spec['d'], label, array_trans.trans(cp_ring_single_cell_pts[ring_type][cp_type][mod_type]))
		
		current_array.write(path_array + filename + '.gds')
		top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))
		


gtest_array_cells = {}
gtest_full_arrays = {}

for gr_type in gtest_cells:
	spec = c.array_spec['gtest'][gr_type]
	filename_array = 'array_gtest_full_' + gr_type
	gtest_array_cells[gr_type] = {}
	gtest_full_arrays[gr_type] = layout.create_cell(filename_array)
	
	current_array = gtest_full_arrays[gr_type]
	
	dy = 0
	
	shape_types = list(gtest_cells[gr_type].keys())
	shape_types.sort()
	
	for shape_type in shape_types:
		filename = 'array_gtest_' + gr_type + '_' + shape_type
		
		gtest_array_cells[gr_type][shape_type] = layout.create_cell(filename)
		current_cell = gtest_array_cells[gr_type][shape_type]
		
		gtest = gtest_cells[gr_type][shape_type]
		
		L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.gr_spec[gr_type]['label'], gtest_cell_pts[gr_type][shape_type])
		
		for dx in range(spec['rep']):
			current_cell.insert(pya.CellInstArray(gtest.cell_index(), pya.Trans(0,False,dx*spec['x'][0],dx*spec['x'][1])))
		
		current_cell.write(path_array + filename + '.gds')
		
		
		current_array.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans(0,False,dy*spec['y'][0],dy*spec['y'][1])))
		
		dy += 1
		
		
	top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))
	current_array.write(path_array + filename_array + '.gds')
	
	
	

top.write(path + filename_full + '.gds')