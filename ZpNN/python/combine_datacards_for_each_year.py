import os
import sys
import commands
import subprocess
import operator

a = 0
f = open("./script/MC_signal_2016.txt", 'r')
current_dir = "/data6/Users/suoh/Limit/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/ZpNN/"
datacard_dir = current_dir + "DataCards/"
os.chdir(datacard_dir)
for line in f: # -- loop over mass points
    if not line: break
    mass_point = line[0:-1]
    os.system("pwd")
    mZp = mass_point.split("_")[2][2:]
    mN = mass_point.split("_")[3][1:]
    channel1 = ""
    channel2 = ""
    if "MuMu" in mass_point:
        channel1 = "MuMu"
        channel2 = "DiMu"
    if "EE" in mass_point:
        channel1 = "EE"
        channel2 = "DiEle"
    
    ## -- Merge inclusive Signal Region for three years : mZp_SR_DiMu, mZp_SR_DiEle
    current_histname = "mZp_SR_" + channel2 + "_DYreweight"
    years = ["2016", "2017", "2018"]
    
    hist_0AK8 = "mZp_0AK8_SR_" + channel2 + "_DYreweight"
    hist_1AK8 = "mZp_1AK8_SR_" + channel2 + "_DYreweight"
    hist_2AK8 = "mZp_2AK8_SR_" + channel2 + "_DYreweight"
    
    for year in years:
         cmd = "combineCards.py mZp_0AK8_" + year + "=shape_" + hist_0AK8 + "_" + mass_point + "_" + year + ".txt"
         cmd = cmd + " mZp_1AK8_" + year + "=shape_" + hist_1AK8 + "_" + mass_point + "_" + year + ".txt"
         cmd = cmd + " mZp_2AK8_" + year + "=shape_" + hist_2AK8 + "_" + mass_point + "_" + year + ".txt"
         cmd = cmd + " > " + datacard_dir + "merged/" + year + "/shape_3AK8_" + mass_point + "_" + year + ".txt"
         print cmd
         os.system(cmd)
         
    # -- abort for test
    a = a + 1
    #if a > 5:
    #    break;
