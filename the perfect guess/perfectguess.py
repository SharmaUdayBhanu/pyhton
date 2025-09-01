import random

class guess:
  def __init__(self , usernumber):
    self.usernumber = usernumber
  
  def guessthenumber(self):
    count = 0
    randomnumber = random.randint(1,100)
    while(randomnumber != self.usernumber):
      self.usernumber = int(input("Guess a Number: "))
      count += 1
      if(self.usernumber < randomnumber):
        print("Your Guessed Number is lesser than expected Number. Please entered a greater number")
      elif(self.usernumber > randomnumber):
        print("Your Guessed Number is greater than expected Number. Please entered a smaller number")
    print(f"🎉 Congratulations! You guessed it right in {count} tries.")

obj = guess(0)
obj.guessthenumber()