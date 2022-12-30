import pya
import math
import label as L
import DFG_250_constants as c
#import DFG_200_constants as c
#import DFG_427_constants as c
#import GaP_SiN_125_constants as c
# import GaPSiNOx_250_constants as c
import photonics as p

from importlib import reload
reload(c)
reload(p)
reload(L)


def lr_shape_constructor(origin,wg_w, wg_r, wg_mf_w, wg_mf_L, wg_cr_w, wg_cr_L, wg_adapt_L, wg_taper_w, wg_taper_L, ring_r, ring_w, ring_d, text_h, text_d, text_num, min_d, gr_span, gr_offset, modefilter=True, res=120):
  # Variant 1 - transmission circuit wraps around ring, drop circuit is straight line. Origin is input insertion point
  # Returns a set of ring and waveguide shapes along with attachement points for grating couplers, label, and marker
  # Radius measured to inner edge of ring, center of waveguide
  # Deprecated, 2019 Mar 22
  
  
  
  #origin = pya.Point(0,0)
  pt_gr_in = origin       # LANDMARK - drop grating attachment point
  
  ring_to_wg = int(wg_cr_w/2) + ring_d + ring_w + ring_r  # distance from center of coupled waveguide to center of ring
  
  dy_in = wg_r + wg_adapt_L*2 + int(wg_cr_L/2)      # vertical distance from input waveguide insertion to center of ring
  if modefilter == True:
    dy_in = dy_in + wg_mf_L +  wg_adapt_L
  
  dy_drop = wg_adapt_L*2 + int(wg_cr_L/2)               # vertical distance from drop waveguide insertion to center of ring
  
  dy_comp = gr_offset + dy_drop - dy_in                # length imbalance between input and drop
  
  dy_comp_in = dy_comp > 0                                          # extra length applied to input side (if false, applied to drop side
  dy_comp_L = abs(dy_comp)
  
  
  
  trans_ring = pya.Trans(ring_to_wg,0)
  trans_gr = pya.Trans(gr_span,0)
  trans_label_1 = pya.Trans(max(text_d,min_d), 0)
  trans_label_2 = pya.Trans(max(text_d,min_d), -1*(min_d + text_h))
  trans_marker = pya.Trans(-1000*c.scale,4000*c.scale)
  
  pt_marker = trans_marker.trans(pt_gr_in);
  
  shapes = set()
  
  last_point = origin
  
  #### Input circuit
  last_point = p.add(shapes,p.waveguide(last_point, 90, wg_w, wg_adapt_L))
  last_point = p.add(shapes,p.wg_curve(last_point, 90, -90, wg_r, wg_w, res))
  last_point = p.add(shapes,p.waveguide(last_point, 0, wg_w, wg_adapt_L))
  
  if dy_comp_in == True:
    last_point = p.add(shapes,p.waveguide(last_point, 0, wg_w, wg_adapt_L+dy_comp_L))
  else:
    last_point = p.add(shapes,p.waveguide(last_point, 0, wg_w, wg_adapt_L))
  
  if modefilter==True:
    last_point = p.add(shapes,p.wg_adapt(last_point,0, wg_w, wg_mf_w, wg_adapt_L))
    last_point = p.add(shapes,p.waveguide(last_point, 0, wg_mf_w, wg_mf_L))
    last_point = p.add(shapes,p.wg_adapt(last_point,0, wg_mf_w, wg_cr_w, wg_adapt_L))
  else:
    last_point = p.add(shapes,p.wg_adapt(last_point,0, wg_w, wg_cr_w, wg_adapt_L))
    
  last_point = p.add(shapes,p.waveguide(last_point, 0, wg_cr_w, int(wg_cr_L/2)))
  pt_cr_in = last_point     # LANDMARK - center of input coupling region
  last_point = p.add(shapes,p.waveguide(last_point, 0, wg_cr_w, int(wg_cr_L/2)))
  last_point = p.add(shapes,p.wg_adapt(last_point, 0, wg_cr_w, wg_w, wg_adapt_L))
  last_point = p.add(shapes,p.waveguide(last_point, 0, wg_w, wg_adapt_L))
  last_point = p.add(shapes,p.wg_curve(last_point, 0, -90, wg_r, wg_w, res))
  last_point = p.add(shapes,p.waveguide(last_point, -90, wg_w, wg_adapt_L))
  
  pt_input_end = last_point
  
  # Derive other landmark points from center of input coupling region
  pt_ring_center = trans_ring.trans(pt_cr_in)   # LANDMARK - center of ring
  pt_cr_drop = trans_ring.trans(pt_ring_center) # LANDMARK - center of drop coupling region
  
  pt_label_1 = trans_label_1.trans(pt_cr_drop) # LANDMARK - label 1 attachment point
  pt_label_2 = trans_label_2.trans(pt_cr_drop) # LANDMARK - label 2 attachment point
  
  ##### Add ring
  p.add(shapes,p.ring(pt_ring_center,ring_r,ring_w,res))
  
  #### Drop port taper
  last_point = pt_cr_drop
  last_point = p.add(shapes,p.waveguide(last_point, 0, wg_cr_w, int(wg_cr_L/2)))
  last_point = p.add(shapes,p.wg_adapt(last_point, 0, wg_cr_w, wg_taper_w, wg_taper_L))
  
  ##### Drop port output circuit
  last_point = pt_cr_drop
  last_point = p.add(shapes,p.waveguide(last_point, 180, wg_cr_w, int(wg_cr_L/2)))
  last_point = p.add(shapes,p.wg_adapt(last_point, 180, wg_cr_w, wg_w, wg_adapt_L))
  if dy_comp_in == False:
    last_point = p.add(shapes,p.waveguide(last_point, 180, wg_w, wg_adapt_L+dy_comp_L))
  else:
    last_point = p.add(shapes,p.waveguide(last_point, 180, wg_w, wg_adapt_L))
  
  pt_gr_drop = last_point       # LANDMARK - drop grating attachment point
  
  pt_gr_trans = trans_gr.trans(pt_gr_drop)        # LANDMARK - trans grating attachment point
  
  p.add(shapes,p.wg_p2p_curve(pt_input_end,pt_gr_trans, 270, 180, wg_r, wg_w, res))     # Connect trans grating to waveguide
  
  
  return (shapes, (pt_gr_in,3), (pt_gr_trans,2), (pt_gr_drop,2), (pt_label_1,0), (pt_label_2,0), (pt_marker,0))
  

