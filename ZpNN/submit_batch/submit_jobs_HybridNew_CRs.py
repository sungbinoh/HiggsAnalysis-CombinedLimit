import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8

now = datetime.datetime.now()
temp_dir = "HybridNew_" + binning

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
    
    # -- copy run.sh for each job
    os.system("cp run.sh run_2sig_down.sh")
    os.system("cp run.sh run_1sig_down.sh")
    os.system("cp run.sh run_central.sh")
    os.system("cp run.sh run_1sig_up.sh")
    os.system("cp run.sh run_2sig_up.sh")

    # -- Edit run.sh files
    file_run_2sig_down = open("run_2sig_down.sh", 'a')
    file_run_1sig_down = open("run_1sig_down.sh", 'a')
    file_run_central = open("run_central.sh", 'a')
    file_run_1sig_up = open("run_1sig_up.sh", 'a')
    file_run_2sig_up = open("run_2sig_up.sh", 'a')

    current_dir = os.getcwd()
    
    file_run_2sig_down.write("\n" + "cd " + current_dir + "\n")
    file_run_1sig_down.write("\n" + "cd " + current_dir + "\n")
    file_run_central.write("\n" + "cd " + current_dir + "\n")
    file_run_1sig_up.write("\n" + "cd " + current_dir + "\n")
    file_run_2sig_up.write("\n" + "cd " + current_dir + "\n")
    
    # -- 0.025 0.16 0.5 0.84 0.975
    file_run_2sig_down.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + "_CRs.txt --expectedFromGrid 0.025 -T 100 &> log_2sig_down.txt\n")
    file_run_1sig_down.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + "_CRs.txt --expectedFromGrid 0.16 -T 100 &> log_1sig_down.txt\n")
    file_run_central.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + "_CRs.txt --expectedFromGrid 0.5 -T 100 &> log_central.txt\n")
    file_run_1sig_up.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + "_CRs.txt --expectedFromGrid 0.84 -T 100 &> log_1sig_up.txt\n")
    file_run_2sig_up.write("combine -M HybridNew --LHCmode LHC-limits shape_" + binning + "_" + mass_point + "_CRs.txt --expectedFromGrid 0.975 -T 100 &> log_2sig_up.txt\n")

    file_run_2sig_down.close()
    file_run_1sig_down.close()
    file_run_central.close()
    file_run_1sig_up.close()
    file_run_2sig_up.close()

    # -- Edit submit.jds
    file_submit = open("submit_no_exe.jds", 'a')
    file_submit.write("\n"+"request_memory = 20000\n")
    file_submit.close()
    
    # -- copy submit.jds
    os.system("cp submit_no_exe.jds submit_2sig_down.jds")
    os.system("cp submit_no_exe.jds submit_1sig_down.jds")
    os.system("cp submit_no_exe.jds submit_central.jds")
    os.system("cp submit_no_exe.jds submit_1sig_up.jds")
    os.system("cp submit_no_exe.jds submit_2sig_up.jds")
    
    # -- Edit jds files
    file_jds_2sig_down = open("submit_2sig_down.jds", 'a')
    file_jds_1sig_down = open("submit_1sig_down.jds", 'a')
    file_jds_central = open("submit_central.jds", 'a')
    file_jds_1sig_up = open("submit_1sig_up.jds", 'a')
    file_jds_2sig_up = open("submit_2sig_up.jds", 'a')
    
    file_jds_2sig_down.write("\n" + "executable = run_2sig_down.sh\n")
    file_jds_1sig_down.write("\n" + "executable = run_1sig_down.sh\n")
    file_jds_central.write("\n" + "executable = run_central.sh\n")
    file_jds_1sig_up.write("\n" + "executable = run_1sig_up.sh\n")
    file_jds_2sig_up.write("\n" + "executable = run_2sig_up.sh\n")
    
    file_jds_2sig_down.write("log = condor_2sig_down.log\n")
    file_jds_1sig_down.write("log = condor_1sig_down.log\n")
    file_jds_central.write("log = condor_central.log\n")
    file_jds_1sig_up.write("log = condor_1sig_up.log\n")
    file_jds_2sig_up.write("log = condor_2sig_up.log\n")
    
    file_jds_2sig_down.write("output = job_2sig_down.log\n" + "error = job_2sig_down.err\n")
    file_jds_1sig_down.write("output = job_1sig_down.log\n" + "error = job_1sig_down.err\n")
    file_jds_central.write("output = job_central.log\n" + "error = job_central.err\n")
    file_jds_1sig_up.write("output = job_1sig_up.log\n" + "error = job_1sig_up.err\n")
    file_jds_2sig_up.write("output = job_2sig_up.log\n" + "error = job_2sig_up.err\n")
    
    file_jds_2sig_down.write("\n" + "queue 1")
    file_jds_1sig_down.write("\n" + "queue 1")
    file_jds_central.write("\n" + "queue 1")
    file_jds_1sig_up.write("\n" + "queue 1")
    file_jds_2sig_up.write("\n" + "queue 1")

    file_jds_2sig_down.close()
    file_jds_1sig_down.close()
    file_jds_central.close()
    file_jds_1sig_up.close()
    file_jds_2sig_up.close()


    # -- Submit Job
    submit_job_2sig_down = "condor_submit -batch-name Combine_" + binning + "_HybridNew submit_2sig_down.jds"
    submit_job_1sig_down = "condor_submit -batch-name Combine_" + binning + "_HybridNew submit_1sig_down.jds"
    submit_job_central = "condor_submit -batch-name Combine_" + binning + "_HybridNew submit_central.jds"
    submit_job_1sig_up = "condor_submit -batch-name Combine_" + binning + "_HybridNew submit_1sig_up.jds"
    submit_job_2sig_up = "condor_submit -batch-name Combine_" + binning + "_HybridNew submit_2sig_up.jds"
    
    os.system(submit_job_2sig_down)
    os.system(submit_job_1sig_down)
    os.system(submit_job_central)
    os.system(submit_job_1sig_up)
    os.system(submit_job_2sig_up)

    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break
f.close()
