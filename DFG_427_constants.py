# Constants for SHG/DFG devices in 427nm GaP on SiO2
# Wavelength modes are designated: 1-1550TE, 2-1080TE, 3-637TM, 4-775TM, 5-Multiple (SHG), 6-Multiple (DFG)
# All lengths are in nanometers

scale = 20  # Layout resolution is 1/scale nm
res = 120   # Number of points in a circle


text_spec ={'h':4000*scale,\
            't':400*scale,\
            'd':2600*scale,\
            'res':36}

# Waveguide curve radii for each wavelength. Loss ring radius is 1.2x waveguide radius.
# Note that most of the loss is in the transition from straight to curve
       # Define waveguide spec types with dictionaries for radius, widths, and lengths
       
wg_spec = {'1550TE':{'r':{},'w':{},'L':{}},\
                    '1080TE':{'r':{},'w':{},'L':{}},\
                    '637TM':{'r':{},'w':{},'L':{}},\
                    '775TM':{'r':{},'w':{},'L':{}},\
                    'IR':{'r':{},'w':{},'L':{}},\
                    'Multi':{'r':{},'w':{},'L':{}}}

wg_spec['1550TE']['r']['std'] = 4000*scale   #S
wg_spec['1550TE']['w']['wg'] = 450*scale    
wg_spec['1550TE']['w']['mf'] = 370*scale    
wg_spec['1550TE']['L']['adapt'] = 4000*scale
wg_spec['1550TE']['L']['taper'] = 8000*scale
wg_spec['1550TE']['L']['bz'] = 2000*scale

wg_spec['1080TE']['r']['std'] = 3000*scale    #
wg_spec['1080TE']['w']['wg'] = 340*scale    
wg_spec['1080TE']['w']['mf'] = 180*scale    
wg_spec['1080TE']['L']['adapt'] = 3500*scale
wg_spec['1080TE']['L']['taper'] = 6000*scale
wg_spec['1080TE']['L']['bz'] = 5000*scale

wg_spec['637TM']['r']['std'] = 2500*scale   #
wg_spec['637TM']['w']['wg'] = 60*scale
wg_spec['637TM']['w']['mf'] = 40*scale                # Some waveguide specs have mode filters defined
wg_spec['637TM']['L']['mf'] = 2000*scale    #
wg_spec['637TM']['L']['adapt'] = 2000*scale
wg_spec['637TM']['L']['taper'] = 3000*scale
wg_spec['637TM']['L']['bz'] = 1500*scale

wg_spec['775TM']['r']['std'] = 2500*scale   #
wg_spec['775TM']['w']['wg'] = 100*scale
wg_spec['775TM']['w']['mf'] = 40*scale
wg_spec['775TM']['L']['mf'] = 2500*scale    #
wg_spec['775TM']['L']['adapt'] = 2500*scale
wg_spec['775TM']['L']['taper'] = 4000*scale
wg_spec['775TM']['L']['bz'] = 1750*scale

wg_spec['Multi']['r']['std'] = 4000*scale     #
wg_spec['Multi']['w']['wg'] = 420*scale
wg_spec['Multi']['L']['adapt'] = 4000*scale
wg_spec['Multi']['L']['taper'] = 6000*scale
wg_spec['Multi']['L']['bz'] = 5000*scale

wg_spec['IR']['r']['std'] = 4000*scale     #
wg_spec['IR']['w']['wg'] = 400*scale
wg_spec['IR']['L']['adapt'] = 4000*scale
wg_spec['IR']['L']['taper'] = 6000*scale
wg_spec['IR']['L']['bz'] = 4000*scale


ring_spec = {'1550TE':{},\
             '1080TE':{},\
             '637TM':{},\
             '775TM':{},\
             'SHG':{},\
             'DFG':{}}

