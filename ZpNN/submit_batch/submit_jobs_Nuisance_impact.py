import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8

now = datetime.datetime.now()
temp_dir = "Nuisanse_impact_" + binning + "_SR"

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
    file_run.write("text2workspace.py shape_" + binning + "_" + mass_point + ".txt -m 125\n")
    file_run.write("combineTool.py -M Impacts -d shape_" + binning + "_" + mass_point + ".root -m 125 --doInitialFit --robustFit 1 -t -1 --expectSignal 1 --rMin -20\n")
    file_run.write("combineTool.py -M Impacts -d shape_" + binning + "_" + mass_point + ".root -m 125 --robustFit 1 --doFits -t -1 --expectSignal 1 --rMin -20\n")
    file_run.write("combineTool.py -M Impacts -d shape_" + binning + "_" + mass_point + ".root -m 125 -o impacts.json\n")
    file_run.write("plotImpacts.py -i impacts.json -o impacts\n")
    file_run.write("mv impacts.pdf /data6/Users/suoh/Limit/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/ZpNN/output/Nuisance_Impact/" + binning + "_" + mass_point + ".pdf")
    
    # -- Submit Job
    submit_job = "condor_submit -batch-name Combine_" + binning + "_Nuisanse_impact submit.jds"
    os.system(submit_job)
    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break
f.close()
