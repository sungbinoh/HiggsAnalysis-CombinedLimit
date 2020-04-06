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

f = open("./script/MC_signal_2016.txt", 'r')
for line in f: # -- loop over mass points
    if not line: break
    mass_point = line[0:-1]
    mZp = mass_point.split("_")[2][2:]
    mN = mass_point.split("_")[3][1:]
    channel = ""
    if "MuMu" in mass_point:
        channel = "MuMu"
    if "EE" in mass_point:
        channel = "EE"
    
    # -- Declare dict 
    dict_limit[channel][int(mZp)] = dict()

    
f = open("./script/MC_signal_2016.txt", 'r')
for line in f: # -- loop over mass points 
    if not line: break
    mass_point = line[0:-1]
    #print mass_point
    mZp = mass_point.split("_")[2][2:]
    mN = mass_point.split("_")[3][1:]
   
    # -- Get limit values
    os.chdir("./" + temp_dir + "/"+ mass_point)
    
    channel = ""
    if "MuMu" in mass_point:
        channel = "MuMu"
    if "EE" in mass_point:
        channel = "EE"
    logs = open("./log.txt").readlines()
    
    limit_2sig_down = "empty"
    limit_1sig_down = "empty"
    limit_central = "empty"
    limit_1sig_up = "empty"
    limit_2sig_up = "empty"
    
    for l in logs:
        l = l[0:-1]
        
        if "Expected  2.5%: r < " in l:
            limit_2sig_down = l.replace("Expected  2.5%: r < ","")
        if "Expected 16.0%: r < " in l:
            limit_1sig_down = l.replace("Expected 16.0%: r < ","")
        if "Expected 50.0%: r < " in l:
            limit_central = l.replace("Expected 50.0%: r < ","")
        if "Expected 84.0%: r < " in l:
            limit_1sig_up = l.replace("Expected 84.0%: r < ","")
        if "Expected 97.5%: r < " in l:
            limit_2sig_up = l.replace("Expected 97.5%: r < ","")
        

        # Limit: r < 0.326386 +/- 0.0363156 @ 95% CL
        #if "Limit: r < " in l:
        #  words = l.split()
        #  limit_central = words[3]
    
    if "empty" in limit_2sig_down :
        os.chdir(current_dir)
        continue
    print mZp + ", " + mN + " : " + limit_2sig_down + ", " + limit_1sig_down + ", " + limit_central + ", " + limit_1sig_up + ", " + limit_2sig_up
    dict_limit[channel][int(mZp)][int(mN)] = [float(limit_2sig_down), float(limit_1sig_down), float(limit_central), float(limit_1sig_up), float(limit_2sig_up)]

    os.chdir(current_dir)
          
    #abort for test
    a = a + 1
    #if a > 5:
    #    break

sort_dict_limit = sorted(dict_limit.items(), key=operator.itemgetter(0))

for i in dict_limit.keys():
    for j in dict_limit[i].keys():
        for k in dict_limit[i][j].keys():
            #if("MuMu") in i:
                current_value = dict_limit[i][j][k]
                #print i + "\t" + j + "\t" + k + "\t" + current_value

sort_dict_limit_EE = sort_dict_limit[0]
sort_dict_limit_MuMu = sort_dict_limit[1]

def Channel(t):
    return t[0]
 
def mZp(t):
    return t[1][0]

def mN(t):
    return t[1][1][0]

sort_sort_dict_limit_EE = sorted(sort_dict_limit_EE[1].items(), key=operator.itemgetter(0))
sort_sort_dict_limit_MuMu = sorted(sort_dict_limit_MuMu[1].items(), key=operator.itemgetter(0))

f_output_EE = open("./output/Result_" + binning + "_EE.txt", 'w')
for i in sort_sort_dict_limit_EE:
    current_list = sorted(i[1].items(), key=operator.itemgetter(0))
    for j in current_list:
        f_output_EE.write( str(i[0]) + "\t" + str(j[0]) + "\t" + str(j[1][0]) + "\t" + str(j[1][1]) + "\t" + str(j[1][2])+ "\t" + str(j[1][3]) + "\t" + str(j[1][4]) + "\n" )

f_output_EE.close()

f_output_MuMu = open("./output/Result_" + binning + "_MuMu.txt", 'w')
for i in sort_sort_dict_limit_MuMu:
    current_list = sorted(i[1].items(), key=operator.itemgetter(0))
    for j in current_list:
        f_output_MuMu.write( str(i[0]) + "\t" + str(j[0]) + "\t" + str(j[1][0]) + "\t" + str(j[1][1]) + "\t" + str(j[1][2])+ "\t" + str(j[1][3]) + "\t" + str(j[1][4]) + "\n" )

f_output_MuMu.close()

f.close()