def lr_from_spec(origin, wg_path, ring_path, ring_cp_path, gr_path, gr_shape_path, layout_path):
  # Paths should be lists of strings that can be used in order to retrieve the target specifications
  # cp and shape paths navigate within the ring and gr specs
  # returns a tuple containing a set of shapes followed by attachment points
  # attachment points include a point followed by a rotation
  
  wg_spec = c.wg_spec
  for handle in wg_path:
    wg_spec = wg_spec[handle]
  
  ring_spec = c.ring_spec
  for handle in ring_path:
    ring_spec = ring_spec[handle]
    
  cp_spec = ring_spec['cp']
  for handle in ring_cp_path:
    cp_spec = cp_spec[handle]
  
  gr_spec = c.gr_spec
  for handle in gr_path:
    gr_spec = gr_spec[handle]
    
  shape_spec = gr_spec['shape']
  for handle in gr_shape_path:
    shape_spec = shape_spec[handle]
    
  layout_spec = c.layout_spec
  for handle in layout_path:
    layout_spec = layout_spec[handle]
    
  wg_w = wg_spec['w']['wg']
  wg_r = wg_spec['r']['std']
  wg_cr_w = wg_spec['w']['cr']
  wg_cr_L = wg_spec['L']['cr']
  wg_adapt_L = wg_spec['L']['adapt']
  wg_taper_w = 20*c.scale
  wg_taper_L = wg_spec['L']['taper']
  
  ring_r = ring_spec['r']
  ring_w = ring_spec['w']
  
  ring_d = cp_spec['d']
  
  text_h = c.text_spec['h']
  text_d = c.text_spec['d']
  text_num = 2
  
  min_d = layout_spec['min']
  gr_span = layout_spec['span']
  gr_offset = layout_spec['offset'] + shape_spec['L_total']
  
  
  if 'mf' in wg_spec:
    modefilter = True
    wg_mf_w = wg_spec['w']['mf']
    wg_mf_L = wg_spec['L']['mf']
  else:
    modefilter = False
    wg_mf_w = wg_w 
    wg_mf_L = wg_adapt_L
    
  return  lr_shape_constructor(origin,wg_w, wg_r, wg_mf_w, wg_mf_L, wg_cr_w, wg_cr_L, wg_adapt_L, wg_taper_w, wg_taper_L,\
                                                      ring_r, ring_w, ring_d, text_h, text_d, text_num, min_d, gr_span, gr_offset, modefilter, c.res)
   

def gr_from_spec(origin, wg_path, gr_path, gr_shape_path, angle=0):

  wg_spec = c.wg_spec
  for handle in wg_path:
    wg_spec = wg_spec[handle]
    
  gr_spec = c.gr_spec
  for handle in gr_path:
    gr_spec = gr_spec[handle]
    
    
  shape_spec = gr_spec['shape']
  for handle in gr_shape_path:
    shape_spec = shape_spec[handle]
    
  if 'ecc' in shape_spec:
    return p.ellipse_gc(origin, angle, shape_spec['arc'], shape_spec['theta'], shape_spec['ecc'], wg_spec['w']['wg'], [shape_spec['L']] + gr_spec['ribs'], gr_spec['gaps'], c.res)
  else:
    return p.grating_coupler_end(origin, angle, wg_spec['w']['wg'], shape_spec['w'], shape_spec['L'], [0] + gr_spec['ribs'], gr_spec['gaps'], 36)
    
    
def gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path, variant=1):

  wg_spec = c.wg_spec
  for handle in wg_path:
    wg_spec = wg_spec[handle]
  
  gr_spec = c.gr_spec
  for handle in gr_path:
    gr_spec = gr_spec[handle]
    
  shape_spec = gr_spec['shape']
  for handle in gr_shape_path:
    shape_spec = shape_spec[handle]
    
  layout_spec = c.layout_spec
  for handle in layout_path:
    layout_spec = layout_spec[handle]
      
  shapes = set()
  last_pt = origin
  pt_gr_in = origin
  
  if variant == 1:
    label_trans = pya.Trans(0,False,0,int(wg_spec['r']['std'] - c.text_spec['h']/2))
  
    last_pt = p.add(shapes, p.waveguide(last_pt, 0, wg_spec['w']['wg'], wg_spec['L']['adapt']))[0]
    last_pt = p.add(shapes, p.wg_curve(last_pt, 0, 90, wg_spec['r']['std'], wg_spec['w']['wg'], c.res))[0]
    last_pt = p.add(shapes, p.waveguide(last_pt, 90, wg_spec['w']['wg'], wg_spec['L']['adapt']))[0]
    
    if 'mf' in wg_spec['w']:
      last_pt = p.add(shapes, p.wg_adapt(last_pt, 90, wg_spec['w']['wg'], wg_spec['w']['mf'],wg_spec['L']['adapt'], 36))[0]
      last_pt = p.add(shapes, p.waveguide(last_pt, 90, wg_spec['w']['mf'], wg_spec['L']['mf']))[0]
      last_pt = p.add(shapes, p.wg_adapt(last_pt, 90, wg_spec['w']['mf'], wg_spec['w']['wg'],wg_spec['L']['adapt'], 36))[0]
    
    balance = last_pt.x + shape_spec['L_total'] + layout_spec['offset'] + wg_spec['L']['adapt']
    
    last_pt = p.add(shapes, p.waveguide(last_pt, 90, wg_spec['w']['wg'], max(0,balance)))[0]
    last_pt = p.add(shapes, p.wg_curve(last_pt, 90, 180, wg_spec['r']['std'], wg_spec['w']['wg'], c.res))[0]
    
    pt_label = label_trans.trans(last_pt) 
    
    last_pt = p.add(shapes, p.waveguide(last_pt, 270, wg_spec['w']['wg'], max(0,-balance)))[0]
    last_pt = p.add(shapes, p.waveguide(last_pt, 270, wg_spec['w']['wg'], wg_spec['L']['adapt']))[0]
    
    pt_gr_out = last_pt
    rot_gr_out = 3
      
    
  elif variant == 2:
    label_trans = pya.Trans(0,False,-1*wg_spec['r']['std'] - c.text_spec['d'],-0.5*c.text_spec['h'])
    pt_label = label_trans.trans(last_pt)
    
    if 'mf' in wg_spec['w']:
      last_pt = p.add(shapes, p.wg_adapt(last_pt, 0,  wg_spec['w']['wg'], wg_spec['w']['mf'],wg_spec['L']['adapt'], 36))[0]      
      last_pt = p.add(shapes, p.wg_curve(last_pt, 0, 90, wg_spec['r']['std'], wg_spec['w']['mf'], c.res))[0]      
      #last_pt = p.add(shapes, p.wg_bez_curve(last_pt, 0, 90, wg_spec['w']['mf'], wg_spec['L']['bz'], c.res))
      last_pt = p.add(shapes, p.wg_adapt(last_pt, 90, wg_spec['w']['mf'], wg_spec['w']['wg'],wg_spec['L']['adapt'], 36))[0]
    else:
      last_pt = p.add(shapes, p.waveguide(last_pt, 0, wg_spec['w']['wg'], wg_spec['L']['adapt']))[0]
      last_pt = p.add(shapes, p.wg_curve(last_pt, 0, 90, wg_spec['r']['std'], wg_spec['w']['wg'], c.res))[0]
      #last_pt = p.add(shapes, p.wg_bez_curve(last_pt, 0, 90, wg_spec['w']['wg'], wg_spec['L']['bz'], c.res))
      last_pt = p.add(shapes, p.waveguide(last_pt, 90, wg_spec['w']['wg'], wg_spec['L']['adapt']))[0]
    
    pt_gr_out = last_pt    
    rot_gr_out = 1
    
  return (shapes, (pt_gr_in,2), (pt_gr_out,rot_gr_out), (pt_label,0))


def coupled_ring_from_spec(origin, ring_path, ring_mod, ring_cp_path, wg_path, layout_path, layout_cp_path):
	
	path_check = [len(ring_cp_path), len(wg_path), len(layout_cp_path)]
	
	assert max(path_check)==min(path_check)
	#assert max(path_check) in [2,3]
	
	ring_spec = c.ring_spec
	for handle in ring_path:
		ring_spec = ring_spec[handle]
	
	cp_spec = [ring_spec['cp']]*len(ring_cp_path)
	
	for spec in range(len(cp_spec)):
		for handle in ring_cp_path[spec]:
			cp_spec[spec] = cp_spec[spec][handle]
	
	wg_spec = [c.wg_spec]*len(wg_path)
	for spec in range(len(wg_spec)):
		for handle in wg_path[spec]:
			wg_spec[spec] = wg_spec[spec][handle]
	
	# gr_spec = [c.gr_spec]*len(gr_path)
	# for spec in range(len(gr_spec)):
		# for handle in gr_path[spec]:
			# gr_spec[spec] = gr_spec[spec][handle]
	
	# shape_spec = [spec['shape'] for spec in gr_spec]
	# for spec in range(len(shape_spec)):
		# for handle in gr_shape_path[spec]:
			# shape_spec[spec] = shape_spec[spec][handle]
	
	layout_spec = c.layout_spec
	for handle in layout_path:
		layout_spec = layout_spec[handle]
		
	layout_cp_spec = [layout_spec['cp']]*len(layout_cp_path)
	for spec in range(len(layout_cp_spec)):
		for handle in layout_cp_path[spec]:
			layout_cp_spec[spec] = layout_cp_spec[spec][handle]
		
	return coupled_ring_constructor(origin, ring_spec,	ring_mod, cp_spec, wg_spec, layout_spec, layout_cp_spec)
			
	
