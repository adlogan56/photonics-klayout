import pya
import math
import photonics as p
import DFG2_constants as c

def loss_ring_1_ell(width, radius, gap, TE, res):
  ## Loss-analysis two-port ring strucutre for 1550nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  if TE:
    wg_w = c.wg_1TE_w
    wg_wf = c.wg_1TE_wf
  else:
    wg_w = c.wg_1TM_w
    wg_wf = c.wg_1TM_wf
  
  wg_r = c.wg_1_r
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 2000*c.scale
  a_len = 6000*c.scale
  t_len = 10000*c.scale
  
  angle_trans = 0
  angle_couple = 140
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+25000*c.scale, 17500*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r, port_in.y)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.ellipse_gc(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len*2/3)
  (in_4, in_approach) = p.wg_adapt(in_wp_3, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_5, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = {in_1}
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  (trans1, trans_wp_1) = p.wg_curve(in_to_trans, -90, -180, wg_r, wg_w, res)
  (trans2, port_trans) = p.waveguide(trans_wp_1, 90, wg_w, a_len*2/3)
  
  shapes.add(trans1)
  shapes.add(trans2)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.waveguide(out_wp_1,90, wg_wf, a_len/2)
  (out_3, out_wp_3) = p.wg_adapt(out_wp_2, 90, wg_wf, wg_w, a_len, 40, 2)
  (out_4, out_to_couple) = p.wg_curve(out_wp_3, 90, angle_couple-90, wg_r, wg_w, res)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-3000*c.scale,wg_r-(c.text_h/2)))
  point_text = text_trans.trans(port_trans)
  
  return (shapes, port_in, port_trans, port_couple, point_marker, point_text)
  

def loss_ring_2_ell(width, radius, gap, res):
  ## Loss-analysis two-port ring strucutre for 1080nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  
  wg_w = c.wg_2TE_w
  wg_wf = c.wg_2TE_wf
  
  wg_r = c.wg_2_r
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 1500*c.scale
  a_len = 4500*c.scale
  t_len = 8000*c.scale
  
  angle_trans = 0
  angle_couple = 140
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+21000*c.scale, 15500*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r, port_in.y)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.ellipse_gc(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len*2/3)
  (in_4, in_approach) = p.wg_adapt(in_wp_3, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_5, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = {in_1}
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  (trans1, trans_wp_1) = p.wg_curve(in_to_trans, -90, -180, wg_r, wg_w, res)
  (trans2, port_trans) = p.waveguide(trans_wp_1, 90, wg_w, a_len/3)
  
  shapes.add(trans1)
  shapes.add(trans2)

  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.waveguide(out_wp_1,90, wg_wf, a_len/2) 
  (out_3, out_wp_3) = p.wg_adapt(out_wp_2, 90, wg_wf, wg_w, a_len, 40, 2)
  (out_4, out_to_couple) = p.wg_curve(out_wp_3, 90, angle_couple-90, wg_r, wg_w, res)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-3000*c.scale,wg_r-(c.text_h/2)))
  point_text = text_trans.trans(port_trans)
  
  return (shapes, port_in, port_trans, port_couple, point_marker, point_text)
  


def loss_ring_3_ell(width, radius, gap, TE, res):
  ## Loss-analysis two-port ring strucutre for 1550nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  if TE:
    wg_w = c.wg_3TE_w
    wg_wf = c.wg_3TE_wf
  else:
    wg_w = c.wg_3TM_w
    wg_wf = c.wg_3TM_wf
  
  wg_r = c.wg_3_r
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 1000*c.scale
  a_len = 2500*c.scale
  t_len = 6000*c.scale
  
  angle_trans = 0
  angle_couple = 140
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+16000*c.scale, 13000*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r*11/10, port_in.y-wg_r/10)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.ellipse_gc(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len*2/3)
  (in_4, in_approach) = p.wg_adapt(in_wp_3, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_5, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = {in_1}
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  
  
  (trans1, trans_wp_1) = p.waveguide(in_to_trans, 270, wg_w, a_len*5/4)
  (trans2, trans_wp_2) = p.wg_curve(trans_wp_1, 270, -90, wg_r, wg_w, res)
  (trans3, trans_wp_3) = p.waveguide(trans_wp_2, 180, wg_w, a_len)
  (trans4, port_trans) = p.wg_curve(trans_wp_3, 180, -90, wg_r, wg_w, res)
  
  shapes.add(trans1)
  shapes.add(trans2)
  shapes.add(trans3)
  shapes.add(trans4)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.waveguide(out_wp_1,90, wg_wf, a_len/2) 
  (out_3, out_wp_3) = p.wg_adapt(out_wp_2, 90, wg_wf, wg_w, a_len, 40, 2)
  (out_4, out_to_couple) = p.wg_curve(out_wp_3, 90, angle_couple-90, wg_r, wg_w, res)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-1000*c.scale,-wg_r-(c.text_h/2)-(a_len/2)))
  point_text = text_trans.trans(in_to_trans)
  
  return (shapes, port_in, port_trans, port_couple, point_marker, point_text)



