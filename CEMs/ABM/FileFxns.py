from __future__ import division
import numpy as np
# import sys
# import os

# part 4 (below) open and clear data files
# txt = comma separated values
def Write_to_File(mydir, iDict, MainDF, disease):
    #sick, x_coords, y_coords, ages, sex, dsi, dsr, dsv, ebs, ebr, ebv, vac, rec, con
        
    file_names = ['inds_data', 'sick_data', 'x_coords_data','y_coords_data'
                  'age_data', 'sex_data', 'dsi_data', 'dsr_data', 'dsv_data',
                  'ebs_data', 'ebr_data', 'ebv_data', 'vac_data', 'rec_data',
                  '.txt', 'w+')
    OUT.close()
    
    OUT = open(mydir + 'CEMs/SimData/con_data.txt', 'w+')
    OUT.close()
    
    OUT = open(mydir + 'CEMs/SimData/Compiled_Data.txt', 'w+')
    OUT.write("model,clr,t, imm, Disease, N, sex, avg_age, inf_ded, nat_ded, Sick, dsi, ebs, Healthy, rec, dsr, ebr, vac, area, extinct\n")
    #       x, clr, t, imm, disease, Ni, sex, ages, inf_ded, nat_ded, NumSick, dsi, ebs, Healthy, rec, dsr, ebr, vac, A, extiny
    OUT.close()

def Clear_to_File(mydir,x, clr,t, imm, disease, Ni,  inds, sick, x_coords, y_coords, ages,  inf_ded, nat_ded, NumSick, sex, dsi, dsr, dsv, ebs, Healthy, ebr, ebv, vac, rec, A, con):
    OUT = open(mydir + 'CEMs/SimData/inds_data.txt', 'a+')
    outlist = str(inds).strip('[]') # in the list of inds strip all "[]" from the list then assigen it to the variable of outlist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
    OUT.write(outlist+'\n')
    #print>>OUT, outlist
    OUT.close()

    OUT = open(mydir + 'CEMs/SimData/sick_data.txt', 'a+')
    outlist = str(sick).strip('[]') # in the list of sick strip all "[]" from the list then assigen it to the variable of oulist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
    OUT.write(outlist+'\n')
    #print>>OUT, outlist
    OUT.close()


    OUT = open(mydir + 'CEMs/SimData/x_coords_data.txt', 'a+')
    outlist = str(x_coords).strip('[]') # in the list of x_coords strip all "[]" from the list then assigen it to the variable of outlist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
    OUT.write(outlist+'\n')
    #print>>OUT, outlist
    OUT.close()

    OUT = open(mydir + 'CEMs/SimData/y_coords_data.txt', 'a+')
    outlist = str(y_coords).strip('[]') # in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
    OUT.write(outlist+'\n')
    #print>>OUT, outlist
    OUT.close()
    
    OUT = open(mydir + 'CEMs/SimData/Compiled_Data.txt', 'a+')
    extinct = False
    if len(inds) == 0: extinct = True # This True/False designation will be used for accessing data when making figures
    outlist = str([x, clr, t, imm, disease, Ni, sex, np.mean(ages), inf_ded, nat_ded, NumSick, dsi, ebs, Healthy, rec, dsr, ebr, vac, A, extinct]).strip('[]')# in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
    '''         model,clr, t, imm, disease, N, sex, ages, inf_ded, nat_ded, Sick, rec, Healthy, area, extincts      '''
    outlist = outlist.replace(' ', '') # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
    outlist = outlist.replace("'", '')
    OUT.write(outlist+'\n')
    #print>>OUT, outlist
    OUT.close()

    Ni = len(inds)
    Si = len(list(set(sick)))
    NumSick = sum(sick)
    Healthy = len(sick) - sum(sick)