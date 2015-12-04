full_names = ['Nobita Nobi', 'Shizuka Minamoto', 'Takeshi Goda', 'Suneo Honekawa']
first_names = []
last_names = []
index = 0
for name in full_names:
    first_name, last_name = name.split(' ')
    first_names.insert(len(first_name), first_name)
    last_names.insert(len(last_name), last_name)
    
print'first names ', first_names
print 'last name ' , last_names 

