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

path = 'C:/Users/adlogan/Dropbox/Frequency Conversion/Data/KLayout/DFG250/2019 06 22 Inv SHG Chip/'
path_test = path + 'Devices/'
path_array = path + 'Arrays/'

filename_full = 'DFG250_SHG_Inv_v2'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

top = layout.create_cell("top")

marker = layout.create_cell("marker")

stretch_mod = range(-90,50+1,10)
expand_mod = range(-10,10+1,10)


for shape in p.marker(origin, c.scale, c.res)[0]:
	marker.shapes(GaP).insert(shape)

digits = L.label_gen(c.text_spec['h'], c.text_spec['t'], c.text_spec['res'])

digit_cells = {}

for handle in digits:
  digit_cells[handle] = layout.create_cell(handle)
  for shape in digits[handle]:
    digit_cells[handle].shapes(GaP).insert(shape)
	

grating_cells = {}

for lambda_type in ['SHG']:
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
	resonator_cells[len_type] = {}
	for exp_type in expand_mod:
		filename = 'resonator_L' + str(len_type) + '_x' + str(exp_type)
		
		resonator_cells[len_type][exp_type] = layout.create_cell(filename)
		
		resonator = p.inverse_design_v1(45, 0, len_type*c.scale, exp_type*c.scale, c.scale)
		
		for shape in resonator:
			resonator_cells[len_type][exp_type].shapes(GaP).insert(shape)
		
		resonator_cells[len_type][exp_type].write(path_test + filename + '.gds')



gtest_cells = {}
gtest_cell_pts = {}

for lambda_type in ['SHG']:
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


res_test_cells = {}
res_test_cell_pts = {}

for len_type in stretch_mod:
	res_test_cells[len_type] = {}
	res_test_cell_pts[len_type] = {}
	for exp_type in expand_mod:
		filename = 'res_test_L' + str(len_type) + '_x' + str(exp_type)
		
		res_test_cells[len_type][exp_type] = layout.create_cell(filename)
		current_cell = res_test_cells[len_type][exp_type]
		
		res_test_cell_pts[len_type][exp_type] = pya.Point(6000*c.scale,0)
		
		current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(2,False,0,0)))
		
		current_point = origin
		
		(shapes, current_point) = p.waveguide(current_point,0,c.wg_spec['Multi']['w']['wg'], 2000*c.scale)
		(current_point,) = p.add(shapes, p.wg_bez_curve(current_point,0,45,c.wg_spec['Multi']['w']['wg'],c.wg_spec['Multi']['L']['bz'],100))
		(current_point,) = p.add(shapes, p.waveguide(current_point,45,c.wg_spec['Multi']['w']['wg'], 2000*c.scale))
		(current_point,) = p.add(shapes, p.wg_adapt(current_point,45,c.wg_spec['Multi']['w']['wg'], (465 + exp_type)*c.scale, c.wg_spec['Multi']['L']['adapt']))
		
		current_cell.insert(pya.CellInstArray(resonator_cells[len_type][exp_type].cell_index(), pya.Trans(0,False,current_point.x,current_point.y)))
		
		for shape in shapes:
			current_cell.shapes(GaP).insert(shape)
		
		
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
			
				current_cell.insert(pya.CellInstArray(resonator_cells[len_type][0].cell_index(), pya.Trans(0, False, pt_res.x, pt_res.y)))
				
				current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
				L.label_insert(current_cell, digit_cells, c.text_spec['d'], '490', pt_label_1[0])
				
				current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts['cis']['in'][1],False,cp_pts['cis']['in'][0].x,cp_pts['cis']['in'][0].y)))
				current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts['trans']['in'][1],False,cp_pts['trans']['in'][0].x,cp_pts['trans']['in'][0].y)))
				
				if cp_type == 'grating':
					current_cell.insert(pya.CellInstArray(grating_cells['SHG']['ell'].cell_index(), pya.Trans(cp_pts['trans']['out'][1],False,cp_pts['trans']['out'][0].x,cp_pts['trans']['out'][0].y)))
				
				current_cell.write(path_test + filename + '.gds')
				top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans()))
				dc_cell_pts[dc_type][cp_type][len_type] = pt_label_2[0]



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
	

rtest_array_cells = {}
rtest_full_array = layout.create_cell('res_test_full_array')
dy = 0

for exp_type in expand_mod:
	filename = 'res_test_array_x' + str(exp_type)
	rtest_array_cells[exp_type] = layout.create_cell(filename)
	current_cell = rtest_array_cells[exp_type]
	dx = 0
	current_cell.insert(pya.CellInstArray(marker.cell_index(),pya.Trans(0,False,-6000*c.scale,0)))
	for len_type in stretch_mod:
		current_cell.insert(pya.CellInstArray(res_test_cells[len_type][exp_type].cell_index(),pya.Trans(0,False,dx*12000*c.scale,0)))
		dx+=1
	
	current_cell.write(path_array + filename + '.gds')
	
	rtest_full_array.insert(pya.CellInstArray(current_cell.cell_index(),pya.Trans(0,False,dy*0*c.scale,dy*42000*c.scale)))
	
	dy += 1

rtest_full_array.write(path_array + 'res_test_full_array.gds')
top.insert(pya.CellInstArray(rtest_full_array.cell_index(),pya.Trans()))

	

top.write(path + filename_full + '.gds')