def coupled_ring_constructor(origin, ring_spec,	ring_mod, cp_specs, wg_specs, layout_spec, layout_cp_specs):
	dr = 0
	dw = 0
	if ('r' in ring_mod) and ('dr' in ring_spec):
		dr = ring_mod['r']*ring_spec['dr']
	if ('w' in ring_mod) and ('dw' in ring_spec):
		dw = ring_mod['w']*ring_spec['dw']
		dr -= round(dw/2)
	
	r = ring_spec['r'] + dr
	if 'w' in ring_spec:
		w = ring_spec['w'] + dw
		shapes = p.ring(origin, r, w, c.res)[0]
	else:
		w = 0
		shapes = p.circle(origin, r, c.res)[0]
		
	shapes = p.ring(origin, r, w, c.res)[0]
	
	trans_marker = pya.Trans(layout_spec['marker'][0],layout_spec['marker'][1])
	pt_marker = trans_marker.trans(origin)
	
	trans_label_1 = pya.Trans(layout_spec['label'][0],layout_spec['label'][1])
	trans_label_2 = pya.Trans(0, round(-1.2*c.text_spec['h']))
	
	pt_label_1 = trans_label_1.trans(origin)
	pt_label_2 = trans_label_2.trans(pt_label_1)
	
	
	cp_pts = []
	
	for (cp_spec, wg_spec, layout_cp_spec) in zip(cp_specs, wg_specs, layout_cp_specs):
		
		if 'theta' in cp_spec:
			theta_1 = layout_cp_spec['theta'] - cp_spec['theta']/2
			theta_2 = layout_cp_spec['theta'] + cp_spec['theta']/2
			r_cp = r + w + cp_spec['d'] + cp_spec['w']/2
			
			
			(pt_cp_1, pt_cp_2) = p.add(shapes, p.curve_center(origin, theta_1, theta_2, r_cp, cp_spec['w'], c.res))
			
			theta_in = (90*math.ceil(theta_1/90) + 180)%360
			theta_out = (90*math.floor(theta_2/90))%360
			
			if (theta_1+180)%360 == theta_in:
				pt_cp_in = pt_cp_1
			else:
				pt_cp_in = p.add(shapes, p.wg_bez_curve(pt_cp_1, (theta_1+180)%360, theta_in - (theta_1+180)%360, cp_spec['w'], wg_spec['L']['bz'], c.res))[0]
			
			if (theta_2)%360 == theta_out:
				pt_cp_out = pt_cp_2
			else:
				pt_cp_out = p.add(shapes, p.wg_bez_curve(pt_cp_2, (theta_2)%360, theta_out - (theta_2)%360, cp_spec['w'], wg_spec['L']['bz'], c.res))[0]
			
			
		else:
			r_cp = r + w + cp_spec['d'] + cp_spec['w']/2
			trans_cp_center = pya.Trans(round(r_cp*math.cos((layout_cp_spec['theta'])*math.pi/180)),round(r_cp*math.sin((layout_cp_spec['theta'])*math.pi/180)))
			pt_cp_center = trans_cp_center.trans(origin)
			
			pt_cp_1 = p.add(shapes, p.waveguide(pt_cp_center, (layout_cp_spec['theta']+180)%360, cp_spec['w'], round(cp_spec['L']/2)))[0]
			pt_cp_2 = p.add(shapes, p.waveguide(pt_cp_center, layout_cp_spec['theta']%360, cp_spec['w'], round(cp_spec['L']/2)))[0]
			
			if layout_cp_spec['theta']%90 == 0:
				pt_cp_in = pt_cp_1
				pt_cp_out = pt_cp_2
				theta_in = (layout_cp_spec['theta']+180)%360
				theta_out = layout_cp_spec['theta']%360
			else:
				theta_in = (90*math.ceil(layout_cp_spec['theta']/90) + 180)%360
				theta_out = (90*math.floor(layout_cp_spec['theta']/90))%360
				
				pt_cp_in = p.add(shapes, p.wg_bez_curve(pt_cp_1, (layout_cp_spec['theta']+180)%360, theta_in - (layout_cp_spec['theta']+180)%360, cp_spec['w'], wg_spec['L']['bz'], c.res))[0]
				pt_cp_out = p.add(shapes, p.wg_bez_curve(pt_cp_2, (layout_cp_spec['theta'])%360, theta_out - (layout_cp_spec['theta'])%360, cp_spec['w'], wg_spec['L']['bz'], c.res))[0]
	
		
		
		
		#print(theta_in)
		#print(theta_out)
		
		if 'in' in layout_cp_spec:
		
			check_mf = (('mf' in wg_spec['w']) and ('mf' in layout_cp_spec['in']))
			
			bend = 1		#input branch works backward from ring, cw bends look ccw
			if 'curl' in layout_cp_spec['in']:
				if layout_cp_spec['in']['curl'] == 'ccw':
					bend = -1
			
			#print(bend)
			
			pt_last = pt_cp_in
			rot_last = round((theta_in%360)/90)
			
			put_mf = False
			if check_mf:
				if layout_cp_spec['in']['mf'] == rot_last:
					put_mf = True
			#print(put_mf)
			if put_mf:		# If modefilter falls in the first waveguide span, the adapters are different
				pt_last = p.add(shapes, p.wg_adapt(pt_last, theta_in, cp_spec['w'], wg_spec['w']['mf'], wg_spec['L']['adapt'],c.res))[0]
				pt_last = p.add(shapes, p.waveguide(pt_last, theta_in, wg_spec['w']['mf'], round(2*wg_spec['L']['adapt']/3),c.res))[0]
				pt_last = p.add(shapes, p.wg_adapt(pt_last, theta_in, wg_spec['w']['mf'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
				check_mf = False
			else:		# If no modefilter in first span, change waveguide width from coupling to standard
				pt_last = p.add(shapes, p.wg_adapt(pt_last, theta_in, cp_spec['w'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
			
			while rot_last != layout_cp_spec['in']['orient']:
				#print(rot_last)
				
				put_mf = False
				if check_mf:
					if layout_cp_spec['in']['mf'] == rot_last:
						put_mf = True
				
				if put_mf:
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['wg'], wg_spec['w']['mf'], wg_spec['L']['adapt'],c.res))[0]
					pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['mf'], round(2*wg_spec['L']['adapt']/3),c.res))[0]
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['mf'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
					check_mf = False
				
				loc_last = (pt_last.x, pt_last.y)
				coord = (rot_last+1)%2
				coord_dirn = 2*(((rot_last%3)==0)-0.5)
				d_delta = 0
				
				if ('pt' in layout_cp_spec['in']) and (rot_last + bend == layout_cp_spec['in']['orient']):
					d_delta = coord_dirn*(layout_cp_spec['in']['pt'][coord] - loc_last[coord]) - wg_spec['L']['bz']
				elif (rot_last in layout_cp_spec['in']['min']):
					
					d_delta = coord_dirn*(layout_cp_spec['in']['min'][rot_last] - loc_last[coord]) - wg_spec['L']['bz']
					
				if d_delta > 0:
					pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['wg'], d_delta))[0]
				
				pt_last = p.add(shapes, p.wg_bez_curve(pt_last, rot_last*90, bend*90, wg_spec['w']['wg'], wg_spec['L']['bz'], c.res))[0]
				rot_last = (rot_last + bend)%4
		
			loc_last = (pt_last.x, pt_last.y)		# last stretch before grating
			coord = (rot_last+1)%2
			coord_dirn = 2*(((rot_last%3)==0)-0.5)
			d_delta = 0
			
			if ('pt' in layout_cp_spec['in']):
				d_delta = coord_dirn*(layout_cp_spec['in']['pt'][coord] - loc_last[coord]) - wg_spec['L']['bz']
			
			if d_delta > 0:
				pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['wg'], d_delta))[0]
				
			pt_in = pt_last
			rot_in = rot_last
		
		else:		#if no input path spec exists, end with a waveguide taper
			pt_in = p.add(shapes, p.wg_adapt(pt_cp_in, theta_in, cp_spec['w'], 20*c.scale, wg_spec['L']['taper'], c.res))[0]
			rot_in = round((theta_in%360)/90)
		
		
		
		if 'out' in layout_cp_spec:
		
			check_mf = (('mf' in wg_spec['w']) and ('mf' in layout_cp_spec['out']))
			
			bend = -1		#output branch defaults to cw bends
			if 'curl' in layout_cp_spec['out']:
				if layout_cp_spec['out']['curl'] == 'ccw':
					bend = 1
			
			#print(bend)
			
			pt_last = pt_cp_out
			rot_last = round((theta_out%360)/90)
			
			put_mf = False
			if check_mf:
				if layout_cp_spec['out']['mf'] == rot_last:
					put_mf = True
					
			#print(put_mf)
			
			if put_mf:		# If modefilter falls in the first waveguide span, the adapters are different
				pt_last = p.add(shapes, p.wg_adapt(pt_last, theta_out, cp_spec['w'], wg_spec['w']['mf'], wg_spec['L']['adapt'],c.res))[0]
				pt_last = p.add(shapes, p.waveguide(pt_last, theta_out, wg_spec['w']['mf'], round(2*wg_spec['L']['adapt']/3),c.res))[0]
				pt_last = p.add(shapes, p.wg_adapt(pt_last, theta_out, wg_spec['w']['mf'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
				check_mf = False
			else:		# If no modefilter in first span, change waveguide width from coupling to standard
				pt_last = p.add(shapes, p.wg_adapt(pt_last, theta_out, cp_spec['w'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
			
			while rot_last != layout_cp_spec['out']['orient']:
				#print(rot_last)
				put_mf = False
				if check_mf:
					if layout_cp_spec['out']['mf'] == rot_last:
						put_mf = True
				
				if put_mf:
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['wg'], wg_spec['w']['mf'], wg_spec['L']['adapt'],c.res))[0]
					pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['mf'], round(2*wg_spec['L']['adapt']/3),c.res))[0]
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['mf'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
					check_mf = False
				
				loc_last = (pt_last.x, pt_last.y)
				coord = (rot_last+1)%2
				coord_dirn = 2*(((rot_last%3)==0)-0.5)
				d_delta = 0
				
				if ('pt' in layout_cp_spec['out']) and (rot_last + bend == layout_cp_spec['out']['orient']):
					d_delta = coord_dirn*(layout_cp_spec['out']['pt'][coord] - loc_last[coord]) - wg_spec['L']['bz']
				elif (rot_last in layout_cp_spec['out']['min']):
					d_delta = coord_dirn*(layout_cp_spec['out']['min'][rot_last] - loc_last[coord]) - wg_spec['L']['bz']
					
				if d_delta > 0:
					pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['wg'], d_delta))[0]
				
				pt_last = p.add(shapes, p.wg_bez_curve(pt_last, rot_last*90, bend*90, wg_spec['w']['wg'], wg_spec['L']['bz'], c.res))[0]
				rot_last = (rot_last + bend)%4
		
			loc_last = (pt_last.x, pt_last.y)		# last stretch before grating
			coord = (rot_last+1)%2
			coord_dirn = 2*(((rot_last%3)==0)-0.5)
			d_delta = 0
			
			if ('pt' in layout_cp_spec['out']):
				d_delta = coord_dirn*(layout_cp_spec['out']['pt'][coord] - loc_last[coord]) - wg_spec['L']['bz']
			
			if d_delta > 0:
				pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['wg'], d_delta))[0]
				
			pt_out = pt_last
			rot_out = rot_last
		
		else: #if no output path spec exists, end with a waveguide taper
			pt_out = p.add(shapes, p.wg_adapt(pt_cp_out, theta_out, cp_spec['w'], 20*c.scale, wg_spec['L']['taper'], c.res))[0]
			rot_out = round((theta_out%360)/90)
		
		cp_pts = cp_pts + [[(pt_in, rot_in),(pt_out,rot_out)]]
		
	
	return (shapes,cp_pts,(pt_marker,0),(pt_label_1,0),(pt_label_2,0))
	

