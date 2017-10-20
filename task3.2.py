#task3 code 2 for data access list

file=open('running-config.cfg','r')
f=open('newfile.cfg','w')
list=[] #empty list

for line in file:
#divide file into lines

  if 'access-list' in line:
    print(line)
    f.write(line)


file.close()
f.close()
