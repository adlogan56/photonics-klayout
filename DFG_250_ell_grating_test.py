import pya
import math
#from importlib import reload
import DFG_250_constants as cons
#import GaP_SiN_125_constants as cons
import photonics as p

from importlib import reload
reload(p)
reload(cons)

layout = pya.Layout()
layout.dbu = 0.001/cons.scale
GaP = layout.layer(1,0)

origin = pya.Point(0,0)

path = 'C:\\Users\\adlogan\\Dropbox\\Frequency Conversion\\Data\\KLayout\\2019_06_20 Gratings\\'

arc = [20,25,30]            # arc of elliptical focusing gratings
angle = [10,20,30]          # angle with major axis
eccentricity = [0.05,0.1,0.15]   # ellipse eccentricity
length = [a*cons.scale for a in [6000,8000,10000]]    # ellipse expansion length

write_ellipse = True;



for gr_type in cons.gr_spec:

  if (gr_type=='SHG') | (gr_type=='DFG'):
    wg_type = 'Multi'
  else:
    wg_type = gr_type
  
  print(wg_type)
  
  wg_width = cons.wg_spec[wg_type]['w']['wg']
  
  (wg, end) = p.waveguide(origin, 180, wg_width, cons.scale*6000)
  # (grating_str, gr_enter, gr_end) = p.grating_coupler_end(origin, 0, wg_width, cons.gr_adapt_spec[gr_type][0], cons.gr_adapt_spec[gr_type][1],\
                                                         # [max(int(a*cons.gr_adjust[gr_type]),cons.d_min) for a in [0] + cons.gr_spec[gr_type][0]],\
                                                         # [max(int(a*cons.gr_adjust[gr_type]),cons.d_min) for a in cons.gr_spec[gr_type][1]], 40, 2)
  
  # grating_str.update(wg)
  
  # name_str = 'grating_str_' + gr_type
  # cell_str = layout.create_cell(name_str)
  
  # for s in grating_str:
    # cell_str.shapes(GaP).insert(s)
  
  # cell_str.write(path + name_str + '.gds')
  
  if write_ellipse == True:
    for theta in arc:
      for phi in angle:
        for ecc in eccentricity:
          for L in length:
            grating_ell = p.ellipse_gc(origin, 0, theta, phi, ecc, wg_width,\
                                      [L] + cons.gr_spec[gr_type]['ribs'],\
                                      cons.gr_spec[gr_type]['gaps'], cons.res)[0]
              
            grating_ell.update(wg)
              
            name_ell = 'grating_ell_' + gr_type + '_a' + str(theta) + '_t' + str(phi) + '_e' + str(int(ecc*100)) + '_L' + str(int(L/(cons.scale*1000)))
              
            cell_ell = layout.create_cell(name_ell)
              
            for s in grating_ell:
              cell_ell.shapes(GaP).insert(s)
              
              cell_ell.write(path + name_ell + '.gds') 