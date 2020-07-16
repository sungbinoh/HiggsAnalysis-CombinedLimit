import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8

now = datetime.datetime.now()
temp_dir = "Goodness_of_fit_" + binning

make_tmp_dir = "mkdir " + temp_dir
os.system(make_tmp_dir)

#hist_name = ["mZp_2AK8_SR_b_veto_DiEle", "mZp_2AK8_SR_b_veto_DiMu", 

a = 0
#f = open("../filelist_Zprime_miniaod.txt", 'r')
f = open("../script/MC_signal_injection_test_list.txt", 'r')
for line in f: # -- loop over mass points 
    if not line: break
    mass_point = line[0:-1]
    # -- check output directory
    print mass_point
       
    # -- making dir of each mass point & copy scripts
    os.system("mkdir ./" + temp_dir + "/" + mass_point)
    os.system("cp scripts/* ./" + temp_dir + "/"+ mass_point)
    os.system("cp ../DataCards/merged/shape_" + binning + "_" + mass_point + "_CRs.txt ./" + temp_dir + "/"+ mass_point)
    os.chdir("./" + temp_dir + "/"+ mass_point)
    
    # -- Edit run.sh
    file_run = open("run.sh", 'a')
    current_dir = os.getcwd()
    file_run.write("\n" + "cd " + current_dir + "\n")
    file_run.write("combine -M GoodnessOfFit shape_" + binning + "_" + mass_point + "_CRs.txt --algo=KS &> log_KS.txt\n")
    file_run.write("combine -M GoodnessOfFit shape_" + binning + "_" + mass_point + "_CRs.txt --algo=KS -t 200 -s 1 &> log_KS_toys.txt\n")
    file_run.write("combine -M GoodnessOfFit shape_" + binning + "_" + mass_point + "_CRs.txt --algo=AD &> log_AD.txt\n")
    file_run.write("combine -M GoodnessOfFit shape_" + binning + "_" + mass_point + "_CRs.txt --algo=AD -t 200 -s 1 &> log_AD_toys.txt\n")
    file_run.write("combine -M GoodnessOfFit shape_" + binning + "_" + mass_point + "_CRs.txt --algo=saturated &> log_saturated.txt\n")
    file_run.write("combine -M GoodnessOfFit shape_" + binning + "_" + mass_point + "_CRs.txt --algo=saturated --toysFreq -t 200 &> log_saturated_toys.txt")

    # -- Submit Job
    submit_job = "condor_submit -batch-name Combine_" + binning + "_Goodness_of_fit submit.jds"
    os.system(submit_job)
    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break
f.close()
