import pya
import math
import photonics as p
import label as L
import DFG_250_constants as c
import DFG_250_structures as s
import layout_from_csv_fn as inv

from importlib import reload
reload(s)
reload(c)
reload(p)
reload(L)
reload(inv)

path = 'C:/Users/adlogan/Dropbox/Projects/Frequency Conversion/Layout/KLayout/DFG250/2021_06_11 Inv2 SHG Chip/'
path_test = path + 'Devices/'
path_array = path + 'Arrays/'

filename_full = 'DFG250_SHG_Inv2'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

top = layout.create_cell("top")

marker = layout.create_cell("marker")

expand_mod =  range(-40,31,2) #  [-40,0,40]  

array_dx = 11000*c.scale
res_wg_w = 465*c.scale


for shape in p.marker(origin, c.scale, c.res)[0]:
	marker.shapes(GaP).insert(shape)

digits = L.label_gen(c.text_spec['h'], c.text_spec['t'], c.text_spec['res'])

digit_cells = {}

for handle in digits:
    digit_cells[handle] = layout.create_cell(handle)
    for shape in digits[handle]:
        digit_cells[handle].shapes(GaP).insert(shape)
	

label_cells = {}

for tick in [-40,-30,-20,-10,0,10,20,30]:
    current_cell = layout.create_cell('label_' + str(tick));
    L.label_insert(current_cell, digit_cells, c.text_spec['d'], str(tick))
    top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans(0,False, (250000*c.scale + tick*array_dx/2), -20000*c.scale)))
    top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans(0,False, (235000*c.scale + tick*array_dx/2), 225000*c.scale)))
    label_cells[tick] = current_cell


grating_cells = {}

for lambda_type in ['1550TE','SHG']:
	grating_cells[lambda_type] = {}
	for shape_type in c.gr_spec[lambda_type]['shape']:
		filename = 'grating_' + lambda_type + '_' + shape_type
		gr_path = [lambda_type]
		gr_shape_path = [shape_type]
		if lambda_type in c.wg_spec:
			wg_path = [lambda_type]
		else:
			wg_path = ['Multi']
		
		grating = s.gr_from_spec(origin,wg_path,gr_path,gr_shape_path, angle=45)
		
		grating_cells[lambda_type][shape_type] = layout.create_cell(filename)
		
		for shape in grating[0]:
			grating_cells[lambda_type][shape_type].shapes(GaP).insert(shape)
		
		grating_cells[lambda_type][shape_type].write(path_test + filename + '.gds')
		
        
resonator_cells = {}
resonator_end_trans = {}


for expand_type in expand_mod:
    filename = 'resonator_x' + str(expand_type)
    
    (resonator, end_trans) = inv.inverse_design_v2(45, 0, 0, c.scale*expand_type, c.scale, diagonal=True)
    
    resonator_cells[expand_type] = layout.create_cell(filename)
    
    resonator_end_trans[expand_type] = end_trans
    
    for shape in resonator:
        resonator_cells[expand_type].shapes(GaP).insert(shape)
        
    resonator_end_trans[expand_type] = end_trans
    
    resonator_cells[expand_type].write(path_test + filename + '.gds')
    

resonator_cp_cells = {}

