import os
import sys
import commands
import subprocess
import operator

a = 0
current_dir = "/data6/Users/suoh/Limit/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/ZpNN/"
datacard_dir = current_dir + "DataCards/"
os.chdir(datacard_dir)

channels = ["DiMu", "DiEle"]
    
for channel2 in channels:
    hist_0AK8 = "mZp_0AK8_SR_" + channel2 + "_DYreweight"
    hist_1AK8 = "mZp_1AK8_SR_" + channel2 + "_DYreweight"
    hist_2AK8 = "mZp_2AK8_SR_" + channel2 + "_DYreweight"
    hist_0AK8_DY_CR = "mZp_0AK8_CR_Zmass_" + channel2 + "_DYreweight"
    hist_1AK8_DY_CR = "mZp_1AK8_CR_Zmass_" + channel2 + "_DYreweight"
    hist_2AK8_DY_CR = "mZp_2AK8_CR_Zmass_" + channel2 + "_DYreweight"
    hist_0AK8_emu_SR = "mZp_0AK8_SR_EMu_DYreweight"
    hist_1AK8_emu_SR = "mZp_1AK8_SR_EMu_DYreweight"
    hist_2AK8_emu_SR = "mZp_2AK8_SR_EMu_DYreweight"

    ## -- Merge three N(AK8) bins : 0AK8, 1AK8, 2AK8
    cmd = "combineCards.py"
    cmd = cmd + " mZp_0AK8_DY_CR_2018=shape_" + hist_0AK8_DY_CR + "_2018.txt"
    cmd = cmd + " mZp_1AK8_DY_CR_2018=shape_" + hist_1AK8_DY_CR + "_2018.txt"
    cmd = cmd + " mZp_2AK8_DY_CR_2018=shape_" + hist_2AK8_DY_CR + "_2018.txt"
    cmd = cmd + " mZp_0AK8_DY_CR_2017=shape_" + hist_0AK8_DY_CR + "_2017.txt"
    cmd = cmd + " mZp_1AK8_DY_CR_2017=shape_" + hist_1AK8_DY_CR + "_2017.txt"
    cmd = cmd + " mZp_2AK8_DY_CR_2017=shape_" + hist_2AK8_DY_CR + "_2017.txt"
    cmd = cmd + " mZp_0AK8_DY_CR_2016=shape_" + hist_0AK8_DY_CR + "_2016.txt"
    cmd = cmd + " mZp_1AK8_DY_CR_2016=shape_" + hist_1AK8_DY_CR + "_2016.txt"
    cmd = cmd + " mZp_2AK8_DY_CR_2016=shape_" + hist_2AK8_DY_CR + "_2016.txt"
    cmd = cmd + " mZp_0AK8_emu_SR_2018=shape_" + hist_0AK8_emu_SR + "_2018.txt"
    cmd = cmd + " mZp_0AK8_emu_SR_2017=shape_" + hist_0AK8_emu_SR + "_2017.txt"
    cmd = cmd + " mZp_0AK8_emu_SR_2016=shape_" + hist_0AK8_emu_SR + "_2016.txt"
    cmd = cmd + " mZp_1AK8_emu_SR_2018=shape_" + hist_1AK8_emu_SR + "_2018.txt"
    cmd = cmd + " mZp_1AK8_emu_SR_2017=shape_" + hist_1AK8_emu_SR + "_2017.txt"
    cmd = cmd + " mZp_1AK8_emu_SR_2016=shape_" + hist_1AK8_emu_SR + "_2016.txt"
    cmd = cmd + " mZp_2AK8_emu_SR_2018=shape_" + hist_2AK8_emu_SR + "_2018.txt"
    cmd = cmd + " mZp_2AK8_emu_SR_2017=shape_" + hist_2AK8_emu_SR + "_2017.txt"
    cmd = cmd + " mZp_2AK8_emu_SR_2016=shape_" + hist_2AK8_emu_SR + "_2016.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_3AK8_" + channel2 + "_CRs.txt"
    print cmd
    os.system(cmd)
    
    # -- abort for test
    a = a + 1
    #if a > 5:
    #    break;
