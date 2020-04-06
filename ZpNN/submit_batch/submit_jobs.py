import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
histname = sys.argv[1]

now = datetime.datetime.now()
temp_dir = histname + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute)

make_tmp_dir = "mkdir " + temp_dir
os.system(make_tmp_dir)

#hist_name = ["mZp_2AK8_SR_b_veto_DiEle", "mZp_2AK8_SR_b_veto_DiMu", 

a = 0
#f = open("../filelist_Zprime_miniaod.txt", 'r')
f = open("../script/MC_signal_" + year + ".txt", 'r')
for line in f: # -- loop over mass points 
    if not line: break
    mass_point = line[0:-1]
    # -- check output directory
    print mass_point
       
    # -- making dir of each mass point & copy scripts
    os.system("mkdir ./" + temp_dir + "/" + mass_point)
    os.system("cp scripts/* ./" + temp_dir + "/"+ mass_point)
    os.system("cp ../DataCards/" + year + "/shape_" + mass_point + ".txt ./" + temp_dir + "/"+ mass_point)
    os.chdir("./" + temp_dir + "/"+ mass_point)
    
    # -- Edit run.sh
    file_run = open("run.sh", 'a')
    current_dir = os.getcwd()
    file_run.write("\n" + "cd " + current_dir + "\n")
    file_run.write("combine -M AsymptoticLimits shape_" + mass_point + ".txt &> log.txt")
    
    # -- Submit Job
    submit_job = "condor_submit -batch-name Combine_" + mass_point + " submit.jds"
    os.system(submit_job)
    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break
f.close()
