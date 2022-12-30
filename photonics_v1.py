import pya
import math
#import numpy
#from scipy.interpolate import CubicSpline

def waveguide(origin, angle, width, length):
  orig = pya.Trans(0, False, origin)
  hw = width/2.0
  rad = angle*math.pi/180.0
  end = pya.Trans(0, False, round(-length*math.sin(rad)), round(length*math.cos(rad)))
  
  points = [orig.trans(pya.Point(round(hw*math.cos(rad)),round(hw*math.sin(rad)))),\
            orig.trans(pya.Point(round(-length*math.sin(rad)+hw*math.cos(rad)),round(length*math.cos(rad)+hw*math.sin(rad)))),\
            orig.trans(pya.Point(round(-length*math.sin(rad)-hw*math.cos(rad)),round(length*math.cos(rad)-hw*math.sin(rad)))),\
            orig.trans(pya.Point(round(-hw*math.cos(rad)),round(-hw*math.sin(rad))))]
            
  wg = pya.SimplePolygon(points)
  
  return (wg,end.trans(origin))
  
  
  
  
def taper(origin, angle, width_start, width_end, length):
  orig = pya.Trans(0, False, origin)
  hw1 = width_start/2.0
  hw2 = width_end/2.0
  rad = angle*math.pi/180.0
  end = pya.Trans(0, False, round(-length*math.sin(rad)), round(length*math.cos(rad)))
  
  points = [orig.trans(pya.Point(round(hw1*math.cos(rad)),round(+hw1*math.sin(rad)))),\
            orig.trans(pya.Point(round(-length*math.sin(rad)+hw2*math.cos(rad)),round(length*math.cos(rad)+hw2*math.sin(rad)))),\
            orig.trans(pya.Point(round(-length*math.sin(rad)-hw2*math.cos(rad)),round(length*math.cos(rad)-hw2*math.sin(rad)))),\
            orig.trans(pya.Point(round(-hw1*math.cos(rad)),round(-hw1*math.sin(rad))))]
            
  wg = pya.SimplePolygon(points)
  
  return (wg,end.trans(origin))


def circle(origin, radius, res):
  orig = pya.Trans(0,False,origin)
  
  rad = [2*a*math.pi/res for a in range(res+1)]
  points = [orig.trans(pya.Point(round((radius)*math.cos(a)),round((radius)*math.sin(a)))) for a in rad]

  circ = pya.SimplePolygon(points)
  
  return circ

def ring(origin, inner_radius, width, res):
  orig = pya.Trans(0, False, origin)
  
  rad = [2*a*math.pi/res for a in range(res+1)]
  
  outer_ring = [orig.trans(pya.Point(round((inner_radius+width)*math.cos(a)),round((inner_radius+width)*math.sin(a)))) for a in rad]
  inner_ring = [orig.trans(pya.Point(round((inner_radius)*math.cos(a)),round((inner_radius)*math.sin(a)))) for a in rad]
  
  #ring = pya.Polygon(outer_ring)
  #ring.insert_hole(inner_ring)
  
  ring = pya.SimplePolygon(outer_ring + inner_ring[::-1])
  
  return ring
  
  
  

def curve_center(origin, angle_start, angle_end, radius, width, res):
  orig = pya.Trans(0, False, origin)
  
  angle_range = angle_end-angle_start
  points = int((abs(angle_range)/360.0)*res)
  angle_step = angle_range*1.0/points
  
  rad = [(angle_start + a*angle_step)*math.pi/180.0 for a in range(0,points)] + [angle_end*math.pi/180.0]
  
  outer_edge = [orig.trans(pya.Point(round((radius+width/2.0)*math.cos(a)),round((radius+width/2.0)*math.sin(a)))) for a in rad]
  inner_edge = [orig.trans(pya.Point(round((radius-width/2.0)*math.cos(a)),round((radius-width/2.0)*math.sin(a)))) for a in rad]
  
  curve = pya.SimplePolygon(outer_edge + inner_edge[::-1])
  
  start_point = orig.trans(pya.Point(round((radius)*math.cos(rad[0])),round((radius)*math.sin(rad[0]))))
  end_point = orig.trans(pya.Point(round((radius)*math.cos(rad[-1])),round((radius)*math.sin(rad[-1]))))
  
  return (curve,start_point,end_point) 
  
  
  