ring_spec['DFG']['SR003minus_5305'] = {'cp':{}}  # Design from October 2019; single ring, 1550/1080/637, TE00/TE00/TM03, M1+M2-M3 = -2, center radius 5305nm
ring_spec['DFG']['SR003minus_5305']['w'] = 690*scale #Ring width, in nm
ring_spec['DFG']['SR003minus_5305']['r'] = 4960*scale  #Ring inner radius
ring_spec['DFG']['SR003minus_5305']['dw'] = round(0.5*scale)
ring_spec['DFG']['SR003minus_5305']['label'] = '401'
ring_spec['DFG']['SR003minus_5305']['cp']['IR'] = {} #  Simultaneous 1080TE and 1550TE
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['50K'] = {}  #Simulated ~45K 1080, ~45K 1550
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['50K']['d'] = 180*scale
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['50K']['w'] = 320*scale 
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['50K']['theta'] = 120  
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['100K'] = {}  #Simulated ~100K 1080, ~90K 1550
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['100K']['d'] = 200*scale
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['100K']['w'] = 320*scale 
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['100K']['theta'] = 120  
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['250K'] = {}  #Simulated ~240K 1080, ~125K 1550
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['250K']['d'] = 220*scale
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['250K']['w'] = 320*scale
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['250K']['theta'] = 120
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['500K'] = {}  #Simulated ~650K 1080, ~170K 1550
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['500K']['d'] = 240*scale
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['500K']['w'] = 320*scale  
ring_spec['DFG']['SR003minus_5305']['cp']['IR']['500K']['theta'] = 120
ring_spec['DFG']['SR003minus_5305']['cp']['637TM'] = {}
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['20K'] = {}  #Simulated ~20K
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['20K']['d'] = 200*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['20K']['w'] = 50*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['20K']['theta'] = 90
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['50K'] = {}  #Simulated ~56K
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['50K']['d'] = 215*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['50K']['w'] = 50*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['50K']['theta'] = 90
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['100K'] = {} #Simulated ~113K
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['100K']['d'] = 225*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['100K']['w'] = 50*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['100K']['theta'] = 90
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['150K'] = {} #Simulated ~160K
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['150K']['d'] = 230*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['150K']['w'] = 50*scale
ring_spec['DFG']['SR003minus_5305']['cp']['637TM']['150K']['theta'] = 90


ring_spec['DFG']['SR014minus_4225'] = {'cp':{}}  # Design from October 2019; single ring, 1550/1080/637, TE00/TE01/TM04, M1+M2-M3 = -2, center radius 4225nm 
ring_spec['DFG']['SR014minus_4225']['w'] = 810*scale #Ring width, in nm
ring_spec['DFG']['SR014minus_4225']['r'] = 3820*scale  #Ring inner radius
ring_spec['DFG']['SR014minus_4225']['dw'] = round(0.5*scale)
ring_spec['DFG']['SR014minus_4225']['label'] = '402'
ring_spec['DFG']['SR014minus_4225']['cp']['IR'] = {} #  Simultaneous 1080TE and 1550TE
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['200K'] = {}  # Simulated ~225K 1080, 125K 1550
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['200K']['d'] = 140*scale
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['200K']['w'] = 300*scale 
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['200K']['L'] = 5000*scale
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['400K'] = {}  # Simulated ~400K 1080, ~225K 1550
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['400K']['d'] = 160*scale
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['400K']['w'] = 300*scale 
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['400K']['L'] = 5000*scale
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['750K'] = {}  # Simulated ~735K 1080, 355K 1550
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['750K']['d'] = 180*scale
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['750K']['w'] = 300*scale 
ring_spec['DFG']['SR014minus_4225']['cp']['IR']['750K']['L'] = 5000*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM'] = {}
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['20K'] = {}  #Simulated 22K
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['20K']['d'] = 160*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['20K']['w'] = 40*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['20K']['theta'] = 45
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['50K'] = {}  #Simulated ~52K
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['50K']['d'] = 175*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['50K']['w'] = 40*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['50K']['theta'] = 45
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['100K'] = {}  #Simulated ~92K
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['100K']['d'] = 185*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['100K']['w'] = 40*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['100K']['theta'] = 45
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['150K'] = {}  #Simulated ~165K
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['150K']['d'] = 195*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['150K']['w'] = 40*scale
ring_spec['DFG']['SR014minus_4225']['cp']['637TM']['150K']['theta'] = 45





# Grating Specs
d_min = 50*scale
gr_spec = {'1550TE':{'shape':{}},\
                    '1080TE':{'shape':{}},\
                    '637TM':{'shape':{}},\
                    '775TM':{'shape':{}},\
                    'SHG':{'shape':{}},\
                    'IR':{'shape':{}},\
                    'DFG':{'shape':{}}}

