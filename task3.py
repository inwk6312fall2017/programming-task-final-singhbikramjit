#configration task final  quiz task3
#part1

file= open('running-config.cfg','r')

f= open('conf.cfg','w') #OPEN NEW FILE TO ADD DATA

for line in file:
  f.write(line.replace('172','192'))

file.close()
 

#for line in f:
 # print(line)
f.close() 
#creat new file with name conf task done