def wg_curve(origin, angle_start, angle_delta, radius, width, res):
  #under construction
  rad_start = angle_start*math.pi/180.0
  if (angle_delta >= 0):
    center_correct = pya.Trans(0,False,round(-radius*math.cos(rad_start)),round(-radius*math.sin(rad_start)))
    (curve,start_point,end_point) = curve_center(center_correct.trans(origin),angle_start,angle_start+angle_delta,radius,width,res)
  else:
    center_correct = pya.Trans(0,False,round(radius*math.cos(rad_start)),round(radius*math.sin(rad_start)))
    (curve,end_point,start_point) = curve_center(center_correct.trans(origin),angle_start+angle_delta+180,angle_start+180,radius,width,res)
    
  return (curve,end_point)
    
    
    
def wg_adapt(origin, angle, width_start, width_end, length, points=40, precision=3):
  center = points/2.0
  orig = pya.Trans(0, False, origin)
  rad = angle*math.pi/180.0
  end = pya.Trans(0, False, round(-length*math.sin(rad)), round(length*math.cos(rad)))
  
  scale = [ 1.0/(1+math.exp(-1*(precision/center)*(x-center))) for x in range(0,points+1)]
  scale = [(s-min(scale))/(max(scale)-min(scale)) for s in scale]
    
  hw = [ 0.5*(width_start + (width_end-width_start)*s) for s in scale]
  spine = [ x*1.0*length/points for x in range(0,points+1)]
  
  
  edge1 = [orig.trans(pya.Point(round(x*math.cos(rad)-y*math.sin(rad)),round(x*math.sin(rad)+y*math.cos(rad)))) for (x,y) in zip(hw,spine)]
  edge2 = [orig.trans(pya.Point(round(-x*math.cos(rad)-y*math.sin(rad)),round(-x*math.sin(rad)+y*math.cos(rad)))) for (x,y) in zip(hw,spine)]
  
  wg = pya.SimplePolygon(edge1 + edge2[::-1])
  
  return (wg,end.trans(origin))



def curve_center_adapt(origin, angle_start, angle_end, radius, width_start, width_end, res, precision=4):
  orig = pya.Trans(0, False, origin)
  
  angle_range = angle_end-angle_start
  points = int((abs(angle_range)/360.0)*res)
  angle_step = angle_range*1.0/points
  center = points/2.0
  
  scale = [ 1.0/(1+math.exp(-1*(precision/center)*(x-center))) for x in range(0,points+1)]
  scale = [(s-min(scale))/(max(scale)-min(scale)) for s in scale]
  
  width = [ (width_start + (width_end-width_start)*s) for s in scale]
  
  rad = [(angle_start + a*angle_step)*math.pi/180.0 for a in range(0,points)] + [angle_end*math.pi/180.0]
  
  outer_edge = [orig.trans(pya.Point(round((radius+w/2.0)*math.cos(a)),round((radius+w/2.0)*math.sin(a)))) for (w,a) in zip(width,rad)]
  inner_edge = [orig.trans(pya.Point(round((radius-w/2.0)*math.cos(a)),round((radius-w/2.0)*math.sin(a)))) for (w,a) in zip(width,rad)]
  
  curve = pya.SimplePolygon(outer_edge + inner_edge[::-1])
  
  start_point = orig.trans(pya.Point(round((radius)*math.cos(rad[0])),round((radius)*math.sin(rad[0]))))
  end_point = orig.trans(pya.Point(round((radius)*math.cos(rad[-1])),round((radius)*math.sin(rad[-1]))))
  
  return (curve,start_point,end_point)

  
def wg_curve_adapt(origin, angle_start, angle_delta, radius, width_start, width_end, res, precision=3):
  rad_start = angle_start*math.pi/180.0
  if (angle_delta >= 0):
    center_correct = pya.Trans(0,False,round(-radius*math.cos(rad_start)),round(-radius*math.sin(rad_start)))
    (curve,start_point,end_point) = curve_center_adapt(center_correct.trans(origin),angle_start,angle_start+angle_delta,radius,width_start,width_end,res,precision)
  else:
    center_correct = pya.Trans(0,False,round(radius*math.cos(rad_start)),round(radius*math.sin(rad_start)))
    (curve,end_point,start_point) = curve_center_adapt(center_correct.trans(origin),angle_start+angle_delta+180,angle_start+180,radius,width_end,width_start,res,precision)
  
  return (curve,end_point)



