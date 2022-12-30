# Constants for SHG/DFG devices in 250nm GaP on SiO2
# Wavelength modes are designated: 1-1550TE, 2-1080TE, 3-637TM, 4-775TM, 5-Multiple (SHG), 6-Multiple (DFG)
# All lengths are in nanometers

import copy

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

wg_spec['1550TE']['r']['std'] = 4500*scale
wg_spec['1550TE']['w']['wg'] = 600*scale
wg_spec['1550TE']['w']['cr'] = 500*scale
wg_spec['1550TE']['L']['cr'] = 4000*scale
wg_spec['1550TE']['L']['adapt'] = 4000*scale
wg_spec['1550TE']['L']['taper'] = 8000*scale
wg_spec['1550TE']['L']['bz'] = 4000*scale

wg_spec['1080TE']['r']['std'] = 3600*scale
wg_spec['1080TE']['w']['wg'] = 380*scale
wg_spec['1080TE']['w']['mf'] = 300*scale
wg_spec['1080TE']['w']['cr'] = 250*scale
wg_spec['1080TE']['L']['cr'] = 3000*scale
wg_spec['1080TE']['L']['adapt'] = 3500*scale
wg_spec['1080TE']['L']['taper'] = 6000*scale
wg_spec['1080TE']['L']['bz'] = 3500*scale

wg_spec['637TM']['r']['std'] = 2500*scale
wg_spec['637TM']['w']['wg'] = 110*scale
wg_spec['637TM']['w']['mf'] = 70*scale                # Some waveguide specs have mode filters defined
wg_spec['637TM']['w']['cr'] = 100*scale
wg_spec['637TM']['L']['cr'] = 2000*scale
wg_spec['637TM']['L']['mf'] = 2000*scale
wg_spec['637TM']['L']['adapt'] = 2000*scale
wg_spec['637TM']['L']['taper'] = 3000*scale
wg_spec['637TM']['L']['bz'] = 2500*scale

wg_spec['775TM']['r']['std'] = 2800*scale
wg_spec['775TM']['w']['wg'] = 150*scale
#wg_spec['775TM']['w']['mf'] = 110*scale
wg_spec['775TM']['w']['cr'] = 120*scale
wg_spec['775TM']['L']['cr'] = 2000*scale
wg_spec['775TM']['L']['mf'] = 2500*scale
wg_spec['775TM']['L']['adapt'] = 2500*scale
wg_spec['775TM']['L']['taper'] = 4000*scale
wg_spec['775TM']['L']['bz'] = 3000*scale

wg_spec['Multi']['r']['std'] = 4500*scale
wg_spec['Multi']['w']['wg'] = 465*scale
wg_spec['Multi']['w']['cr'] = 465*scale
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

# ring_spec['1550TE']['nar'] = {'cp':{}}                                     # Define 'nar' variant of '1550TE' ring type with dictionary for coupling specs
# ring_spec['1550TE']['nar']['w'] = 600*scale                           # Define ring width and radius
# ring_spec['1550TE']['nar']['r'] = int(4800-600/2)*scale
# ring_spec['1550TE']['nar']['cp']['20K'] = {}                              # Define '20K' coupling spec
# ring_spec['1550TE']['nar']['cp']['20K']['d'] = 130*scale           # This is a straight coupling region, so only a distance is defined
# ring_spec['1550TE']['nar']['cp']['20K']['label'] = '00'
# ring_spec['1550TE']['nar']['cp']['200K'] = {}
# ring_spec['1550TE']['nar']['cp']['200K']['d'] = 280*scale
# ring_spec['1550TE']['nar']['cp']['200K']['label'] = '01'



