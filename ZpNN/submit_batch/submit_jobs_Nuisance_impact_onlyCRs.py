import os
import sys
import commands
import datetime
import subprocess
import time

#year = sys.argv[1]
#binning = sys.argv[1] # -- Inclusive, 3AK8, 4AK8

now = datetime.datetime.now()
temp_dir = "Nuisanse_impact_onlyCRs"

make_tmp_dir = "mkdir " + temp_dir
os.system(make_tmp_dir)

channels = ["DiEle", "DiMu"]

a = 0

for channel in channels:
    # -- making dir of each mass point & copy scripts
    os.system("mkdir ./" + temp_dir + "/" + channel)
    os.system("cp scripts/* ./" + temp_dir + "/"+ channel)
    os.system("cp ../DataCards/merged/shape_3AK8_" + channel + "_CRs.txt ./" + temp_dir + "/"+ channel)
    os.chdir("./" + temp_dir + "/"+ channel)
    
    # -- Edit run.sh
    file_run = open("run.sh", 'a')
    current_dir = os.getcwd()
    file_run.write("\n" + "cd " + current_dir + "\n")
    file_run.write("text2workspace.py shape_3AK8_" + channel + "_CRs.txt -m 125 --X-allow-no-signal\n")
    file_run.write("combineTool.py -M Impacts -d shape_3AK8_" + channel + "_CRs.root -m 125 --doInitialFit --robustFit 1 -t -1 --expectSignal 1 --rMin -20\n")
    file_run.write("combineTool.py -M Impacts -d shape_3AK8_" + channel + "_CRs.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal 1 --rMin -20\n")
    file_run.write("combineTool.py -M Impacts -d shape_3AK8_" + channel + "_CRs.root -m 125 -o impacts.json\n")
    file_run.write("plotImpacts.py -i impacts.json -o impacts\n")
    file_run.write("mv impacts.pdf /data6/Users/suoh/Limit/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/ZpNN/output/Nuisance_Impact/3AK8_" + channel + "_CRs.pdf")
    
    # -- Submit Job
    submit_job = "condor_submit -batch-name Combine_3AK8_onlyCRs_Nuisanse_impact submit.jds"
    os.system(submit_job)
    os.chdir("../../")
    #abort for test
    a = a + 1
    #if a > 5:
    #    break

