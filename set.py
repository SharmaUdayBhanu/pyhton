# How to create empty set
# s = {} this will create a empty dictionary
# s = set()  this will create an empty set 

# s = {1 , 34 ,56 , 5 ,6 ,6 ,7}
# print(len(s))
# print(s) set always prints unique unordered values


# Write a program to input eight numbers from the user and display all the unique numbers (once)

# s = set()
# for i in range(8):
#   number = int(input())
#   s.add(number)
# print(s)


# Can we have a set with 18 (int) and '18' (str) as a value in it?
# s = set()
# s.add('18')
# s.add(18)
# print(s)


# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# dic = {}
# for i in range(2):
#   key = input()
#   value = input()
#   dic.update({key: value})
# print(dic)


# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry" , [1 ,2]}
print(s)
# we cannot have list in set because they are not not hashable