def loss_ring_4_ell(width, radius, gap, res):
  ## Loss-analysis two-port ring strucutre for 1550nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  
  wg_w = c.wg_4TM_w
  wg_wf = c.wg_4TM_wf
  
  wg_r = c.wg_4_r
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 1000*c.scale
  a_len = 3000*c.scale
  t_len = 6000*c.scale
  
  angle_trans = 0
  angle_couple = 140
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+24000*c.scale, 15000*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r*11/10, port_in.y-wg_r/10)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.ellipse_gc(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len*2/3)
  (in_4, in_approach) = p.wg_adapt(in_wp_3, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_5, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = {in_1}
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  
  
  (trans1, trans_wp_1) = p.waveguide(in_to_trans, 270, wg_w, a_len*3)
  (trans2, trans_wp_2) = p.wg_curve(trans_wp_1, 270, -90, wg_r, wg_w, res)
  (trans3, trans_wp_3) = p.waveguide(trans_wp_2, 180, wg_w, a_len)
  (trans4, port_trans) = p.wg_curve(trans_wp_3, 180, -90, wg_r, wg_w, res)
  
  shapes.add(trans1)
  shapes.add(trans2)
  shapes.add(trans3)
  shapes.add(trans4)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.waveguide(out_wp_1,90, wg_wf, a_len/2) 
  (out_3, out_wp_3) = p.wg_adapt(out_wp_2, 90, wg_wf, wg_w, a_len, 40, 2)
  (out_4, out_to_couple) = p.wg_curve(out_wp_3, 90, angle_couple-90, wg_r, wg_w, res)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(0,-wg_r-(c.text_h/2)-(a_len/2)))
  point_text = text_trans.trans(in_to_trans)
  
  return (shapes, port_in, port_trans, port_couple, point_marker, point_text)

def loss_ring_1_ref(width, radius, gap, TE, res):
  ## Loss-analysis two-port ring strucutre for 1550nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  if TE:
    wg_w = c.wg_1TE_w
    wg_wf = c.wg_1TE_wf
  else:
    wg_w = c.wg_1TM_w
    wg_wf = c.wg_1TM_wf
  
  wg_r = c.wg_1_r
  y_w = c.y_1_w
  y_L = c.y_1_L
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 2000*c.scale
  a_len = 6000*c.scale
  t_len = 10000*c.scale
  
  angle_trans = 160
  angle_couple = 120
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+25000*c.scale, 19500*c.scale)
  port_trans = pya.Point(wg_r+wg_w+50000*c.scale, 2000*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r, port_in.y)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.grating(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len/2)
  (in_y, y_trans, y_ref) = p.junction_y(in_wp_3, 270, wg_wf, y_w, y_L)
  (in_4, in_wp_4) = p.wg_curve(y_trans, 270, 40, wg_r, wg_wf, res)
  (in_5, in_wp_5) = p.wg_curve(in_wp_4, 310, -40, wg_r, wg_wf, res)
  (in_6, in_approach) = p.wg_adapt(in_wp_5, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_7, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = in_y
  shapes.add(in_1)
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_6)
  shapes.add(in_7)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  (ref1, ref_wp_1) = p.wg_curve(y_ref, 270, -40, wg_r, wg_wf, res)
  (ref2, ref_wp_2) = p.wg_curve(ref_wp_1, 230, 40, wg_r, wg_wf, res)
  (ref3, ref_wp_3) = p.wg_adapt(ref_wp_2, 270, wg_wf, wg_w, a_len, 40, 2)
  (ref4, port_ref) = p.wg_curve(ref_wp_3, 270, -180, wg_r, wg_w, res)
  
  shapes.add(ref1)
  shapes.add(ref2)
  shapes.add(ref3)
  shapes.add(ref4)
  
  (trans1, trans_wp_1) = p.wg_curve(in_to_trans, 270, angle_trans-270, wg_r, wg_w, res)
  trans2 = p.wg_p2p_curve(trans_wp_1, port_trans, angle_trans, 90, wg_r, wg_w, res)
  
  shapes.add(trans1)
  shapes.add(trans2)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.wg_curve(out_wp_1, 90, angle_couple-90, wg_r, wg_wf, res)
  (out_3, out_wp_3) = p.waveguide(out_wp_2,angle_couple, wg_wf, a_len/2) 
  (out_4, out_to_couple) = p.wg_adapt(out_wp_3, angle_couple, wg_wf, wg_w, a_len, 40, 2)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-3000*c.scale,wg_r-(c.text_h/2)))
  point_text = text_trans.trans(port_ref)
  
  return (shapes, port_in, port_trans, port_couple, port_ref, point_marker, point_text)
  

