import pya
import math


scale = 8
res = 360


path = 'C:\\Users\\adlogan\\Dropbox\\Projects\\Frequency Conversion\\Layout\\KLayout\\2021_11_26_GaP_Stamp\\'
path_test = path + 'Devices\\'

filename_full = 'GaP_stamp_ell_gratings'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/scale
GaP = layout.layer(1,0)

top = layout.create_cell("top")





def confocal_ellipse_section(origin, focal_offset, focal_angle, focal_length, section_width, arc, arc_offset, res = 360, scale = 8):
  # Creates a section of an ellipsoid ring such that the inner and outer ellipses have the same foci. 
  # Angles in degrees, lengths in nm
  
  n_pts = math.ceil(res*arc/360) # number of points in each ellipse arc
  d_theta = arc/n_pts # number of degrees between points
  theta_base = [(math.pi/180)*(90+(a*d_theta)-(arc/2)+arc_offset) for a in range(n_pts+1)]
  
   
  d_1 = focal_length
  d_2 = d_1 + section_width
  
  inner_major = 0.5*(d_1 + math.sqrt(d_1**2 + (2*focal_offset)**2 - 4*d_1*focal_offset*math.cos((math.pi/180)*(90+focal_angle))))
  inner_minor = math.sqrt(inner_major**2 - focal_offset**2)
  outer_major = 0.5*(d_2 + math.sqrt(d_2**2 + (2*focal_offset)**2 - 4*d_2*focal_offset*math.cos((math.pi/180)*(90+focal_angle))))
  outer_minor = math.sqrt(outer_major**2 - focal_offset**2)  
  
  r_1 = [(inner_minor**2)/(inner_major + focal_offset*math.cos(theta_base[x] - (math.pi/180)*focal_angle)) for x in range(len(theta_base))]
  r_2 = [(outer_minor**2)/(outer_major + focal_offset*math.cos(theta_base[x] - (math.pi/180)*focal_angle)) for x in range(len(theta_base))]
  
  x_1 = [round(scale*(r_1[x] * math.cos(theta_base[x]))) for x in range(len(theta_base))]
  y_1 = [round(scale*(r_1[x] * math.sin(theta_base[x]))) for x in range(len(theta_base))]
  x_2 = [round(scale*(r_2[-1-x] * math.cos(theta_base[-1-x]))) for x in range(len(theta_base))]
  y_2 = [round(scale*(r_2[-1-x] * math.sin(theta_base[-1-x]))) for x in range(len(theta_base))]
  
  poly_points = []
  
  for (x,y) in zip(x_1+x_2,y_1+y_2):
    trans = pya.Trans(x,y)
    poly_points = poly_points + [trans*origin]
    
  return poly_points
  

exp_origin = pya.Trans(0,-2000*scale)*origin

poly_plate = pya.Polygon([pya.Point(-3000*scale,0),pya.Point(-3000*scale,4000*scale),pya.Point(3000*scale,4000*scale),pya.Point(3000*scale,0)])

w_wg_738 = 350
w_wg_946 = 550

poly_wg_738 = pya.Box(scale*-w_wg_738/2, scale*-3000, scale*w_wg_738/2, 0)
poly_wg_946 = pya.Box(scale*-w_wg_946/2, scale*-3000, scale*w_wg_946/2, 0)

w_exp_738 = 2000*scale*math.tan((math.pi/180)*25)
w_exp_946 = 2000*scale*math.tan((math.pi/180)*20)

poly_exp_738 = pya.Polygon([exp_origin, pya.Point(round(-w_exp_738/2),0), pya.Point(round(w_exp_738/2),0)])
poly_exp_946 = pya.Polygon([exp_origin, pya.Point(round(-w_exp_946/2),0), pya.Point(round(w_exp_946/2),0)])

f_738 = [500,1000,1000]
L_738 = [500,500,2000]
theta_738 = [30,60,60]
period_738 = 700
cycle_738 = 0.7
arc_738 = [32,32,32]
arc_off_738 = [0,0,0]#[-8,-7,-8]

f_946 = [500,500,1000]
L_946 = [500,2000,500]
theta_946 = [0,0,60]
period_946 = 800
cycle_946 = 0.7
arc_946 = [27,27,27]
arc_off_946 = [0,0,0]

for (f,L,theta,arc,off) in zip(f_738,L_738,theta_738,arc_738,arc_off_738):
  cell_name = "ell738_f" + str(f) + "_L" + str(L) + "_t" + str(theta)
  cell = layout.create_cell(cell_name)
  
  cell.shapes(GaP).insert(poly_wg_738)
  cell.shapes(GaP).insert(poly_exp_738)
  
  plate = poly_plate.dup()
  w = period_738 * cycle_738
  
  etch_pts_1 = confocal_ellipse_section(exp_origin, f, theta, 2000+L, w,arc, off, res, scale)
  etch_pts_2 = confocal_ellipse_section(exp_origin, f, theta, 2000+L+period_738, w, arc, off, res, scale)
  
  plate.insert_hole(etch_pts_1)
  plate.insert_hole(etch_pts_2)
  
  cell.shapes(GaP).insert(plate)
  
  cell.write(path_test + cell_name + '.gds')
  

for (f,L,theta,arc,off) in zip(f_946,L_946,theta_946,arc_946,arc_off_946):
  cell_name = "ell946_f" + str(f) + "_L" + str(L) + "_t" + str(theta)
  cell = layout.create_cell(cell_name)
  
  cell.shapes(GaP).insert(poly_wg_946)
  cell.shapes(GaP).insert(poly_exp_946)
  
  plate = poly_plate.dup()
  w = period_946 * cycle_946
  
  etch_pts_1 = confocal_ellipse_section(exp_origin, f, theta, 2000+L, w,arc, off, res, scale)
  etch_pts_2 = confocal_ellipse_section(exp_origin, f, theta, 2000+L+period_738, w, arc, off, res, scale)
  
  plate.insert_hole(etch_pts_1)
  plate.insert_hole(etch_pts_2)
  
  cell.shapes(GaP).insert(plate)
  
  cell.write(path_test + cell_name + '.gds')
  


