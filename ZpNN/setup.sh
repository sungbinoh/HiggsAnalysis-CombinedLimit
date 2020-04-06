#!/bin/bash
export LIMIT_WORKING_DIR=`pwd`
export CMSSW_PATH='/data6/Users/suoh/Limit/CMSSW_10_2_13/src/'
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch; source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cd $CMSSW_PATH
eval `scramv1 runtime -sh`
cd $LIMIT_WORKING_DIR
unset PYTHONPATH