#Modified DFG427 Chip 2 2TE design
gr_spec['IR']['ribs'] = [a*scale for a in [630,505,600,610,115,235,245,50]]
gr_spec['IR']['gaps'] = [a*scale for a in [50,100,50,300,300,300,150,200]]
gr_spec['IR']['label'] = '6'
gr_spec['IR']['shape']['str'] = {}
gr_spec['IR']['shape']['str']['w'] = 2500*scale
gr_spec['IR']['shape']['str']['L'] = 10000*scale
gr_spec['IR']['shape']['ell'] = {}
gr_spec['IR']['shape']['ell']['L'] = 12000*scale
gr_spec['IR']['shape']['ell']['arc'] = 25
gr_spec['IR']['shape']['ell']['theta'] = 30
gr_spec['IR']['shape']['ell']['ecc'] = 0.15

#DFG427 Chip 1 design
correction_3TM = 637.0/631;
gr_spec['637TM']['ribs'] = [max(d_min, round(a*correction_3TM*scale)) for a in [180,320,170,170,170,160,240]]
gr_spec['637TM']['gaps'] = [max(d_min, round(a*correction_3TM*scale)) for a in [50,50,50,150,150,150,150]]
gr_spec['637TM']['label'] = '0'
gr_spec['637TM']['shape']['str'] = {}
gr_spec['637TM']['shape']['str']['w'] = 1500*scale
gr_spec['637TM']['shape']['str']['L'] = 8000*scale
gr_spec['637TM']['shape']['ell'] = {}
gr_spec['637TM']['shape']['ell']['L'] = 10000*scale
gr_spec['637TM']['shape']['ell']['arc'] = 20
gr_spec['637TM']['shape']['ell']['theta'] = 45
gr_spec['637TM']['shape']['ell']['ecc'] = 0.1

gr_spec['637TM']['shape']['str']['L_total'] = gr_spec['637TM']['shape']['str']['L'] +  sum(gr_spec['637TM']['ribs']) + sum(gr_spec['637TM']['ribs'])
gr_spec['637TM']['shape']['ell']['L_total'] = gr_spec['637TM']['shape']['ell']['L'] +  sum(gr_spec['637TM']['ribs']) + sum(gr_spec['637TM']['ribs'])

gr_spec['IR']['shape']['str']['L_total'] = gr_spec['IR']['shape']['str']['L'] +  sum(gr_spec['IR']['ribs']) + sum(gr_spec['IR']['ribs'])
gr_spec['IR']['shape']['ell']['L_total'] = gr_spec['IR']['shape']['ell']['L'] +  sum(gr_spec['IR']['ribs']) + sum(gr_spec['IR']['ribs'])



# Layout specifications

layout_spec = {'gtest':{},\
			   'cp_ring':{}}



layout_spec['gtest']['1550TE'] = {}
layout_spec['gtest']['1550TE']['offset'] = 5000*scale

layout_spec['gtest']['1080TE'] = {}
layout_spec['gtest']['1080TE']['offset'] = 4000*scale

layout_spec['gtest']['637TM'] = {}
layout_spec['gtest']['637TM']['offset'] = 4000*scale

layout_spec['gtest']['775TM'] = {}
layout_spec['gtest']['775TM']['offset'] = 4000*scale

layout_spec['gtest']['SHG'] = {}
layout_spec['gtest']['SHG']['offset'] = 5000*scale

layout_spec['gtest']['DFG'] = {}
layout_spec['gtest']['DFG']['offset'] = 5000*scale

layout_spec['gtest']['IR'] = {}
layout_spec['gtest']['IR']['offset'] = 4000*scale




#Layout specification for coupled ring resonators
#Each entry should have (x,y) coordinates 'marker' and 'label' and a dictionary 'cp' containing coupling specs
#Each 'cp' entry should contain an angle 'theta', the angular position (in degrees) of the center of the coupling region. 0 is the right (+x) side of the circle, increasing ccw

layout_spec['cp_ring']['DFG'] = {}



layout_spec['cp_ring']['DFG']['SR003minus_5305'] = {'cp':{}}
layout_spec['cp_ring']['DFG']['SR003minus_5305']['marker'] = (7000*scale, 7000*scale)
layout_spec['cp_ring']['DFG']['SR003minus_5305']['label'] = (7000*scale, -27500*scale)
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std'] = {'IR':{},'637TM':{}}
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['theta'] = 180
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['in']['orient'] = 1     # orientation of the input grating coupler. 0 is up, 1 is left, etc
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['in']['curl'] = 'ccw'   # input circuit tends to bend counter-clockwise (defaults to clockwise)
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['in']['pt'] = (5000*scale, -38000*scale)   #Intended input to grating coupler?
#layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['in']['min'][0] = 15000*scale
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['in']['min'][3] = 20000*scale
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['out']['pt'] = (0*scale, -20000*scale)
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['IR']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['theta'] = 0
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['in']['pt'] = (7000*scale, -20000*scale)
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['out']['pt'] = (11000*scale, -4000*scale)
#layout_spec['cp_ring']['DFG']['SR003minus_5305']['cp']['std']['637TM']['out']['min'][3] = 21000*scale

