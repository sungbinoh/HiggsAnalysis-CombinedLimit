import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8

now = datetime.datetime.now()
temp_dir = binning + "_fit_b"

make_tmp_dir = "mkdir " + temp_dir
os.system(make_tmp_dir)

#hist_name = ["mZp_2AK8_SR_b_veto_DiEle", "mZp_2AK8_SR_b_veto_DiMu", 
channels = ["DiMu", "DiEle"]

a = 0
# -- making dir of each mass point & copy scripts
for channel in channels:
    os.system("mkdir ./" + temp_dir + "/" + channel)
    os.system("cp scripts/* ./" + temp_dir + "/" + channel)
    os.system("cp ../DataCards/merged/shape_3AK8_" + channel + "_CRs_fake_signal.txt ./" + temp_dir + "/" + channel)
    os.system("cp ../DataCards/merged/*CR_Zmass*" + channel + "*fake_signal.txt ./" + temp_dir + "/" + channel)
    os.system("cp ../DataCards/merged/*SR_EMu" + "*_fake_signal.txt ./" + temp_dir + "/" + channel)
    os.chdir("./" + temp_dir + "/" + channel)
    
    # -- Edit run.sh
    file_run = open("run.sh", 'a')
    current_dir = os.getcwd()
    file_run.write("\n" + "cd " + current_dir + "\n")
    file_run.write("text2workspace.py shape_3AK8_" + channel + "_CRs_fake_signal.txt\n")
    file_run.write("combine -M FitDiagnostics -d shape_3AK8_" + channel + "_CRs_fake_signal.root -n _fit_result --saveShapes --saveWithUncertainties\n")
    file_run.write("cp fitDiagnostics_fit_result.root /data6/Users/suoh/HN_pair_analysis/rootfiles/fitDiagnostics/fitDiagnostics_fit_result_" + channel + ".root\n")
    file_run.write("text2workspace.py shape_0AK8_CR_Zmass_" + channel + "_fake_signal.txt\n")
    file_run.write("text2workspace.py shape_1AK8_CR_Zmass_" + channel +"_fake_signal.txt\n")
    file_run.write("text2workspace.py shape_2AK8_CR_Zmass_" + channel +"_fake_signal.txt\n")
    file_run.write("text2workspace.py shape_0AK8_SR_EMu_fake_signal.txt\n")
    file_run.write("text2workspace.py shape_1AK8_SR_EMu_fake_signal.txt\n")
    file_run.write("text2workspace.py shape_2AK8_SR_EMu_fake_signal.txt\n")
    file_run.write("PostFitShapesFromWorkspace -w shape_0AK8_CR_Zmass_" + channel + "_fake_signal.root -o output_mZp_0AK8_CR_Zmass_" + channel + "_fake_signal.root --postfit --sampling -f fitDiagnostics_fit_result.root:fit_b --total-shapes\n")
    file_run.write("PostFitShapesFromWorkspace -w shape_1AK8_CR_Zmass_" + channel + "_fake_signal.root -o output_mZp_1AK8_CR_Zmass_" + channel + "_fake_signal.root --postfit --sampling -f fitDiagnostics_fit_result.root:fit_b --total-shapes\n")
    file_run.write("PostFitShapesFromWorkspace -w shape_2AK8_CR_Zmass_" + channel + "_fake_signal.root -o output_mZp_2AK8_CR_Zmass_" + channel + "_fake_signal.root --postfit --sampling -f fitDiagnostics_fit_result.root:fit_b --total-shapes\n")
    file_run.write("PostFitShapesFromWorkspace -w shape_0AK8_SR_EMu_fake_signal.root -o output_mZp_0AK8_SR_EMu_fake_signal.root --postfit --sampling -f fitDiagnostics_fit_result.root:fit_b --total-shapes\n")
    file_run.write("PostFitShapesFromWorkspace -w shape_1AK8_SR_EMu_fake_signal.root -o output_mZp_1AK8_SR_EMu_fake_signal.root --postfit --sampling -f fitDiagnostics_fit_result.root:fit_b --total-shapes\n")
    file_run.write("PostFitShapesFromWorkspace -w shape_2AK8_SR_EMu_fake_signal.root -o output_mZp_2AK8_SR_EMu_fake_signal.root --postfit --sampling -f fitDiagnostics_fit_result.root:fit_b --total-shapes\n")

    
    # -- Submit Job
    submit_job = "condor_submit -batch-name fit_b_" + binning + " submit.jds"
    os.system(submit_job)
    os.chdir("../../")