def curve_center_taper(origin, angle_start, angle_end, radius, width_start, width_end, res, precision=3):
  orig = pya.Trans(0, False, origin)
  
  angle_range = angle_end-angle_start
  points = int((abs(angle_range)/360.0)*res)
  angle_step = angle_range*1.0/points
  center = points/2.0
  
  scale = [ 1.0*x/points for x in range(0,points+1)]
  
  width = [ (width_start + (width_end-width_start)*s) for s in scale]
  
  rad = [(angle_start + a*angle_step)*math.pi/180.0 for a in range(0,points)] + [angle_end*math.pi/180.0]
  
  outer_edge = [orig.trans(pya.Point(round((radius+w/2.0)*math.cos(a)),round((radius+w/2.0)*math.sin(a)))) for (w,a) in zip(width,rad)]
  inner_edge = [orig.trans(pya.Point(round((radius-w/2.0)*math.cos(a)),round((radius-w/2.0)*math.sin(a)))) for (w,a) in zip(width,rad)]
  
  curve = pya.SimplePolygon(outer_edge + inner_edge[::-1])
  
  start_point = orig.trans(pya.Point(round((radius)*math.cos(rad[0])),round((radius)*math.sin(rad[0]))))
  end_point = orig.trans(pya.Point(round((radius)*math.cos(rad[-1])),round((radius)*math.sin(rad[-1]))))
  
  return (curve,start_point,end_point)



def wg_curve_taper(origin, angle_start, angle_delta, radius, width_start, width_end, res, precision=3):
  rad_start = angle_start*math.pi/180.0
  if (angle_delta >= 0):
    center_correct = pya.Trans(0,False,round(-radius*math.cos(rad_start)),round(-radius*math.sin(rad_start)))
    (curve,start_point,end_point) = curve_center_taper(center_correct.trans(origin),angle_start,angle_start+angle_delta,radius,width_start,width_end,res,precision)
  else:
    center_correct = pya.Trans(0,False,round(radius*math.cos(rad_start)),round(radius*math.sin(rad_start)))
    (curve,end_point,start_point) = curve_center_taper(center_correct.trans(origin),angle_start+angle_delta+180,angle_start+180,radius,width_end,width_start,res,precision)
  
  return (curve,end_point)
  
  
  
def grating(origin, angle, width, ribs, gaps):
  #should have one more rib than gap
  hw = width/2.0
  rad = angle*math.pi/180.0
  (wg_simple, end_point) = waveguide(origin, angle, width, sum(gaps)+sum(ribs))
  grate = pya.Polygon(wg_simple)
  current_point = origin
  for (a,b) in zip(ribs,gaps):
    rib_trans = pya.Trans(0, False, round(-a*math.sin(rad)), round(a*math.cos(rad)))
    current_point = rib_trans.trans(current_point)
    current_orig = pya.Trans(0,False,current_point)
    points = [current_orig.trans(pya.Point(round(hw*math.cos(rad)),round(+hw*math.sin(rad)))),\
            current_orig.trans(pya.Point(round(-b*math.sin(rad)+hw*math.cos(rad)),round(b*math.cos(rad)+hw*math.sin(rad)))),\
            current_orig.trans(pya.Point(round(-b*math.sin(rad)-hw*math.cos(rad)),round(b*math.cos(rad)-hw*math.sin(rad)))),\
            current_orig.trans(pya.Point(round(-hw*math.cos(rad)),round(-hw*math.sin(rad))))]
    
    grate.insert_hole(points)
  
    gap_trans = pya.Trans(0, False, round(-b*math.sin(rad)), round(b*math.cos(rad)))
    current_point = gap_trans.trans(current_point)
  return (grate, end_point)
  
  
  