def loss_ring_2_ref(width, radius, gap, res):
  ## Loss-analysis two-port ring strucutre for 1080nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  
  wg_w = c.wg_2TE_w
  wg_wf = c.wg_2TE_wf
  
  wg_r = c.wg_2_r
  y_w = c.y_2_w
  y_L = c.y_2_L
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 1500*c.scale
  a_len = 4500*c.scale
  t_len = 8000*c.scale
  
  angle_trans = 165
  angle_couple = 120
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+21000*c.scale, 17000*c.scale)
  port_trans = pya.Point(wg_r+wg_w+42000*c.scale, 1500*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r, port_in.y)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.grating(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len/2)
  (in_y, y_trans, y_ref) = p.junction_y(in_wp_3, 270, wg_wf, y_w, y_L)
  (in_4, in_wp_4) = p.wg_curve(y_trans, 270, 40, wg_r, wg_wf, res)
  (in_5, in_wp_5) = p.wg_curve(in_wp_4, 310, -40, wg_r, wg_wf, res)
  (in_6, in_approach) = p.wg_adapt(in_wp_5, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_7, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = in_y
  shapes.add(in_1)
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_6)
  shapes.add(in_7)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  (ref1, ref_wp_1) = p.wg_curve(y_ref, 270, -40, wg_r, wg_wf, res)
  (ref2, ref_wp_2) = p.wg_curve(ref_wp_1, 230, 40, wg_r, wg_wf, res)
  (ref3, ref_wp_3) = p.wg_adapt(ref_wp_2, 270, wg_wf, wg_w, a_len, 40, 2)
  (ref4, ref_wp_4) = p.wg_curve(ref_wp_3, 270, -180, wg_r, wg_w, res)
  (ref5, port_ref) = p.waveguide(ref_wp_4, 90, wg_w, a_len)
  
  shapes.add(ref1)
  shapes.add(ref2)
  shapes.add(ref3)
  shapes.add(ref4)
  shapes.add(ref5)
  
  (trans1, trans_wp_1) = p.wg_curve(in_to_trans, 270, angle_trans-270, wg_r, wg_w, res)
  trans2 = p.wg_p2p_curve(trans_wp_1, port_trans, angle_trans, 90, wg_r, wg_w, res)
  
  shapes.add(trans1)
  shapes.add(trans2)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.wg_curve(out_wp_1, 90, angle_couple-90, wg_r, wg_wf, res)
  (out_3, out_wp_3) = p.waveguide(out_wp_2,angle_couple, wg_wf, a_len/2) 
  (out_4, out_to_couple) = p.wg_adapt(out_wp_3, angle_couple, wg_wf, wg_w, a_len, 40, 2)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-3000*c.scale,wg_r-(c.text_h/2)))
  point_text = text_trans.trans(port_ref)
  
  return (shapes, port_in, port_trans, port_couple, port_ref, point_marker, point_text)
  


def loss_ring_3_ref(width, radius, gap, TE, res):
  ## Loss-analysis two-port ring strucutre for 1550nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  
  if TE:
    wg_w = c.wg_3TE_w
    wg_wf = c.wg_3TE_wf
  else:
    wg_w = c.wg_3TM_w
    wg_wf = c.wg_3TM_wf
  
  wg_r = c.wg_3_r
  y_w = c.y_3_w
  y_L = c.y_3_L
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 1000*c.scale
  a_len = 2500*c.scale
  t_len = 6000*c.scale
  
  angle_trans = 165
  angle_couple = 115
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+16000*c.scale, 14000*c.scale)
  port_trans = pya.Point(wg_r+wg_w+32000*c.scale, 1000*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r, port_in.y)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.grating(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len/2)
  (in_y, y_trans, y_ref) = p.junction_y(in_wp_3, 270, wg_wf, y_w, y_L)
  (in_4, in_wp_4) = p.wg_curve(y_trans, 270, 40, wg_r, wg_wf, res)
  (in_5, in_wp_5) = p.wg_curve(in_wp_4, 310, -40, wg_r, wg_wf, res)
  (in_6, in_approach) = p.wg_adapt(in_wp_5, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_7, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = in_y
  shapes.add(in_1)
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_6)
  shapes.add(in_7)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  (ref1, ref_wp_1) = p.wg_curve(y_ref, 270, -40, wg_r, wg_wf, res)
  (ref2, ref_wp_2) = p.wg_curve(ref_wp_1, 230, 40, wg_r, wg_wf, res)
  (ref3, ref_wp_3) = p.wg_adapt(ref_wp_2, 270, wg_wf, wg_w, a_len, 40, 2)
  (ref4, port_ref) = p.wg_curve(ref_wp_3, 270, -180, wg_r*5/4, wg_w, res)
  
  shapes.add(ref1)
  shapes.add(ref2)
  shapes.add(ref3)
  shapes.add(ref4)
  
  (trans1, trans_wp_1) = p.wg_curve(in_to_trans, 270, angle_trans-270, wg_r*3/2, wg_w, res)
  trans2 = p.wg_p2p_curve(trans_wp_1, port_trans, angle_trans, 90, wg_r, wg_w, res)
  
  shapes.add(trans1)
  shapes.add(trans2)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.wg_curve(out_wp_1, 90, angle_couple-90, wg_r, wg_wf, res)
  (out_3, out_wp_3) = p.waveguide(out_wp_2,angle_couple, wg_wf, a_len/2) 
  (out_4, out_to_couple) = p.wg_adapt(out_wp_3, angle_couple, wg_wf, wg_w, a_len, 40, 2)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-3000*c.scale,(wg_r*5/4)-(c.text_h/2)))
  point_text = text_trans.trans(port_ref)
  
  return (shapes, port_in, port_trans, port_couple, port_ref, point_marker, point_text)



