# 1 . Create a class (2-D vector) and use it to create another class representing a 3-D vector.
# class twodVector:
#   def __init__(self , i , j):
#     self.i = i
#     self.j = j
#   def show(self):
#     print(f"The 2d vector is {self.i}i , {self.j}j")  
# class threedVector(twodVector):
#   def __init__(self , i , j , k):
#     super().__init__(i , j)
#     self.k = k
#   def show(self):
#     print(f"The 2d vector is {self.i}i , {self.j}j , {self.k}k")  

# a = twodVector(1 ,2)
# a.show()
# b = threedVector(5 , 2, 3)
# b.show()


# 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from
# 'Pets'. Add a method 'bark' to class 'Dog'.
# class Animals:
#   pass
# class Pets(Animals):
#   pass
# class Dog(Pets):
#   @staticmethod
#   def bark():
#     print("Bow Bow !!")

# d = Dog()
# d.bark()


# 3. Create a class 'Employee' and add salary and increment properties to it.Write a method 'salaryAfterlncrement' method with a @property decorator with a setter
# which changes the value of increment based on the salary.
class Employee:
  salary = 23000000
  increment = 20
  @property
  def salaryAfterlncrement(self):
    return (self.salary + self.salary * (self.increment/100))
  @salaryAfterlncrement.setter
  def salaryAfterlncrement(self, salary):
    if salary <= 200000:
      self.increment = 30
    else:
      self.increment = 10   # example: adjust for higher salary


e = Employee()
print("Before:", e.salaryAfterlncrement)

# Using setter
e.salaryAfterlncrement = 150000   # changes increment
print("After:", e.salaryAfterlncrement)