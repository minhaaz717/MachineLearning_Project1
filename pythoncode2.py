dog={} #creating an empty dictionary

#assigning and adding key value pairs
dog={
    'name':'Harry',
    'color':'Black',
    'breed':'Golden Retriever',
    'legs':'long',
    'age':'3 years'
}
print(dog)

#creating a student dictionary
student_dict={
    'first_name':'Minhaaz',
    'last_name':'Shaik',
    'age':22,
    'country':'US',
    'marital_status':'Single',
    'skills':[ "Python", "Core Java", "AWS", "SQL"],
    'address':{
        'street':'Hardy St',
        'zipcode':'66223'
    }
    }
print(student_dict)

#length of student_dict    
print(len(student_dict))

#to print output of skills and its datatype
print(type(student_dict['skills']))
student_dict['skills'].extend(['DB','Testing'])

#printing keys
keys=student_dict.keys()
print(keys)

#printing values
values=student_dict.values()
print(values)

