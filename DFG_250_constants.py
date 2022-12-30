# Constants for SHG/DFG devices in 250nm GaP on SiO2
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
wg_spec['1550TE']['L']['bz'] = 4000*scale

wg_spec['1080TE']['r']['std'] = 3000*scale
wg_spec['1080TE']['w']['wg'] = 350*scale
wg_spec['1080TE']['w']['mf'] = 300*scale
wg_spec['1080TE']['w']['cr'] = 250*scale
wg_spec['1080TE']['L']['cr'] = 3000*scale
wg_spec['1080TE']['L']['adapt'] = 3500*scale
wg_spec['1080TE']['L']['taper'] = 6000*scale
wg_spec['1080TE']['L']['bz'] = 3000*scale

wg_spec['637TM']['r']['std'] = 2500*scale
wg_spec['637TM']['w']['wg'] = 100*scale
wg_spec['637TM']['w']['mf'] = 60*scale                # Some waveguide specs have mode filters defined
wg_spec['637TM']['w']['cr'] = 100*scale
wg_spec['637TM']['L']['cr'] = 2000*scale
wg_spec['637TM']['L']['mf'] = 2000*scale
wg_spec['637TM']['L']['adapt'] = 2000*scale
wg_spec['637TM']['L']['taper'] = 3000*scale
wg_spec['637TM']['L']['bz'] = 1500*scale

wg_spec['775TM']['r']['std'] = 2500*scale
wg_spec['775TM']['w']['wg'] = 140*scale
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

ring_spec['1550TE']['nar'] = {'cp':{}}                                     # Define 'nar' variant of '1550TE' ring type with dictionary for coupling specs
ring_spec['1550TE']['nar']['w'] = 600*scale                           # Define ring width and radius
ring_spec['1550TE']['nar']['r'] = int(4800-600/2)*scale
ring_spec['1550TE']['nar']['cp']['20K'] = {}                              # Define '20K' coupling spec
ring_spec['1550TE']['nar']['cp']['20K']['d'] = 130*scale           # This is a straight coupling region, so only a distance is defined
ring_spec['1550TE']['nar']['cp']['20K']['label'] = '00'
ring_spec['1550TE']['nar']['cp']['200K'] = {}
ring_spec['1550TE']['nar']['cp']['200K']['d'] = 280*scale
ring_spec['1550TE']['nar']['cp']['200K']['label'] = '01'

ring_spec['1550TE']['std'] = {'cp':{}}                                    
ring_spec['1550TE']['std']['w'] = 650*scale                         
ring_spec['1550TE']['std']['r'] = int(4800-650/2)*scale
ring_spec['1550TE']['std']['cp']['20K'] = {}                              
ring_spec['1550TE']['std']['cp']['20K']['d'] = 120*scale
ring_spec['1550TE']['std']['cp']['20K']['label'] = '02'
ring_spec['1550TE']['std']['cp']['200K'] = {}
ring_spec['1550TE']['std']['cp']['200K']['d'] = 260*scale
ring_spec['1550TE']['std']['cp']['200K']['label'] = '03'

ring_spec['1550TE']['wid'] = {'cp':{}}                              
ring_spec['1550TE']['wid']['w'] = 700*scale                      
ring_spec['1550TE']['wid']['r'] = int(4800-700/2)*scale
ring_spec['1550TE']['wid']['cp']['20K'] = {}                        
ring_spec['1550TE']['wid']['cp']['20K']['d'] = 110*scale 
ring_spec['1550TE']['wid']['cp']['20K']['label'] = '04'
ring_spec['1550TE']['wid']['cp']['200K'] = {}
ring_spec['1550TE']['wid']['cp']['200K']['d'] = 255*scale
ring_spec['1550TE']['wid']['cp']['200K']['label'] = '05'

ring_spec['1080TE']['nar'] = {'cp':{}}
ring_spec['1080TE']['nar']['w'] = 320*scale
ring_spec['1080TE']['nar']['r'] = int(3600-320/2)*scale
ring_spec['1080TE']['nar']['cp']['20K'] = {}
ring_spec['1080TE']['nar']['cp']['20K']['d'] = 135*scale
ring_spec['1080TE']['nar']['cp']['20K']['label'] = '10'
ring_spec['1080TE']['nar']['cp']['200K'] = {}
ring_spec['1080TE']['nar']['cp']['200K']['d'] = 245*scale
ring_spec['1080TE']['nar']['cp']['200K']['label'] = '11'

ring_spec['1080TE']['std'] = {'cp':{}}
ring_spec['1080TE']['std']['w'] = 360*scale
ring_spec['1080TE']['std']['r'] = int(3600-360/2)*scale
ring_spec['1080TE']['std']['cp']['20K'] = {}
ring_spec['1080TE']['std']['cp']['20K']['d'] = 90*scale
ring_spec['1080TE']['std']['cp']['20K']['label'] = '12'
ring_spec['1080TE']['std']['cp']['200K'] = {}
ring_spec['1080TE']['std']['cp']['200K']['d'] = 205*scale
ring_spec['1080TE']['std']['cp']['200K']['label'] = '13'