# ring_spec['DFG']['3minus_2870'] = {'cp':{}}
# ring_spec['DFG']['3minus_2870']['w'] = 740*scale
# ring_spec['DFG']['3minus_2870']['r'] = 2500*scale
# ring_spec['DFG']['3minus_2870']['label'] = '502'
# ring_spec['DFG']['3minus_2870']['dw'] = round(0.5*scale)
# ring_spec['DFG']['3minus_2870']['cp']['1550TE'] = {}
# ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K'] = {}
# ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K']['w'] = 480*scale
# ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K']['d'] = 220*scale
# ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K']['theta'] = 40
# ring_spec['DFG']['3minus_2870']['cp']['1080TE'] = {}
# ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K'] = {}
# ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K']['w'] = 320*scale
# ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K']['d'] = 135*scale
# ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K']['theta'] = 55
# ring_spec['DFG']['3minus_2870']['cp']['637TM'] = {}
# ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K'] = {}
# ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K']['w'] = 130*scale
# ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K']['d'] = 60*scale
# ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K']['theta'] = 10




#d_gr = [a*scale for a in [50, 75, 100, 150, 200, 250, 300]]
d_gr_1 = [a*scale for a in [60,80,100,120,140,160,180,200,220,240,260,280,300]]
d_min = 50*scale


# gr_spec = {'1550TE':{'shape':{}},\
                    # '1080TE':{'shape':{}},\
                    # '637TM':{'shape':{}},\
                    # '775TM':{'shape':{}},\
                    # 'SHG':{'shape':{}},\
                    # 'DFG':{'shape':{}}}

gr_spec = { '1550TE':{},\
            '1080TE':{},\
            '637TM':{},\
            '775TM':{},\
            'SHG':{},\
            'DFG':{}
            }

# 1TE Run 1 Design 7, 2021 05 11
gr_spec['1550TE']['1'] =   {   
                            'ribs':[max(1.08*a*scale,d_min) for a in  [685,190,565,105,235,725,725,480,410]],\
                            'gaps':[max(1.08*d_gr_1[i-1],d_min) for i in [12,2,11,9,13,12,11,10,13]],\
                            'label':'0',    \
                            'shape':{       \
                                'str':{
                                    'w':3000*scale,\
                                    'L':10000*scale
                                },\
                                'foc':{
                                    'L':2000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell1':{         # UPDATE
                                    'L':8000*scale,\
                                    'arc':25,\
                                    'theta':15,\
                                    'ecc':0.2
                                },\
                                'ell2':{         # UPDATE
                                    'L':6000*scale,\
                                    'arc':30,\
                                    'theta':15,\
                                    'ecc':0.3
                                }
                            }
                        }

# 1TE Run 1 Design 20, 2021 05 11
gr_spec['1550TE']['2'] =   {   
                            'ribs':[max(0.98*a*scale,d_min) for a in  [775,190,305,110,65,460]],\
                            'gaps':[max(0.98*d_gr_1[i-1],d_min) for i in [3,13,1,5,11,8]],\
                            'label':'0',    \
                            'shape':{       \
                                'str':{
                                    'w':3000*scale,\
                                    'L':10000*scale
                                },\
                                'foc':{
                                    'L':4000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell1':{         # UPDATE
                                    'L':10000*scale,\
                                    'arc':20,\
                                    'theta':15,\
                                    'ecc':0.2
                                },\
                                'ell2':{         # UPDATE
                                    'L':8000*scale,\
                                    'arc':25,\
                                    'theta':15,\
                                    'ecc':0.2
                                },\
                                'ell3':{         # UPDATE
                                    'L':6000*scale,\
                                    'arc':30,\
                                    'theta':15,\
                                    'ecc':0.3
                                }
                            }
                        }

# 1TE Run 2 Design 12, 2021 05 11
gr_spec['1550TE']['3'] =   {   
                            'ribs':[max(0.94*a*scale,d_min) for a in  [230,565,480,740,235,305,560,285,75,550]],\
                            'gaps':[max(0.94*d_gr_1[i-1],d_min) for i in [4,3,4,12,1,1,5,7,11,6]],\
                            'label':'0',    \
                            'shape':{       \
                                'str':{
                                    'w':3000*scale,\
                                    'L':10000*scale
                                },\
                                'foc':{
                                    'L':2000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell':{         # UPDATE
                                    'L':8000*scale,\
                                    'arc':20,\
                                    'theta':10,\
                                    'ecc':0.2
                                }
                            }
                        }