def loss_ring_4_ref(width, radius, gap, res):
  ## Loss-analysis two-port ring strucutre for 1550nm (430nm GaP), for elliptical gratings
  ## Returns a set containing all of the shapes for the ring, coupling structures, and labels
  
  wg_w = c.wg_4TM_w
  wg_wf = c.wg_4TM_wf
  
  wg_r = c.wg_4_r
  y_w = c.y_4_w
  y_L = c.y_4_L
  
  
  # internal constants for the length of the coupling region (c),
  # adaptation length to the coupling region,
  # and the length of the taper on the drop port side
  c_len = 1000*c.scale
  a_len = 3000*c.scale
  t_len = 6000*c.scale
  
  angle_trans = 170
  angle_couple = 115
  
  
  # Define reference points; intended to keep all structures in first quadrant
  port_in = pya.Point(wg_r+wg_w+20000*c.scale, 16000*c.scale)
  port_trans = pya.Point(wg_r+wg_w+41000*c.scale, 1000*c.scale)
  port_couple = pya.Point(wg_r+wg_w, port_in.y - wg_r)
  point_marker = pya.Point(port_in.x + wg_r, port_in.y)
  
  center_trans = pya.Trans(0, False, pya.Point(0,round(1.5*width) + gap + radius))
  
  
  # Input grating structure
  #grating_in = p.grating(port_in, 180, g_arc, g_theta, g_ecc, wg_w, [g_exp] + g_ribs, g_gaps, res)
  #shapes = grating_in   # Define the shapes collection
  
  # Add a circular marker (useful for autofocus, etc)
  #mark = p.marker(point_marker, c.scale, res)
  #shapes.update(mark)
  
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, -90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, -90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, -90, wg_wf, a_len/2)
  (in_y, y_trans, y_ref) = p.junction_y(in_wp_3, 270, wg_wf, y_w, y_L)
  (in_4, in_wp_4) = p.wg_curve(y_trans, 270, 40, wg_r, wg_wf, res)
  (in_5, in_wp_5) = p.wg_curve(in_wp_4, 310, -40, wg_r, wg_wf, res)
  (in_6, in_approach) = p.wg_adapt(in_wp_5, -90, wg_wf, width, a_len, 40, 2)
  (in_c1, in_mid) = p.waveguide(in_approach, -90, width, c_len)
  (in_c2, in_depart) = p.waveguide(in_mid, -90, width, c_len)
  (in_7, in_to_trans) = p.wg_adapt(in_depart, -90, width, wg_w, a_len, 40, 2)
  
  shapes = in_y
  shapes.add(in_1)
  shapes.add(in_2)
  shapes.add(in_3)
  shapes.add(in_4)
  shapes.add(in_5)
  shapes.add(in_6)
  shapes.add(in_7)
  shapes.add(in_c1)
  shapes.add(in_c2)
  
  (ref1, ref_wp_1) = p.wg_curve(y_ref, 270, -40, wg_r, wg_wf, res)
  (ref2, ref_wp_2) = p.wg_curve(ref_wp_1, 230, 40, wg_r, wg_wf, res)
  (ref3, ref_wp_3) = p.wg_adapt(ref_wp_2, 270, wg_wf, wg_w, a_len, 40, 2)
  (ref4, port_ref) = p.wg_curve(ref_wp_3, 270, -180, wg_r*5/4, wg_w, res)
  
  shapes.add(ref1)
  shapes.add(ref2)
  shapes.add(ref3)
  shapes.add(ref4)
  
  (trans1, trans_wp_1) = p.wg_curve(in_to_trans, 270, angle_trans-270, wg_r*3/2, wg_w, res)
  trans2 = p.wg_p2p_curve(trans_wp_1, port_trans, angle_trans, 90, wg_r, wg_w, res)
  
  shapes.add(trans1)
  shapes.add(trans2)

  
  
  ring_center = center_trans.trans(in_mid)
  out_mid = center_trans.trans(ring_center)
  
  ring = p.ring(ring_center, radius, width, res)
  shapes.add(ring)
  
  (out_c1, out_depart) = p.waveguide(out_mid, 90, width, c_len)
  (out_c2, out_depart2) = p.waveguide(out_mid, -90, width, c_len)
  (out_taper, out_end) = p.wg_adapt(out_depart2, -90, width, 20*c.scale, t_len, 20, 1.5)
  (out_1, out_wp_1) = p.wg_adapt(out_depart, 90, width, wg_wf, a_len, 40, 2)
  (out_2, out_wp_2) = p.wg_curve(out_wp_1, 90, angle_couple-90, wg_r, wg_wf, res)
  (out_3, out_wp_3) = p.waveguide(out_wp_2,angle_couple, wg_wf, a_len/2) 
  (out_4, out_to_couple) = p.wg_adapt(out_wp_3, angle_couple, wg_wf, wg_w, a_len, 40, 2)
  
  shapes.add(out_1)
  shapes.add(out_2)
  shapes.add(out_3)
  shapes.add(out_4)
  shapes.add(out_c1)
  shapes.add(out_c2)
  shapes.add(out_taper)
  
  
  
  (couple_1, midpoint_couple) = p.wg_curve(port_couple,90,-180,wg_r,wg_w,res)
  con_couple  = p.wg_p2p_curve(out_to_couple, midpoint_couple, angle_couple, 90, wg_r, wg_w, res)
  
  shapes.add(couple_1)
  shapes.add(con_couple)
  
  text_trans = pya.Trans(0,False, pya.Point(-3000*c.scale,(wg_r*5/4)-(c.text_h/2)))
  point_text = text_trans.trans(port_ref)
  
  return (shapes, port_in, port_trans, port_couple, port_ref, point_marker, point_text)