for lambda_type in grating_cells:
    resonator_cp_cells[lambda_type] = {}
    for shape_type in grating_cells[lambda_type]:
        resonator_cp_cells[lambda_type][shape_type] = {}
        
        filename = 'cp_resonator_' + lambda_type + '_' + shape_type + '_test'
        current_cell = layout.create_cell(filename)
        
        if lambda_type in c.wg_spec:
            wg_type = lambda_type;
        else:
            wg_type = 'Multi'
        
        
        w_wg = c.wg_spec[wg_type]['w']['wg']
    
        in_pt = origin;
        (shapes, last_pt) = p.waveguide(origin, 45, w_wg, (8000+12400+3000)*c.scale)
        
        out_pt = p.add(shapes, p.wg_bez_curve(last_pt, 45, -90, w_wg, 5000*c.scale, 360))[0]
        
        print(out_pt)
        
        gr_out_pt = p.add(shapes,p.waveguide(out_pt, 315, w_wg, 3000*c.scale))[0]
        
        for shape in shapes:
            current_cell.shapes(GaP).insert(shape)
           
        
        current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(2,False, in_pt.x, in_pt.y)))
        current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(3,False, gr_out_pt.x, gr_out_pt.y)))
        
        current_cell.write(path_test + filename + '.gds')
        resonator_cp_cells[lambda_type][shape_type]['test'] = current_cell
        
        
        for resonator_type in resonator_cells:
        
            filename = 'cp_resonator_' + lambda_type + '_' + shape_type + '_x' + str(resonator_type)
            current_cell = layout.create_cell(filename)
            
            w_wg = c.wg_spec[wg_type]['w']['wg']
            w_res = res_wg_w + resonator_type*c.scale
            
            #Waveguide width problem fixed, but offset problem persists, along with overlap at output and overlap/gap at input
            
            in_pt = origin;
            (shapes, last_pt) = p.waveguide(origin, 45, w_wg, 3000*c.scale)
            last_pt = p.add(shapes,p.wg_adapt(last_pt, 45, w_wg, w_res, 4000*c.scale))[0]
            res_pt = last_pt
            res_out_pt = resonator_end_trans[resonator_type]*res_pt
            
            
            last_pt = p.add(shapes,p.wg_adapt(res_out_pt, 45, w_res, w_wg, 4000*c.scale))[0]
            
            out_pt = p.add(shapes, p.wg_bez_curve(last_pt, 45, -90, w_wg, 5000*c.scale, 360))[0]
            
            gr_out_pt = p.add(shapes,p.waveguide(out_pt, 315, w_wg, 3000*c.scale))[0]
            
            for shape in shapes:
                current_cell.shapes(GaP).insert(shape)
               
            
            current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(2,False, in_pt.x, in_pt.y)))
            current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(3,False, gr_out_pt.x, gr_out_pt.y)))
            current_cell.insert(pya.CellInstArray(resonator_cells[resonator_type].cell_index(), pya.Trans(0,False, res_pt.x, res_pt.y)))
            
            current_cell.write(path_test + filename + '.gds')
            resonator_cp_cells[lambda_type][shape_type][resonator_type] = current_cell
            
            

array_cells = {}


array_num = 0;
for lambda_type in grating_cells:
    array_cells[lambda_type] = {}
    for shape_type in grating_cells[lambda_type]:
    
    
        filename = 'res_array_' + lambda_type + '_' + shape_type
        
        current_cell = layout.create_cell(filename)
        
        x_position = 0
        
        current_cell.insert(pya.CellInstArray(resonator_cp_cells[lambda_type][shape_type]['test'].cell_index(), pya.Trans(0,False, x_position*array_dx, 0)))
        x_position = x_position + 1
        current_cell.insert(pya.CellInstArray(resonator_cp_cells[lambda_type][shape_type]['test'].cell_index(), pya.Trans(0,False, x_position*array_dx, 0)))
        x_position = x_position + 1
        
        for resonator_type in expand_mod:
            current_cell.insert(pya.CellInstArray(resonator_cp_cells[lambda_type][shape_type][resonator_type].cell_index(), pya.Trans(0,False, x_position*array_dx, 0)))
            x_position = x_position + 1
            
        current_cell.insert(pya.CellInstArray(resonator_cp_cells[lambda_type][shape_type]['test'].cell_index(), pya.Trans(0,False, x_position*array_dx, 0)))
        x_position = x_position + 1
        current_cell.insert(pya.CellInstArray(resonator_cp_cells[lambda_type][shape_type]['test'].cell_index(), pya.Trans(0,False, x_position*array_dx, 0)))
        
        
        current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(0,False, x_position*array_dx, 14000*c.scale)))
        
        array_cells[lambda_type][shape_type] = current_cell
        current_cell.write(path_array + filename + '.gds')
        top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans(0,False, 0, array_num*60000*c.scale)))
        
        array_num = array_num + 1
        

top.write(path + filename_full + '.gds')        