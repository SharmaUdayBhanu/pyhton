class employee:
  age = 21
  salary = 1200000 #class Attribute


  def __init__(self , name , salary , age): #This is an dunder method which is automatically called
    self.name = name
    self.age = age
    self.salary = salary

  
  ### static method ###
  @staticmethod # this is a decorator
  def greet():
    print("Good Morning Pineapple , Looking very good very nice")



obj = employee("Aditya" , 222000 , 22)
#obj.Name = "Uday" #name = instance attribute , rest unchanged are class attributes as they directly belong to the class
print(obj.name , obj.age , obj.salary)
#obj.getInfo() 
# employee.getInfo(obj)
#self should be given because it converts into employee.getInfo(obj)
#obj.greet()