def grating_loop(wl, res, TE=True):
  assert (wl in {1,2,3,4})
  if wl == 1:
    wg_r = c.wg_1_r
    port_in = pya.Point(32500*c.scale,17500*c.scale)
    a_len = 6000*c.scale
    x_len = 5000*c.scale
    if TE:
      wg_w = c.wg_1TE_w
      wg_wf = c.wg_1TE_wf
    else:
      wg_w = c.wg_1TM_w
      wg_wf = c.wg_1TM_wf
    
  elif wl == 2:
    wg_r = c.wg_2_r
    port_in = pya.Point(25500*c.scale,15500*c.scale)
    a_len = 4500*c.scale
    x_len = 4000*c.scale
    wg_w = c.wg_2TE_w
    wg_wf = c.wg_2TE_wf
  elif wl == 3:
    wg_r = c.wg_3_r*3/2
    port_in = pya.Point(21500*c.scale,11000*c.scale)
    a_len = 2500*c.scale
    x_len = 6000*c.scale
    if TE:
      wg_w = c.wg_3TE_w
      wg_wf = c.wg_3TE_wf
    else:
      wg_w = c.wg_3TM_w
      wg_wf = c.wg_3TM_wf
  else:
    wg_r = c.wg_4_r*3/2
    port_in = pya.Point(25500*c.scale,12500*c.scale)
    a_len = 3000*c.scale
    x_len = 8000*c.scale
    wg_w = c.wg_4TM_w
    wg_wf = c.wg_4TM_wf
    
  (in_1, in_wp_1) = p.wg_curve(port_in, 0, 90, wg_r, wg_w, res)
  (in_2, in_wp_2) = p.wg_adapt(in_wp_1, 90, wg_w, wg_wf, a_len, 40, 2)
  (in_3, in_wp_3) = p.waveguide(in_wp_2, 90, wg_wf, a_len/2)
  (in_4, in_wp_4) = p.wg_adapt(in_wp_3, 90, wg_wf, wg_w, a_len, 40, 2)
  (in_5, in_to_out) = p.waveguide(in_wp_4, 90, wg_w, x_len)
  (in_6, port_out) = p.wg_curve(in_to_out, 90, 180, wg_r, wg_w, res)
  
  shapes = {in_1, in_2, in_3, in_4, in_5, in_6}
  
  point_marker = pya.Point(in_to_out.x, in_to_out.y - wg_r)
  point_text = pya.Point(in_to_out.x + 3000*c.scale, in_to_out.y - wg_r - (c.text_h/2))
  
  return (shapes, port_in, port_out, point_marker, point_text)