def wg_adapt_offset(origin, angle, offset, width_start, width_end, length, points=40, precision_adapt=4, precision_offset=3):
  center = points/2.0
  orig = pya.Trans(0, False, origin)
  rad = angle*math.pi/180.0
  end = pya.Trans(0, False, round(offset*math.cos(rad)-length*math.sin(rad)), round(offset*math.sin(rad)+length*math.cos(rad)))
  
  scale_adapt = [ 1.0/(1+math.exp(-1*(precision_adapt/center)*(x-center))) for x in range(0,points+1)]
  scale_adapt = [(s-min(scale_adapt))/(max(scale_adapt)-min(scale_adapt)) for s in scale_adapt]
    
  scale_offset = [ 1.0/(1+math.exp(-1*(precision_offset/center)*(x-center))) for x in range(0,points+1)]
  scale_offset = [(s-min(scale_offset))/(max(scale_offset)-min(scale_offset)) for s in scale_offset]
  
  hw = [ 0.5*(width_start + (width_end-width_start)*s) for s in scale_adapt]
  elevation = [ offset*s for s in scale_offset]
  spine = [ x*1.0*length/points for x in range(0,points+1)]
  
  
  edge1 = [orig.trans(pya.Point(round((x+w)*math.cos(rad)-y*math.sin(rad)),round((x+w)*math.sin(rad)+y*math.cos(rad)))) for (w,y,x) in zip(hw,spine,elevation)]
  edge2 = [orig.trans(pya.Point(round((x-w)*math.cos(rad)-y*math.sin(rad)),round((x-w)*math.sin(rad)+y*math.cos(rad)))) for (w,y,x) in zip(hw,spine,elevation)]
  
  wg = pya.SimplePolygon(edge1 + edge2[::-1])
  
  return (wg,end.trans(origin))

def wg_p2p_curve(origin, endpoint, angle_start, angle_end, radius, width, res):
  # not for parallel lines
  if angle_start == angle_end:
    return pya.Path([origin,endpoint],width)
  elif angle_end > angle_start:
    p1 = origin
    p2 = endpoint
    theta1 = angle_start
    theta2 = angle_end
  else:
    p1 = endpoint
    p2 = origin
    theta1 = angle_end+180
    theta2 = angle_start+180
  
  
  rad1 = theta1*math.pi/180.0
  rad2 = theta2*math.pi/180.0
  delta_x = p2.x - p1.x
  delta_y = p2.y - p1.y
  
  angle_range = theta2-theta1
  points = int((abs(angle_range)/360.0)*res)
  angle_step = angle_range*1.0/points
  rad = [(theta1 + a*angle_step)*math.pi/180.0 for a in range(0,points)] + [theta2*math.pi/180.0]
  delta_x_curve = round(radius*(math.cos(rad2)-math.cos(rad1)))
  delta_y_curve = round(radius*(math.sin(rad2)-math.sin(rad1)))
  
  delta_x_straight = delta_x - delta_x_curve
  delta_y_straight = delta_y - delta_y_curve
  
  dxdL1 = -1*math.sin(rad1)
  dydL1 = math.cos(rad1)
  dxdL2 = -1*math.sin(rad2)
  dydL2 = math.cos(rad2)
  
  det = (dxdL1*dydL2) - (dydL1*dxdL2)
  
  span1 = (dydL2*delta_x_straight - dxdL2*delta_y_straight)/det
  span2 = (-dydL1*delta_x_straight + dxdL1*delta_y_straight)/det
  
  s1_trans = pya.Trans(0,False,round(span1*dxdL1),round(span1*dydL1))
  s2_trans = pya.Trans(0,False,round(-span2*dxdL2),round(-span2*dydL2))
  
  curve_start = s1_trans.trans(p1)
  curve_end = s2_trans.trans(p2)
  
  center_adj = pya.Trans(0,False,round(-radius*math.cos(rad1)),round(-radius*math.sin(rad1)))
  
  curve_center = center_adj.trans(curve_start)
  curve_arc = [pya.Trans(0,False,round(radius*math.cos(theta)),round(radius*math.sin(theta))) for theta in rad] 
  curve_points = [t.trans(curve_center) for t in curve_arc]
  
  points = [p1, curve_start] + curve_points + [curve_end, p2]
  path = pya.Path(points,width)
  
  return path.simple_polygon()
  
def wg_p2p_offset(origin, endpoint, angle, width, points=40, precision=3):
#under construction
  x1 = origin.x
  x2 = endpoint.x
  y1 = origin.y
  y2 = endpoint.y
  
  rad = angle*math.pi/180
  
  delta_x = x2-x1
  delta_y = y2-y1
  
  d_parallel = -delta_x*sin(rad) + delta_y*cos(rad)
  d_perp = -delta_x*cos(rad)


