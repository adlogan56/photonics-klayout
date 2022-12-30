# Constants for SHG/DFG devices in 250nm GaP on 250 nm SiNx on SiO2
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
                    'Multi':{'r':{},'w':{},'L':{}}}

wg_spec['1550TE']['r']['std'] = 4000*scale
wg_spec['1550TE']['w']['wg'] = 550*scale
wg_spec['1550TE']['w']['cr'] = 500*scale
wg_spec['1550TE']['L']['cr'] = 4000*scale
wg_spec['1550TE']['L']['adapt'] = 4000*scale
wg_spec['1550TE']['L']['taper'] = 8000*scale
wg_spec['1550TE']['L']['bz'] = 2500*scale

wg_spec['1080TE']['r']['std'] = 3000*scale
wg_spec['1080TE']['w']['wg'] = 350*scale
wg_spec['1080TE']['w']['mf'] = 300*scale
wg_spec['1080TE']['w']['cr'] = 250*scale
wg_spec['1080TE']['L']['cr'] = 3000*scale
wg_spec['1080TE']['L']['adapt'] = 3500*scale
wg_spec['1080TE']['L']['taper'] = 6000*scale
wg_spec['1080TE']['L']['bz'] = 3000*scale

wg_spec['637TM']['r']['std'] = 2500*scale
wg_spec['637TM']['w']['wg'] = 120*scale
wg_spec['637TM']['w']['mf'] = 80*scale                # Some waveguide specs have mode filters defined
wg_spec['637TM']['w']['cr'] = 100*scale
wg_spec['637TM']['L']['cr'] = 2000*scale
wg_spec['637TM']['L']['mf'] = 2000*scale
wg_spec['637TM']['L']['adapt'] = 2000*scale
wg_spec['637TM']['L']['taper'] = 3000*scale
wg_spec['637TM']['L']['bz'] = 1500*scale

wg_spec['775TM']['r']['std'] = 2500*scale
wg_spec['775TM']['w']['wg'] = 160*scale
#wg_spec['775TM']['w']['mf'] = 110*scale
wg_spec['775TM']['w']['cr'] = 120*scale
wg_spec['775TM']['L']['cr'] = 2000*scale
wg_spec['775TM']['L']['mf'] = 2500*scale
wg_spec['775TM']['L']['adapt'] = 2500*scale
wg_spec['775TM']['L']['taper'] = 4000*scale
wg_spec['775TM']['L']['bz'] = 2000*scale

wg_spec['Multi']['r']['std'] = 4000*scale
wg_spec['Multi']['w']['wg'] = 500*scale
wg_spec['Multi']['w']['cr'] = 500*scale
wg_spec['Multi']['L']['cr'] = 1000*scale
wg_spec['Multi']['L']['adapt'] = 4000*scale
wg_spec['Multi']['L']['taper'] = 6000*scale
wg_spec['Multi']['L']['bz'] = 5000*scale

# Ring resonators specs: (radius,width) accessed by type (eg. SHG or 1550TE) then variant (eg. v1)
# Define categories of ring resonator specifications
ring_spec = {'1550TE':{},\
             '1080TE':{},\
             '637TM':{},\
             '775TM':{},\
             'SHG':{},\
             'DFG':{}}

ring_spec['1550TE']['lr_v1'] = {'cp':{}}                                     # Define 'lr_v1' variant of '1550TE' ring type with dictionary for coupling specs
ring_spec['1550TE']['lr_v1']['w'] = 700*scale                           # Define ring width and radius
ring_spec['1550TE']['lr_v1']['r'] = 8000*scale
ring_spec['1550TE']['lr_v1']['label'] = '1'
ring_spec['1550TE']['lr_v1']['cp']['1550TE'] = {}                             # Define coupling specs for 1550TE wavelength
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['45K'] = {}                       # Define '45K' coupling spec
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['45K']['w'] = 560*scale           # This variant uses a custom waveguide width instead of the standard for this waveguide type 
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['45K']['d'] = 220*scale           # This is a wrapped coupling region, so both distance and angle are defined
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['45K']['theta'] = 45          
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['200K'] = {}
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['200K']['w'] = 560*scale
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['200K']['d'] = 300*scale
ring_spec['1550TE']['lr_v1']['cp']['1550TE']['200K']['theta'] = 45

