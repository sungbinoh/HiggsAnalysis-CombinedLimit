import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8
years = ["2016", "2017", "2018"]
now = datetime.datetime.now()
temp_dir = binning

for year in years:
    make_tmp_dir = "mkdir " + temp_dir + "_" + year
    os.system(make_tmp_dir)


#hist_name = ["mZp_2AK8_SR_b_veto_DiEle", "mZp_2AK8_SR_b_veto_DiMu", 

a = 0
#f = open("../filelist_Zprime_miniaod.txt", 'r')
f = open("../script/MC_signal_2016.txt", 'r')
for line in f: # -- loop over mass points 
    if not line: break
    mass_point = line[0:-1]
    # -- check output directory
    print mass_point
    
    for year in years:
        os.system("mkdir ./" + temp_dir + "_" + year + "/" + mass_point)
        os.system("cp scripts/* ./" + temp_dir + "_" + year + "/"+ mass_point)
        os.system("cp ../DataCards/merged/" + year + "/shape_" + binning + "_" + mass_point + "_" + year + ".txt ./" + temp_dir + "_" + year + "/"+ mass_point)
        os.chdir("./" + temp_dir + "_" + year + "/"+ mass_point)
    
        # -- Edit run.sh
        file_run = open("run.sh", 'a')
        current_dir = os.getcwd()
        file_run.write("\n" + "cd " + current_dir + "\n")
        file_run.write("combine -M AsymptoticLimits shape_" + binning + "_" + mass_point + "_" + year + ".txt &> log.txt")
        
        # -- Submit Job
        submit_job = "condor_submit -batch-name Combine_" + binning + "_" + year + " submit.jds"
        os.system(submit_job)
        os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break


f.close()