def dir_coupler_from_spec(origin, dc_path, wg_path, layout_path, layout_cp_path):
	
	dc_spec = c.dc_spec
	for handle in dc_path:
		dc_spec = dc_spec[handle]
				
	wg_spec = c.wg_spec
	for handle in wg_path:
		wg_spec = wg_spec[handle]		

	layout_spec = c.layout_spec
	for handle in layout_path:
		layout_spec = layout_spec[handle]
		
	layout_cp_spec = layout_spec['cp']
	for handle in layout_cp_path:
		layout_cp_spec = layout_cp_spec[handle]
		
	return dir_coupler_constructor(origin, dc_spec, wg_spec, layout_spec, layout_cp_spec)
	

def dir_coupler_constructor(origin, dc_spec, wg_spec, layout_spec, layout_cp_spec):
	
	w_dc = {}
	w_dc['cis'] = dc_spec['w']
	if 'w2' in dc_spec:
		w_dc['trans']  = dc_spec['w2']
	else:
		w_dc['trans'] = w_dc['cis']

	(shapes, pt_cis_in, pt_cis_out, pt_trans_in, pt_trans_out) = p.dir_coupler_bez(origin, 0, w_dc['cis'], w_dc['trans'], dc_spec['d'], dc_spec['L'], dc_spec['offset'], c.res)
	
	
	trans_marker = pya.Trans(layout_spec['marker'][0],layout_spec['marker'][1])
	pt_marker = trans_marker.trans(origin)
	
	trans_label = pya.Trans(layout_spec['label'][0],layout_spec['label'][1])
	trans_label_2 = pya.Trans(0, round(-1.2*c.text_spec['h']))
	pt_label_1 = trans_label.trans(origin)
	pt_label_2 = trans_label_2.trans(pt_label_1)
	
	
	dc_pts = {'cis':{'in':(pt_cis_in,2), 'out':(pt_cis_out,0)}, 'trans':{'in':(pt_trans_in,2),'out':(pt_trans_out,0)}}
	
	cp_pts = {'cis':{},'trans':{}}
	
	for side in dc_pts:
		for end in dc_pts[side]:
			
			pt_last = dc_pts[side][end][0]
			rot_last = dc_pts[side][end][1]
			
			if end in layout_cp_spec[side]:
				
				bend = 1
				
				if side == 'trans':
					bend = bend*-1
				if end == 'in':
					bend = bend*-1
				if dc_spec['offset'] < 0:
					bend = bend*-1
				if 'curl' in layout_cp_spec[side][end]:
					if layout_cp_spec[side][end]['curl'] == 'in':
						bend = bend*-1
				
				check_mf = (('mf' in wg_spec['w']) and ('mf' in layout_cp_spec[side][end]))
				
				
				put_mf = False
				if check_mf:
					if layout_cp_spec[side][end]['mf'] == rot_last:
						put_mf = True
				
				if put_mf:		# If modefilter falls in the first waveguide span, the adapters are different
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, w_dc[side], wg_spec['w']['mf'], wg_spec['L']['adapt'],c.res))[0]
					pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['mf'], round(2*wg_spec['L']['adapt']/3),c.res))[0]
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['mf'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
					check_mf = False
				else:		# If no modefilter in first span, change waveguide width from coupling to standard
					pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, w_dc[side], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
					
					
				while rot_last != layout_cp_spec[side][end]['orient']:
					#print(rot_last)
					put_mf = False
					if check_mf:
						if layout_cp_spec[side][end]['mf'] == rot_last:
							put_mf = True
					
					if put_mf:
						pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['wg'], wg_spec['w']['mf'], wg_spec['L']['adapt'],c.res))[0]
						pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['mf'], round(2*wg_spec['L']['adapt']/3),c.res))[0]
						pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, wg_spec['w']['mf'], wg_spec['w']['wg'], wg_spec['L']['adapt'],c.res))[0]
						check_mf = False
					
					loc_last = (pt_last.x, pt_last.y)
					coord = (rot_last+1)%2
					coord_dirn = 2*(((rot_last%3)==0)-0.5)
					d_delta = 0
					
					if ('pt' in layout_cp_spec[side][end]) and (rot_last + bend == layout_cp_spec[side][end]['orient']):
						d_delta = coord_dirn*(layout_cp_spec[side][end]['pt'][coord] - loc_last[coord]) - wg_spec['L']['bz']
					elif (rot_last in layout_cp_spec[side][end]['min']):
						d_delta = coord_dirn*(layout_cp_spec[side][end]['min'][rot_last] - loc_last[coord]) - wg_spec['L']['bz']
					
					if d_delta > 0:
						pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['wg'], d_delta))[0]
				
					pt_last = p.add(shapes, p.wg_bez_curve(pt_last, rot_last*90, bend*90*min(1,abs(rot_last-layout_cp_spec[side][end]['orient'])), wg_spec['w']['wg'], wg_spec['L']['bz'], c.res))[0]
					
					if abs(rot_last-layout_cp_spec[side][end]['orient']) < 1:
						rot_last = layout_cp_spec[side][end]['orient']
					else:
						rot_last = (rot_last + bend)%4
		
				loc_last = (pt_last.x, pt_last.y)		# last stretch before grating
				coord = (rot_last+1)%2
				coord_dirn = 2*(((rot_last%3)==0)-0.5)
				d_delta = 0
				
				
			
				if ('pt' in layout_cp_spec[side][end]):
					d_delta = coord_dirn*(layout_cp_spec[side][end]['pt'][coord] - loc_last[coord]) - wg_spec['L']['bz']
			
				if d_delta > 0:
					pt_last = p.add(shapes, p.waveguide(pt_last, rot_last*90, wg_spec['w']['wg'], d_delta))[0]
					
				
				
			else:
				pt_last = p.add(shapes, p.wg_adapt(pt_last, rot_last*90, w_dc[side], 20*c.scale, wg_spec['L']['taper'], c.res))[0]	# no spec -> end in taper
				
			cp_pts[side][end] = (pt_last,rot_last)
	
	return (shapes, cp_pts, (pt_marker,0), (pt_label_1,0), (pt_label_2,0))


