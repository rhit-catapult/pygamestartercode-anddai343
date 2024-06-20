print("guess my number")

import random
number = random.randint(1, 100)
counter=1
#print(number)
guess = int(input("Guess a number between 1 and 100 "))
while(guess!=number):
  if(guess > number):
    print("your guess was too high")
  elif(guess < number):
    print("your guess was too low")
  guess = int(input("Guess a number between 1 and 100 "))
  counter+=1

print(f"it took u {counter} guesses")

# I feel paralyzed