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

temp_dir = "/submit_batch/Goodness_of_fit_" + binning + "/"

f = open("./script/MC_signal_injection_test_list.txt", 'r')
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


f = open("./script/MC_signal_injection_test_list.txt", 'r')
for line in f: # -- loop over mass points 
    if not line: break
    mass_point = line[0:-1]
    
    ## -- Go to Directory of a mass point
    mZp = mass_point.split("_")[2][2:]
    mN = mass_point.split("_")[3][1:]
    os.chdir("./" + temp_dir + "/"+ mass_point)
    
    channel = ""
    if "MuMu" in mass_point:
        channel = "MuMu"
    if "EE" in mass_point:
        channel = "EE"
    
    print mass_point
    denom = 500 ## -- 500 toys for each test
    ## -- Read KS test logs and collect results into a list
    result_KS = "empty"
    log_KS = open("./log_KS.txt").readlines()
    for l in log_KS:
        if "Kolmogorov-Smirnov test statistic: " in l:
            result_KS = l.replace("Kolmogorov-Smirnov test statistic: ", "")

    list_result_KS = [float(result_KS)]
    log_KS_toys = open("./log_KS_toys.txt").readlines()
    for l in log_KS_toys:
        if "Kolmogorov-Smirnov test statistic: " in l:
            current_toy_result = l.replace("Kolmogorov-Smirnov test statistic: ", "")
            list_result_KS.append(float(current_toy_result))

    #print list_result_KS
        
    numer_KS = 0
    for i in range(1, len(list_result_KS)):
        current_result = list_result_KS[i]
        if float(result_KS) < current_result:
            numer_KS = numer_KS + 1
    p_value_KS = float(numer_KS) / denom
    print "p_value_KS : " + str(p_value_KS) + ", numer_KS = " + str(numer_KS)
            

    ## -- Read AD test logs and collect results into a list
    result_AD = "empty"
    log_AD = open("./log_AD.txt").readlines()
    for l in log_AD:
        if "Anderson-Darling test statistic: " in l:
            result_AD = l.replace("Anderson-Darling test statistic: ", "")

    list_result_AD = [float(result_AD)]
    log_AD_toys = open("./log_AD_toys.txt").readlines()
    for l in log_AD_toys:
        if "Anderson-Darling test statistic: " in l:
            current_toy_result = l.replace("Anderson-Darling test statistic: ", "")
            list_result_AD.append(float(current_toy_result))

    numer_AD = 0
    for i in range(1, len(list_result_AD)):
        current_result = list_result_AD[i]
        if float(result_AD) < current_result:
            numer_AD = numer_AD + 1
        
    p_value_AD = float(numer_AD) / denom
    print "p_value_AD : " + str(p_value_AD) + ", numer_AD = " + str(numer_AD)

    ## -- Read Saturated Model test logs and collect results into a list 
    result_saturated = "empty"
    log_saturated = open("./log_saturated.txt").readlines()
    for l in log_saturated:
        if "Best fit test statistic: " in l:
            result_saturated = l.replace("Best fit test statistic: ", "")

    list_result_saturated = [float(result_saturated)]

    log_saturated_toys = open("./log_saturated_toys.txt").readlines()
    for l in log_saturated_toys:
        if "Best fit test statistic: " in l:
            current_toy_result = l.replace("Best fit test statistic: ", "")
            list_result_saturated.append(float(current_toy_result))

    numer_saturated = 0
    for i in range(1, len(list_result_saturated)):
        current_result = list_result_saturated[i]
        if float(result_saturated) < current_result:
            numer_saturated = numer_saturated + 1

    p_value_saturated = float(numer_saturated) / denom
    print "p_value_saturated : " + str(p_value_saturated) + ", numer_saturated = " + str(numer_saturated)


    dict_limit[channel][int(mZp)][int(mN)] = [p_value_KS, p_value_AD, p_value_saturated]



    print "------------------------------------------------------------------"
    os.chdir(current_dir)



sort_dict_limit = sorted(dict_limit.items(), key=operator.itemgetter(0))

for i in dict_limit.keys():
    for j in dict_limit[i].keys():
        for k in dict_limit[i][j].keys():
            current_value = dict_limit[i][j][k]
            
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

f_output_EE = open("./output/Goodness_of_fit_" + binning + "_EE.txt", 'w')
for i in sort_sort_dict_limit_EE:
    current_list = sorted(i[1].items(), key=operator.itemgetter(0))
    for j in current_list:
        f_output_EE.write( str(i[0]) + "\t" + str(j[0]) + "\t" + str(j[1][0]) + "\t" + str(j[1][1]) + "\t" + str(j[1][2])+ "\t" + "\n" )

f_output_EE.close()

f_output_MuMu = open("./output/Goodness_of_fit_" + binning + "_MuMu.txt", 'w')
for i in sort_sort_dict_limit_MuMu:
    current_list = sorted(i[1].items(), key=operator.itemgetter(0))
    for j in current_list:
        f_output_MuMu.write( str(i[0]) + "\t" + str(j[0]) + "\t" + str(j[1][0]) + "\t" + str(j[1][1]) + "\t" + str(j[1][2])+ "\t" + "\n" )

f_output_MuMu.close()

f.close()