def runout(wl, x_len, res, TE=True):
  assert (wl in {1,2,3,4})
  if wl == 1:
    wg_r = c.wg_1_r
    #wg_rb = c.wg_1_r*5/4
    port_in = pya.Point(16500*c.scale,8000*c.scale)
    a_len = 6000*c.scale
    b_len = 3500*c.scale
    c_len = 4200*c.scale
    d_len = 17000*c.scale
    e_len = 2000*c.scale
    f_len = 0;
    if TE:
      wg_w = c.wg_1TE_w
      wg_wf = c.wg_1TE_wf
    else:
      wg_w = c.wg_1TM_w
      wg_wf = c.wg_1TM_wf   
  elif wl == 2:
    wg_r = c.wg_2_r
    #wg_rb = c.wg_2_r*5/4
    port_in = pya.Point(12000*c.scale,6000*c.scale)
    a_len = 4500*c.scale
    b_len = 5500*c.scale
    c_len = 4500*c.scale
    d_len = 16000*c.scale
    e_len = 1500*c.scale
    f_len = 0;
    wg_w = c.wg_2TE_w
    wg_wf = c.wg_2TE_wf
  elif wl == 3:
    wg_r = c.wg_3_r*5/4
    #wg_rb = c.wg_3_r*3/2
    port_in = pya.Point(9000*c.scale,5000*c.scale)
    a_len = 2500*c.scale
    b_len = 7000*c.scale
    c_len = 2500*c.scale
    d_len = 17500*c.scale
    e_len = 2000*c.scale
    f_len = 5000*c.scale;
    if TE:
      wg_w = c.wg_3TE_w
      wg_wf = c.wg_3TE_wf
    else:
      wg_w = c.wg_3TM_w
      wg_wf = c.wg_3TM_wf
  else:
    wg_r = c.wg_4_r*6/5
    #wg_rb = c.wg_4_r*3/2
    port_in = pya.Point(9000*c.scale,5000*c.scale)
    a_len = 3000*c.scale
    b_len = 6000*c.scale
    c_len = 3000*c.scale
    d_len = 17000*c.scale
    e_len = 1000*c.scale
    f_len = 0;
    wg_w = c.wg_4TM_w
    wg_wf = c.wg_4TM_wf
    
  angle_curve_1 = 49
  angle_curve_2 = 30
    
  (in_1, in_wp_1) = p.wg_curve(port_in, 90, -90, wg_r, wg_w, res)
  (long_1, long_end_1) = p.waveguide(in_wp_1, 0, wg_w, x_len+d_len)
  (curve_1, curve_wp_1) = p.wg_curve(long_end_1, 0, -angle_curve_1, wg_r, wg_w, res)
  (curve_2, curve_wp_2) = p.wg_curve(curve_wp_1, -angle_curve_1, 180+2*angle_curve_1, wg_r, wg_w, res)
  (curve_3, curve_wp_3) = p.wg_curve(curve_wp_2, 180+angle_curve_1, -angle_curve_1, wg_r, wg_w, res)
  (long_2, long_end_2) = p.waveguide(curve_wp_3, 180, wg_w, x_len + d_len + e_len/2 + wg_r)
  (base_1, base_wp_1) = p.wg_curve(long_end_2, 180, 90, wg_r, wg_w, res)
  (base_2, base_wp_2) = p.wg_adapt(base_wp_1, 270,wg_w, wg_wf, a_len, 40, 2)
  (base_3, base_wp_3) = p.waveguide(base_wp_2, 270, wg_wf, a_len*4/10)
  (base_4, base_wp_4) = p.wg_adapt(base_wp_3, 270,wg_wf, wg_w, a_len, 40, 2)
  (base_5, base_wp_5) = p.waveguide(base_wp_4, 270, wg_w, b_len)
  (base_6, base_wp_6) = p.wg_curve(base_wp_5, 270, 90, wg_r, wg_w, res)
  (base_7, base_wp_7) = p.waveguide(base_wp_6, 0, wg_w, e_len)
  (base_8, base_wp_8) = p.wg_curve(base_wp_7, 0, 90, wg_r, wg_w, res)
  (base_9, base_wp_9) = p.waveguide(base_wp_8, 90, wg_w, c_len)
  (base_10, base_wp_10) = p.wg_curve(base_wp_9, 90, -90, wg_r, wg_w, res)
  (long_3, long_end_3) = p.waveguide(base_wp_10, 0, wg_w, x_len+d_len)
  (curve_4, curve_wp_4) = p.wg_curve(long_end_3, 0, angle_curve_2, wg_r, wg_w, res)
  (curve_5, curve_wp_5) = p.wg_curve(curve_wp_4, angle_curve_2, -180-2*angle_curve_2, wg_r, wg_w, res)
  (curve_6, curve_wp_6) = p.wg_curve(curve_wp_5, 180-angle_curve_2, angle_curve_2, wg_r, wg_w, res)
  (long_4, long_end_4) = p.waveguide(curve_wp_6, 180, wg_w, x_len)
  (out_1, port_out) = p.waveguide(long_end_4, 180, wg_w, f_len)
  
  
  shapes = {in_1, out_1}
  shapes.update({long_1, long_2, long_3, long_4})
  shapes.update({curve_1,curve_2,curve_3,curve_4,curve_5,curve_6})
  shapes.update({base_1,base_2,base_3,base_4,base_5,base_6,base_7,base_8,base_9,base_10})
  
  
  point_marker = pya.Point(port_in.x, port_in.y + wg_r)
  point_text_1 = pya.Point(port_in.x + c.text_h/2, port_in.y + wg_r + 3600*c.scale)
  point_text_2 = pya.Point(port_in.x + c.text_h/2, port_in.y + wg_r + 11500*c.scale)
  
  return (shapes, port_in, port_out, point_marker, point_text_1, point_text_2) 