ring_spec['637TM']['lr_v1'] = {'cp':{}}
ring_spec['637TM']['lr_v1']['w'] = 300*scale
ring_spec['637TM']['lr_v1']['r'] = 8000*scale
ring_spec['637TM']['lr_v1']['label'] = '3'
ring_spec['637TM']['lr_v1']['cp']['637TM'] = {}  
ring_spec['637TM']['lr_v1']['cp']['637TM']['16K'] = {}
ring_spec['637TM']['lr_v1']['cp']['637TM']['16K']['w'] = 150*scale
ring_spec['637TM']['lr_v1']['cp']['637TM']['16K']['d'] = 80*scale
ring_spec['637TM']['lr_v1']['cp']['637TM']['16K']['theta'] = 70
ring_spec['637TM']['lr_v1']['cp']['637TM']['80K'] = {}
ring_spec['637TM']['lr_v1']['cp']['637TM']['80K']['w'] = 150*scale
ring_spec['637TM']['lr_v1']['cp']['637TM']['80K']['d'] = 120*scale
ring_spec['637TM']['lr_v1']['cp']['637TM']['80K']['theta'] = 70

ring_spec['637TM']['lr_v2'] = {'cp':{}}
ring_spec['637TM']['lr_v2']['w'] = 300*scale
ring_spec['637TM']['lr_v2']['r'] = 8000*scale
ring_spec['637TM']['lr_v2']['label'] = '3'
ring_spec['637TM']['lr_v2']['cp']['637TM'] = {}  
ring_spec['637TM']['lr_v2']['cp']['637TM']['20K'] = {}
ring_spec['637TM']['lr_v2']['cp']['637TM']['20K']['w'] = 120*scale
ring_spec['637TM']['lr_v2']['cp']['637TM']['20K']['d'] = 80*scale
ring_spec['637TM']['lr_v2']['cp']['637TM']['20K']['theta'] = 15
ring_spec['637TM']['lr_v2']['cp']['637TM']['50K'] = {}
ring_spec['637TM']['lr_v2']['cp']['637TM']['50K']['w'] = 120*scale
ring_spec['637TM']['lr_v2']['cp']['637TM']['50K']['d'] = 100*scale
ring_spec['637TM']['lr_v2']['cp']['637TM']['50K']['theta'] = 15
ring_spec['637TM']['lr_v2']['cp']['637TM']['200K'] = {}
ring_spec['637TM']['lr_v2']['cp']['637TM']['200K']['w'] = 120*scale
ring_spec['637TM']['lr_v2']['cp']['637TM']['200K']['d'] = 130*scale
ring_spec['637TM']['lr_v2']['cp']['637TM']['200K']['theta'] = 15




ring_spec['SHG']['SR003_R7770_W940'] = {'cp':{}}
ring_spec['SHG']['SR003_R7770_W940']['w'] = 940*scale
ring_spec['SHG']['SR003_R7770_W940']['r'] = 7300*scale
ring_spec['SHG']['SR003_R7770_W940']['label'] = '501'
ring_spec['SHG']['SR003_R7770_W940']['dw'] = round(0.5*scale)
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE'] = {}
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['50K'] = {}
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['50K']['d'] = 240*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['50K']['w'] = 440*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['50K']['theta'] = 45
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['160K'] = {}
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['160K']['d'] = 360*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['160K']['w'] = 440*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['1550TE']['160K']['theta'] = 45
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM'] = {}
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['18K'] = {}
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['18K']['d'] = 160*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['18K']['w'] = 120*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['18K']['theta'] = 30
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['56K'] = {}
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['56K']['d'] = 190*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['56K']['w'] = 120*scale
ring_spec['SHG']['SR003_R7770_W940']['cp']['775TM']['56K']['theta'] = 30