ring_spec['1080TE']['wid'] = {'cp':{}}
ring_spec['1080TE']['wid']['w'] = 400*scale
ring_spec['1080TE']['wid']['r'] = int(3600-400/2)*scale
ring_spec['1080TE']['wid']['cp']['20K'] = {}
ring_spec['1080TE']['wid']['cp']['20K']['d'] = 65*scale
ring_spec['1080TE']['wid']['cp']['20K']['label'] = '14'
ring_spec['1080TE']['wid']['cp']['200K'] = {}
ring_spec['1080TE']['wid']['cp']['200K']['d'] = 175*scale
ring_spec['1080TE']['wid']['cp']['200K']['label'] = '15'

ring_spec['637TM']['nar'] = {'cp':{}}
ring_spec['637TM']['nar']['w'] = 120*scale
ring_spec['637TM']['nar']['r'] = int(3000-120/2)*scale
ring_spec['637TM']['nar']['cp']['20K'] = {}
ring_spec['637TM']['nar']['cp']['20K']['d'] = 120*scale
ring_spec['637TM']['nar']['cp']['20K']['label'] = '20'
ring_spec['637TM']['nar']['cp']['200K'] = {}
ring_spec['637TM']['nar']['cp']['200K']['d'] = 170*scale
ring_spec['637TM']['nar']['cp']['200K']['label'] = '21'

ring_spec['637TM']['std'] = {'cp':{}}
ring_spec['637TM']['std']['w'] = 140*scale
ring_spec['637TM']['std']['r'] = int(3000-140/2)*scale
ring_spec['637TM']['std']['cp']['20K'] = {}
ring_spec['637TM']['std']['cp']['20K']['d'] = 110*scale
ring_spec['637TM']['std']['cp']['20K']['label'] = '22'
ring_spec['637TM']['std']['cp']['200K'] = {}
ring_spec['637TM']['std']['cp']['200K']['d'] = 160*scale
ring_spec['637TM']['std']['cp']['200K']['label'] = '23'

ring_spec['637TM']['wid'] = {'cp':{}}
ring_spec['637TM']['wid']['w'] = 160*scale
ring_spec['637TM']['wid']['r'] = int(3000-160/2)*scale
ring_spec['637TM']['wid']['cp']['20K'] = {}
ring_spec['637TM']['wid']['cp']['20K']['d'] = 100*scale
ring_spec['637TM']['wid']['cp']['20K']['label'] = '24'
ring_spec['637TM']['wid']['cp']['200K'] = {}
ring_spec['637TM']['wid']['cp']['200K']['d'] = 150*scale
ring_spec['637TM']['wid']['cp']['200K']['label'] = '25'

ring_spec['775TM']['nar'] = {'cp':{}}
ring_spec['775TM']['nar']['w'] = 120*scale
ring_spec['775TM']['nar']['r'] = int(3000-120/2)*scale
ring_spec['775TM']['nar']['cp']['20K'] = {}
ring_spec['775TM']['nar']['cp']['20K']['d'] = 185*scale
ring_spec['775TM']['nar']['cp']['20K']['label'] = '30'
ring_spec['775TM']['nar']['cp']['200K'] = {}
ring_spec['775TM']['nar']['cp']['200K']['d'] = 260*scale
ring_spec['775TM']['nar']['cp']['200K']['label'] = '31'

ring_spec['775TM']['std'] = {'cp':{}}
ring_spec['775TM']['std']['w'] = 150*scale
ring_spec['775TM']['std']['r'] = int(3000-150/2)*scale
ring_spec['775TM']['std']['cp']['20K'] = {}
ring_spec['775TM']['std']['cp']['20K']['d'] = 175*scale
ring_spec['775TM']['std']['cp']['20K']['label'] = '32'
ring_spec['775TM']['std']['cp']['200K'] = {}
ring_spec['775TM']['std']['cp']['200K']['d'] = 245*scale
ring_spec['775TM']['std']['cp']['200K']['label'] = '33'

ring_spec['775TM']['wid'] = {'cp':{}}
ring_spec['775TM']['wid']['w'] = 180*scale
ring_spec['775TM']['wid']['r'] = int(3000-180/2)*scale
ring_spec['775TM']['wid']['cp']['20K'] = {}
ring_spec['775TM']['wid']['cp']['20K']['d'] = 155*scale
ring_spec['775TM']['wid']['cp']['20K']['label'] = '34'
ring_spec['775TM']['wid']['cp']['200K'] = {}
ring_spec['775TM']['wid']['cp']['200K']['d'] = 220*scale
ring_spec['775TM']['wid']['cp']['200K']['label'] = '35'


ring_spec['SHG']['v1'] = {'cp':{}}
ring_spec['SHG']['v1']['w'] = 940*scale
ring_spec['SHG']['v1']['r'] = 1600*scale
ring_spec['SHG']['v1']['cp']['1550TE'] = {}
ring_spec['SHG']['v1']['cp']['1550TE']['20K'] = {}
ring_spec['SHG']['v1']['cp']['1550TE']['20K']['d'] = 160*scale
ring_spec['SHG']['v1']['cp']['1550TE']['20K']['label'] = '40'
ring_spec['SHG']['v1']['cp']['1550TE']['200K'] = {}
ring_spec['SHG']['v1']['cp']['1550TE']['200K']['d'] = 315*scale
ring_spec['SHG']['v1']['cp']['1550TE']['200K']['label'] = '41'
ring_spec['SHG']['v1']['cp']['775TM'] = {}
ring_spec['SHG']['v1']['cp']['775TM']['20K'] = {}
ring_spec['SHG']['v1']['cp']['775TM']['20K']['d'] = 160*scale
ring_spec['SHG']['v1']['cp']['775TM']['20K']['label'] = '50'
ring_spec['SHG']['v1']['cp']['775TM']['200K'] = {}
ring_spec['SHG']['v1']['cp']['775TM']['200K']['d'] = 230*scale
ring_spec['SHG']['v1']['cp']['775TM']['200K']['label'] = '51'

