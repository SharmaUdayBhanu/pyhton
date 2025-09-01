# # 1. Write a program to open three files 1 .txt, 2.txt and 3.txt if any these files are not
# # present, a message without exiting the program must be printed prompting the same.
# try:
#   with open("poems.txt") as f1:
#     print(f1.read())
#   with open("file.txt") as f2:
#     print(f2.read())
#   with open("my file.txt") as f3:
#     print(f3.read())

# except FileNotFoundError as e:
#   print(f"{e.filename} does not exist")


# # 2. write a program to print third, fifth and seventh element from a list using enumerate function.
# l = {1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 , 9}
# for index , i in enumerate(l):
#   if index == 2 or index == 4 or index == 6:
#     print(f"{i} at index {index}")

# # 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
# n = int(input("Enter Your desired number:"))
# l = [1 , 2, 3 ,4 ,5 , 6 ,7 ,8 , 9 ,10]
# mul = [n*i for i in l]
# print(mul)

# # 4. Write a program to display a/b where a and b are integers. If b=O, display infinite by
# # handling the 'ZeroDivisionError'.
# try:
#   a = int(input("a:"))
#   b = int(input("b:"))
#   print(a/b)
# except ZeroDivisionError as e:
#   print("Infinity")
  
# 5. store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter Your desired number:"))
l = [1 , 2, 3 ,4 ,5 , 6 ,7 ,8 , 9 ,10]
mul = [n*i for i in l]
# print(mul)
with open("Tables.txt" , "a") as f:
  f.write(f"Table of {n} is: \n {mul}\n")
with open("Tables.txt", "r") as f:
    print(f.read())
