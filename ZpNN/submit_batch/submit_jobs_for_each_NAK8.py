import os
import sys
import commands
import datetime
import subprocess
import time

AK8s = ["0AK8", "1AK8", "2AK8"]
now = datetime.datetime.now()

for AK8 in AK8s:
    make_tmp_dir = "mkdir " + AK8
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
    
    for AK8 in AK8s:
        os.system("mkdir ./" + AK8 + "/" + mass_point)
        os.system("cp scripts/* ./" + AK8 + "/"+ mass_point)
        os.system("cp ../DataCards/merged/" + AK8 + "/shape_" + AK8 + "_" + mass_point + ".txt ./" + AK8 + "/"+ mass_point)
        os.chdir("./" + AK8 + "/"+ mass_point)
    
        # -- Edit run.sh
        file_run = open("run.sh", 'a')
        current_dir = os.getcwd()
        file_run.write("\n" + "cd " + current_dir + "\n")
        file_run.write("combine -M AsymptoticLimits shape_" + AK8 + "_" + mass_point + ".txt &> log.txt")
        
        # -- Submit Job
        submit_job = "condor_submit -batch-name Combine_" + AK8 + " submit.jds"
        os.system(submit_job)
        os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break


f.close()
