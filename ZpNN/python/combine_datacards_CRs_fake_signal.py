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
    hist_0AK8_DY_CR = "mZp_0AK8_CR_Zmass_" + channel2 + "_DYreweight"
    hist_1AK8_DY_CR = "mZp_1AK8_CR_Zmass_" + channel2 + "_DYreweight"
    hist_2AK8_DY_CR = "mZp_2AK8_CR_Zmass_" + channel2 + "_DYreweight"
    hist_0AK8_emu_SR = "mZp_0AK8_SR_EMu_DYreweight"
    hist_1AK8_emu_SR = "mZp_1AK8_SR_EMu_DYreweight"
    hist_2AK8_emu_SR = "mZp_2AK8_SR_EMu_DYreweight"

    ## -- Merge three N(AK8) bins : 0AK8, 1AK8, 2AK8
    cmd = "combineCards.py"
    cmd = cmd + " mZp_0AK8_CR_Zmass_" + channel2 + "_2018=shape_" + hist_0AK8_DY_CR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_CR_Zmass_" + channel2 + "_2018=shape_" + hist_1AK8_DY_CR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_CR_Zmass_" + channel2 + "_2018=shape_" + hist_2AK8_DY_CR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_CR_Zmass_" + channel2 + "_2017=shape_" + hist_0AK8_DY_CR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_CR_Zmass_" + channel2 + "_2017=shape_" + hist_1AK8_DY_CR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_CR_Zmass_" + channel2 + "_2017=shape_" + hist_2AK8_DY_CR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_CR_Zmass_" + channel2 + "_2016=shape_" + hist_0AK8_DY_CR + "_2016_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_CR_Zmass_" + channel2 + "_2016=shape_" + hist_1AK8_DY_CR + "_2016_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_CR_Zmass_" + channel2 + "_2016=shape_" + hist_2AK8_DY_CR + "_2016_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_SR_EMu_2018=shape_" + hist_0AK8_emu_SR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_SR_EMu_2017=shape_" + hist_0AK8_emu_SR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_SR_EMu_2016=shape_" + hist_0AK8_emu_SR + "_2016_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_SR_EMu_2018=shape_" + hist_1AK8_emu_SR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_SR_EMu_2017=shape_" + hist_1AK8_emu_SR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_SR_EMu_2016=shape_" + hist_1AK8_emu_SR + "_2016_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_SR_EMu_2018=shape_" + hist_2AK8_emu_SR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_SR_EMu_2017=shape_" + hist_2AK8_emu_SR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_SR_EMu_2016=shape_" + hist_2AK8_emu_SR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_3AK8_" + channel2 + "_CRs_fake_signal.txt"
    print cmd
    os.system(cmd)

    cmd = "combineCards.py"
    cmd = cmd + " mZp_0AK8_CR_Zmass_" + channel2 + "_2018=shape_" + hist_0AK8_DY_CR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_CR_Zmass_" + channel2 + "_2017=shape_" + hist_0AK8_DY_CR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_CR_Zmass_" + channel2 + "_2016=shape_" + hist_0AK8_DY_CR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_0AK8_CR_Zmass_" + channel2 + "_fake_signal.txt"
    print cmd
    os.system(cmd)
    
    cmd = "combineCards.py"
    cmd = cmd + " mZp_1AK8_CR_Zmass_" + channel2 + "_2018=shape_" + hist_1AK8_DY_CR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_CR_Zmass_" + channel2 + "_2017=shape_" + hist_1AK8_DY_CR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_CR_Zmass_" + channel2 + "_2016=shape_" + hist_1AK8_DY_CR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_1AK8_CR_Zmass_" + channel2 + "_fake_signal.txt"
    print cmd
    os.system(cmd)
    
    cmd = "combineCards.py"
    cmd = cmd + " mZp_2AK8_CR_Zmass_" + channel2 + "_2018=shape_" + hist_2AK8_DY_CR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_CR_Zmass_" + channel2 + "_2017=shape_" + hist_2AK8_DY_CR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_CR_Zmass_" + channel2 + "_2016=shape_" + hist_2AK8_DY_CR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_2AK8_CR_Zmass_" + channel2 + "_fake_signal.txt"
    print cmd
    os.system(cmd)

    cmd = "combineCards.py"
    cmd = cmd + " mZp_0AK8_SR_EMu_2018=shape_" + hist_0AK8_emu_SR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_SR_EMu_2017=shape_" + hist_0AK8_emu_SR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_0AK8_SR_EMu_2016=shape_" + hist_0AK8_emu_SR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_0AK8_SR_EMu_fake_signal.txt"
    print cmd
    os.system(cmd)

    cmd = "combineCards.py"
    cmd = cmd + " mZp_1AK8_SR_EMu_2018=shape_" + hist_1AK8_emu_SR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_SR_EMu_2017=shape_" + hist_1AK8_emu_SR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_1AK8_SR_EMu_2016=shape_" + hist_1AK8_emu_SR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_1AK8_SR_EMu_fake_signal.txt"
    print cmd
    os.system(cmd)
    
    cmd = "combineCards.py"
    cmd = cmd + " mZp_2AK8_SR_EMu_2018=shape_" + hist_2AK8_emu_SR + "_2018_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_SR_EMu_2017=shape_" + hist_2AK8_emu_SR + "_2017_fake_signal.txt"
    cmd = cmd + " mZp_2AK8_SR_EMu_2016=shape_" + hist_2AK8_emu_SR + "_2016_fake_signal.txt"
    cmd = cmd + " > " + datacard_dir + "merged/shape_2AK8_SR_EMu_fake_signal.txt"
    print cmd
    os.system(cmd)
    
    # -- abort for test
    a = a + 1
    #if a > 5:
    #    break;