def junction_y(origin, angle, width_in, width_max, length, points=40, precision=2.4, balance=0.65):
  # requires width_max > 40
  l_main = math.ceil(balance*length)
  l_second = math.floor((1-balance)*length)
  width_second = round(width_max/2) - 20
  shift = round(width_second/2) + 20
  theta = angle*math.pi/180
  
  t_left = pya.Trans(0, False, pya.Point(-shift*math.cos(theta),-shift*math.sin(theta)))
  t_right = pya.Trans(0, False, pya.Point(shift*math.cos(theta),shift*math.sin(theta)))
  
  (main, midpoint) = wg_adapt(origin, angle, width_in, width_max, l_main, points, precision)
  (left, left_port) = wg_adapt(t_left.trans(midpoint), angle, width_second, width_in, l_second, points, precision)
  (right, right_port) = wg_adapt(t_right.trans(midpoint), angle, width_second, width_in, l_second, points, precision)
  
  return ({main,left,right},left_port,right_port)
  
def junction_split(origin, angle, width_in, width_max, length, points=40, precision=3):
  # requires width_max > 40
  width_second = round(width_max/2) - 20
  shift = round(width_second/2) + 20
  theta = angle*math.pi/180
  
  offset = round((width_second-width_in)/2)
  
  t_left = pya.Trans(0, False, pya.Point(-shift*math.cos(theta),-shift*math.sin(theta)))
  t_right = pya.Trans(0, False, pya.Point(shift*math.cos(theta),shift*math.sin(theta)))
  
  (left, left_port) = wg_adapt_offset(t_left.trans(origin), angle, -offset, width_second, width_in, length, points, precision, precision)
  (right, right_port) = wg_adapt_offset(t_right.trans(origin), angle, offset, width_second, width_in, length, points, precision, precision)
  
  return ({left,right},left_port,right_port)

def grating_coupler(origin, angle, width_wg, width_gr, length_taper, ribs, gaps, points, precision=2):
  #origin is the start point of the grating (closest landmark to the actual focus point)
  (gr, gr_end) = grating(origin,angle,width_gr,ribs,gaps)
  (taper, gr_enter) = wg_adapt(origin,angle+180, width_gr, width_wg,length_taper,points,precision)
  
  return ({gr,taper}, gr_enter, gr_end)
  
  
def grating_coupler_end(origin, angle, width_wg, width_gr, length_taper, ribs, gaps, points, precision=2):
  #origin is the start point of the grating (closest landmark to the actual focus point)
  (taper, gr_enter) = wg_adapt(origin,angle, width_wg, width_gr,length_taper,points,precision)
  (gr, gr_end) = grating(gr_enter,angle,width_gr,ribs,gaps)
  
  return ({gr,taper}, gr_enter, gr_end) 
  
#def wg_p2p_spline(origin, destination, angle_start, angle_end, width, points):
  #on hold until numpy/scipy are built

def ellipse(origin, angle_delta, a, ecc, res):
  
  rad = [x*2*math.pi/res for x in range(res)]
  rad_delta = angle_delta*math.pi/180.0
  
  org_trans = pya.Trans(origin)
  
  radius = [a*(1-ecc**2)/(1-ecc*math.cos(theta+rad_delta)) for theta in rad]
  
  x_coord = [-r*math.sin(theta) for (r,theta) in zip(radius,rad)]
  y_coord = [r*math.cos(theta) for (r,theta) in zip(radius,rad)]
  
  points = [org_trans.trans(pya.Point(round(x),round(y))) for (x,y) in zip(x_coord,y_coord)]
  
  return pya.SimplePolygon(points)
  