# 4TM Run 2 Design 3, 2021 05 11
gr_spec['775TM']['1'] =   {   
                            'ribs':[max(0.98*a*scale,d_min) for a in  [310,485,260,465,55,355,685,280,465]],\
                            'gaps':[max(0.98*d_gr_1[i-1],d_min) for i in [2,4,10,6,4,12,12,11,8]],\
                            'label':'0',    \
                            'shape':{       \
                                'str':{
                                    'w':2000*scale,\
                                    'L':6000*scale
                                },\
                                'foc':{
                                    'L':2000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell':{         # UPDATE
                                    'L':8000*scale,\
                                    'arc':20,\
                                    'theta':10,\
                                    'ecc':0.2
                                }
                            }
                        }

# 4TM Run 2 Design 18, 2021 05 11
gr_spec['775TM']['2'] =   {   
                            'ribs':[max(1.00*a*scale,d_min) for a in  [725,615,290,130,365,710,445,450,395]],\
                            'gaps':[max(1.00*d_gr_1[i-1],d_min) for i in [1,2,13,12,4,5,3,5,11]],\
                            'label':'0',    \
                            'shape':{       \
                                'str':{
                                    'w':2000*scale,\
                                    'L':6000*scale
                                },\
                                'foc':{
                                    'L':2000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell1':{         # UPDATE
                                    'L':10000*scale,\
                                    'arc':20,\
                                    'theta':15,\
                                    'ecc':0.2
                                },\
                                'ell2':{         # UPDATE
                                    'L':6000*scale,\
                                    'arc':30,\
                                    'theta':15,\
                                    'ecc':0.2
                                }
                            }
                        }

# 4TM Run 2 Design 19, 2021 05 11
gr_spec['775TM']['3'] =   {   
                            'ribs':[max(0.94*a*scale,d_min) for a in  [195,535,445,565,670,205,220,425]],\
                            'gaps':[max(0.94*d_gr_1[i-1],d_min) for i in [8,3,13,1,5,6,7,11]],\
                            'label':'0',    \
                            'shape':{       \
                                'str':{
                                    'w':2000*scale,\
                                    'L':6000*scale
                                },\
                                'foc':{
                                    'L':2000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell':{         # UPDATE
                                    'L':8000*scale,\
                                    'arc':20,\
                                    'theta':10,\
                                    'ecc':0.2
                                }
                            }
                        }



# SHG Run 2 Design 13, 2021 05 11
gr_spec['SHG']['1'] =   {   
                            'ribs':[max(1.05*a*scale,d_min) for a in  [675,555,380,90,730,405,385,100,530,440,750,720]],\
                            'gaps':[max(1.05*d_gr_1[i-1],d_min) for i in [6,11,2,11,5,13,1,5,2,1,1,10]],\
                            'label':'4',    \
                            'shape':{       \
                                'str':{
                                    'w':3000*scale,\
                                    'L':10000*scale
                                },\
                                'foc':{
                                    'L':2000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell1':{
                                    'L':8000*scale,\
                                    'arc':20,\
                                    'theta':10,\
                                    'ecc':0.2
                                },\
                                'ell2':{
                                    'L':8000*scale,\
                                    'arc':25,\
                                    'theta':15,\
                                    'ecc':0.2
                                },\
                                'ell3':{
                                    'L':6000*scale,\
                                    'arc':30,\
                                    'theta':15,\
                                    'ecc':0.3
                                }
                            }
                        }


# # SHG Run 2 Design 16, 2021 05 11       Nonfunctional in telecom band on 2021_05_16 chip
# gr_spec['SHG']['2'] =   {   
                            # 'ribs':[max(1.1*a*scale,d_min) for a in  [335,255,125,280,610,475]],\
                            # 'gaps':[max(1.1*d_gr_1[i-1],d_min) for i in [1,6,10,6,9,10]],\
                            # 'label':'4',    \
                            # 'shape':{       \
                                # 'str':{
                                    # 'w':3000*scale,\
                                    # 'L':10000*scale
                                # },\
                                # 'ell':{
                                    # 'L':10000*scale,\
                                    # 'arc':25,\
                                    # 'theta':10,\
                                    # 'ecc':0.2
                                # }
                            # }
                        # }