def y_tree_forward(wl, res, TE=True, l_scale=1.0, w_scale=1.0):
  assert (wl in {1,2,3,4})
  if wl == 1:
    wg_r = c.wg_1_r
    y_w = round(c.y_1_w*w_scale)
    y_L = round(c.y_1_L*l_scale)
    port_in = pya.Point(27500*c.scale,61500*c.scale)
    a_len = 6000*c.scale
    b_len = 9000*c.scale
    c_len = 17000*c.scale
    d_len = 6000*c.scale
    if TE:
      wg_w = c.wg_1TE_w
      wg_wf = c.wg_1TE_wf
    else:
      wg_w = c.wg_1TM_w
      wg_wf = c.wg_1TM_wf
    
  elif wl == 2:
    wg_r = c.wg_2_r
    y_w = round(c.y_2_w*w_scale)
    y_L = round(c.y_2_L*l_scale)
    port_in = pya.Point(24000*c.scale,50500*c.scale)
    a_len = 4500*c.scale
    b_len = 9000*c.scale
    c_len = 15000*c.scale
    d_len = 7000*c.scale
    wg_w = c.wg_2TE_w
    wg_wf = c.wg_2TE_wf
  elif wl == 3:
    wg_r = c.wg_3_r
    y_w = round(c.y_3_w*w_scale)
    y_L = round(c.y_3_L*l_scale)
    port_in = pya.Point(19000*c.scale,35000*c.scale)
    a_len = 2500*c.scale
    b_len = 10000*c.scale
    c_len = 12000*c.scale
    d_len = 5000*c.scale
    if TE:
      wg_w = c.wg_3TE_w
      wg_wf = c.wg_3TE_wf
    else:
      wg_w = c.wg_3TM_w
      wg_wf = c.wg_3TM_wf
  else:
    wg_r = c.wg_4_r
    y_w = round(c.y_4_w*w_scale)
    y_L = round(c.y_4_L*l_scale)
    port_in = pya.Point(17500*c.scale,41000*c.scale)
    a_len = 3000*c.scale
    b_len = 8000*c.scale
    c_len = 17000*c.scale
    d_len = 3000*c.scale
    wg_w = c.wg_4TM_w
    wg_wf = c.wg_4TM_wf
  
  angle_offset = 30
  
  (in_1, in_wp_1) = p.wg_adapt(port_in, 0, wg_w, wg_wf, a_len, 40, 2)
  (in_2, in_wp_2) = p.waveguide(in_wp_1, 0, wg_wf, a_len/3)
  (y_1, y_1_left, y_1_right) = p.junction_y(in_wp_2, 0, wg_wf, y_w, y_L)
  
  shapes = y_1
  shapes.update({in_1, in_2})
  
  (left_1, left_wp_1) = p.wg_curve(y_1_left, 0, 90, wg_r, wg_wf, res)
  (left_2, left_wp_2) = p.wg_adapt(left_wp_1, 90, wg_wf, wg_w, a_len, 40, 2)
  (left_3, left_wp_3) = p.waveguide(left_wp_2, 90, wg_w, b_len)
  (left_4, left_wp_4) = p.wg_curve(left_wp_3, 90, 90, wg_r, wg_w, res)
  (left_5, left_wp_5) = p.waveguide(left_wp_4, 180, wg_w, d_len)
  (left_6, port_left) = p.wg_curve(left_wp_5, 180, 90, wg_r, wg_w, res)
  
  shapes.update({left_1,left_2,left_3,left_4,left_5,left_6})
  
  (right_1, right_wp_1) = p.wg_curve(y_1_right, 0, -90, wg_r, wg_wf, res)
  (right_2, right_wp_2) = p.wg_adapt(right_wp_1, 270, wg_wf, wg_w, a_len, 40, 2)
  (right_3, right_wp_3) = p.wg_curve(right_wp_2, 270, -90, wg_r, wg_w, res)
  (right_4, right_wp_4) = p.waveguide(right_wp_3, 180, wg_w, c_len)
  (right_5, right_wp_5) = p.wg_adapt(right_wp_4, 180, wg_w, wg_wf, a_len, 40, 2)
  (right_6, right_wp_6) = p.waveguide(right_wp_5, 180, wg_wf, a_len/3)
  (y_2, y_2_left, y_2_right) = p.junction_y(right_wp_6, 180, wg_wf, y_w, y_L)
  
  shapes.update(y_2)
  shapes.update({right_1,right_2,right_3,right_4,right_5,right_6})
  
  (first_1, first_wp_1) = p.wg_curve(y_2_right, 180, -90, wg_r, wg_wf, res)
  (first_2, port_first) = p.wg_adapt(first_wp_1, 90, wg_wf, wg_w, a_len, 40, 2)
  
  (first_con_1, first_wp_c1) = p.wg_curve(y_2_left, 180, angle_offset, wg_r, wg_wf, res)
  (first_con_2, first_wp_c2) = p.wg_curve(first_wp_c1, 180+angle_offset, -angle_offset, wg_r, wg_wf, res)
  (first_con_3, first_wp_c3) = p.waveguide(first_wp_c2, 180, wg_wf, a_len/3)
  (y_3, y_3_left, y_3_right) = p.junction_y(first_wp_c3, 180, wg_wf, y_w, y_L)
  
  shapes.update({first_1, first_2})
  shapes.update({first_con_1, first_con_2, first_con_3})
  shapes.update(y_3)
  
  (second_1, second_wp_1) = p.wg_curve(y_3_right, 180, -90, wg_r, wg_wf, res)
  (second_2, port_second) = p.wg_adapt(second_wp_1, 90, wg_wf, wg_w, a_len, 40, 2)
  
  (second_con_1, second_wp_c1) = p.wg_curve(y_3_left, 180, angle_offset, wg_r, wg_wf, res)
  (second_con_2, second_wp_c2) = p.wg_curve(second_wp_c1, 180+angle_offset, -angle_offset, wg_r, wg_wf, res)
  (second_con_3, second_wp_c3) = p.waveguide(second_wp_c2, 180, wg_wf, a_len/3)
  (y_4, y_4_left, y_4_right) = p.junction_y(second_wp_c3, 180, wg_wf, y_w, y_L)
  
  shapes.update({second_1, second_2})
  shapes.update({second_con_1, second_con_2, second_con_3})
  shapes.update(y_4)
  
  (third_1, third_wp_1) = p.wg_curve(y_4_right, 180, -90, wg_r, wg_wf, res)
  (third_2, port_third) = p.wg_adapt(third_wp_1, 90, wg_wf, wg_w, a_len, 40, 2)
  
  (third_con_1, third_wp_c1) = p.wg_curve(y_4_left, 180, angle_offset, wg_r, wg_wf, res)
  (third_con_2, third_wp_c2) = p.wg_curve(third_wp_c1, 180+angle_offset, -angle_offset-90, wg_r, wg_wf, res)
  (third_con_3, third_wp_c3) = p.wg_adapt(third_wp_c2, 90, wg_wf, 10*c.scale, a_len*2, 40, 1.8)
  
  shapes.update({third_1, third_2})
  shapes.update({third_con_1, third_con_2, third_con_3})
  
  
  point_text = pya.Point(in_wp_2.x + wg_r*2/3, in_wp_2.y)
  point_marker_1 = pya.Point(port_left.x, port_left.y + 4000*c.scale)
  point_marker_2 = pya.Point(port_second.x, port_second.y + 4000*c.scale)
  
  return(shapes, port_in, port_left, port_first, port_second, port_third, point_text, point_marker_1, point_marker_2)
  
  