def ellipse_taper(origin, angle, arc, angle_delta, ecc, width_start, radius_center, res):
  #
  rad = angle*math.pi/180.0
  rad_arc = arc*math.pi/180.0
  rad_delta = angle_delta*math.pi/180.0
  
  end = pya.Trans(pya.Point(round(-radius_center*math.sin(rad)),round(radius_center*math.cos(rad))))
  org_trans = pya.Trans(origin)  
  
  points = round(arc*res/360)
  step = rad_arc/points
  half_arc = rad_arc/2
  
  rad_points = [x*step-half_arc+rad for x in range(points)] + [half_arc+rad]
  
  a = radius_center*(1-ecc*math.cos(rad_delta))/(1-ecc**2)
  
  radius = [a*(1-ecc**2)/(1-ecc*math.cos(theta+rad_delta)) for theta in rad_points]
  
  x_coord = [width_start*math.cos(rad)/2.0] + [-r*math.sin(theta) for (r,theta) in zip(radius,rad_points)] + [-width_start*math.cos(rad)/2.0]
  y_coord = [width_start*math.sin(rad)/2.0] + [r*math.cos(theta) for (r,theta) in zip(radius,rad_points)] + [-width_start*math.sin(rad)/2.0]
  
  points = [org_trans.trans(pya.Point(round(x),round(y))) for (x,y) in zip(x_coord,y_coord)]
  
  return pya.SimplePolygon(points)

def ellipse_arc(origin, angle, arc, angle_delta, ecc, radius_start, radius_end, res):
  #
  rad = angle*math.pi/180.0
  rad_arc = arc*math.pi/180.0
  rad_delta = angle_delta*math.pi/180.0
  
  org_trans = pya.Trans(origin)  
  
  points = round(arc*res/360)
  step = rad_arc/points
  half_arc = rad_arc/2
  
  rad_points = [x*step-half_arc+rad for x in range(points)] + [half_arc+rad]
  
  a1 = radius_start*(1-ecc*math.cos(rad_delta))/(1-ecc**2)
  a2 = radius_end*(1-ecc*math.cos(rad_delta))/(1-ecc**2)
  
  radius1 = [a1*(1-ecc**2)/(1-ecc*math.cos(theta+rad_delta)) for theta in rad_points]
  radius2 = [a2*(1-ecc**2)/(1-ecc*math.cos(theta+rad_delta)) for theta in rad_points[::-1]]
  
  x_coord = [-r*math.sin(theta) for (r,theta) in zip(radius1,rad_points)] + [-r*math.sin(theta) for (r,theta) in zip(radius2,rad_points[::-1])]
  y_coord = [r*math.cos(theta) for (r,theta) in zip(radius1,rad_points)] + [r*math.cos(theta) for (r,theta) in zip(radius2,rad_points[::-1])]
  
  points = [org_trans.trans(pya.Point(round(x),round(y))) for (x,y) in zip(x_coord,y_coord)]
  
  return pya.SimplePolygon(points)


def ellipse_gc(origin, angle, arc, angle_delta, ecc, width_start, ribs, gaps, res):
  
  shapes = {ellipse_taper(origin, angle, arc, angle_delta, ecc, width_start, ribs[0], res)}
  
  current_radius = ribs[0]
  
  for i in range(len(gaps)):
    shapes.add(ellipse_arc(origin, angle, arc, angle_delta, ecc, current_radius+gaps[i], current_radius+gaps[i]+ribs[i+1], res))
    current_radius += gaps[i] + ribs[i+1]
  
  return shapes
  

def marker(origin, scale, res):
  return {ring(origin, scale*100, scale*100, res), ring(origin, scale*300, scale*100, res), ring(origin, scale*500, scale*100, res), ring(origin, scale*700, scale*1300, res)}

#scale = 100
#layout = pya.Layout()
#layout.dbu = 0.001/scale
#GaP = layout.layer(1,0)
#
#top = layout.create_cell("pattern")
#
#res = 120
#
#grating_1TE_gaps = [a*scale for a in [150,150,300,300,300,150]]
#grating_1TE_ribs = [a*scale for a in [16000,610,590,740,750,690,520]]
#
#gc = ellipse_gc(pya.Point(0,0), 0, 30, 45, 0.3, 550*scale, grating_1TE_ribs, grating_1TE_gaps, res)
#(wg, wg_end) = waveguide(pya.Point(0,0), 180, 550*scale, 10000*scale)
#
#for shape in gc:
#  top.shapes(GaP).insert(shape)
#top.shapes(GaP).insert(wg)
#
#top.write("C:\\Users\\Alan\\Desktop\\OptoSpin Projects\\KLayout\\photoTest.gds")