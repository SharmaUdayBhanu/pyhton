# I. Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.

'''class Programmer:
  company = "Microsoft"
  def __init__(self , name , age , salary):
    self.name = name
    self.age = age
    self.salary = salary

p = Programmer("Bhanu" ,21 ,  1200000)
print(p.name , p.age , p.salary , p.company)'''

# 2. Write a class "calculator" capable of finding square, cube and square root of a
# number.

'''class Calculator:
  def square(self , n):
    return n * n
  def cube(self , n):
    return n * n * n
  def squareRoot(self , n):
    return n ** 0.5

obj = Calculator()
print(obj.square(2) , obj.cube(2) , obj.squareRoot(2))'''

# 5. Write a class Train which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class Train:
  noOfSeats = 150
  fair = 50
  def booTicket(self):
    if Train.noOfSeats > 0:
      print("Seat booked Successfully :)")
      Train.noOfSeats-=1
  def getStatus(self):
    print(f"Available Seats are: {Train.noOfSeats}")
  
  def getFairInfo(self):
    print("Enter the number of seats you want to book")
    seats = int(input())
    if seats <= Train.noOfSeats:
      print(f"fair: {seats*Train.fair}")
    else:
      print(f"Only {Train.noOfSeats} are available")

obj = Train()
obj.booTicket()
obj.getStatus()
obj.getFairInfo()

