# Pyhton Object-Oriented Programming

class employee:  #class
    pass

#instances of the class
emp_1=employee()
emp_2=employee()

print(emp_1)
print(emp_2)
#both have different loaction in the memory

emp_1.first ="Lavya"
emp_1.last="Singh"
emp_1.email="lavya8534@gmail.com"
emp_1.pay=10000000000

emp_2.first ="Shashannkkk"
emp_2.last="Shekhar"
emp_2.email="sahss8534@gmail.com"
emp_2.pay=2000000000

print(emp_1.email,emp_2.email)