ring_spec['SHG']['2minus_2100'] = {'cp':{}}
ring_spec['SHG']['2minus_2100']['w'] = 780*scale
ring_spec['SHG']['2minus_2100']['r'] = 1710*scale

ring_spec['SHG']['3minus_4920'] = {'cp':{}}
ring_spec['SHG']['3minus_4920']['w'] = 1010*scale
ring_spec['SHG']['3minus_4920']['r'] = 4415*scale
ring_spec['SHG']['3minus_4920']['cp']['1550TE'] = {}
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['20K'] = {}
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['20K']['d'] = 220*scale
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['20K']['w'] = 500*scale
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['20K']['theta'] = 86
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['100K'] = {}
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['100K']['d'] = 300*scale
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['100K']['w'] = 500*scale
ring_spec['SHG']['3minus_4920']['cp']['1550TE']['100K']['theta'] = 86
ring_spec['SHG']['3minus_4920']['cp']['775TM'] = {}
ring_spec['SHG']['3minus_4920']['cp']['775TM']['200K'] = {}
ring_spec['SHG']['3minus_4920']['cp']['775TM']['200K']['d'] = 220*scale
ring_spec['SHG']['3minus_4920']['cp']['775TM']['200K']['w'] = 120*scale
ring_spec['SHG']['3minus_4920']['cp']['775TM']['200K']['theta'] = 28.5

