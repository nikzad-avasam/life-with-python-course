'''
false values in python conditionals

False
None
Zero
''
{}
[]
()


'''
con = ()
if con:
    print('this is true')
else:
    print('this is false ')

# is
'''
a = [1,2,3]
b = a
#print(a==b)
print(id(a))
print(id(b))

print(id(a) == id(b))
print(a is b )
'''
#switch case python
'''
x = 7
if x==2:
    print('x is two')
elif x==3:
    print('x is three')
elif x==4:
    print('x is four')
elif x==5:
    print('x is five')
else:
    print('x is default')
'''

'''
and
or
not
'''
'''
user = 'admin'
logged_in = True

if not logged_in:
    print('you must logged in')
else:
    print('welcome')

'''
'''
if user == 'admin' and logged_in:
    print('dear admin welcome')
else:
    print('you are not admin')
'''
'''
if user=='admin' or logged_in:
    print('you are admin or you are loggedin ')
else:
    print('you must be admin or logged in')
'''   
# == , is 
# !=
# < , > , <= ,>=
'''
x = 5

if x >= 11:
    print(' x is larger than 11')
else:
    print('x is smaller than 11')
'''
'''
if True:
    print('this is true valuee')
    
if False:
    print('second if is true')
'''

