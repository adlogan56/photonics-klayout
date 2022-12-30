import pya
import math
import photonics as p
import label as L
import DFG_250_constants as c
import DFG_250_structures as s

from importlib import reload
reload(s)
reload(c)
reload(p)
reload(L)

path = 'C:/Users/adlogan/Dropbox/Frequency Conversion/Data/KLayout/DFG250/2019_03_25 Structures/'
path_test = path + 'Devices/'
path_array = path + 'Arrays/'

filename_full = 'DFG250_SHG_1'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

top = layout.create_cell("top")

marker = layout.create_cell("marker")

ring_mod = {'3minus_5000':range(-20,20)}#, '2minus_2100':[0]}
stretch_mod = range(-90,30,10)

for shape in p.marker(origin, c.scale, c.res)[0]:
	marker.shapes(GaP).insert(shape)

digits = L.label_gen(c.text_spec['h'], c.text_spec['t'], c.text_spec['res'])

digit_cells = {}

for handle in digits:
  digit_cells[handle] = layout.create_cell(handle)
  for shape in digits[handle]:
    digit_cells[handle].shapes(GaP).insert(shape)
	

grating_cells = {}

for lambda_type in c.gr_spec:
	grating_cells[lambda_type] = {}
	for shape_type in c.gr_spec[lambda_type]['shape']:
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

resonator_cells = {}

for len_type in stretch_mod:
	filename = 'resonator_L' + str(len_type)
	
	resonator_cells[len_type] = layout.create_cell(filename)
	
	resonator = p.inverse_design_v1(45, 0, len_type*c.scale, 0, c.scale)
	
	for shape in resonator:
		resonator_cells[len_type].shapes(GaP).insert(shape)
	
	resonator_cells[len_type].write(path_test + filename + '.gds')

cp_ring_cells = {}
cp_ring_cell_pts = {}

for ring_type in ring_mod:
	cp_ring_cells[ring_type] = {}
	cp_ring_cell_pts[ring_type] = {}
	ring_path = ['SHG',ring_type]
	wg_path = [['1550TE'],['775TM']]
	layout_path = ['cp_ring','SHG',ring_type]
	layout_cp_path = [['std','1550TE'],['std','775TM']]
	for cp_type in c.ring_spec['SHG'][ring_type]['cp']['1550TE']:
		cp_ring_cells[ring_type][cp_type] = {}
		cp_ring_cell_pts[ring_type][cp_type] = {}
		ring_cp_path = [['1550TE',cp_type],['775TM',cp_type]]
		for mod_type in ring_mod[ring_type]:
			filename = 'cpring_' + ring_type + '_c' + cp_type + '_w' + str(mod_type)
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


dc_cells = {}
dc_cell_pts = {}

for dc_type in c.layout_spec['dc']['SHG']['sym_v1']['cp']:	
	wg_path = ['Multi']
	dc_path = ['SHG','sym_v1']
	layout_path = ['dc','SHG','sym_v1']
	
	if dc_type == 'test':
		filename = 'dc_SHG_sym_v1_test'
		dc_cells[dc_type] = layout.create_cell(filename)
		current_cell = dc_cells[dc_type]
		
		layout_cp_path = ['test']
		(shapes, cp_pts, pt_marker, pt_label_1, pt_label_2) = s.dir_coupler_from_spec(origin, dc_path, wg_path, layout_path, layout_cp_path)
		
		for shape in shapes:
			current_cell.shapes(GaP).insert(shape)
			
		current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
		L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.gr_spec['SHG']['label'], pt_label_1[0])
		
		for side in cp_pts:
			for end in cp_pts[side]:
				current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts[side][end][1],False,cp_pts[side][end][0].x,cp_pts[side][end][0].y)))
		
		current_cell.write(path_test + filename + '.gds')
		dc_cell_pts[dc_type] = pt_label_2[0]
		
	elif dc_type == 'resonator':
		
		dc_cells[dc_type] = {}
		dc_cell_pts[dc_type] = {}
		
		for cp_type in c.layout_spec['dc']['SHG']['sym_v1']['cp'][dc_type]:
			dc_cells[dc_type][cp_type] = {}
			dc_cell_pts[dc_type][cp_type] = {}
			
			for len_type in resonator_cells:
				layout_cp_path = [dc_type,cp_type]
				
				dc_cells[dc_type][cp_type][len_type] = {}
				dc_cell_pts[dc_type][cp_type][len_type] = {}
				
				filename = 'dc_SHG_sym_v1_' + dc_type + '_' + cp_type + '_L' + str(len_type)
				dc_cells[dc_type][cp_type][len_type] = layout.create_cell(filename)
				
				current_cell = dc_cells[dc_type][cp_type][len_type]
				
				(shapes, cp_pts, pt_marker, pt_label_1, pt_label_2) = s.dir_coupler_from_spec(origin, dc_path, wg_path, layout_path, layout_cp_path)
				
				
				pt_res = p.add(shapes,p.wg_adapt(cp_pts['cis']['out'][0], 45, c.wg_spec['Multi']['w']['wg'], 465*c.scale, c.wg_spec['Multi']['L']['adapt'],c.res))[0]
				
				for shape in shapes:
					current_cell.shapes(GaP).insert(shape)
			
				current_cell.insert(pya.CellInstArray(resonator_cells[len_type].cell_index(), pya.Trans(0, False, pt_res.x, pt_res.y)))
				
				current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
				L.label_insert(current_cell, digit_cells, c.text_spec['d'], '490', pt_label_1[0])
				
				current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts['cis']['in'][1],False,cp_pts['cis']['in'][0].x,cp_pts['cis']['in'][0].y)))
				current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts['trans']['in'][1],False,cp_pts['trans']['in'][0].x,cp_pts['trans']['in'][0].y)))
				
				if cp_type == 'grating':
					current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts['trans']['out'][1],False,cp_pts['trans']['out'][0].x,cp_pts['trans']['out'][0].y)))
				
				current_cell.write(path_test + filename + '.gds')
				dc_cell_pts[dc_type][cp_type][len_type] = pt_label_2[0]


	