d_gr = [a*scale for a in [50, 75, 100, 150, 200, 250, 300]]
d_min = 50*scale


gr_spec = {'1550TE':{'shape':{}},\
                    '637TM':{'shape':{}},\
                    '775TM':{'shape':{}}}

gr_spec['1550TE']['ribs'] = [max(1*a*scale,d_min) for a in [645,495,140,670,285,325,760,750,285]]
gr_spec['1550TE']['gaps'] = [max(1*d_gr[i-1],d_min) for i in [1,4,1,7,3,4,4,4,6]]
gr_spec['1550TE']['label'] = '0'
gr_spec['1550TE']['shape']['str'] = {}
gr_spec['1550TE']['shape']['str']['w'] = 3500*scale
gr_spec['1550TE']['shape']['str']['L'] = 12000*scale
gr_spec['1550TE']['shape']['ell'] = {}
gr_spec['1550TE']['shape']['ell']['L'] = 12000*scale
gr_spec['1550TE']['shape']['ell']['arc'] = 30
gr_spec['1550TE']['shape']['ell']['theta'] = 30
gr_spec['1550TE']['shape']['ell']['ecc'] = 0.1

#gr_spec['1080TE']['ribs'] = [max(1.00*a*scale,d_min) for a in [105,445,780,550,560,80,245,710]]
#gr_spec['1080TE']['gaps'] = [max(1.00*d_gr[i-1],d_min) for i in [4,2,7,7,1,7,6,2]]
#gr_spec['1080TE']['label'] = '1'
#gr_spec['1080TE']['shape']['str'] = {}
#gr_spec['1080TE']['shape']['str']['w'] = 2500*scale
#gr_spec['1080TE']['shape']['str']['L'] = 10000*scale
#gr_spec['1080TE']['shape']['ell'] = {}
#gr_spec['1080TE']['shape']['ell']['L'] = 10000*scale
#gr_spec['1080TE']['shape']['ell']['arc'] = 30
#gr_spec['1080TE']['shape']['ell']['theta'] = 20
#gr_spec['1080TE']['shape']['ell']['ecc'] = 0.1

gr_spec['637TM']['ribs'] = [max(0.98*a*scale,d_min) for a in [385,310,615,310,265,205,280,135,710]]
gr_spec['637TM']['gaps'] = [max(0.98*d_gr[i-1],d_min) for i in [1,5,5,4,5,2,7,5,1]]
gr_spec['637TM']['label'] = '2'
gr_spec['637TM']['shape']['str'] = {}
gr_spec['637TM']['shape']['str']['w'] = 1500*scale
gr_spec['637TM']['shape']['str']['L'] = 8000*scale
gr_spec['637TM']['shape']['ell'] = {}
gr_spec['637TM']['shape']['ell']['L'] = 6000*scale
gr_spec['637TM']['shape']['ell']['arc'] = 25
gr_spec['637TM']['shape']['ell']['theta'] = 30
gr_spec['637TM']['shape']['ell']['ecc'] = 0.1

gr_spec['775TM']['ribs'] = [max(1.04*a*scale,d_min) for a in [540,225,150,485,555,465,795,495,165]]
gr_spec['775TM']['gaps'] = [max(1.04*d_gr[i-1],d_min) for i in [1,2,6,5,1,7,6,6,3]]
gr_spec['775TM']['label'] = '3'
gr_spec['775TM']['shape']['str'] = {}
gr_spec['775TM']['shape']['str']['w'] = 1800*scale
gr_spec['775TM']['shape']['str']['L'] = 8000*scale
gr_spec['775TM']['shape']['ell'] = {}
gr_spec['775TM']['shape']['ell']['L'] = 8000*scale
gr_spec['775TM']['shape']['ell']['arc'] = 25
gr_spec['775TM']['shape']['ell']['theta'] = 30
gr_spec['775TM']['shape']['ell']['ecc'] = 0.1