layout_spec['cp_ring']['DFG']['SR014minus_4225'] = {'cp':{}}
layout_spec['cp_ring']['DFG']['SR014minus_4225']['marker'] = (7000*scale, 5000*scale)
layout_spec['cp_ring']['DFG']['SR014minus_4225']['label'] = (12500*scale, 4000*scale)
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std'] = {'IR':{},'637TM':{}}
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['theta'] = 180
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['in']['orient'] = 1     # orientation of the input grating coupler. 0 is up, 1 is left, etc
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['in']['curl'] = 'ccw'   # input circuit tends to bend counter-clockwise (defaults to clockwise)
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['in']['pt'] = (15000*scale, -24000*scale)   #Intended input to grating coupler?
#layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['in']['min'][0] = 15000*scale
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['in']['min'][3] = 22000*scale
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['out']['pt'] = (0*scale, -20000*scale)
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['IR']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['theta'] = 0
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['in']['pt'] = (8500*scale, -17000*scale)
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['out']['pt'] = (11000*scale, -2000*scale)
#layout_spec['cp_ring']['DFG']['SR014minus_4225']['cp']['std']['637TM']['out']['min'][3] = 21000*scale



#Device array specifications

array_spec = {'lr':{},\
			  'gtest':{},\
			  'cp_ring':{},\
			  'dc':{}}
			  

array_spec['gtest']['1550TE'] = {}
array_spec['gtest']['1550TE']['x'] = (8500*scale, 8500*scale)
array_spec['gtest']['1550TE']['y'] = (32000*scale, -24000*scale)
array_spec['gtest']['1550TE']['rep'] = 3

array_spec['gtest']['1080TE'] = {}
array_spec['gtest']['1080TE']['x'] = (7500*scale, 7500*scale)
array_spec['gtest']['1080TE']['y'] = (27000*scale, -22000*scale)
array_spec['gtest']['1080TE']['rep'] = 3

array_spec['gtest']['637TM'] = {}
array_spec['gtest']['637TM']['x'] = (5000*scale, 5000*scale)
array_spec['gtest']['637TM']['y'] = (20000*scale, -14500*scale)
array_spec['gtest']['637TM']['rep'] = 3

array_spec['gtest']['775TM'] = {}
array_spec['gtest']['775TM']['x'] = (6000*scale, 6000*scale)
array_spec['gtest']['775TM']['y'] = (22000*scale, -17000*scale)
array_spec['gtest']['775TM']['rep'] = 3

array_spec['gtest']['SHG'] = {}
array_spec['gtest']['SHG']['x'] = (10500*scale, 10500*scale)
array_spec['gtest']['SHG']['y'] = (38000*scale, -28000*scale)
array_spec['gtest']['SHG']['rep'] = 3

array_spec['gtest']['IR'] = {}
array_spec['gtest']['IR']['x'] = (10500*scale, 10500*scale)
array_spec['gtest']['IR']['y'] = (38000*scale, -28000*scale)
array_spec['gtest']['IR']['rep'] = 3

array_spec['gtest']['DFG'] = {}
array_spec['gtest']['DFG']['x'] = (9000*scale, 9000*scale)
array_spec['gtest']['DFG']['y'] = (33000*scale, -24500*scale)
array_spec['gtest']['DFG']['rep'] = 3



array_spec['cp_ring']['SR003minus_5305'] = {}
array_spec['cp_ring']['SR003minus_5305']['std'] = {}
array_spec['cp_ring']['SR003minus_5305']['std']['x'] = (31000*scale, 0*scale)
array_spec['cp_ring']['SR003minus_5305']['std']['y'] = (0*scale, 64000*scale)
array_spec['cp_ring']['SR003minus_5305']['std']['x_num'] = 10

array_spec['cp_ring']['SR014minus_4225'] = {}
array_spec['cp_ring']['SR014minus_4225']['std'] = {}
array_spec['cp_ring']['SR014minus_4225']['std']['x'] = (31000*scale, 0*scale)
array_spec['cp_ring']['SR014minus_4225']['std']['y'] = (0*scale, 47000*scale)
array_spec['cp_ring']['SR014minus_4225']['std']['x_num'] = 10