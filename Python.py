import random
n = random.randrange(1,10)
guess = int(input("Enter any no.: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter no. again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter no. again: "))
    else:
      break
print("you guessed it right!!")