#gr_spec['SHG']['ribs'] = [max((1/0.982)*a*scale,d_min) for a in  [240,775,520,470,625,295,790,255,725]]
#gr_spec['SHG']['gaps'] = [max(d_gr[i-1],d_min) for i in [2,2,2,1,6,2,4,7,6]]
#gr_spec['SHG']['label'] = '4'
#gr_spec['SHG']['shape']['str'] = {}
#gr_spec['SHG']['shape']['str']['w'] = 3500*scale
#gr_spec['SHG']['shape']['str']['L'] = 12000*scale
#gr_spec['SHG']['shape']['ell'] = {}
#gr_spec['SHG']['shape']['ell']['L'] = 10000*scale
#gr_spec['SHG']['shape']['ell']['arc'] = 25
#gr_spec['SHG']['shape']['ell']['theta'] = 30
#gr_spec['SHG']['shape']['ell']['ecc'] = 0.15

# gr_spec['SHG_old']['ribs'] = [max(0.99*a*scale,d_min) for a in  [280,510,260,580,600,290,710,520,490,130,430,170,750,170,770,790,470,180,50]]
# gr_spec['SHG_old']['gaps'] = [max(0.99*d_gr[i-1],d_min) for i in [1,1,1,1,1,3,2,7,5,3,1,3,1,1,1,2,4,4,5 ]]
# gr_spec['SHG_old']['label'] = '4'
# gr_spec['SHG_old']['shape']['str'] = {}
# gr_spec['SHG_old']['shape']['str']['w'] = 3500*scale
# gr_spec['SHG_old']['shape']['str']['L'] = 12000*scale
# gr_spec['SHG_old']['shape']['ell'] = {}
# gr_spec['SHG_old']['shape']['ell']['L'] = 12000*scale
# gr_spec['SHG_old']['shape']['ell']['arc'] = 30
# gr_spec['SHG_old']['shape']['ell']['theta'] = 30
# gr_spec['SHG_old']['shape']['ell']['ecc'] = 0.1

#gr_spec['DFG']['ribs'] = [max(0.97*a*scale,d_min) for a in [380,380,380,630,740,490,540,190,180,620]]
#gr_spec['DFG']['gaps'] = [max(0.97*d_gr[i-1],d_min) for i in [7,1,1,1,3,7,3,7,6,5]]
#gr_spec['DFG']['label'] = '5'
#gr_spec['DFG']['shape']['str'] = {}
#gr_spec['DFG']['shape']['str']['w'] = 3500*scale
#gr_spec['DFG']['shape']['str']['L'] = 12000*scale
#gr_spec['DFG']['shape']['ell'] = {}
#gr_spec['DFG']['shape']['ell']['L'] = 12000*scale
#gr_spec['DFG']['shape']['ell']['arc'] = 30
#gr_spec['DFG']['shape']['ell']['theta'] = 30
#gr_spec['DFG']['shape']['ell']['ecc'] = 0.1


gr_spec['1550TE']['shape']['str']['L_total'] = gr_spec['1550TE']['shape']['str']['L'] +  sum(gr_spec['1550TE']['ribs']) + sum(gr_spec['1550TE']['ribs'])
gr_spec['1550TE']['shape']['ell']['L_total'] = gr_spec['1550TE']['shape']['ell']['L'] +  sum(gr_spec['1550TE']['ribs']) + sum(gr_spec['1550TE']['ribs'])

#gr_spec['1080TE']['shape']['str']['L_total'] = gr_spec['1080TE']['shape']['str']['L'] +  sum(gr_spec['1080TE']['ribs']) + sum(gr_spec['1080TE']['ribs'])
#gr_spec['1080TE']['shape']['ell']['L_total'] = gr_spec['1080TE']['shape']['ell']['L'] +  sum(gr_spec['1080TE']['ribs']) + sum(gr_spec['1080TE']['ribs'])

