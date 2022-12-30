import pya
import math
import photonics as p

def label_insert(cell, label_cells, d, text, origin = pya.Point(0,0) ):
  
  spacing = [pya.Trans(pya.Point(origin.x + a*d, origin.y)) for a in range(len(text))]
  
  digits = [label_cells[b] for b in text]
  
  for (digit,pos) in zip(digits,spacing):
    cell.insert(pya.CellInstArray(digit.cell_index(),pos))
  
  return True


def label_gen(h, t, res):
  
  w = h/2
  r = (w-t)/2
  
  cent1_0 = pya.Point(w/2,h/4)
  
  
  (curv1_0, left_0, right_0) = p.curve_center(cent1_0, 180, 360, r, t, res)
  (line1_0, right_top_0) = p.waveguide(right_0, 0, t, h/2)
  (curv2_0, left_top_0) = p.wg_curve(right_top_0, 0, 180, r, t, res)
  (line2_0, left2_0) = p.waveguide(left_top_0, 180, t, h/2)
  
  zero = {curv1_0,curv2_0,line1_0,line2_0}
  
  
  start_1 = pya.Point(w/2,0)
  mark1_1 = pya.Point((w-t)/2, h - t/2)
  mark2_1 = pya.Point(w/2 - 2*t, t/2)
  
  (line1_1, top_1) = p.waveguide(start_1, 0, t, h)
  (line2_1, end1_1) = p.waveguide(mark1_1, 90, t, t)
  (line3_1, end2_1) = p.waveguide(mark2_1, 270, t, 4*t)
  
  one = {line1_1, line2_1, line3_1}
  
  
  cent1_2 = pya.Point(w/2, 3*h/4)
  end_2 = pya.Point(w, t/2)
  angle_2 = -35
  
  (curv1_2, mid_2, start_2) = p.curve_center(cent1_2, angle_2, 180, r, t, res)
  curv2_2 = p.wg_p2p_curve(mid_2, end_2, 180+angle_2, 270, r/3, t, res)
  
  two = {curv1_2, curv2_2}
  
  
  
  start_3 = pya.Point(0,t/2)
  
  (line1_3, low_3) = p.waveguide(start_3, 270, t, r+t/4)
  (curv1_3, mid_3) = p.wg_curve(low_3, 270, 180, r+t/4, t, res)
  (curv2_3, top_3) = p.wg_curve(mid_3, 270, 180, r+t/4, t, res)
  (line2_3, end1_3) = p.waveguide(mid_3, 90, t, r)
  (line3_3, end2_3) = p.waveguide(top_3, 90, t, r+t/4)
  
  three = {curv1_3, curv2_3, line1_3, line2_3, line3_3}
  
  
  
  top1_4 = pya.Point(t/2,h)
  mid_4 = pya.Point(w-t, h/2)
  base_4 = pya.Point(w-t/2, 0)
  
  curv1_4 = p.wg_p2p_curve(top1_4, mid_4, 180, 270, r/2, t, res)
  (line1_4,top2_4) = p.waveguide(base_4, 0, t, h)
  
  four = {curv1_4, line1_4}
  
  
  
  start1_5 = pya.Point(0,t/2)
  start2_5 = pya.Point(t/2,(h+t)/2)
  end2_5 = pya.Point(w,h-t/2)
  
  (line1_5, low_5) = p.waveguide(start1_5, 270, t, r+t/4)
  (curv1_5, mid_5) = p.wg_curve(low_5, 270, 180, r+t/4, t, res)
  (line2_5, end1_5) = p.waveguide(mid_5, 90, t, r+t/4)
  curv2_5 = p.wg_p2p_curve(start2_5, end2_5, 0, -90, r/2, t, res)

  five = {curv1_5, curv2_5, line1_5, line2_5}
  
  
  
  cent1_6 = pya.Point(w/2,3*h/4)
  
  (curv1_6, right_6, left_6) = p.curve_center(cent1_6, 0, 180, r, t, res)
  (line1_6, left_bottom_6) = p.waveguide(left_6, 180, t, h/2)
  (curv2_6, mid_6) = p.wg_curve(left_bottom_6, 180, 360, r, t, res)
  #(line2_6, left2_6) = p.waveguide(mid_6, 90, t, w/2)
  
  six = {curv1_6,curv2_6,line1_6}     #,line2_6}
  
  
  start_7 = pya.Point(0, h-t/2)
  end_7 = pya.Point(t/2,t/2)
  angle_7 = 152.5
  
  line1_7 = p.wg_p2p_curve(start_7, end_7, 270, angle_7, r/2, t, res)
  
  seven = {line1_7}  
  
  
  
  cent1_8 = pya.Point(w/2, h/4)
  cent2_8 = pya.Point(w/2, 3*h/4)
  
  ring1_8 = p.ring(cent1_8, r-t/2, t, res)
  ring2_8 = p.ring(cent2_8, r-t/2, t, res)
  
  eight = {ring1_8, ring2_8}
  
  
  start_9 = pya.Point(w-t/2, 3*h/4)
  angle_9 = 0
  
  (curv1_9, end1_9) = p.wg_curve(start_9, 0, 360+angle_9, r, t, res)
  (line1_9, end2_9) = p.waveguide(start_9, 180-angle_9, t, 3*h/4)
  
  nine = {curv1_9, line1_9}
  
  
  start_dash = pya.Point(w/8,h/2)
  
  (line_dash,end_dash) = p.waveguide(start_dash, 270, t, 3*w/4);
  
  dash = {line_dash}
  
  space = set()
  
  return {'0':zero, '1':one, '2':two, '3':three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine, '-':dash, ' ':space}

