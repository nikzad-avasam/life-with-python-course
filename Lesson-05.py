student = { 'name':'ali' , 'age': 30 , 'course':['math,physics']  }
#print(student['course'])
#print(student.get('phone','Phone Not Found'))
'''
student['phone'] = '09350000000'
student['name'] = 'sam'

student.update({'name':'nasim','age':21,'city':'tabriz','phone':'555-55-55'})

del student['city']
del student['age']
print(student)
'''
#print(len(student))
#print(student.keys())
#print(student.items())

for key, value in student.items():
        print(key,value)