gr_spec['637TM']['shape']['str']['L_total'] = gr_spec['637TM']['shape']['str']['L'] +  sum(gr_spec['637TM']['ribs']) + sum(gr_spec['637TM']['ribs'])
gr_spec['637TM']['shape']['ell']['L_total'] = gr_spec['637TM']['shape']['ell']['L'] +  sum(gr_spec['637TM']['ribs']) + sum(gr_spec['637TM']['ribs'])

gr_spec['775TM']['shape']['str']['L_total'] = gr_spec['775TM']['shape']['str']['L'] +  sum(gr_spec['775TM']['ribs']) + sum(gr_spec['775TM']['ribs'])
gr_spec['775TM']['shape']['ell']['L_total'] = gr_spec['775TM']['shape']['ell']['L'] +  sum(gr_spec['775TM']['ribs']) + sum(gr_spec['775TM']['ribs'])

#gr_spec['SHG']['shape']['str']['L_total'] = gr_spec['SHG']['shape']['str']['L'] +  sum(gr_spec['SHG']['ribs']) + sum(gr_spec['SHG']['ribs'])
#gr_spec['SHG']['shape']['ell']['L_total'] = gr_spec['SHG']['shape']['ell']['L'] +  sum(gr_spec['SHG']['ribs']) + sum(gr_spec['SHG']['ribs'])

#gr_spec['DFG']['shape']['str']['L_total'] = gr_spec['DFG']['shape']['str']['L'] +  sum(gr_spec['DFG']['ribs']) + sum(gr_spec['DFG']['ribs'])
#gr_spec['DFG']['shape']['ell']['L_total'] = gr_spec['DFG']['shape']['ell']['L'] +  sum(gr_spec['DFG']['ribs']) + sum(gr_spec['DFG']['ribs'])



# Layout specifications

layout_spec = {'gtest':{},\
			   'cp_ring':{}}


layout_spec['gtest']['1550TE'] = {}
layout_spec['gtest']['1550TE']['offset'] = 5000*scale

#layout_spec['gtest']['1080TE'] = {}
#layout_spec['gtest']['1080TE']['offset'] = 4000*scale

layout_spec['gtest']['637TM'] = {}
layout_spec['gtest']['637TM']['offset'] = 4000*scale

layout_spec['gtest']['775TM'] = {}
layout_spec['gtest']['775TM']['offset'] = 4000*scale

#layout_spec['gtest']['SHG'] = {}
#layout_spec['gtest']['SHG']['offset'] = 5000*scale

#layout_spec['gtest']['DFG'] = {}
#layout_spec['gtest']['DFG']['offset'] = 5000*scale



layout_spec['cp_ring']['1550TE'] = {}

