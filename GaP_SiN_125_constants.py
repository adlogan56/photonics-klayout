# Constants for photonic devices in 125nm GaP on 330nm/4um SiN/SiO2/Si, with a 230nm ridge etched into the SiN
# All lengths are in nanometers

scale = 20  # Layout resolution is 1/scale nm
res = 120   # Number of points in a circle


text_spec ={'h':4000*scale,\
            't':400*scale,\
            'd':2600*scale,\
            'res':36}
            

wg_spec = {'600TE':{'r':{},'w':{},'L':{}},\
           '600TM':{'r':{},'w':{},'L':{}}}
          
wg_spec['600TE']['r']['std'] = 1500*scale
wg_spec['600TE']['w']['wg'] = 160*scale
wg_spec['600TE']['w']['cr'] = 120*scale
wg_spec['600TE']['L']['cr'] = 2000*scale
wg_spec['600TE']['L']['adapt'] = 2000*scale
wg_spec['600TE']['L']['taper'] = 5000*scale
wg_spec['600TE']['L']['bz'] = 1500*scale

d_gr = [a*scale for a in [60,80,100,120,150,200,250,300]]
d_min = 50*scale

		  
gr_spec = {'600TE':{'shape':{}},\
          '600TM':{'shape':{}}}
          
gr_spec['600TE']['ribs'] = [max(0.975*a*scale,d_min) for a in [710,305,695,525,665,235,300,480]]
gr_spec['600TE']['gaps'] = [max(d_gr[i-1],d_min) for i in [2,6,7,2,6,2,5,5]]
gr_spec['600TE']['label'] = '0'
gr_spec['600TE']['shape']['str'] = {}
gr_spec['600TE']['shape']['str']['w'] = 1500*scale
gr_spec['600TE']['shape']['str']['L'] = 8000*scale
gr_spec['600TE']['shape']['ell'] = {}
gr_spec['600TE']['shape']['ell']['L'] = 8000*scale
gr_spec['600TE']['shape']['ell']['arc'] = 20
gr_spec['600TE']['shape']['ell']['theta'] = 30
gr_spec['600TE']['shape']['ell']['ecc'] = 0.1




ring_spec = {'disc':{}}

ring_spec['disc']['r420'] = {'cp':{}}
ring_spec['disc']['r420']['r'] = 420*scale
ring_spec['disc']['r420']['dr'] = round(0.5*scale)
ring_spec['disc']['r420']['cp']['600TE'] = {}
ring_spec['disc']['r420']['cp']['600TE']['20K'] = {}
ring_spec['disc']['r420']['cp']['600TE']['20K']['w'] = 130*scale
ring_spec['disc']['r420']['cp']['600TE']['20K']['d'] = 80*scale
ring_spec['disc']['r420']['cp']['600TE']['20K']['theta'] = 45
ring_spec['disc']['r420']['cp']['600TE']['50K'] = {}
ring_spec['disc']['r420']['cp']['600TE']['50K']['w'] = 130*scale
ring_spec['disc']['r420']['cp']['600TE']['50K']['d'] = 110*scale
ring_spec['disc']['r420']['cp']['600TE']['50K']['theta'] = 45
ring_spec['disc']['r420']['cp']['600TE']['100K'] = {}
ring_spec['disc']['r420']['cp']['600TE']['100K']['w'] = 130*scale
ring_spec['disc']['r420']['cp']['600TE']['100K']['d'] = 135*scale
ring_spec['disc']['r420']['cp']['600TE']['100K']['theta'] = 45
ring_spec['disc']['r420']['cp']['600TE']['200K'] = {}
ring_spec['disc']['r420']['cp']['600TE']['200K']['w'] = 130*scale
ring_spec['disc']['r420']['cp']['600TE']['200K']['d'] = 160*scale
ring_spec['disc']['r420']['cp']['600TE']['200K']['theta'] = 45


ring_spec['disc']['r700'] = {'cp':{}}
ring_spec['disc']['r700']['r'] = 700*scale
ring_spec['disc']['r700']['dr'] = round(0.5*scale)
ring_spec['disc']['r700']['cp']['600TE'] = {}
ring_spec['disc']['r700']['cp']['600TE']['20K'] = {}
ring_spec['disc']['r700']['cp']['600TE']['20K']['w'] = 130*scale
ring_spec['disc']['r700']['cp']['600TE']['20K']['d'] = 80*scale
ring_spec['disc']['r700']['cp']['600TE']['20K']['theta'] = 45
ring_spec['disc']['r700']['cp']['600TE']['50K'] = {}
ring_spec['disc']['r700']['cp']['600TE']['50K']['w'] = 130*scale
ring_spec['disc']['r700']['cp']['600TE']['50K']['d'] = 110*scale
ring_spec['disc']['r700']['cp']['600TE']['50K']['theta'] = 45
ring_spec['disc']['r700']['cp']['600TE']['100K'] = {}
ring_spec['disc']['r700']['cp']['600TE']['100K']['w'] = 130*scale
ring_spec['disc']['r700']['cp']['600TE']['100K']['d'] = 135*scale
ring_spec['disc']['r700']['cp']['600TE']['100K']['theta'] = 45
ring_spec['disc']['r700']['cp']['600TE']['200K'] = {}
ring_spec['disc']['r700']['cp']['600TE']['200K']['w'] = 130*scale
ring_spec['disc']['r700']['cp']['600TE']['200K']['d'] = 160*scale
ring_spec['disc']['r700']['cp']['600TE']['200K']['theta'] = 45





layout_spec = {'lr':{},\
               'gtest':{},\
			   'cp_ring':{},\
			   'multi_ring':{},\
			   'dc':{}}


layout_spec['gtest']['600TE'] = {}
layout_spec['gtest']['600TE']['offset'] = 4000*scale


layout_spec['multi_ring']['disc'] = {}

layout_spec['multi_ring']['disc']['r420'] = {'cp':{}}
layout_spec['multi_ring']['disc']['r420']['marker'] = (-6000*scale, 0*scale)
layout_spec['multi_ring']['disc']['r420']['label'] = (-11000*scale, 4500*scale)

layout_spec['multi_ring']['disc']['r700'] = {'cp':{}}
layout_spec['multi_ring']['disc']['r700']['marker'] = (-6000*scale, 0*scale)
layout_spec['multi_ring']['disc']['r700']['label'] = (-11000*scale, 4500*scale)


array_spec = {'lr':{},\
               'gtest':{},\
			   'cp_ring':{},\
			   'multi_ring':{},\
			   'dc':{}}

array_spec['multi_ring']['disc'] = {}

array_spec['multi_ring']['disc']['r420'] = {}
array_spec['multi_ring']['disc']['r420']['x'] = (20000*scale,0*scale)
array_spec['multi_ring']['disc']['r420']['y'] = (0*scale,30000*scale)
array_spec['multi_ring']['disc']['r420']['x_num'] = 10

array_spec['multi_ring']['disc']['r700'] = {}
array_spec['multi_ring']['disc']['r700']['x'] = (20000*scale,0*scale)
array_spec['multi_ring']['disc']['r700']['y'] = (0*scale,30000*scale)
array_spec['multi_ring']['disc']['r700']['x_num'] = 10



array_spec['gtest']['600TE'] = {}
array_spec['gtest']['600TE']['x'] = (5000*scale, 5000*scale)
array_spec['gtest']['600TE']['y'] = (20000*scale, -14500*scale)
array_spec['gtest']['600TE']['rep'] = 3



