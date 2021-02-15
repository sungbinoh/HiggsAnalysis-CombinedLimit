import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Injected events : 0, 1, 3, 6

now = datetime.datetime.now()
temp_dir = "Signal_injection_" + binning + "_evts"

make_tmp_dir = "mkdir " + temp_dir
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
    
    if "EE" in mass_point:
        continue
    
    # -- making dir of each mass point & copy scripts
    os.system("mkdir ./" + temp_dir + "/" + mass_point)
    os.system("cp scripts/* ./" + temp_dir + "/"+ mass_point)
    copy_datacard = "cp ../DataCards/Signal_injection/shape_mZp_2AK8_SR_DiMu_DYreweight_" + mass_point + "_" + binning + "_injected.txt ./" + temp_dir + "/"+ mass_point
    if binning == "-1":
        copy_datacard = "cp ../DataCards/Signal_injection/shape_mZp_2AK8_SR_DiMu_DYreweight_" + mass_point + ".txt ./" + temp_dir + "/"+ mass_point
    os.system(copy_datacard)
    os.chdir("./" + temp_dir + "/"+ mass_point)
    
    # -- Edit run.sh
    file_run = open("run.sh", 'a')
    current_dir = os.getcwd()
    file_run.write("\n" + "cd " + current_dir + "\n")
    cmd_run = "combine -M AsymptoticLimits shape_mZp_2AK8_SR_DiMu_DYreweight_" + mass_point +  "_" + binning + "_injected.txt &> log.txt"
    if binning == "-1":
        cmd_run = "combine -M AsymptoticLimits shape_mZp_2AK8_SR_DiMu_DYreweight_" + mass_point + ".txt &> log.txt"
    file_run.write(cmd_run)
    
    # -- Submit Job
    submit_job = "condor_submit -batch-name Signal_injection_" + binning + " submit.jds"
    os.system(submit_job)
    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break
f.close()
