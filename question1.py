first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']

fullnames = [f+" "+n for f,n in zip(first_names, last_names)]
#print(zip(first_names,last_names))

#for f in first_names:
#    for l in last_names:
#       full_names.append(f + ' '+ l)

print(fullnames)