layout_spec['cp_ring']['1550TE']['lr_v1'] = {'cp':{}}
#layout_spec['cp_ring']['1550TE']['lr_v1']['marker'] = (6000*scale, -14000*scale)
#layout_spec['cp_ring']['1550TE']['lr_v1']['label'] = (-1000*scale, -16000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['marker'] = (0000*scale, -13000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['label'] = (-5500*scale, -15000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std'] = {'1550TE':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['theta'] = 180
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['in']['pt'] = (6000*scale, -42000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['in']['min'][0] = 10000*scale
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['in']['min'][3] = 14000*scale
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['out']['pt'] = (-7000*scale, -16000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['std']['1550TE']['out']['curl'] = 'ccw'


layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp'] = {'1550TE':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['theta'] = 180
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['in']['orient'] = 2
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['in']['pt'] = (20000*scale, -16000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['in']['min'][0] = 20000*scale
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['in']['min'][3] = 12000*scale
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['out']['orient'] = 3
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['out']['pt'] = (-1000*scale, -42000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['inp']['1550TE']['out']['curl'] = 'ccw'


layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['drop'] = {'1550TE':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['drop']['1550TE']['theta'] = 0
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['drop']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['drop']['1550TE']['in']['orient'] = 2
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['drop']['1550TE']['in']['pt'] = (-5000*scale, -16000*scale)
layout_spec['cp_ring']['1550TE']['lr_v1']['cp']['drop']['1550TE']['in']['curl'] = 'ccw'



layout_spec['cp_ring']['637TM'] = {}

layout_spec['cp_ring']['637TM']['lr_v1'] = {'cp':{}}
layout_spec['cp_ring']['637TM']['lr_v1']['marker'] = (6000*scale, -14000*scale)
layout_spec['cp_ring']['637TM']['lr_v1']['label'] = (-1000*scale, -16000*scale)
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std'] = {'637TM':{}}
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['theta'] = 180
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['in']['orient'] = 1
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['in']['pt'] = (8000*scale, -25000*scale)
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['in']['min'][0] = 10000*scale
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['in']['min'][3] = 12000*scale
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['out']['pt'] = (-7000*scale, -12000*scale)
layout_spec['cp_ring']['637TM']['lr_v1']['cp']['std']['637TM']['out']['curl'] = 'ccw'



layout_spec['cp_ring']['637TM']['lr_v2'] = {'cp':{}}
layout_spec['cp_ring']['637TM']['lr_v2']['marker'] = (0000*scale, -13000*scale)
layout_spec['cp_ring']['637TM']['lr_v2']['label'] = (-5500*scale, -15000*scale)
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std'] = {'637TM':{}}
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['theta'] = 180
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['in']['orient'] = 2
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['in']['pt'] = (16000*scale, -12000*scale)
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['in']['min'][0] = 10000*scale
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['in']['min'][3] = 12000*scale
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['out']['orient'] = 3
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['out']['pt'] = (1000*scale, -28000*scale)
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['std']['637TM']['out']['curl'] = 'ccw'

layout_spec['cp_ring']['637TM']['lr_v2']['cp']['drop'] = {'637TM':{}}
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['drop']['637TM']['theta'] = 0
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['drop']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['drop']['637TM']['in']['orient'] = 2
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['drop']['637TM']['in']['pt'] = (-5000*scale, -12000*scale)
layout_spec['cp_ring']['637TM']['lr_v2']['cp']['drop']['637TM']['in']['curl'] = 'ccw'


layout_spec['cp_ring']['SHG'] = {}

layout_spec['cp_ring']['SHG']['SR003_R7770_W940'] = {'cp':{}}
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['marker'] = (7000*scale, -24000*scale)
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['label'] = (10000*scale, 7500*scale)
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std'] = {'1550TE':{},'775TM':{}}
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['theta'] = 180
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['in']['pt'] = (18000*scale, -40000*scale)
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['in']['min'][0] = 14000*scale
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['in']['min'][3] = 22000*scale
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['out']['pt'] = (-7000*scale, -18000*scale)
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['theta'] = -45
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['in'] = {'min':{}}
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['in']['orient'] = 3
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['in']['pt'] = (4000*scale, -30000*scale)
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['out'] = {'min':{}}
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['out']['orient'] = 2
layout_spec['cp_ring']['SHG']['SR003_R7770_W940']['cp']['std']['775TM']['out']['pt'] = (15000*scale, -6000*scale)




#Device array specifications

array_spec = {'gtest':{},\
			  'cp_ring':{}}




array_spec['gtest']['1550TE'] = {}
array_spec['gtest']['1550TE']['x'] = (8500*scale, 8500*scale)
array_spec['gtest']['1550TE']['y'] = (32000*scale, -24000*scale)
array_spec['gtest']['1550TE']['rep'] = 3

#array_spec['gtest']['1080TE'] = {}
#array_spec['gtest']['1080TE']['x'] = (7500*scale, 7500*scale)
#array_spec['gtest']['1080TE']['y'] = (27000*scale, -22000*scale)
#array_spec['gtest']['1080TE']['rep'] = 3

array_spec['gtest']['637TM'] = {}
array_spec['gtest']['637TM']['x'] = (5000*scale, 5000*scale)
array_spec['gtest']['637TM']['y'] = (20000*scale, -14500*scale)
array_spec['gtest']['637TM']['rep'] = 3

array_spec['gtest']['775TM'] = {}
array_spec['gtest']['775TM']['x'] = (6000*scale, 6000*scale)
array_spec['gtest']['775TM']['y'] = (22000*scale, -17000*scale)
array_spec['gtest']['775TM']['rep'] = 3

#array_spec['gtest']['SHG'] = {}
#array_spec['gtest']['SHG']['x'] = (10500*scale, 10500*scale)
#array_spec['gtest']['SHG']['y'] = (38000*scale, -28000*scale)
#array_spec['gtest']['SHG']['rep'] = 3

#array_spec['gtest']['DFG'] = {}
#array_spec['gtest']['DFG']['x'] = (9000*scale, 9000*scale)
#array_spec['gtest']['DFG']['y'] = (33000*scale, -24500*scale)
#array_spec['gtest']['DFG']['rep'] = 3


array_spec['cp_ring']['1550TE'] = {}

array_spec['cp_ring']['1550TE']['lr_v1'] = {}
array_spec['cp_ring']['1550TE']['lr_v1']['std'] = {}
array_spec['cp_ring']['1550TE']['lr_v1']['std']['x'] = (31000*scale, 0*scale)
array_spec['cp_ring']['1550TE']['lr_v1']['std']['y'] = (0*scale, 66000*scale)
array_spec['cp_ring']['1550TE']['lr_v1']['std']['x_num'] = 5

array_spec['cp_ring']['1550TE']['lr_v1'] = {}
array_spec['cp_ring']['1550TE']['lr_v1']['drop'] = {}
array_spec['cp_ring']['1550TE']['lr_v1']['drop']['x'] = (42000*scale, 0*scale)
array_spec['cp_ring']['1550TE']['lr_v1']['drop']['y'] = (0*scale, 66000*scale)
array_spec['cp_ring']['1550TE']['lr_v1']['drop']['x_num'] = 5



array_spec['cp_ring']['637TM'] = {}

array_spec['cp_ring']['637TM']['lr_v1'] = {}
array_spec['cp_ring']['637TM']['lr_v1']['std'] = {}
array_spec['cp_ring']['637TM']['lr_v1']['std']['x'] = (25000*scale, 0*scale)
array_spec['cp_ring']['637TM']['lr_v1']['std']['y'] = (0*scale, 42000*scale)
array_spec['cp_ring']['637TM']['lr_v1']['std']['x_num'] = 5

array_spec['cp_ring']['637TM']['lr_v1'] = {}
array_spec['cp_ring']['637TM']['lr_v1']['drop'] = {}
array_spec['cp_ring']['637TM']['lr_v1']['drop']['x'] = (32000*scale, 0*scale)
array_spec['cp_ring']['637TM']['lr_v1']['drop']['y'] = (0*scale, 42000*scale)
array_spec['cp_ring']['637TM']['lr_v1']['drop']['x_num'] = 5


array_spec['cp_ring']['637TM']['lr_v2'] = {}
array_spec['cp_ring']['637TM']['lr_v2']['drop'] = {}
array_spec['cp_ring']['637TM']['lr_v2']['drop']['x'] = (25000*scale, 0*scale)
array_spec['cp_ring']['637TM']['lr_v2']['drop']['y'] = (0*scale, 42000*scale)
array_spec['cp_ring']['637TM']['lr_v2']['drop']['x_num'] = 5



array_spec['cp_ring']['SHG'] = {}

array_spec['cp_ring']['SHG']['SR003_R7770_W940'] = {}
array_spec['cp_ring']['SHG']['SR003_R7770_W940']['std'] = {}
array_spec['cp_ring']['SHG']['SR003_R7770_W940']['std']['x'] = (40000*scale, 0*scale)
array_spec['cp_ring']['SHG']['SR003_R7770_W940']['std']['y'] = (0*scale, 65000*scale)
array_spec['cp_ring']['SHG']['SR003_R7770_W940']['std']['x_num'] = 5

