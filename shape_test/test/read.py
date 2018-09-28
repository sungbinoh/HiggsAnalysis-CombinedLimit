import os

lines = open('masses.txt').readlines()

whichs = [
"shape",
"count"
]

channels = [
"MuMu",
"ElEl",
]

for which in whichs:

  for channel in channels:

    out = open('results_'+which+'_'+channel+'.txt','w')

    for line in lines:
      sample = line.strip('\n')

      logs = open('logs/'+which+'/log_'+channel+'_'+sample+'.txt').readlines()

      limit_2sig_down = ""
      limit_1sig_down = ""
      limit_central = ""
      limit_1sig_up = ""
      limit_2sig_up = ""

      for l in logs:
        l = l.strip('\n')

        '''
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
        '''

        # Limit: r < 0.326386 +/- 0.0363156 @ 95% CL
        if "Limit: r < " in l:
          words = l.split()
          limit_central = words[3]

      out.write(sample+'\t'+limit_central+'\n')
      #out.write(sample+'\t'+limit_2sig_down+'\t'+limit_1sig_down+'\t'+limit_central+'\t'+limit_1sig_up+'\t'+limit_2sig_up+'\n')


    out.close()

