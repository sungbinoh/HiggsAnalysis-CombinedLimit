#!/bin/bash
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /data6/Users/suoh/Limit/CMSSW_10_2_13/src/
eval `scramv1 runtime -sh`
unset PYTHONPATH
