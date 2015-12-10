records = [{"name":  " Pedro" , 'age': 22} , {"name":  " Juan" , 'age': 23}, {"name":  " Pepe" , 'age': 24}] 

# Sort name using funciton
def foo(value):
    return value.get('name')
print 'sort name using function ', sorted(records, key=foo )

# Sort age using function
def bar(value):
    return value.get('age')
print 'sort age using function ', sorted(records, key=bar)

# Sort name using lambda
print 'sort name using lambda ', sorted(records, key=lambda x:x.get('name'))

# Sort age using lambda
print 'sort age using lambda', sorted(records, key=lambda x:x.get('age'))

