# f = open("my file.txt" , 'w')
# st = "Hi there this write opration!!"
# data = f.write(st)
# print(data)
# f.close()

# same can be done using with statement you dont have to explicitly use close() 
# with open("file.txt" , "r") as f:
#   # st = "Bhanu Uday Sharma"
#   # f.write(st)
#   print(f.read())


#### 1. Write a program to read the text contains the word 'twinkle'. m a given file 'poems.txt' and find out whether it ####


# with open("poems.txt") as f:
#   data = f.read()
#   if("twinkle" in data):
#     print("Present")
#   else:
#     print("Absent")


# 2. The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
# previous Hi-score. You need to write a program to update the Hi-score whenever the
# game() function breaks the Hi-score.


# import random
# def game():
#   return random.randint(1 , 100)
# scored = game()
# with open("Highscore.txt" , "r") as f:
#   highscore = f.read()
#   if(highscore != ""):
#     highscore = int(highscore)
#   else:
#     highscore = 0
  
# if scored > highscore:
#     with open("Highscore.txt", "w") as f:
#         f.write(str(scored))


# 4. A file contains a word "Donkey" multiple times. You need to write a program which
# replace this word with ##### by updating the same file.

with open("cusswordremove.txt") as f:
  st = f.read()


cusswords = ["donkey" , "monkey" , "cunt" , "Moron"]


for cussword in cusswords:
  cussword = cussword.lower()
  st = st.lower()
  st = st.replace(cussword , "####")
with open("cusswordremove.txt" , "w") as f:
  f.write(st)
