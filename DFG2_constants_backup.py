# all units in nanometers
# for 430nm GaP
scale = 20
res = 120

wg_1TE_w = 550*scale
wg_1TE_wf = 400*scale
wg_2TE_w = 360*scale
wg_2TE_wf = 230*scale
wg_3TE_w = 190*scale
wg_3TE_wf = 100*scale

wg_1TM_w = 400*scale
wg_1TM_wf = 320*scale
wg_3TM_w = 110*scale
wg_3TM_wf = 40*scale
wg_4TM_w = 170*scale
wg_4TM_wf = 70*scale

wg_1_r = 6000*scale
wg_2_r = 5000*scale
wg_3_r = 3000*scale
wg_4_r = 3200*scale

y_1_w = 1200*scale
y_2_w = 900*scale
y_3_w = 600*scale
y_4_w = 700*scale

y_1_L = 8000*scale
y_2_L = 6000*scale
y_3_L = 4500*scale
y_4_L = 4500*scale


correction_1TE = 1550.0/1590    #chip 1 grating
grating_1TE_gaps = [round(a*correction_1TE*scale) for a in [150,150,300,300,300,150]]
grating_1TE_ribs = [round(a*correction_1TE*scale) for a in [610,590,740,750,690,520]]
grating_1_w = 3500*scale
grating_1_len = 12000*scale #for straight grating
grating_1TE_exp = 12000*scale # for elliptical
grating_1TE_arc = 30
grating_1_theta = 45
grating_1_ecc = 0.1

correction_1TM = 1550.0/1535  #2017 Aug 6 Run 2
grating_1TM_gaps = [round(a*correction_1TM*scale) for a in [50,50,50,100,200,250,250]]
grating_1TM_ribs = [round(a*correction_1TM*scale) for a in [660,560,490,570,610,550,330]]
grating_1TM_exp = 12000*scale # for elliptical
grating_1TM_arc = 30

#correction_2TE = 1081.4/1040   #Chip 1 grating
#grating_2TE_gaps = [round(a*correction_2TE*scale) for a in [150,250,250,250,150,150]]
#grating_2TE_ribs = [round(a*correction_2TE*scale) for a in [360,340,340,340,280,280]]
correction_2TE = 1081.4/1061    #2017 Aug 7 Run 5
grating_2TE_gaps = [round(a*correction_2TE*scale) for a in [50,100,50,300,300,300,150,200]]
grating_2TE_ribs = [round(a*correction_2TE*scale) for a in [720,580,690,700,130,270,280,50]]
grating_2_w = 2500*scale
grating_2_len = 10000*scale #for straight grating
grating_2TE_exp = 10000*scale # for elliptical
grating_2TE_arc = 30
grating_2_theta = 45
grating_2_ecc = 0.1

correction_3TM = 637.0/631; #Chip 1 grating
grating_3TM_gaps = [round(a*correction_3TM*scale) for a in [50,50,50,150,150,150,150]]
grating_3TM_ribs = [round(a*correction_3TM*scale) for a in [180,320,170,170,170,160,240]]
grating_3_w = 1500*scale
grating_3_len = 8000*scale #for straight grating
grating_3TM_exp = 10000*scale # for elliptical
grating_3TM_arc = 20
grating_3_theta = 45
grating_3_ecc = 0.1

correction_3TE = 637.0/632;   #2017 Aug 7 Run 6
grating_3TE_gaps = [round(a*correction_3TE*scale) for a in [75,75,75,50,75,300,75]]
grating_3TE_ribs = [round(a*correction_3TE*scale) for a in [390,100,600,130,190,770,210]]
grating_3TE_exp = 8000*scale # for elliptical
grating_3TE_arc = 30

correction_4TM = 775.0/750
grating_4TM_gaps = [round(a*correction_4TM*scale) for a in [50,50,150,150,150,150,150]]
grating_4TM_ribs = [round(a*correction_4TM*scale) for a in [450,480,240,480,200,350,350]]
grating_4_w = 2000*scale
grating_4_len = 8000*scale #for straight grating
grating_4TM_exp = 10000*scale # for elliptical
grating_4TM_arc = 20
grating_4_theta = 45
grating_4_ecc = 0.1

text_h = 4000*scale
text_t = 400*scale
text_d = 2800*scale
text_res = 36


