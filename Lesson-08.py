def kwargsTest(*args , **kwargs):
    for kw, value in kwargs.items():
        print(kw,value)
  

kwargsTest(name='ali',code=125451,age=22,family='samani')

'''
def jam(*args , **kwargs):
    
    result = 0
    
    for arg in args:
        result += arg

    return result

print(jam(1,2,5,6,1,5))
'''
'''
def pname(name='***',family='***'):
    msg = name+" is your name and your family is "+family
    return msg

print(pname(family='nikzad',name='sam'))
'''
'''
def sfunc(y):
    return y

print(sfunc('hello World . Im iranian') )
'''
'''
def hello_function(x):
    #print(x)
    return x

result = hello_function('string test')
print(result)
'''
