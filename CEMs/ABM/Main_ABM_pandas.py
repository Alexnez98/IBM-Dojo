from __future__ import division
import numpy as np
from random import choice, shuffle
import sys
import os
2qaimport pandas as pd
from numpy.random import seed

# mydir = os.path.expanduser('~/GitHub/Python-ABMs/CEMs/ABM')
mydir = os.path.expanduser('~/GitHub/IBM-Dojo/CEMs/ABM')

sys.path.append(mydir)

import SimFxns

file_name = '2020_07_11_1635_MasterData.txt'
MainDF = pd.read_csv(mydir + '/GIS_Data_Frame/'+file_name, delimiter="\t")

ch_names = list(MainDF['Chapters'])
ch_lats = list(MainDF['Lat'])
ch_lons = list(MainDF['Lon'])

#for i, val in enumerate(ch_names):
#    print(val, ch_lats[i], ch_lons[i])
#sys.exit()
    
#print(len(ch_names), len(ch_lats), len(ch_lats))
#sys.exit()

ch_pops = list(MainDF['Population'])
N = sum(ch_pops)

ch_rel_popsize = np.array(ch_pops)/N # relative pop size = probability

############ Above: code taken from Main_ABM.py

# -----------------------------------------------------------------------------

############ Below: declaring dataframe using column names
      
column_names = ['sex', 'age', 'dsi', 'dsr', 'dsv','ebs', 'ebr', 'ebv', 'vac', 
                'rec', 'con', 'inf', 'home_chapter', 'c_lat', 'c_lon', 'alive']               
               
df_NN = pd.DataFrame(columns = column_names)

############ Below: filling dataframe

### Get sexes
df_NN['sex'] = np.random.binomial(1, 0.53, N)  # 1 == Female ; 0 = Male    

### Get ages
Age_0_9 = 30558/N
Age_10_19 = 34320/N
Age_20_29 = 23827/N
Age_30_39 = 19797/N
Age_40_49 = 22123/N
Age_50_59 = 19469/N
Age_60_69 = 12307/N
Age_70_79 = 6980/N
Age_80 = 3599/N

age_groups = [0, 10, 20, 30, 40, 50, 60, 70, 80]
demographies = [Age_0_9,Age_10_19, Age_20_29, Age_30_39, Age_40_49, Age_50_59,
                Age_60_69, Age_70_79, Age_80]

df_NN['age'] = np.random.choice(age_groups, size=N, replace=True, p=demographies)

### Get home chapters
#rand_seed = np.random.randint(0)

seed(0)
df_NN['home_chapter'] = np.random.choice(ch_names, size = N, 
     replace=True, p=ch_rel_popsize)

seed(0)
df_NN['c_lat'] = np.random.choice(ch_lats, size = N, 
     replace=True, p=ch_rel_popsize)

seed(0)
df_NN['c_lon'] = np.random.choice(ch_lons, size = N, 
     replace=True, p=ch_rel_popsize)

#print(df_NN['home_chapter'][0], df_NN['c_lat'][0], df_NN['c_lon'][0])

df_NN['dsi'] = 0
df_NN['dsr'] = 0
df_NN['dss'] = 0
df_NN['ebs'] = 0
df_NN['ebr'] = 0
df_NN['ebv'] = 0
df_NN['vac'] = 0
df_NN['rec'] = 0
df_NN['con'] = 0
df_NN['inf'] = 0
df_NN['alive'] = 1

female_df = df_NN[df_NN['sex'] == 1]

for x in range(1):
    N = 1000 #individual organisms
    S = 1  # Number of species
    nat_ded = 0.1
    inf_ded = 0.6
    imm = 2  
    # Lists for properties of individuals
    inds = list(range(N))
    sick = [0]*N
    x_coords = [0]*N
    y_coords = [0]*N 
    ages = np.random.randint(0, 7500, len(inds)) # age in days
    sex = np.random.binomial(1, 0.5, len(inds)) # 1 = male; 0 = female
    dsi = [0]*N
    dsr = [0]*N
    ebs = [0]*N
    ebr = [0]*N
    vac = [0]*N
    rec = [0]*N 
    con = [0]*N
    days = 1

    t = 0 # start at generation 0
    for i in range(days):
        inds = df_NN.index.tolist()
        shuffle(inds)
        for j, i1 in enumerate(inds):
            if j >= 10:
                sys.exit()
            print(len(inds))
            t += 1 # increment generation 
            j = choice([0])
            if j == 0:
                female_df, df_NN = SimFxns.reproduce(female_df, df_NN)
            elif j == 1:
                inds, sick, x_coords, y_coords = SimFxns.death(inds, sick,x_coords, y_coords)
                # take death list values and assign them to inds, sick, x_coords, y_coords
            elif j == 2:
                inds, sick, x_coords, y_coords = SimFxns.dispersal(inds, sick, x_coords, y_coords)
            elif j == 3:
                inds, sick, x_coords, y_coords = SimFxns.immigration(inds, sick, x_coords, y_coords)
            elif j == 4:
                inds, sick, x_coords, y_coords = SimFxns.infection(inds, sick, x_coords, y_coords)
            elif j == 5:
                inds, sick, x_coords, y_coords = SimFxns.recover(inds, sick, x_coords, y_coords, rec)
            elif j == 6:
                inds, sick, x_coords, y_coords = SimFxns.incubation(inds, sick, x_coords, y_coords)
        Ni = len(inds)
        Si = len(list(set(sick)))
        NumSick = sum(sick)
        Healthy = len(sick) - sum(sick)
        
print(df_NN.shape)
print(list(df_NN))
sys.exit()