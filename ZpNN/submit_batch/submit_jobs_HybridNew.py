import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8

now = datetime.datetime.now()
temp_dir = "HybridNew_" + binning + "_SR"

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
    os.system("cp ../DataCards/merged/shape_" + binning + "_" + mass_point + ".txt ./" + temp_dir + "/"+ mass_point)
    os.chdir("./" + temp_dir + "/"+ mass_point)
    
    # -- Edit run.sh
    file_run = open("run.sh", 'a')
    current_dir = os.getcwd()
    file_run.write("\n" + "cd " + current_dir + "\n")
    # -- 0.025 0.16 0.5 0.84 0.975
    file_run.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + ".txt --expectedFromGrid 0.025 -T 500 &> log_2sig_down.txt\n")
    file_run.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + ".txt --expectedFromGrid 0.16 -T 500 &> log_1sig_down.txt\n")
    file_run.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + ".txt --expectedFromGrid 0.5 -T 500 &> log_central.txt\n")
    file_run.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + ".txt --expectedFromGrid 0.84 -T 500 &> log_1sig_up.txt\n")
    file_run.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + ".txt --expectedFromGrid 0.975 -T 500 &> log_2sig_up.txt\n")

    # -- Submit Job
    submit_job = "condor_submit -batch-name Combine_" + binning + "_HybridNew submit.jds"
    os.system(submit_job)
    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break
f.close()