# SHG Run 3 Design 5, 2021 05 11
gr_spec['SHG']['3'] =   {   
                            'ribs':[max(0.88*a*scale,d_min) for a in  [490,535,80,460,400,235,80,585]],\
                            'gaps':[max(0.88*d_gr_1[i-1],d_min) for i in [9,10,11,11,12,11,5,8]],\
                            'label':'4',    \
                            'shape':{       \
                                'str':{
                                    'w':3000*scale,\
                                    'L':10000*scale
                                },\
                                'foc':{
                                    'L':4000*scale,\
                                    'arc':20,\
                                    'theta':0,\
                                    'ecc':0
                                },\
                                'ell1':{     # UPDATE
                                    'L':10000*scale,\
                                    'arc':20,\
                                    'theta':25,\
                                    'ecc':0.2
                                },\
                                'ell2':{     # UPDATE
                                    'L':8000*scale,\
                                    'arc':25,\
                                    'theta':25,\
                                    'ecc':0.2
                                },\
                                'ell3':{     # UPDATE
                                    'L':6000*scale,\
                                    'arc':30,\
                                    'theta':25,\
                                    'ecc':0.2
                                }
                            }
                        }


# Copies of 1550TE and 775TM gratings for SHG use
gr_spec['SHG']['1nir'] =   copy.deepcopy(gr_spec['775TM']['1'])
gr_spec['SHG']['2nir'] =   copy.deepcopy(gr_spec['775TM']['2'])
gr_spec['SHG']['3nir'] =   copy.deepcopy(gr_spec['775TM']['3'])
gr_spec['SHG']['1ir'] =   copy.deepcopy(gr_spec['1550TE']['1'])
gr_spec['SHG']['2ir'] =   copy.deepcopy(gr_spec['1550TE']['2'])
gr_spec['SHG']['3ir'] =   copy.deepcopy(gr_spec['1550TE']['3'])


# gr_spec['SHG']['ribs'] = [max(1.05*a*scale,d_min) for a in  [675,555,380,90,730,405,385,100,530,440,750,720]]
# gr_spec['SHG']['gaps'] = [max(d_gr_1[i-1],d_min) for i in [6,11,2,11,5,13,1,5,2,1,1,10]]
# gr_spec['SHG']['label'] = '4'
# gr_spec['SHG']['shape']['str'] = {}
# gr_spec['SHG']['shape']['str']['w'] = 3000*scale
# gr_spec['SHG']['shape']['str']['L'] = 10000*scale
# gr_spec['SHG']['shape']['ell'] = {}
# gr_spec['SHG']['shape']['ell']['L'] = 8000*scale
# gr_spec['SHG']['shape']['ell']['arc'] = 20
# gr_spec['SHG']['shape']['ell']['theta'] = 10
# gr_spec['SHG']['shape']['ell']['ecc'] = 0.2



for gr_type in gr_spec:
    for design_type in gr_spec[gr_type]:
        temp = gr_spec[gr_type][design_type]
        for shape_type in temp['shape']:
            if 'L_total' not in temp['shape'][shape_type]:
                temp['shape'][shape_type]['L_total'] = temp['shape'][shape_type]['L'] + sum(temp['ribs']) + sum(temp['gaps'])
                print(gr_type, design_type, shape_type,(sum(temp['ribs']) + sum(temp['gaps']))/scale)

# gr_spec['SHG']['shape']['str']['L_total'] = gr_spec['SHG_1']['shape']['str']['L'] +  sum(gr_spec['SHG_1']['ribs']) + sum(gr_spec['SHG_1']['gaps'])
# gr_spec['SHG']['shape']['ell']['L_total'] = gr_spec['SHG_1']['shape']['ell']['L'] +  sum(gr_spec['SHG_1']['ribs']) + sum(gr_spec['SHG_1']['gaps'])

# gr_spec['SHG']['shape']['str']['L_total'] = gr_spec['SHG_2']['shape']['str']['L'] +  sum(gr_spec['SHG_2']['ribs']) + sum(gr_spec['SHG_2']['gaps'])
# gr_spec['SHG']['shape']['ell']['L_total'] = gr_spec['SHG_2']['shape']['ell']['L'] +  sum(gr_spec['SHG_2']['ribs']) + sum(gr_spec['SHG_2']['gaps'])