# lr_cells = {}
# lr_cell_pts = {}

# for lambda_type in c.ring_spec:
	# if lambda_type not in lr_cells:
		# lr_cells[lambda_type] = {}
		# lr_cell_pts[lambda_type] = {}
		
	# if lambda_type in c.wg_spec:	#Single WL loss rings
		# wg_path = [lambda_type]
		# gr_path = [lambda_type]
		# gr_shape_path = ['ell']
		
		# layout_path = ['lr',lambda_type]
		
		# for ring_type in c.ring_spec[lambda_type]:
			# if ring_type not in lr_cells[lambda_type]:
				# lr_cells[lambda_type][ring_type] = {}
				# lr_cell_pts[lambda_type][ring_type] = {}
			# ring_path = [lambda_type,ring_type]
			# for couple_type in c.ring_spec[lambda_type][ring_type]['cp']:
				# filename = 'lr_' + lambda_type + '_' + ring_type + '_c' + couple_type
				# ring_cp_path = [couple_type]
			
				# lr_cells[lambda_type][ring_type][couple_type] = layout.create_cell(filename)
				
				# current_cell = lr_cells[lambda_type][ring_type][couple_type]
				
				
				# (lr_shapes, pt_gr_in, pt_gr_trans, pt_gr_drop, pt_label_1, pt_label_2, pt_marker) = s.lr_from_spec(origin, wg_path, ring_path, ring_cp_path, gr_path, gr_shape_path, layout_path)
				
				# for shape in lr_shapes:
					# current_cell.shapes(GaP).insert(shape)
				
				# current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
				# current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_drop[1],False,pt_gr_drop[0].x,pt_gr_drop[0].y)))
				# current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_trans[1],False,pt_gr_trans[0].x,pt_gr_trans[0].y)))
				# current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
				
				# L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.ring_spec[lambda_type][ring_type]['cp'][couple_type]['label'], pt_label_1[0])
				
				# lr_cell_pts[lambda_type][ring_type][couple_type] = pt_label_2[0]
				
				# current_cell.write(path_test + filename + '.gds')
		
		
	# elif lambda_type == 'SHG':	#SHG Case
		# ring_path = ['SHG','v1']
		
		# for wl_type in c.ring_spec['SHG']['v1']['cp']:
			# if wl_type not in lr_cells['SHG']:
				# lr_cells['SHG'][wl_type] = {}
				# lr_cell_pts['SHG'][wl_type] = {}
			# gr_path = [wl_type]
			# wg_path = [wl_type]
			# gr_shape_path = ['ell']
			# layout_path = ['lr','SHG','v1',wl_type]
			
			# for couple_type in c.ring_spec['SHG']['v1']['cp'][wl_type]:
				# filename = 'lr_SHGv1_' + wl_type + '_c' + couple_type
				# ring_cp_path = [wl_type,couple_type]
				
				# lr_cells['SHG'][wl_type][couple_type] = layout.create_cell(filename)
				
				# current_cell = lr_cells['SHG'][wl_type][couple_type]
				
				# (lr_shapes, pt_gr_in, pt_gr_trans, pt_gr_drop, pt_label_1, pt_label_2, pt_marker) = s.lr_from_spec(origin, wg_path, ring_path, ring_cp_path, gr_path, gr_shape_path, layout_path)
				
				# for shape in lr_shapes:
					# current_cell.shapes(GaP).insert(shape)
				
				# current_cell.insert(pya.CellInstArray(grating_cells[wl_type]['ell'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
				# current_cell.insert(pya.CellInstArray(grating_cells[wl_type]['ell'].cell_index(), pya.Trans(pt_gr_drop[1],False,pt_gr_drop[0].x,pt_gr_drop[0].y)))
				# current_cell.insert(pya.CellInstArray(grating_cells[wl_type]['ell'].cell_index(), pya.Trans(pt_gr_trans[1],False,pt_gr_trans[0].x,pt_gr_trans[0].y)))
				# current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
				
				# L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.ring_spec['SHG']['v1']['cp'][wl_type][couple_type]['label'], pt_label_1[0])
				
				# lr_cell_pts['SHG'][wl_type][couple_type] = pt_label_2[0]
				
				# current_cell.write(path_test + filename + '.gds')
	

