# letter = """
# Dear <|Name|>
# you are selected!
# <|Date|>
# """
# print(letter.replace("<|Name|>" , "Bhanu").replace("<|Date|>" , "30th August 2025"))

## tuple
# a = (1 , 2, 3, 5)
# print(a)
# print(type(a))

# Write a program to store seven fruits in a l' t entered by the user.

# fruits = []
# for i in range(7):
#   fruit = input()
#   fruits.append(fruit)
# print(f"Fruits Entered are: {fruits}")


# Write a program to accept marks of 6 students and display them in a sorted manner.
Students = []
for i in range(6):
  marks = int(input())
  Students.append(marks)
Students.sort()
print(f"Sorted Marks are: {Students}")