# # directional coupler specifications

# dc_spec = {'SHG':{}}

# dc_spec['SHG']['sym_v1'] = {}
# dc_spec['SHG']['sym_v1']['w'] = 450*scale
# dc_spec['SHG']['sym_v1']['d'] = 105*scale
# dc_spec['SHG']['sym_v1']['L'] = 18000*scale # originally 20000*scale
# dc_spec['SHG']['sym_v1']['offset'] = 2500*scale
# dc_spec['SHG']['asym_v1'] = {}
# dc_spec['SHG']['asym_v1']['w'] = 500*scale
# dc_spec['SHG']['asym_v1']['w2'] = 450*scale
# dc_spec['SHG']['asym_v1']['d'] = 100*scale
# dc_spec['SHG']['asym_v1']['L'] = 18500*scale
# dc_spec['SHG']['asym_v1']['offset'] = 2500*scale


# Layout specifications

layout_spec = {'lr':{},\
               'gtest':{},\
			   'cp_ring':{}}

layout_spec['lr']['1550TE'] = {}
layout_spec['lr']['1550TE']['span'] = 16000*scale
layout_spec['lr']['1550TE']['offset'] = 5000*scale
layout_spec['lr']['1550TE']['min'] = 2000*scale

layout_spec['lr']['1080TE'] = {}
layout_spec['lr']['1080TE']['span'] = 14000*scale
layout_spec['lr']['1080TE']['offset'] = 4000*scale
layout_spec['lr']['1080TE']['min'] = 2000*scale

layout_spec['lr']['637TM'] = {}
layout_spec['lr']['637TM']['span'] = 10000*scale
layout_spec['lr']['637TM']['offset'] = 4000*scale
layout_spec['lr']['637TM']['min'] = 1500*scale

layout_spec['lr']['775TM'] = {}
layout_spec['lr']['775TM']['span'] = 12000*scale
layout_spec['lr']['775TM']['offset'] = 4000*scale
layout_spec['lr']['775TM']['min'] = 1500*scale

layout_spec['lr']['SHG'] = {'v1':{'1550TE':{},'775TM':{}}}
layout_spec['lr']['SHG']['v1']['1550TE']['span'] = 16000*scale
layout_spec['lr']['SHG']['v1']['1550TE']['offset'] = 5000*scale
layout_spec['lr']['SHG']['v1']['1550TE']['min'] = 2000*scale
layout_spec['lr']['SHG']['v1']['775TM']['span'] = 12000*scale
layout_spec['lr']['SHG']['v1']['775TM']['offset'] = 4000*scale
layout_spec['lr']['SHG']['v1']['775TM']['min'] = 1500*scale

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


# layout_spec['cp_ring']['SHG'] = {}