gtest_cells = {}
gtest_cell_pts = {}

for lambda_type in c.gr_spec:
	if lambda_type not in gtest_cells:
		gtest_cells[lambda_type] = {}
		gtest_cell_pts[lambda_type] = {}
	
	if lambda_type in c.wg_spec:
		wg_path = [lambda_type]
	else:
		wg_path = ['Multi']
	
	gr_path = [lambda_type]
	layout_path = ['gtest',lambda_type]
	
	for shape_type in c.gr_spec[lambda_type]['shape']:
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
		
	
	
	filename = 'gtest_' + lambda_type + '_hyb'
	gr_shape_path = ['ell']
		
	gtest_cells[lambda_type]['hyb'] = layout.create_cell(filename)
		
	current_cell = gtest_cells[lambda_type]['hyb']
		
	(gtest_shapes, pt_gr_in, pt_gr_out, pt_label) = s.gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path, 2)

	for shape in gtest_shapes:
		current_cell.shapes(GaP).insert(shape)

	current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['str'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
	current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_out[1],False,pt_gr_out[0].x,pt_gr_out[0].y)))
		
	gtest_cell_pts[lambda_type]['hyb'] = pt_label[0]
				
	current_cell.write(path_test + filename + '.gds')	



cp_ring_array_cells = {}
cp_label = {'10K':'0', '20K':'1', '50K':'2', '100K':'3', '200K':'4', '500K':'5', '1M':'6'}

for ring_type in cp_ring_cells:
	cp_ring_array_cells[ring_type] = {}
	
	for cp_type in cp_ring_cells[ring_type]:
		filename = 'array_cp_ring_' + ring_type + '_cp' + cp_type
		cp_ring_array_cells[ring_type][cp_type] = layout.create_cell(filename)
		
		current_array = cp_ring_array_cells[ring_type][cp_type]
		x_num = c.array_spec['cp_ring'][ring_type]['std']['x_num']
		
		for dy in range(math.ceil(len(cp_ring_cells[ring_type][cp_type])/x_num)):
			for dx in range(x_num):
				array_trans = pya.Trans(0,False,dx*c.array_spec['cp_ring'][ring_type]['std']['x'],dy*c.array_spec['cp_ring'][ring_type]['std']['y'])
				
				mod_type = ring_mod[ring_type][dx + dy*x_num]
				
				current_array.insert(pya.CellInstArray(cp_ring_cells[ring_type][cp_type][mod_type].cell_index(), array_trans))
				
				label = cp_label[cp_type] + str(dy) + str(dx)
				
				L.label_insert(current_array, digit_cells, c.text_spec['d'], label, array_trans.trans(cp_ring_cell_pts[ring_type][cp_type][mod_type]))
		
		current_array.write(path_array + filename + '.gds')
		top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))	

dc_array_cells = {}

