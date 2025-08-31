# import math
# ##Numbers##

# # rest all are as usual
# print(10/3)
# print(10//3)#this will give integer

# #To round off
# print(round(2.9))
# print(round(2.4))
# #absolute value
# print(abs(-2.7))

# print(math.ceil(2.2))
# print(math.floor(2.2))
# ##strings##

# course_name = "   Python programming  "
# # length
# length = len(course_name)
# #uppercase->returns new string og string not effected
# print(course_name.upper())
# #to lowercase
# print(course_name.lower())
# # capitalize evry words forst letter
# print(course_name.title())
# #removes spaces from both ends
# print(course_name.strip())
# #removes spaces from left
# print(course_name.lstrip())
# #removes spaces from right
# print(course_name.rstrip())
# #returs the index
# print(course_name.find("pro"))
# #replace the character with other (case sensative)
# print(course_name.replace("P", "j"))
# #returns true or false if the substring or character is present
# print("pro" in course_name)
# #opposite of in checks what is not there
# print("pro" not in course_name)
# #print
# # print(f"length of course_name is: {length}")


#Type Conversion
# x = int(input("x: "))
# print(type(x))
# y = int(x)+1
# print(y)

#if-else
# if x > 1:
#   print("greater than 1")
# elif x < 1:
#   print("leass than 1")
# else:
#   print("equal to 1")

#ternary oprator
# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# if "bb" < "bh":
#   print("wohoo")

#for-loop
# start , end -1 , step
# for n in range(1 , 6 , 2):
#   print(n)

#printing characters
# for ch in "Python":
#   print(ch)

#printing numbers
# for n in [1 , 2 , 3, 4 ,5 ]:
#   print(n)

##while loop
# num = 100
# while num > 0:
#   print(num)
#   num//=2

# command = ""
# while command.lower() != "quit":
#   command = input(">>")
#   print("Echo: " , command)

#excercise count even numbers
# count = 0
# n = 4
# while n > 0:
#   number = int(input())
#   n-=1
#   if number % 2 == 0:
#         count+=1
# print(f"We have {count} even numbers")



##functions
def greet(first_name , last_name):
  print(f"Hi! , {first_name} {last_name}")

greet("Bhanu Uday" , "Sharma")