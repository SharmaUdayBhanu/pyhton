##decorators###

# class Employee:
#   a = 1
#   @classmethod
#   def show(cls):
#     print(f"{cls.a}")

# e = Employee()
# e.a = 33
# e.show()


class Employee:
  @property
  def name(self):
    return (f"{self.fname} \n {self.lname}")
  @name.setter
  def name(self , value):
    self.fname = value.split(" ")[0]
    self.lname = value.split(" ")[1]
  
e = Employee()
e.name = "Bhanu Sharma"
print(e.name)