for dc_type in dc_cells:
  
	if dc_type == 'test':
		filename = 'array_dc_test'
		dc_array_cells[dc_type] = layout.create_cell(filename)
		current_array = dc_array_cells[dc_type]
		
		
		for device in range(c.array_spec['dc'][dc_type]['rep']):
			current_array.insert(pya.CellInstArray(dc_cells[dc_type].cell_index(), pya.Trans(0,False, device*c.array_spec['dc'][dc_type]['x'], 0)))
		
		current_array.write(path_array + filename + '.gds')
		top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))	
  
	else:
		for cp_type in dc_cells[dc_type]:
			filename = 'array_dc_' + dc_type + '_' + cp_type
			dc_array_cells[dc_type] = layout.create_cell(filename)
			current_array = dc_array_cells[dc_type]
						
			
			for device in range(len(stretch_mod)):
				mod_type = stretch_mod[device]
				array_trans = pya.Trans(0,False, device*c.array_spec['dc'][dc_type]['x'], 0)
				
				current_array.insert(pya.CellInstArray(dc_cells[dc_type][cp_type][stretch_mod[device]].cell_index(), array_trans))
				L.label_insert(current_array, digit_cells, c.text_spec['d'], str(device).zfill(2), array_trans.trans(dc_cell_pts[dc_type][cp_type][mod_type]))
			
			current_array.write(path_array + filename + '.gds')
			top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))
			
  


# lr_array_cells = {}

# for ring_type in lr_cells:
	# if ring_type == 'SHG':
		# lr_array_cells[ring_type] = {}
		# for lambda_type in lr_cells[ring_type]:
			# filename = 'array_lr_SHGv1_' + lambda_type
			
			# lr_array_cells[ring_type][lambda_type] = layout.create_cell(filename)
			
			# current_cell = lr_array_cells[ring_type][lambda_type]
			
			# couple_type = list(lr_cells[ring_type][lambda_type].keys())
			
			# couple_type.sort(reverse = True)
			
			# spec = c.array_spec['lr'][ring_type]['v1'][lambda_type]
			
			
			
			# for dx in range(len(couple_type)):
			
				# lr = lr_cells[ring_type][lambda_type][couple_type[dx]]
				# pt = lr_cell_pts[ring_type][lambda_type][couple_type[dx]]
				
				# for dy in range(spec['rep']):
					# transform = pya.Trans(0,False,dx*spec['x'],dy*spec['y'])
					
					# L.label_insert(current_cell, digit_cells, c.text_spec['d'], str(dy) + str(dx), transform.trans(pt))
					
					# current_cell.insert(pya.CellInstArray(lr.cell_index(), transform))
			
			# current_cell.write(path_array + filename + '.gds')
			# top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans()))
	# else:
		# filename = 'array_lr_' + ring_type
		# lr_array_cells[ring_type] = layout.create_cell(filename)
		
		# current_cell = lr_array_cells[ring_type]
		
		# spec = c.array_spec['lr'][ring_type]
		
		# dx = 0
		
		# widths = list(lr_cells[ring_type].keys())
		# widths.sort()
		
		# for width_type in widths:
			# couples = list(lr_cells[ring_type][width_type].keys())
			# couples.sort(reverse = True)
			# for couple_type in couples:
			
				# lr = lr_cells[ring_type][width_type][couple_type]
				# pt = lr_cell_pts[ring_type][width_type][couple_type]
					
				# for dy in range(spec['rep']):
					# transform = pya.Trans(0,False,dx*spec['x'],dy*spec['y'])
					
					# L.label_insert(current_cell, digit_cells, c.text_spec['d'], str(dy) + str(dx), transform.trans(pt))
					
					# current_cell.insert(pya.CellInstArray(lr.cell_index(), transform))
				# dx += 1
		
		# current_cell.write(path_array + filename + '.gds')
		# top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans()))
		

gtest_array_cells = {}
gtest_full_arrays = {}

for gr_type in gtest_cells:
	spec = c.array_spec['gtest'][gr_type]
	filename_array = 'array_gtest_full_' + gr_type
	gtest_array_cells[gr_type] = {}
	gtest_full_arrays[gr_type] = layout.create_cell(filename_array)
	
	current_array = gtest_full_arrays[gr_type]
	
	dx = 0
	
	shape_types = list(gtest_cells[gr_type].keys())
	shape_types.sort()
	
	for shape_type in shape_types:
		filename = 'array_gtest_' + gr_type + '_' + shape_type
		
		gtest_array_cells[gr_type][shape_type] = layout.create_cell(filename)
		current_cell = gtest_array_cells[gr_type][shape_type]
		
		gtest = gtest_cells[gr_type][shape_type]
		
		L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.gr_spec[gr_type]['label'], gtest_cell_pts[gr_type][shape_type])
		
		for dy in range(spec['rep']):
			current_cell.insert(pya.CellInstArray(gtest.cell_index(), pya.Trans(0,False,dy*spec['x'],dy*spec['y'])))
		
		current_cell.write(path_array + filename + '.gds')
		
		
		current_array.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans(0,False,dx*spec['x_full'],dx*spec['y_full'])))
		
		dx += 1
		
		
	top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))
	current_array.write(path_array + filename_array + '.gds')
	
	
	

top.write(path + filename_full + '.gds')