ring_spec['SHG']['3minus_5000'] = {'cp':{}}
ring_spec['SHG']['3minus_5000']['w'] = 1005*scale
ring_spec['SHG']['3minus_5000']['r'] = 4495*scale
ring_spec['SHG']['3minus_5000']['label'] = '401'
ring_spec['SHG']['3minus_5000']['dw'] = round(0.5*scale)
ring_spec['SHG']['3minus_5000']['cp']['1550TE'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['10K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['10K']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['10K']['d'] = 175*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['10K']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['20K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['20K']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['20K']['d'] = 208*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['20K']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['50K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['50K']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['50K']['d'] = 254*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['50K']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['100K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['100K']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['100K']['d'] = 287*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['100K']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['200K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['200K']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['200K']['d'] = 321*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['200K']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['500K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['500K']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['500K']['d'] = 366*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['500K']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['1M'] = {}
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['1M']['w'] = 500*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['1M']['d'] = 400*scale
ring_spec['SHG']['3minus_5000']['cp']['1550TE']['1M']['theta'] = 81
ring_spec['SHG']['3minus_5000']['cp']['775TM'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['10K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['10K']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['10K']['d'] = round(126.3*scale)
ring_spec['SHG']['3minus_5000']['cp']['775TM']['10K']['theta'] = 27
ring_spec['SHG']['3minus_5000']['cp']['775TM']['20K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['20K']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['20K']['d'] = round(143.1*scale)
ring_spec['SHG']['3minus_5000']['cp']['775TM']['20K']['theta'] = 27
ring_spec['SHG']['3minus_5000']['cp']['775TM']['50K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['50K']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['50K']['d'] = 170*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['50K']['theta'] = 27
ring_spec['SHG']['3minus_5000']['cp']['775TM']['100K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['100K']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['100K']['d'] = round(188.8*scale)
ring_spec['SHG']['3minus_5000']['cp']['775TM']['100K']['theta'] = 27
ring_spec['SHG']['3minus_5000']['cp']['775TM']['200K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['200K']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['200K']['d'] = round(207.6*scale)
ring_spec['SHG']['3minus_5000']['cp']['775TM']['200K']['theta'] = 27
ring_spec['SHG']['3minus_5000']['cp']['775TM']['500K'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['500K']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['500K']['d'] = round(232.5*scale)
ring_spec['SHG']['3minus_5000']['cp']['775TM']['500K']['theta'] = 27
ring_spec['SHG']['3minus_5000']['cp']['775TM']['1M'] = {}
ring_spec['SHG']['3minus_5000']['cp']['775TM']['1M']['w'] = 120*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['1M']['d'] = 250*scale
ring_spec['SHG']['3minus_5000']['cp']['775TM']['1M']['theta'] = 27


ring_spec['DFG']['3minus_4815'] = {'cp':{}}
ring_spec['DFG']['3minus_4815']['w'] = 630*scale
ring_spec['DFG']['3minus_4815']['r'] = 4500*scale
ring_spec['DFG']['3minus_4815']['label'] = '501'
ring_spec['DFG']['3minus_4815']['dw'] = round(0.5*scale)    # M changes by ~1 for every ~22nm change in width
ring_spec['DFG']['3minus_4815']['cp']['1550TE'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['50K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['50K']['w'] = 480*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['50K']['d'] = 220*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['50K']['theta'] = 30
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['100K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['100K']['w'] = 480*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['100K']['d'] = 265*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['100K']['theta'] = 30
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['200K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['200K']['w'] = 480*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['200K']['d'] = 315*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['200K']['theta'] = 30
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['500K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['500K']['w'] = 480*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['500K']['d'] = 375*scale
ring_spec['DFG']['3minus_4815']['cp']['1550TE']['500K']['theta'] = 30
ring_spec['DFG']['3minus_4815']['cp']['1080TE'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['50K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['50K']['w'] = 360*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['50K']['d'] = 100*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['50K']['theta'] = 35
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['100K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['100K']['w'] = 360*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['100K']['d'] = 120*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['100K']['theta'] = 35
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['200K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['200K']['w'] = 360*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['200K']['d'] = 140*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['200K']['theta'] = 35
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['500K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['500K']['w'] = 360*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['500K']['d'] = 170*scale
ring_spec['DFG']['3minus_4815']['cp']['1080TE']['500K']['theta'] = 35
ring_spec['DFG']['3minus_4815']['cp']['637TM'] = {}
ring_spec['DFG']['3minus_4815']['cp']['637TM']['20K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['637TM']['20K']['w'] = 90*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['20K']['d'] = 95*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['20K']['theta'] = 15
ring_spec['DFG']['3minus_4815']['cp']['637TM']['50K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['637TM']['50K']['w'] = 90*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['50K']['d'] = 115*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['50K']['theta'] = 15
ring_spec['DFG']['3minus_4815']['cp']['637TM']['100K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['637TM']['100K']['w'] = 90*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['100K']['d'] = 130*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['100K']['theta'] = 15
ring_spec['DFG']['3minus_4815']['cp']['637TM']['200K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['637TM']['200K']['w'] = 90*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['200K']['d'] = 145*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['200K']['theta'] = 15
ring_spec['DFG']['3minus_4815']['cp']['637TM']['500K'] = {}
ring_spec['DFG']['3minus_4815']['cp']['637TM']['500K']['w'] = 90*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['500K']['d'] = 165*scale
ring_spec['DFG']['3minus_4815']['cp']['637TM']['500K']['theta'] = 15


ring_spec['DFG']['3minus_2870'] = {'cp':{}}
ring_spec['DFG']['3minus_2870']['w'] = 740*scale
ring_spec['DFG']['3minus_2870']['r'] = 2500*scale
ring_spec['DFG']['3minus_2870']['label'] = '502'
ring_spec['DFG']['3minus_2870']['dw'] = round(0.5*scale)
ring_spec['DFG']['3minus_2870']['cp']['1550TE'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K']['w'] = 480*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K']['d'] = 220*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['50K']['theta'] = 40
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['100K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['100K']['w'] = 480*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['100K']['d'] = 260*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['100K']['theta'] = 40
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['200K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['200K']['w'] = 480*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['200K']['d'] = 300*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['200K']['theta'] = 40
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['500K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['500K']['w'] = 480*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['500K']['d'] = 360*scale
ring_spec['DFG']['3minus_2870']['cp']['1550TE']['500K']['theta'] = 40
ring_spec['DFG']['3minus_2870']['cp']['1080TE'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K']['w'] = 320*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K']['d'] = 135*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['50K']['theta'] = 55
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['100K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['100K']['w'] = 320*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['100K']['d'] = 155*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['100K']['theta'] = 55
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['200K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['200K']['w'] = 320*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['200K']['d'] = 175*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['200K']['theta'] = 55
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['500K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['500K']['w'] = 320*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['500K']['d'] = 210*scale
ring_spec['DFG']['3minus_2870']['cp']['1080TE']['500K']['theta'] = 55
ring_spec['DFG']['3minus_2870']['cp']['637TM'] = {}
ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K']['w'] = 130*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K']['d'] = 60*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['20K']['theta'] = 10
ring_spec['DFG']['3minus_2870']['cp']['637TM']['50K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['637TM']['50K']['w'] = 130*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['50K']['d'] = 80*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['50K']['theta'] = 10
ring_spec['DFG']['3minus_2870']['cp']['637TM']['100K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['637TM']['100K']['w'] = 130*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['100K']['d'] = 98*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['100K']['theta'] = 10
ring_spec['DFG']['3minus_2870']['cp']['637TM']['200K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['637TM']['200K']['w'] = 130*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['200K']['d'] = 110*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['200K']['theta'] = 10
ring_spec['DFG']['3minus_2870']['cp']['637TM']['500K'] = {}
ring_spec['DFG']['3minus_2870']['cp']['637TM']['500K']['w'] = 130*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['500K']['d'] = 130*scale
ring_spec['DFG']['3minus_2870']['cp']['637TM']['500K']['theta'] = 10


ring_spec['DFG']['3plus_3275'] = {'cp':{}}
ring_spec['DFG']['3plus_3275']['w'] = 550*scale
ring_spec['DFG']['3plus_3275']['r'] = 3000*scale
ring_spec['DFG']['3plus_3275']['label'] = '503'
ring_spec['DFG']['3plus_3275']['dw'] = round(0.5*scale)
ring_spec['DFG']['3plus_3275']['cp']['1550TE'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['50K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['50K']['w'] = 480*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['50K']['d'] = 220*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['50K']['theta'] = 40
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['100K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['100K']['w'] = 480*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['100K']['d'] = 260*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['100K']['theta'] = 40
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['200K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['200K']['w'] = 480*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['200K']['d'] = 305*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['200K']['theta'] = 40
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['500K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['500K']['w'] = 480*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['500K']['d'] = 360*scale
ring_spec['DFG']['3plus_3275']['cp']['1550TE']['500K']['theta'] = 40
ring_spec['DFG']['3plus_3275']['cp']['1080TE'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['50K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['50K']['w'] = 340*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['50K']['d'] = 110*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['50K']['theta'] = 45
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['100K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['100K']['w'] = 340*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['100K']['d'] = 135*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['100K']['theta'] = 45
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['200K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['200K']['w'] = 340*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['200K']['d'] = 155*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['200K']['theta'] = 45
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['500K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['500K']['w'] = 340*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['500K']['d'] = 185*scale
ring_spec['DFG']['3plus_3275']['cp']['1080TE']['500K']['theta'] = 45
ring_spec['DFG']['3plus_3275']['cp']['637TM'] = {}
ring_spec['DFG']['3plus_3275']['cp']['637TM']['20K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['637TM']['20K']['w'] = 130*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['20K']['d'] = 60*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['20K']['theta'] = 10
ring_spec['DFG']['3plus_3275']['cp']['637TM']['50K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['637TM']['50K']['w'] = 130*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['50K']['d'] = 80*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['50K']['theta'] = 10
ring_spec['DFG']['3plus_3275']['cp']['637TM']['100K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['637TM']['100K']['w'] = 130*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['100K']['d'] = 98*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['100K']['theta'] = 10
ring_spec['DFG']['3plus_3275']['cp']['637TM']['200K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['637TM']['200K']['w'] = 130*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['200K']['d'] = 108*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['200K']['theta'] = 10
ring_spec['DFG']['3plus_3275']['cp']['637TM']['500K'] = {}
ring_spec['DFG']['3plus_3275']['cp']['637TM']['500K']['w'] = 130*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['500K']['d'] = 125*scale
ring_spec['DFG']['3plus_3275']['cp']['637TM']['500K']['theta'] = 10

ring_spec['DFG']['1-4minus_3375'] = {'cp':{}}
ring_spec['DFG']['1-4minus_3375']['w'] = 750*scale
ring_spec['DFG']['1-4minus_3375']['r'] = 3000*scale
ring_spec['DFG']['1-4minus_3375']['label'] = '504'
ring_spec['DFG']['1-4minus_3375']['dw'] = round(0.5*scale)
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['50K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['50K']['w'] = 480*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['50K']['d'] = 220*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['50K']['theta'] = 40
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['100K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['100K']['w'] = 480*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['100K']['d'] = 260*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['100K']['theta'] = 40
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['200K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['200K']['w'] = 480*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['200K']['d'] = 300*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['200K']['theta'] = 40
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['500K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['500K']['w'] = 480*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['500K']['d'] = 360*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1550TE']['500K']['theta'] = 40
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['20K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['20K']['w'] = 300*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['20K']['d'] = 90*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['20K']['theta'] = 25
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['50K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['50K']['w'] = 300*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['50K']['d'] = 115*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['50K']['theta'] = 25
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['100K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['100K']['w'] = 300*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['100K']['d'] = 140*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['100K']['theta'] = 25
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['200K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['200K']['w'] = 300*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['200K']['d'] = 170*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['200K']['theta'] = 25
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['500K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['500K']['w'] = 300*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['500K']['d'] = 200*scale
ring_spec['DFG']['1-4minus_3375']['cp']['1080TE']['500K']['theta'] = 25
ring_spec['DFG']['1-4minus_3375']['cp']['637TM'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['20K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['20K']['w'] = 90*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['20K']['d'] = 80*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['20K']['theta'] = 10
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['50K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['50K']['w'] = 90*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['50K']['d'] = 103*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['50K']['theta'] = 10
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['100K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['100K']['w'] = 90*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['100K']['d'] = 120*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['100K']['theta'] = 10
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['200K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['200K']['w'] = 90*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['200K']['d'] = 135*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['200K']['theta'] = 10
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['500K'] = {}
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['500K']['w'] = 90*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['500K']['d'] = 155*scale
ring_spec['DFG']['1-4minus_3375']['cp']['637TM']['500K']['theta'] = 10



d_gr = [a*scale for a in [50, 75, 100, 150, 200, 250, 300]]
d_min = 50*scale


gr_spec = {'1550TE':{'shape':{}},\
                    '1080TE':{'shape':{}},\
                    '637TM':{'shape':{}},\
                    '775TM':{'shape':{}},\
                    'SHG':{'shape':{}},\
                    'DFG':{'shape':{}}}

gr_spec['1550TE']['ribs'] = [max(0.96*a*scale,d_min) for a in [645,495,140,670,285,325,760,750,285]]
gr_spec['1550TE']['gaps'] = [max(0.96*d_gr[i-1],d_min) for i in [1,4,1,7,3,4,4,4,6]]
gr_spec['1550TE']['label'] = '0'
gr_spec['1550TE']['shape']['str'] = {}
gr_spec['1550TE']['shape']['str']['w'] = 3500*scale
gr_spec['1550TE']['shape']['str']['L'] = 12000*scale
gr_spec['1550TE']['shape']['ell'] = {}
gr_spec['1550TE']['shape']['ell']['L'] = 12000*scale
gr_spec['1550TE']['shape']['ell']['arc'] = 30
gr_spec['1550TE']['shape']['ell']['theta'] = 30
gr_spec['1550TE']['shape']['ell']['ecc'] = 0.1

gr_spec['1080TE']['ribs'] = [max(1.00*a*scale,d_min) for a in [105,445,780,550,560,80,245,710]]
gr_spec['1080TE']['gaps'] = [max(1.00*d_gr[i-1],d_min) for i in [4,2,7,7,1,7,6,2]]
gr_spec['1080TE']['label'] = '1'
gr_spec['1080TE']['shape']['str'] = {}
gr_spec['1080TE']['shape']['str']['w'] = 2500*scale
gr_spec['1080TE']['shape']['str']['L'] = 10000*scale
gr_spec['1080TE']['shape']['ell'] = {}
gr_spec['1080TE']['shape']['ell']['L'] = 10000*scale
gr_spec['1080TE']['shape']['ell']['arc'] = 30
gr_spec['1080TE']['shape']['ell']['theta'] = 20
gr_spec['1080TE']['shape']['ell']['ecc'] = 0.1

gr_spec['637TM']['ribs'] = [max(1.01*a*scale,d_min) for a in [385,310,615,310,265,205,280,135,710]]
gr_spec['637TM']['gaps'] = [max(1.01*d_gr[i-1],d_min) for i in [1,5,5,4,5,2,7,5,1]]
gr_spec['637TM']['label'] = '2'
gr_spec['637TM']['shape']['str'] = {}
gr_spec['637TM']['shape']['str']['w'] = 1500*scale
gr_spec['637TM']['shape']['str']['L'] = 8000*scale
gr_spec['637TM']['shape']['ell'] = {}
gr_spec['637TM']['shape']['ell']['L'] = 6000*scale
gr_spec['637TM']['shape']['ell']['arc'] = 25
gr_spec['637TM']['shape']['ell']['theta'] = 30
gr_spec['637TM']['shape']['ell']['ecc'] = 0.1

gr_spec['775TM']['ribs'] = [max(0.97*a*scale,d_min) for a in [540,225,150,485,555,465,795,495,165]]
gr_spec['775TM']['gaps'] = [max(0.97*d_gr[i-1],d_min) for i in [1,2,6,5,1,7,6,6,3]]
gr_spec['775TM']['label'] = '3'
gr_spec['775TM']['shape']['str'] = {}
gr_spec['775TM']['shape']['str']['w'] = 1800*scale
gr_spec['775TM']['shape']['str']['L'] = 8000*scale
gr_spec['775TM']['shape']['ell'] = {}
gr_spec['775TM']['shape']['ell']['L'] = 8000*scale
gr_spec['775TM']['shape']['ell']['arc'] = 25
gr_spec['775TM']['shape']['ell']['theta'] = 30
gr_spec['775TM']['shape']['ell']['ecc'] = 0.1

gr_spec['SHG']['ribs'] = [max((1/0.982)*a*scale,d_min) for a in  [240,775,520,470,625,295,790,255,725]]
gr_spec['SHG']['gaps'] = [max(d_gr[i-1],d_min) for i in [2,2,2,1,6,2,4,7,6]]
gr_spec['SHG']['label'] = '4'
gr_spec['SHG']['shape']['str'] = {}
gr_spec['SHG']['shape']['str']['w'] = 3500*scale
gr_spec['SHG']['shape']['str']['L'] = 12000*scale
gr_spec['SHG']['shape']['ell'] = {}
gr_spec['SHG']['shape']['ell']['L'] = 10000*scale
gr_spec['SHG']['shape']['ell']['arc'] = 25
gr_spec['SHG']['shape']['ell']['theta'] = 30
gr_spec['SHG']['shape']['ell']['ecc'] = 0.15

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

gr_spec['DFG']['ribs'] = [max(0.97*a*scale,d_min) for a in [380,380,380,630,740,490,540,190,180,620]]
gr_spec['DFG']['gaps'] = [max(0.97*d_gr[i-1],d_min) for i in [7,1,1,1,3,7,3,7,6,5]]
gr_spec['DFG']['label'] = '5'
gr_spec['DFG']['shape']['str'] = {}
gr_spec['DFG']['shape']['str']['w'] = 3500*scale
gr_spec['DFG']['shape']['str']['L'] = 12000*scale
gr_spec['DFG']['shape']['ell'] = {}
gr_spec['DFG']['shape']['ell']['L'] = 12000*scale
gr_spec['DFG']['shape']['ell']['arc'] = 30
gr_spec['DFG']['shape']['ell']['theta'] = 30
gr_spec['DFG']['shape']['ell']['ecc'] = 0.1


gr_spec['1550TE']['shape']['str']['L_total'] = gr_spec['1550TE']['shape']['str']['L'] +  sum(gr_spec['1550TE']['ribs']) + sum(gr_spec['1550TE']['ribs'])
gr_spec['1550TE']['shape']['ell']['L_total'] = gr_spec['1550TE']['shape']['ell']['L'] +  sum(gr_spec['1550TE']['ribs']) + sum(gr_spec['1550TE']['ribs'])

gr_spec['1080TE']['shape']['str']['L_total'] = gr_spec['1080TE']['shape']['str']['L'] +  sum(gr_spec['1080TE']['ribs']) + sum(gr_spec['1080TE']['ribs'])
gr_spec['1080TE']['shape']['ell']['L_total'] = gr_spec['1080TE']['shape']['ell']['L'] +  sum(gr_spec['1080TE']['ribs']) + sum(gr_spec['1080TE']['ribs'])

gr_spec['637TM']['shape']['str']['L_total'] = gr_spec['637TM']['shape']['str']['L'] +  sum(gr_spec['637TM']['ribs']) + sum(gr_spec['637TM']['ribs'])
gr_spec['637TM']['shape']['ell']['L_total'] = gr_spec['637TM']['shape']['ell']['L'] +  sum(gr_spec['637TM']['ribs']) + sum(gr_spec['637TM']['ribs'])

gr_spec['775TM']['shape']['str']['L_total'] = gr_spec['775TM']['shape']['str']['L'] +  sum(gr_spec['775TM']['ribs']) + sum(gr_spec['775TM']['ribs'])
gr_spec['775TM']['shape']['ell']['L_total'] = gr_spec['775TM']['shape']['ell']['L'] +  sum(gr_spec['775TM']['ribs']) + sum(gr_spec['775TM']['ribs'])

gr_spec['SHG']['shape']['str']['L_total'] = gr_spec['SHG']['shape']['str']['L'] +  sum(gr_spec['SHG']['ribs']) + sum(gr_spec['SHG']['ribs'])
gr_spec['SHG']['shape']['ell']['L_total'] = gr_spec['SHG']['shape']['ell']['L'] +  sum(gr_spec['SHG']['ribs']) + sum(gr_spec['SHG']['ribs'])

gr_spec['DFG']['shape']['str']['L_total'] = gr_spec['DFG']['shape']['str']['L'] +  sum(gr_spec['DFG']['ribs']) + sum(gr_spec['DFG']['ribs'])
gr_spec['DFG']['shape']['ell']['L_total'] = gr_spec['DFG']['shape']['ell']['L'] +  sum(gr_spec['DFG']['ribs']) + sum(gr_spec['DFG']['ribs'])


# directional coupler specifications

dc_spec = {'SHG':{}}

dc_spec['SHG']['sym_v1'] = {}
dc_spec['SHG']['sym_v1']['w'] = 450*scale
dc_spec['SHG']['sym_v1']['d'] = 105*scale
dc_spec['SHG']['sym_v1']['L'] = 18000*scale # originally 20000*scale
dc_spec['SHG']['sym_v1']['offset'] = 2500*scale
dc_spec['SHG']['asym_v1'] = {}
dc_spec['SHG']['asym_v1']['w'] = 500*scale
dc_spec['SHG']['asym_v1']['w2'] = 450*scale
dc_spec['SHG']['asym_v1']['d'] = 100*scale
dc_spec['SHG']['asym_v1']['L'] = 18500*scale
dc_spec['SHG']['asym_v1']['offset'] = 2500*scale


# Layout specifications

layout_spec = {'lr':{},\
               'gtest':{},\
			   'cp_ring':{},\
			   'dc':{}}

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


layout_spec['cp_ring']['SHG'] = {}

layout_spec['cp_ring']['SHG']['3minus_5000'] = {'cp':{}}
layout_spec['cp_ring']['SHG']['3minus_5000']['marker'] = (10000*scale, -5000*scale)
layout_spec['cp_ring']['SHG']['3minus_5000']['label'] = (9000*scale, 7500*scale)
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std'] = {'1550TE':{},'775TM':{}}
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['theta'] = 180
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['in']['pt'] = (20000*scale, -31000*scale)
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['in']['min'][0] = 15000*scale
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['in']['min'][3] = 27000*scale
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['out']['pt'] = (-7000*scale, -20000*scale)
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['theta'] = -45
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['in'] = {'min':{}}
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['in']['orient'] = 3
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['in']['pt'] = (8000*scale, -24000*scale)
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['out'] = {'min':{}}
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['out']['orient'] = 2
layout_spec['cp_ring']['SHG']['3minus_5000']['cp']['std']['775TM']['out']['pt'] = (15000*scale, -6000*scale)


layout_spec['cp_ring']['DFG'] = {}

layout_spec['cp_ring']['DFG']['3minus_4815'] = {'cp':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['marker'] = (8000*scale, -2000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['label'] = (2500*scale, -12000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std'] = {'1550TE':{},'1080TE':{},'637TM':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['theta'] = 100
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['pt'] = (21000*scale, -33000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['min'][3] = 26000*scale
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out']['pt'] = (-15000*scale, -24000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['theta'] = 325
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['in']['pt'] = (6000*scale, -22000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out']['pt'] = (15000*scale, -1000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out']['min'][3] = 25000*scale
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['theta'] = 205
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['in']['pt'] = (-8000*scale, -35000*scale)
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['out']['pt'] = (0*scale, -21000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['marker'] = (10000*scale, -5000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['label'] = (4000*scale, -10000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std'] = {'1550TE':{},'1080TE':{},'637TM':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['theta'] = 100
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['orient'] = 1
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['pt'] = (8000*scale, -33000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['min'][0] = 24000*scale
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['in']['min'][3] = 26000*scale
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out']['orient'] = 2
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1550TE']['out']['pt'] = (-15000*scale, -17000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['theta'] = 328
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['in'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['in']['orient'] = 3
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['in']['pt'] = (4000*scale, -22000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out']['orient'] = 2
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out']['pt'] = (20000*scale, -1000*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['1080TE']['out']['min'][3] = 25000*scale
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['theta'] = 190
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['in'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['in']['orient'] = 3
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['in']['pt'] = (-8000*scale, -25500*scale)
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['out'] = {'min':{}}
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['out']['orient'] = 2
# layout_spec['cp_ring']['DFG']['3minus_4815']['cp']['std']['637TM']['out']['pt'] = (0*scale, -10000*scale)

layout_spec['cp_ring']['DFG']['3minus_2870'] = {'cp':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['marker'] = (8000*scale, -2000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['label'] = (1500*scale, -10000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std'] = {'1550TE':{},'1080TE':{},'637TM':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['theta'] = 110
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['pt'] = (21000*scale, -33000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['in']['min'][3] = 26000*scale
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1550TE']['out']['pt'] = (-15000*scale, -24000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['theta'] = 325
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['in']['pt'] = (6000*scale, -22000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out']['pt'] = (15000*scale, -1000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['1080TE']['out']['min'][3] = 25000*scale
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['theta'] = 205
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['in']['pt'] = (-8000*scale, -35000*scale)
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3minus_2870']['cp']['std']['637TM']['out']['pt'] = (0*scale, -21000*scale)

layout_spec['cp_ring']['DFG']['3plus_3275'] = {'cp':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['marker'] = (8000*scale, -2000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['label'] = (2000*scale, -10000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std'] = {'1550TE':{},'1080TE':{},'637TM':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['theta'] = 110
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['in']['pt'] = (21000*scale, -33000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['in']['min'][3] = 26000*scale
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1550TE']['out']['pt'] = (-15000*scale, -24000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['theta'] = 325
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['in']['pt'] = (6000*scale, -22000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['out']['pt'] = (15000*scale, -1000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['1080TE']['out']['min'][3] = 25000*scale
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['theta'] = 205
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['in']['pt'] = (-8000*scale, -35000*scale)
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['3plus_3275']['cp']['std']['637TM']['out']['pt'] = (0*scale, -21000*scale)


layout_spec['cp_ring']['DFG']['1-4minus_3375'] = {'cp':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['marker'] = (8000*scale, -2000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['label'] = (2000*scale, -10000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std'] = {'1550TE':{},'1080TE':{},'637TM':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['theta'] = 110
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['in']['orient'] = 1
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['in']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['in']['pt'] = (21000*scale, -33000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['in']['min'][3] = 26000*scale
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['out']['curl'] = 'ccw'
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1550TE']['out']['pt'] = (-15000*scale, -24000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['theta'] = 325
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['in']['pt'] = (6000*scale, -22000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['out']['pt'] = (15000*scale, -1000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['1080TE']['out']['min'][3] = 25000*scale
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['theta'] = 205
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['in'] = {'min':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['in']['orient'] = 3
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['in']['pt'] = (-8000*scale, -35000*scale)
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['out'] = {'min':{}}
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['out']['orient'] = 2
layout_spec['cp_ring']['DFG']['1-4minus_3375']['cp']['std']['637TM']['out']['pt'] = (0*scale, -21000*scale)



layout_spec['dc']['SHG'] = {}

layout_spec['dc']['SHG']['sym_v1'] = {'cp':{}}
layout_spec['dc']['SHG']['sym_v1']['marker'] = (-5000*scale, -3000*scale)
layout_spec['dc']['SHG']['sym_v1']['label'] = (-12000*scale, 5000*scale)
layout_spec['dc']['SHG']['sym_v1']['cp']['test'] = {'cis':{},'trans':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['cis']['in'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['cis']['in']['orient'] = 1
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['cis']['out'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['cis']['out']['orient'] = 2
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['trans']['in'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['trans']['in']['orient'] = 2
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['trans']['out'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['test']['trans']['out']['orient'] = 2

layout_spec['dc']['SHG']['sym_v1']['cp']['resonator'] = {}

layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating'] = {'cis':{},'trans':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['cis']['in'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['cis']['in']['orient'] = 1
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['cis']['out'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['cis']['out']['orient'] = 0.5
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['trans']['in'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['trans']['in']['orient'] = 2
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['trans']['out'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['grating']['trans']['out']['orient'] = 2

layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper'] = {'cis':{},'trans':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper']['cis']['in'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper']['cis']['in']['orient'] = 1
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper']['cis']['out'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper']['cis']['out']['orient'] = 0.5
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper']['trans']['in'] = {'min':{}}
layout_spec['dc']['SHG']['sym_v1']['cp']['resonator']['taper']['trans']['in']['orient'] = 2

#Device array specifications

array_spec = {'lr':{},\
			  'gtest':{},\
			  'cp_ring':{},\
			  'dc':{}}

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

array_spec['dc']['test'] = {}
array_spec['dc']['test']['x'] = (40000*scale, 0*scale)
array_spec['dc']['test']['y'] = (0*scale, 70000*scale)
array_spec['dc']['test']['rep'] = 3

array_spec['dc']['resonator'] = {}
array_spec['dc']['resonator']['x'] = (40000*scale, 0*scale)
array_spec['dc']['resonator']['y'] = (0*scale, 70000*scale)
array_spec['dc']['resonator']['rep'] = 1

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