def y_tree_back(wl, res, TE=True, l_scale=1.0, w_scale=1.0):
  assert (wl in {1,2,3,4})
  if wl == 1:
    wg_r = c.wg_1_r
    y_w = round(c.y_1_w*w_scale)
    y_L = round(c.y_1_L*l_scale)
    port_trans = pya.Point(23500*c.scale,5000*c.scale)
    a_len = 6000*c.scale
    b_len = 17000*c.scale
    c_len = 17000*c.scale
    d_len = 0
    if TE:
      wg_w = c.wg_1TE_w
      wg_wf = c.wg_1TE_wf
    else:
      wg_w = c.wg_1TM_w
      wg_wf = c.wg_1TM_wf
    
  elif wl == 2:
    wg_r = c.wg_2_r
    y_w = round(c.y_2_w*w_scale)
    y_L = round(c.y_2_L*l_scale)
    port_trans = pya.Point(19500*c.scale,4500*c.scale)
    a_len = 4500*c.scale
    b_len = 14000*c.scale
    c_len = 15000*c.scale
    d_len = 0
    wg_w = c.wg_2TE_w
    wg_wf = c.wg_2TE_wf
  elif wl == 3:
    wg_r = c.wg_3_r
    y_w = round(c.y_3_w*w_scale)
    y_L = round(c.y_3_L*l_scale)
    port_trans = pya.Point(13500*c.scale,3000*c.scale)
    a_len = 2500*c.scale
    b_len = 10000*c.scale
    c_len = 14000*c.scale
    d_len = 3000*c.scale
    if TE:
      wg_w = c.wg_3TE_w
      wg_wf = c.wg_3TE_wf
    else:
      wg_w = c.wg_3TM_w
      wg_wf = c.wg_3TM_wf
  else:
    wg_r = c.wg_4_r
    y_w = round(c.y_4_w*w_scale)
    y_L = round(c.y_4_L*l_scale)
    port_trans = pya.Point(11500*c.scale,2500*c.scale)
    a_len = 3000*c.scale
    b_len = 8000*c.scale
    c_len = 17000*c.scale
    d_len = 3000*c.scale
    wg_w = c.wg_4TM_w
    wg_wf = c.wg_4TM_wf
  
  angle_offset = 50
  
  (trans_1, trans_wp_1) = p.waveguide(port_trans, 90, wg_w, b_len)
  (trans_2, trans_wp_2) = p.wg_curve(trans_wp_1, 90,-90, wg_r, wg_w, res)
  (trans_3, trans_wp_3) = p.waveguide(trans_wp_2, 0, wg_w, d_len)
  (trans_4, trans_wp_4) = p.wg_adapt(trans_wp_3, 0, wg_w, wg_wf, a_len, 40, 2)
  (trans_5, trans_wp_5) = p.wg_curve(trans_wp_4, 0, -90, wg_r, wg_wf, res)
  (trans_6, trans_wp_6) = p.waveguide(trans_wp_5, 270, wg_wf, a_len/3)
  (y_1, y_1_left, y_1_right) = p.junction_y(trans_wp_6, 270, wg_wf, y_w, y_L)
  
  (in_1, in_wp_1) = p.wg_curve(y_1_left, 270, angle_offset, wg_r, wg_wf, res)
  (in_2, in_wp_2) = p.wg_curve(in_wp_1, 270+angle_offset, -angle_offset, wg_r, wg_wf, res)
  (in_3, in_wp_3) = p.wg_adapt(in_wp_2, 270, wg_wf, wg_w, a_len, 40, 2)
  (in_4, in_wp_4) = p.waveguide(in_wp_3, 270, wg_w, c_len)
  (in_5, port_in) = p.wg_curve(in_wp_4, 270, -90, wg_r, wg_w, res)
  
  (cross_1, cross_wp_1) = p.wg_curve(y_1_right, 270, -angle_offset, wg_r, wg_wf, res)
  (cross_2, cross_wp_2) = p.wg_curve(cross_wp_1, 270-angle_offset, angle_offset, wg_r, wg_wf, res)
  (cross_3, port_cross) = p.wg_adapt(cross_wp_2, 270, wg_wf, wg_w, a_len, 40, 2)
  
  shapes = y_1
  shapes.update({trans_1, trans_2, trans_3, trans_4, trans_5, trans_6})
  shapes.update({in_1, in_2, in_3, in_4, in_5})
  shapes.update({cross_1, cross_2, cross_3})
  
  point_text = pya.Point(trans_wp_1.x,trans_wp_1.y + wg_r*2/3)
  point_marker = pya.Point(port_trans.x, port_trans.y + 4000*c.scale)
  
  
  
  return (shapes, port_in, port_trans, port_cross, point_text, point_marker)