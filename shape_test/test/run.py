import os

channels = [
#"MuMu",
"ElEl"
]

lines = open('masses.txt').readlines()

os.system('mkdir -p logs/shape/')
os.system('mkdir -p logs/count/')

counter = 0
for line in lines:
  sample = line.strip('\n')

  ## shape ##

  for channel in channels:

    cmd = 'combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood cards/shape_'+channel+"_"+sample+'.txt -n '+sample+' --expectedFromGrid 0.5 -T 1000 &> logs/shape/log_'+channel+"_"+sample+'.txt &'

    print cmd
    os.system(cmd)

    if (counter is not 0) and (counter%10==0):
      os.system('sleep 30')
    counter += 1

  ## count ##

  for channel in channels:

    cmd = 'combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood cards/count_'+channel+"_"+sample+'.txt -n '+sample+' --expectedFromGrid 0.5 -T 1000 &> logs/count/log_'+channel+"_"+sample+'.txt &'

    print cmd
    os.system(cmd)

    if (counter is not 0) and (counter%10==0):
      os.system('sleep 30')
    counter += 1


