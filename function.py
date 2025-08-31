# def factorial(n):
#   if (n == 1 or n == 0):
#     return 1
#   return n * factorial(n-1)

# ans = factorial(5)
# print(ans)

# 1. Write a program using functions to find greatest of three numbers.
def greatestBtwThree(n1 , n2 , n3):
  if (n1 > n2 and n1 > n3):
    return n1
  elif (n2 > n1 and n2 > n3):
    return n2
  elif (n3 > n1 and n3 > n1):
    return n3
a = int(input())
b = int(input())
c = int(input())
print(greatestBtwThree(a , b, c))