def multi_coupled_ring_constructor(origin, ring_spec, ring_mods, cp_specs, wg_spec, layout_spec):
	# Series of rings or discs all coupled to a single bus waveguide
	# Number of rings/discs given by length of array of ring mods
	
	trans_marker = pya.Trans(layout_spec['marker'][0], layout_spec['marker'][1])
	pt_marker = trans_marker.trans(origin)
	trans_label = pya.Trans(layout_spec['label'][0], layout_spec['label'][1])
	pt_label = trans_label.trans(origin)
	
	if len(ring_mods) == len(cp_specs):
		full_ring_specs = zip(ring_mods,cp_specs)	# If each ring has a different coupling spec
	else:
		full_ring_specs = zip(ring_mods,[cp_specs[0]]*len(ring_mods))	# If each ring has the same coupling spec
	
	pt_in = origin
	
	(shapes,last_point) = p.wg_adapt(pt_in,0,wg_spec['w']['wg'],cp_specs[0]['w'],wg_spec['L']['adapt'])
	
	last_angle = 0
	last_w = cp_specs[0]['w']
	angled = False
	offset = False
	for spec in full_ring_specs:
		w_wg = spec[1]['w']
		if w_wg == last_w:
			last_point = p.add(shapes,p.waveguide(last_point,last_angle,w_wg,round(0.5*wg_spec['L']['adapt'])))[0]
		else:
			last_point = p.add(shapes,p.wg_adapt(last_point,last_angle,last_w,w_wg,wg_spec['L']['adapt']))[0]
		
		last_w = w_wg
		
		dr = 0
		dw = 0
		if ('r' in spec[0]) and ('dr' in ring_spec):
			dr = spec[0]['r']*ring_spec['dr']
		if ('w' in spec[0]) and ('dw' in ring_spec):
			dw = spec[0]['w']*ring_spec['dw']
			dr -= round(dw/2)
		
		
		r = ring_spec['r'] + dr
		if 'w' in ring_spec:
			w = ring_spec['w'] + dw
			#shapes = p.ring(origin, r, w, c.res)[0]
		else:
			w = 0
			#shapes = p.circle(origin, r, c.res)[0]
		
		r_cp = r + w + spec[1]['d'] + spec[1]['w']/2
		
		theta = spec[1]['theta']
		if offset:
			theta *= -1
		if angled:
			theta *= -1
			offset = not offset
		else:
			last_point = p.add(shapes,p.waveguide(last_point,last_angle,w_wg,2*(r+w)))[0]
			
		angled = not angled
		(last_point, center_point) = p.add(shapes,p.wg_curve(last_point,last_angle,theta, r_cp, w_wg, c.res))
		
		last_angle += theta
		
		if 'w' in ring_spec:
			p.add(shapes,p.ring(center_point, r, w, c.res))
		else:
			p.add(shapes,p.circle(center_point, r, c.res))
		
	last_point = p.add(shapes,p.waveguide(last_point,last_angle,last_w,round(0.5*wg_spec['L']['adapt'])))[0]
	last_point = p.add(shapes,p.wg_adapt(last_point,last_angle,last_w,wg_spec['w']['wg'],wg_spec['L']['adapt']))[0]
	if last_angle != 90:
		last_point = p.add(shapes,p.wg_curve(last_point,last_angle,90-last_angle,wg_spec['r']['std'],wg_spec['w']['wg'],c.res))[0]
		last_point = p.add(shapes,p.waveguide(last_point,90,wg_spec['w']['wg'],round(0.5*wg_spec['L']['adapt'])))[0]
	
	pt_out = last_point
	
	return (shapes,(pt_in,2),(pt_out,1),(pt_marker,0),(pt_label,0))



