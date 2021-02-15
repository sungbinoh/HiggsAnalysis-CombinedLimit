import os
import sys
import commands
import subprocess
import time
import operator

binning = sys.argv[1]
#year = sys.argv[1]
#temp_dir = sys.argv[2]
current_dir="/data6/Users/suoh/Limit/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/ZpNN/"
a = 0

dict_limit = dict()
dict_limit["MuMu"] = dict()
dict_limit["EE"] = dict()

temp_dir = "/submit_batch/" + binning + "/"

f = open("./script/MC_signal_injection_test_list.txt", 'r')
for line in f: # -- loop over mass points 
    if not line: break
    mass_point = line[0:-1]
    #print mass_point
    mZp = mass_point.split("_")[2][2:]
    mN = mass_point.split("_")[3][1:]
   
    # -- Get limit values
    os.chdir(current_dir + temp_dir + mass_point)
    
    channel = ""
    if "MuMu" in mass_point:
        channel = "MuMu"
    if "EE" in mass_point:
        channel = "EE"
    
        
    log_central = open("./log_central.txt").readlines()
    log_2sig_down = open("./log_2sig_down.txt").readlines()
    log_1sig_down = open("./log_1sig_down.txt").readlines()
    log_2sig_up = open("./log_2sig_up.txt").readlines()
    log_1sig_up = open("./log_1sig_up.txt").readlines()

    limit_2sig_down = "empty"
    limit_1sig_down = "empty"
    limit_central = "empty"
    limit_1sig_up = "empty"
    limit_2sig_up = "empty"

    
    
    for l in log_central:
        l = l[0:-1]
        if "Limit: r < " in l:
            limit_central = l.replace("Limit: r < ","")
            #words = l.split()
            #limit_central = words[3]
            
    for l in log_2sig_down:
        l = l[0:-1]
        if "Limit: r < " in l:
          words = l.split()
          limit_2sig_down = words[3]

    for l in log_1sig_down:
        l = l[0:-1]
        if "Limit: r < " in l:
          words = l.split()
          limit_1sig_down = words[3]

    for l in log_2sig_up:
        l = l[0:-1]
        if "Limit: r < " in l:
          words = l.split()
          limit_2sig_up = words[3]

    for l in log_1sig_up:
        l = l[0:-1]
        if "Limit: r < " in l:
          words = l.split()
          limit_1sig_up = words[3]
    
    out_line = mZp + "\t" + mN + "\t" + limit_2sig_down + "\t" + limit_1sig_down + "\t" + limit_central + "\t" + limit_1sig_up + "\t" + limit_2sig_up
    #out_line =  channel + "\t" + mZp + "\t" + mN + "\t" + limit_central
    print out_line
f.close()
