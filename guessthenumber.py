import random
n=random.randrange(1,100)
guess=int(input("Enter a number within the range of 1 through 100"))
if guess < n:
    print("Higher")
    guess=int(input("Enter the number again:"))
elif guess > n:
    print("Lower")
    guess=int(input("Enter the number again:"))
else:
    print("You guessed it right")