hist_0AK8_DY_CR_DiMu = "mZp_0AK8_CR_Zmass_DiMu_DYreweight"
hist_1AK8_DY_CR_DiMu = "mZp_1AK8_CR_Zmass_DiMu_DYreweight"
hist_2AK8_DY_CR_DiMu = "mZp_2AK8_CR_Zmass_DiMu_DYreweight"
hist_0AK8_DY_CR_DiEle = "mZp_0AK8_CR_Zmass_DiEle_DYreweight"
hist_1AK8_DY_CR_DiEle = "mZp_1AK8_CR_Zmass_DiEle_DYreweight"
hist_2AK8_DY_CR_DiEle = "mZp_2AK8_CR_Zmass_DiEle_DYreweight"
hist_0AK8_emu_SR = "mZp_0AK8_SR_EMu_DYreweight"
hist_1AK8_emu_SR = "mZp_1AK8_SR_EMu_DYreweight"
hist_2AK8_emu_SR = "mZp_2AK8_SR_EMu_DYreweight"

## -- Merge three N(AK8) bins : 0AK8, 1AK8, 2AK8                                                                                                                                                                                                                            
cmd = "combineCards.py"
cmd = cmd + " mZp_0AK8_CR_Zmass_DiMu_2018=shape_" + hist_0AK8_DY_CR_DiMu + "_2018_fake_signal.txt"
cmd = cmd + " mZp_1AK8_CR_Zmass_DiMu_2018=shape_" + hist_1AK8_DY_CR_DiMu + "_2018_fake_signal.txt"
cmd = cmd + " mZp_2AK8_CR_Zmass_DiMu_2018=shape_" + hist_2AK8_DY_CR_DiMu + "_2018_fake_signal.txt"
cmd = cmd + " mZp_0AK8_CR_Zmass_DiMu_2017=shape_" + hist_0AK8_DY_CR_DiMu + "_2017_fake_signal.txt"
cmd = cmd + " mZp_1AK8_CR_Zmass_DiMu_2017=shape_" + hist_1AK8_DY_CR_DiMu + "_2017_fake_signal.txt"
cmd = cmd + " mZp_2AK8_CR_Zmass_DiMu_2017=shape_" + hist_2AK8_DY_CR_DiMu + "_2017_fake_signal.txt"
cmd = cmd + " mZp_0AK8_CR_Zmass_DiMu_2016=shape_" + hist_0AK8_DY_CR_DiMu + "_2016_fake_signal.txt"
cmd = cmd + " mZp_1AK8_CR_Zmass_DiMu_2016=shape_" + hist_1AK8_DY_CR_DiMu + "_2016_fake_signal.txt"
cmd = cmd + " mZp_2AK8_CR_Zmass_DiMu_2016=shape_" + hist_2AK8_DY_CR_DiMu + "_2016_fake_signal.txt"