#layout_spec['cp_ring']['DFG']['3minus_2870'] = {'cp':{}}
#layout_spec['cp_ring']['DFG']['3minus_2870']['marker'] = (8000*scale, -2000*scale)
#layout_spec['cp_ring']['DFG']['3minus_2870']['label'] = (1500*scale, -10000*scale)
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std'] = {'1550TE':{},'1080TE':{},'637TM':{}}
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['theta'] = 110
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in'] = {'min':{}}
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['orient'] = 1
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['pt'] = (21000*scale, -33000*scale)
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['min'][3] = 26000*scale
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out'] = {'min':{}}
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out']['orient'] = 2
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out']['pt'] = (-15000*scale, -24000*scale)
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['theta'] = 325
#layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['in'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['in']['orient'] = 3
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['in']['pt'] = (6000*scale, -22000*scale)
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out']['orient'] = 2
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out']['pt'] = (15000*scale, -1000*scale)
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out']['min'][3] = 25000*scale
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['theta'] = 205
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['in'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['in']['orient'] = 3
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['in']['pt'] = (-8000*scale, -35000*scale)
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['out'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['out']['orient'] = 2
# layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['out']['pt'] = (0*scale, -21000*scale)


#Device array specifications

array_spec = {'lr':{},\
			  'gtest':{},\
			  'cp_ring':{}}

array_spec['lr']['1550TE'] = {}
array_spec['lr']['1550TE']['x'] = 36000*scale
array_spec['lr']['1550TE']['y'] = 60000*scale
array_spec['lr']['1550TE']['rep'] = 3

array_spec['lr']['1080TE'] = {}
array_spec['lr']['1080TE']['x'] = 29000*scale
array_spec['lr']['1080TE']['y'] = 50000*scale
array_spec['lr']['1080TE']['rep'] = 3

array_spec['lr']['637TM'] = {}
array_spec['lr']['637TM']['x'] = 21000*scale
array_spec['lr']['637TM']['y'] = 35500*scale
array_spec['lr']['637TM']['rep'] = 3

array_spec['lr']['775TM'] = {}
array_spec['lr']['775TM']['x'] = 23500*scale
array_spec['lr']['775TM']['y'] = 41000*scale
array_spec['lr']['775TM']['rep'] = 3

array_spec['lr']['SHG'] = {'v1':{'1550TE':{},'775TM':{}}}
array_spec['lr']['SHG']['v1']['1550TE']['x'] = 30000*scale
array_spec['lr']['SHG']['v1']['1550TE']['y'] = 60000*scale
array_spec['lr']['SHG']['v1']['1550TE']['rep'] = 3
array_spec['lr']['SHG']['v1']['775TM']['x'] = 23000*scale
array_spec['lr']['SHG']['v1']['775TM']['y'] = 41000*scale
array_spec['lr']['SHG']['v1']['775TM']['rep'] = 3



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

array_spec['gtest']['DFG'] = {}
array_spec['gtest']['DFG']['x'] = (9000*scale, 9000*scale)
array_spec['gtest']['DFG']['y'] = (33000*scale, -24500*scale)
array_spec['gtest']['DFG']['rep'] = 3

array_spec['cp_ring']['3minus_5000'] = {}
array_spec['cp_ring']['3minus_5000']['std'] = {}
array_spec['cp_ring']['3minus_5000']['std']['x'] = (38000*scale, 0*scale)
array_spec['cp_ring']['3minus_5000']['std']['y'] = (0*scale, 55000*scale)
array_spec['cp_ring']['3minus_5000']['std']['x_num'] = 10

array_spec['cp_ring']['3minus_4815'] = {}
array_spec['cp_ring']['3minus_4815']['std'] = {}
array_spec['cp_ring']['3minus_4815']['std']['x'] = (46000*scale, 0*scale)
array_spec['cp_ring']['3minus_4815']['std']['y'] = (0*scale, 46000*scale)
array_spec['cp_ring']['3minus_4815']['std']['x_num'] = 10


array_spec['cp_ring']['3minus_2870'] = {}
array_spec['cp_ring']['3minus_2870']['std'] = {}
array_spec['cp_ring']['3minus_2870']['std']['x'] = (46000*scale, 0*scale)
array_spec['cp_ring']['3minus_2870']['std']['y'] = (0*scale, 46000*scale)
array_spec['cp_ring']['3minus_2870']['std']['x_num'] = 10

array_spec['cp_ring']['3plus_3275'] = {}
array_spec['cp_ring']['3plus_3275']['std'] = {}
array_spec['cp_ring']['3plus_3275']['std']['x'] = (46000*scale, 0*scale)
array_spec['cp_ring']['3plus_3275']['std']['y'] = (0*scale, 46000*scale)
array_spec['cp_ring']['3plus_3275']['std']['x_num'] = 10

array_spec['cp_ring']['1-4minus_3375'] = {}
array_spec['cp_ring']['1-4minus_3375']['std'] = {}
array_spec['cp_ring']['1-4minus_3375']['std']['x'] = (46000*scale, 0*scale)
array_spec['cp_ring']['1-4minus_3375']['std']['y'] = (0*scale, 46000*scale)
array_spec['cp_ring']['1-4minus_3375']['std']['x_num'] = 10