#Feature sizes for loss rings
lr_1_d1 = 150*scale
lr_1_d2 = 250*scale

lr_1TE_w1 = 400*scale
lr_1TE_w2 = 550*scale
lr_1TE_w3 = 700*scale
lr_1TE_w = range(400*scale, 900*scale, 50*scale)

lr_1TM_w1 = 320*scale
lr_1TM_w2 = 400*scale
lr_1TM_w3 = 480*scale
lr_1TM_w = range(320*scale, 820*scale, 50*scale)

lr_2_d1 = 120*scale
lr_2_d2 = 200*scale

lr_2TE_w1 = 230*scale
lr_2TE_w2 = 360*scale
lr_2TE_w3 = 500*scale
lr_2TE_w = range(240*scale, 740*scale, 50*scale)

lr_3_d1 = 60*scale
lr_3_d2 = 100*scale

lr_3TE_w1 = 100*scale
lr_3TE_w2 = 200*scale
lr_3TE_w3 = 300*scale
lr_3TE_w = range(100*scale, 600*scale, 50*scale)

lr_3TM_w1 = 50*scale
lr_3TM_w2 = 125*scale
lr_3TM_w3 = 200*scale
lr_3TM_w = range(50*scale, 550*scale, 50*scale)

lr_4_d1 = 80*scale
lr_4_d2 = 120*scale

lr_4TM_w1 = 70*scale
lr_4TM_w2 = 140*scale
lr_4TM_w3 = 210*scale
lr_4TM_w = range(70*scale, 570*scale, 50*scale)

lr_r = range(2000*scale, 7000*scale, 500*scale)

#Lattice constants for elliptical-grating loss rings
lr_ell_1_x1 = 70000*scale
lr_ell_1_y1 = 21000*scale
lr_ell_1_x2 = -42000*scale
lr_ell_1_y2 = 22000*scale

lr_ell_2_x1 = 56000*scale
lr_ell_2_y1 = 17500*scale
lr_ell_2_x2 = -32000*scale
lr_ell_2_y2 = 17500*scale

lr_ell_3_x1 = 40000*scale
lr_ell_3_y1 = 11500*scale
lr_ell_3_x2 = -23000*scale
lr_ell_3_y2 = 13500*scale

lr_ell_4_x1 = 54000*scale
lr_ell_4_y1 = 8000*scale
lr_ell_4_x2 = -31500*scale
lr_ell_4_y2 = 13500*scale

# Lattice constants for reference-grating loss rings
lr_ref_1_x1 = 56000*scale
lr_ref_1_y1 = 37000*scale
lr_ref_1_x2 = -39000*scale
lr_ref_1_y2 = 34000*scale

lr_ref_2_x1 = 43000*scale
lr_ref_2_y1 = 31000*scale
lr_ref_2_x2 = -31000*scale
lr_ref_2_y2 = 29000*scale

lr_ref_3_x1 = 28000*scale
lr_ref_3_y1 = 18000*scale
lr_ref_3_x2 = -20000*scale
lr_ref_3_y2 = 21000*scale

lr_ref_4_x1 = 32000*scale
lr_ref_4_y1 = 20000*scale
lr_ref_4_x2 = -24000*scale
lr_ref_4_y2 = 24000*scale

# 
ro_1_x = 34000*scale
ro_1_y = 300000*scale

ro_2_x = 30000*scale
ro_2_y = 287000*scale

ro_3_x = 24000*scale
ro_3_y = 278000*scale

ro_4_x = 24000*scale
ro_4_y = 278000*scale


DFG_SR2_ring_r = 6900*scale  # Single Ring DFG, 637 TM, version 2 (wide)
DFG_SR2_ring_w = 900*scale

DFG_SR2_couple_1_d = 190*scale
DFG_SR2_couple_1_w = 480*scale
DFG_SR2_couple_1_theta = 87.5

DFG_SR2_couple_2_d = 125*scale
DFG_SR2_couple_2_w = 375*scale
DFG_SR2_couple_2_theta = 110

DFG_SR2_couple_3_d = 100*scale
DFG_SR2_couple_3_w = 100*scale
DFG_SR2_couple_3_theta = 40

DFG_SR2_delta_w = 0.454*scale
DFG_SR2_delta_x = 60000*scale
DFG_SR2_delta_y = 75000*scale
DFG_SR2_array_x = 7
DFG_SR2_array_y = 6