cmd = cmd + " mZp_0AK8_CR_Zmass_DiEle_2018=shape_" + hist_0AK8_DY_CR_DiEle + "_2018_fake_signal.txt"
cmd = cmd + " mZp_1AK8_CR_Zmass_DiEle_2018=shape_" + hist_1AK8_DY_CR_DiEle + "_2018_fake_signal.txt"
cmd = cmd + " mZp_2AK8_CR_Zmass_DiEle_2018=shape_" + hist_2AK8_DY_CR_DiEle + "_2018_fake_signal.txt"
cmd = cmd + " mZp_0AK8_CR_Zmass_DiEle_2017=shape_" + hist_0AK8_DY_CR_DiEle + "_2017_fake_signal.txt"
cmd = cmd + " mZp_1AK8_CR_Zmass_DiEle_2017=shape_" + hist_1AK8_DY_CR_DiEle + "_2017_fake_signal.txt"
cmd = cmd + " mZp_2AK8_CR_Zmass_DiEle_2017=shape_" + hist_2AK8_DY_CR_DiEle + "_2017_fake_signal.txt"
cmd = cmd + " mZp_0AK8_CR_Zmass_DiEle_2016=shape_" + hist_0AK8_DY_CR_DiEle + "_2016_fake_signal.txt"
cmd = cmd + " mZp_1AK8_CR_Zmass_DiEle_2016=shape_" + hist_1AK8_DY_CR_DiEle + "_2016_fake_signal.txt"
cmd = cmd + " mZp_2AK8_CR_Zmass_DiEle_2016=shape_" + hist_2AK8_DY_CR_DiEle + "_2016_fake_signal.txt"
cmd = cmd + " mZp_0AK8_SR_EMu_2018=shape_" + hist_0AK8_emu_SR + "_2018_fake_signal.txt"
cmd = cmd + " mZp_0AK8_SR_EMu_2017=shape_" + hist_0AK8_emu_SR + "_2017_fake_signal.txt"
cmd = cmd + " mZp_0AK8_SR_EMu_2016=shape_" + hist_0AK8_emu_SR + "_2016_fake_signal.txt"
cmd = cmd + " mZp_1AK8_SR_EMu_2018=shape_" + hist_1AK8_emu_SR + "_2018_fake_signal.txt"
cmd = cmd + " mZp_1AK8_SR_EMu_2017=shape_" + hist_1AK8_emu_SR + "_2017_fake_signal.txt"
cmd = cmd + " mZp_1AK8_SR_EMu_2016=shape_" + hist_1AK8_emu_SR + "_2016_fake_signal.txt"
cmd = cmd + " mZp_2AK8_SR_EMu_2018=shape_" + hist_2AK8_emu_SR + "_2018_fake_signal.txt"
cmd = cmd + " mZp_2AK8_SR_EMu_2017=shape_" + hist_2AK8_emu_SR + "_2017_fake_signal.txt"
cmd = cmd + " mZp_2AK8_SR_EMu_2016=shape_" + hist_2AK8_emu_SR + "_2016_fake_signal.txt"
cmd = cmd + " > " + datacard_dir + "merged/shape_3AK8_all_CRs_fake_signal.txt"
print cmd
os.system(cmd)
