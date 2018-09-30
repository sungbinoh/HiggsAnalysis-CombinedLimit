HiggsAnalysis-CombinedLimit (Branch for Z' to NN analysis)
===========================

### Official documentation

[Manual to run combine](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideHiggsAnalysisCombinedLimit#How_to_run_the_tool)

### Standalone compilation in `lxplus`
```
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
source env_standalone.sh 
make -j 8; make # second make fixes compilation error of first
```

* Twiki Page
  * https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHiggsAnalysisCombinedLimit#ROOT6_SLC6_release_CMSSW_7_4_X
### ROOT6 SLC6 release (CMSSW_7_4_X)
    #Setting up the environment (once) 
    export SCRAM_ARCH=slc6_amd64_gcc491
    cmsrel CMSSW_7_4_7
    cd CMSSW_7_4_7/src 
    cmsenv
    git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
    cd HiggsAnalysis/CombinedLimit
    
    #Update to a reccomended tag - currently the reccomended tag is v6.3.1 
    cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
    git fetch origin
    git checkout v6.3.1
    scramv1 b clean; scramv1 b # always make a clean build, as scram doesn't always see updates to src/LinkDef.h

    #Add this (HN pair) remote
    git remote add suoh git@github.com:sungbinoh/HiggsAnalysis-CombinedLimit.git
    
    #pull this branch
    git pull suoh HN_pair #will pull shape_test dir

### Main folder for HN pair analysis is ./shape_test
* Need to make a root file contains bkg & signal shapes
* Need to make a text file contains signal mass points information
  * like masses.txt
* Make.C
  * Read Shape
  * Make cards at ./cards
  * Systematic error : double error_bkgd = 0.50 means 50% systematics
  * How to run
    * For Muon : root -l -b -q "make.C(0)"
    * For Electron : root -l -b -q "make.C(1)"
    * This will make count_XXX.txt and shape_XXX.txt files in ./cards directory
    * Signal is scaled 1/1000 to get big r value for good calculation performance (too small r value gives bad results)
* Now we have all cards needed to estimate limits
  * python run.py
    * modify channels = [] to contain channels you want to run
    * What does this macro run?
      * combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood cards/shape_MuMu_Zp500_HN100.txt -n Zp500_HN100 --expectedFromGrid 0.5 -T 1000 &> logs/shape/log_MuMu_Zp500_HN100.txt &
      * log files are made as logs/shape/log_MuMu_Zp500_HN100.txt
      * These log files contains limit results
  * python read.py
    * This will make .txt file with limit results
    * results_shape_ElEl.txt

  * 
