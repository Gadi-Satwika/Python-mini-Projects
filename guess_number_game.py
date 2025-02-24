import random

def guess(x):
	number = random.randint(1,x)
	guess = 0
	while(guess!=number):
		guess = int(input("Guess the  Secret Number?(Between 1- 100) "))
		if(guess>number):
			print("You are too high!")
		elif(guess<number):
			print("You are too low!")
		else:
			print("Yay! You found the number")
guess(100) 