def multi_coupled_ring_from_spec(origin, ring_path, ring_mods, cp_paths, wg_path, layout_path):

	ring_spec = c.ring_spec
	for handle in ring_path:
		ring_spec = ring_spec[handle]

	wg_spec = c.wg_spec
	for handle in wg_path:
		wg_spec = wg_spec[handle]
		
	layout_spec = c.layout_spec
	for handle in layout_path:
		layout_spec = layout_spec[handle]
		
	cp_specs = []
	for path in cp_paths:
		spec = ring_spec['cp']
		for handle in path:
			spec = spec[handle]
		cp_specs = cp_specs + [spec]
	
	return multi_coupled_ring_constructor(origin, ring_spec, ring_mods, cp_specs, wg_spec, layout_spec)

############################
##### BEGIN TEST BLOCK #####
############################

  
# path = 'C:/Users/adlogan/Dropbox/Frequency Conversion/Data/KLayout/Test/'
# filename = 'test'
# filename_gtest = 'gtest_1'
# filename_dctest = 'dctest_1'

# layout = pya.Layout()

# layout.dbu = 0.001/c.scale
# GaP = layout.layer(1,0)

# origin = pya.Point(0,0)

# top = layout.create_cell("top")
# gr_cell = layout.create_cell("grating")
# gtest_cell = layout.create_cell("grating_test")
# dctest_cell = layout.create_cell("dc_test")

# digits = L.label_gen(c.text_spec['h'], c.text_spec['t'], c.text_spec['res'])

# # for d in digits:
  # # print(d)

# digit_cells = {}

# for handle in digits:
  # digit_cells[handle] = layout.create_cell(handle)
  # for shape in digits[handle]:
    # digit_cells[handle].shapes(GaP).insert(shape)


