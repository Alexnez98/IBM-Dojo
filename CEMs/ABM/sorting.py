# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:36:25 2020

@author: AlexanderNez
"""

from __future__ import division
import numpy as np
from random import choice
import sys
import os
import pandas as pd
from numpy.random import seed

mydir = os.path.expanduser('~/GitHub/IBM-Dojo/CEMs/ABM')
sys.path.append(mydir)

import SimFxns

#OUT = open(mydir + '/SimData/main_data.txt', 'w+')
#print(OUT, 'sim,disease,day,N,Nmale,Nfemale,N_age10orless,N_age20orless, ...') # etc.
#OUT.close()
file_name = '2020_07_11_1635_MasterData.txt'
MainDF = pd.read_csv(mydir + '/GIS_Data_Frame/'+file_name, delimiter="\t")

ch_names = list(set(MainDF['Chapters'])) # List of 110 Navajo Chapter
ch_lats = list(set(MainDF['Lat']) # List of corresponding Lat with respect to their chpater
ch_lons = list(set(MainDF['Lon']) # List of corresponding Lat with respect to their chpater
# set() takes a column and checks if they're no duplicated in the column
# list() turns the unquie set into into a list of variable 

nat_ded = 0.1 # The chance of an indivdual dying from natural causes. 
inf_ded = 0. # The chance of dying for the choosen diseases causes. 
imm = 2  # the rate of how much individuals 
disease = "HantaViruS"
#print(len(chapter_names))
#sys.exit() 

chapter_pops = list(MainDF['Population'])
N = sum(chapter_pops)
 
#print(len(chapter_pops), min(chapter_pops), max(chapter_pops), sum(chapter_pops)/N)
#sys.exit()

ch_rel_popsize = np.array(chapter_pops)/N # relative pop size = probability

num_sims = 1

column_names = ['sex', 'age', 'dsi', 'dsr', 'dsv','ebs', 'ebr', 'ebv', 'vac', 
                'rec', 'con', 'inf', 'home_chapter', 'c_lat', 'c_lon', 'alive']               
               
df_NN = pd.DataFrame(columns = column_names)

df_NN['sex'] = np.random.binomial(1, 0.53, N)  # 1 == Female ; 0 = Male    

### Get ages
Age_0_9 = 30558/N
Age_10_19 = 34320/N
Age_20_29 = 23827/N
Age_30_39 = 19797/N
Age_40_49 = 22123/N
Age_50_59 = 19469/N
Age_60_69 = 12307/N
Age_70_79 = 7667/N
Age_80 = 3599/N

age_groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
demographies = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

age_groups = [10, 20, 30, 40, 50, 60, 70, 80]
demographies = [Age_0_9,Age_10_19, Age_20_29, Age_30_39, Age_40_49, Age_50_59,
                Age_60_69, Age_70_79, Age_80]
df_NN['age'] = np.random.choice(age_groups, size=N, replace=True, 
     p=demographies)

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

print(df_NN.shape)
print(list(df_NN))            

Ni = len(iDict)
print('simulation:', sim, '| Day:', day, ' | N:', N)
keys = iDict.keys()
for i in keys:
   x = keys[i]
   print(x)
   sys.exit()
   #print(key)
   #sys.exit()
   
   # SimFxns ARE COMMENTED OUT FOR THE PURPOSE OF JUST HAVING THE CODE RUN
   # AND HAVING agg_data INITIATED AND PROCESSED       
        
   j = choice([0])#, 1, 2, 3, 4, 5, 6])
   if j == 0 and val['sex'] == 'f':
       iDict = SimFxns.reproduce(key, iDict, MainDF, disease, chDict)
   elif j == 1:
       iDict = SimFxns.death(key, iDict, MainDF, disease, chDict)
   elif j == 2:
       iDict = SimFxns.dispersal(key, iDict, MainDF, disease, chDict)
   elif j == 3:
       iDict = SimFxns.immigration(key, iDict, MainDF, disease, chDict)
   elif j == 4:
       iDict = SimFxns.infection(key, iDict, MainDF, disease, chDict)
   elif j == 5:
       iDict = SimFxns.recover(key, iDict, MainDF, disease, chDict)
   elif j == 6:
       iDict = SimFxns.incubation(key, iDict, MainDF, disease, chDict)
                 
   inf = val['inf']
   rec = val['rec']
   vac = val['vac']
   age = val['age']
   sex = val['sex']
   alive = val['alive']
   ch = val['home_chapter']
        
   p1, p2, p3 = str(), str(), str()
        
   if sex == 'm': p1 = 'm_'
   else: p1 = 'f_'
        
   if alive == 1: p2 = 'a_'
   else: p2 = 'd_'
        
   if rec == 0:
       p3 = 'rec_'
       agg_data[ch][p1+p2+p3+'age'][age] += 1
   if inf == 0:
       p3 = 'inf_'
       agg_data[ch][p1+p2+p3+'age'][age] += 1
   if vac == 0:
       p3 = 'inf_'
       agg_data[ch][p1+p2+p3+'age'][age] += 1
         
       print(agg_data['Becenti'])
    #sys.exit()
        
       outlist = [sim, disease, day, N] # list to hold data 
    
    # Process data in agg_data to get data for outlist
        
    # write data to file for every day
    #OUT = open(mydir + '/SimData/main_data.txt', 'a+')
    #print>>OUT, # what to print
    #OUT.close()
    
       chapter_rel_popsize = sum(chapter_pops)/N