# wg_path = ['600TE']
# ring_path = ['disc','r420']
# cp_paths = [['600TE','20K']]
# ring_mods = [{'r':-40},{'r':-20},{'r':0},{'r':20}]
# layout_path = ['multi_ring','disc','r420']


# shapes = multi_coupled_ring_from_spec(origin, ring_path, ring_mods, cp_paths, wg_path, layout_path)[0]

# for shape in shapes:
	# top.shapes(GaP).insert(shape)
	



# ring_spec = c.ring_spec['SHG']['3minus_5000']
# ring_mod = {'w':3}
# wg_specs = [c.wg_spec['1550TE'],c.wg_spec['775TM']]
# cp_specs = [{'w':500*c.scale,'d':220*c.scale,'theta':80}, {'w':120*c.scale,'d':150*c.scale,'theta':30}]
# layout_spec = {'label':(10000*c.scale, 10000*c.scale), 'marker':(0*c.scale,-10000*c.scale)}
# layout_cp_specs = [{'theta':180, 'in':{'orient':1, 'curl':'ccw', 'pt':(10000*c.scale,-15000*c.scale), 'min':{0:10000*c.scale,3:15000*c.scale}}, 'out':{'orient':3, 'curl':'ccw', 'min':{}}},\
					# {'theta':-40,'in':{'orient':3, 'min':{}}, 'out':{'orient':2, 'mf':3, 'min':{}}}]


# cp_ring_shapes = coupled_ring_constructor(origin, ring_spec, ring_mod, cp_specs, wg_specs, layout_spec, layout_cp_specs)[0]

# for s in cp_ring_shapes:
  # top.shapes(GaP).insert(s)



# wg_spec_dc = c.wg_spec['Multi']
# dc_spec = c.dc_spec['SHG']['sym_v1']
# layout_spec_dc = {'label':(10000*c.scale, 10000*c.scale), 'marker':(0*c.scale,-10000*c.scale)}

# layout_cp_spec_dc = {'cis':{'in':{'orient':3,'min':{}},'out':{'orient':0.5,'min':{}}},\
					# 'trans':{'in':{'orient':2,'min':{}}}}

# dc_shapes = dir_coupler_constructor(origin, dc_spec, wg_spec_dc, layout_spec_dc, layout_cp_spec_dc)[0]

# for s in dc_shapes:
	# dctest_cell.shapes(GaP).insert(s)
	




# dc_shapes = p.dir_coupler(origin, 45, 0, 200*c.scale, 100*c.scale, 10000*c.scale, 2000*c.scale, c.res)[0]

# for shape in dc_shapes:
	# dctest_cell.shapes(GaP).insert(shape)


# wg_path = ['1550TE']
# ring_path = ['SHG','v1']
# ring_cp_path = ['1-20K']
# gr_path = wg_path
# gr_shape_path = ['ell']
# layout_path = ['lr'] + ring_path + wg_path
# layout_path_2 = ['gtest'] + wg_path



# gr_shapes = gr_from_spec(origin, wg_path, gr_path, gr_shape_path)

# for s in gr_shapes[0]:
  # gr_cell.shapes(GaP).insert(s)


# (lr_shapes, pt_gr_in, pt_gr_trans, pt_gr_drop, pt_label_1, pt_label_2) = lr_from_spec(origin, wg_path, ring_path, ring_cp_path, gr_path, gr_shape_path, layout_path)


# #(lr_shapes, pt_gr_in, pt_gr_trans, pt_gr_drop, pt_label_1, pt_label_2) = lr_shape_constructor(origin, c.wg_w[wl_type]['wg'], c.wg_r[wl_type], c.wg_w[wl_type]['mf'], 6000*c.scale,\
# #                                                                                                                                                          c.wg_w[wl_type]['cr'], 2000*c.scale, 3000*c.scale, 20*c.scale, 6000*c.scale, \
# #                                                                                                                                                          c.ring_spec[wl_type]['std'][0], c.ring_spec[wl_type]['std'][1], 250*c.scale, \
# #                                                                                                                                                          c.text_h, c.text_d, 5, 1500*c.scale, c.lr_gr_offset[wl_type], True, c.res)

# for s in lr_shapes:
  # top.shapes(GaP).insert(s)


# L.label_insert(top, digit_cells, c.text_spec['d'], '13', pt_label_1[0])

# L.label_insert(top, digit_cells, c.text_spec['d'], '72', pt_label_2[0])


# top.insert(pya.CellInstArray(gr_cell.cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
# top.insert(pya.CellInstArray(gr_cell.cell_index(), pya.Trans(pt_gr_drop[1],False,pt_gr_drop[0].x,pt_gr_drop[0].y)))
# top.insert(pya.CellInstArray(gr_cell.cell_index(), pya.Trans(pt_gr_trans[1],False,pt_gr_trans[0].x,pt_gr_trans[0].y)))

# #######
# (gtest_shapes, pt_gr_in_2, pt_gr_out_2, pt_label_2) = gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path_2, 2)

# for s in gtest_shapes:
  # gtest_cell.shapes(GaP).insert(s)


# L.label_insert(gtest_cell, digit_cells, c.text_spec['d'], '1', pt_label_2[0])

# gtest_cell.insert(pya.CellInstArray(gr_cell.cell_index(), pya.Trans(pt_gr_in_2[1],False,pt_gr_in_2[0].x,pt_gr_in_2[0].y)))
# gtest_cell.insert(pya.CellInstArray(gr_cell.cell_index(), pya.Trans(pt_gr_out_2[1],False,pt_gr_out_2[0].x,pt_gr_out_2[0].y)))

	
# dctest_cell.write(path + filename_dctest + '.gds')
#top.write(path + filename + '.gds')
# gtest_cell.write(path + filename_gtest + '.gds')