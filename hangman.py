import random
import emoji
stages = [
r"""
+----+
|    |
|    O
|   /|\ 
|   / \     
| """,r"""
+----+
|    |
|    O
|   /|\ 
|   /      
| """,r"""
+----+
|    |
|    O
|   /|\ 
|        
| """,
"""
+----+
|    |
|    O
|   /| 
|        
| """ ,"""
+----+
|    |
|    O
|    | 
|        
| """ ,"""
+----+
|    |
|    O
|    
|        
| """ ,"""
+----+
|    |
|    
|    
|        
| """ ]

#Needed Emojis initialized 
win1 = emoji.emojize(":partying_face:",language = 'alias' )
win2 = emoji.emojize(":tada:",language = 'alias')
win3 = emoji.emojize(":confetti_ball:",language = 'alias')
win4 = emoji.emojize(":fire:",language='alias')

win_reactions = [ win1 +"Yay! You Won The Game" ,
win2+" Congrats! You Crushed It ",
win3+" Victory dance time!",
win4+"You're on Fire"
]

lost1 = emoji.emojize(":cry:",language = 'alias')
lost2 = emoji.emojize(":pensive:",language = 'alias')
lost3 = emoji.emojize(":worried:",language = 'alias')

lost_reactions = [lost1+"You Lost! Try Again",
lost2+"Oops! Better Luck Next Time",
lost3+" Sad, Play Again!"
]

play_again = emoji.emojize(":repeat:",language = 'alias')
#Each Category Function
def Easy_Fruits():
	fruits = ['apple', 'guava', 'mango', 'grape']
	fruits_hints = { 'apple' : 'Keeps the doctor away' , 'guava' : 'Rich in Vitamin C and has a green skin' , 'mango' : 'King of Fruits and loved in Summer' , 'grape': 'comes on bunches' }
	word = random.choice(fruits)
	hint = fruits_hints[word]
	return word,hint
def Medium_Fruits():
	fruits = ['banana', 'orange', 'papaya', 'avacado']
	fruits_hints = { 'banana' : 'Monkeys love them more' , 'orange' : 'Name itself a color' , 'papaya' : 'Orange with inside black seeds' , 'avacado': 'Green and creamy, perfect for guacamole!' }
	word = random.choice(fruits)
	hint = fruits_hints[word]
	return word,hint
def Hard_Fruits():
	fruits = ['pineapple', 'blackberry', 'pomegranate', 'blueberry']
	fruits_hints = { 'pineapple' : 'Spiky Outside, Sweet and tropical Inside' , 'blackberry' : 'Dark Juicy berry, Often used in pies' , 'blueberry' : 'Tiny, blue, and full of  antioxidants' , 'pomegranate': 'Filled with Juicy red seeds!' }
	word = random.choice(fruits)
	hint = fruits_hints[word]
	return word,hint
def Easy_Sports():
	sports = ['golf' ,'rugby' ,'chess' , 'soccer']
	sports_hints = {'golf': 'A game of clubs and small white balls' , 'rugby': 'A tough game like football but without pads!' , 'chess': 'An indoor game of kings and queens', 'soccer': 'Also Called football in most countries' }
	word = random.choice(sports)
	hint = sports_hints[word]
	return word, hint
def Medium_Sports():
	sports = ['baseball' ,'swimming' ,'badminton' , 'cycling']
	sports_hints = {'baseball': 'Hit a home run in this bat-and-ball game' , 'swimming': 'A Water Sport with strokes like freestyle' , 'badminton': 'Played with a shuttle', 'cycling': 'Contains two wheels' }
	word = random.choice(sports)
	hint = sports_hints[word]
	return word, hint
def Hard_Sports():
	sports = ['golf' ,'rugby' ,'chess' , 'soccer']
	sports_hints = {'golf': 'A game of clubs and small white balls' , 'rugby': 'A tough game like football but without pads!' , 'chess': 'An indoor game of kings and queens', 'soccer': 'Also Called football in most countries' }
	word = random.choice(sports)
	hint = sports_hints[word]
	return word, hint
#Easy difficulty level functions
def Easy():
	category = input("\nEnter Category You need: ")
	if category.lower() == 'f':
		word ,hint= Easy_Fruits()
		return word,hint
	elif category.lower() == 's':
		word,hint = Easy_Sports()
		return word,hint
	else:
		print("Enter Valid Cateogory: ")
		Easy()
def  Medium():
	category = input("\nEnter Category You need: ")
	if category.lower() == 'f':
		word ,hint= Medium_Fruits()
		return word,hint
	elif category.lower() == 's':
		word,hint = Medium_Sports()
		return word,hint
	else:
		print("Enter Valid Cateogory: ")
		Medium()
def Hard():
	category = input("\nEnter Category You need: ")
	if category.lower() == 'f':
		word ,hint= Hard_Fruits()
		return word,hint
	elif category.lower() == 's':
		word,hint = Hard_Sports()
		return word,hint
	else:
		print("Enter Valid Cateogory: ")
		Hard()
#Getting difficulty level from user and calling category functions		
user_input = None
def difficulty_level():
	global user_input
	user_input = input("\nEnter You Difficulty Level:(Easy/Medium/Hard) ")
	print("\nCategories:\n 1. Fruits (F) \n2. Sports (S)") 
	if user_input.lower() == 'easy':
		word,hint = Easy()
	elif user_input.lower() == 'medium':
		word,hint = Medium()
	elif user_input.lower() == 'hard':
		word,hint =  Hard()
	else:
		print("Enter Valid Difficulty Level")
		difficulty_level()
	
	return word,hint
	
#Main function
def start_game():
	tries = 6
	play = True
	chosen_word ,word_hint = difficulty_level()
	letters = []
	for each in chosen_word:
		letters += "_"
	print(letters)
	print("About the word: ", word_hint)
	while play:
		game_over = False
		guessed_letters = []
		while not game_over  :
			guess_letter = input("Guess a Letter: ")
			count = 0
			for i in range(len(chosen_word)):
				if guess_letter == chosen_word[i] :
					letters[i] = guess_letter
					count+=1
			print(letters)
		
			if guess_letter in guessed_letters:
				print("\nYou have already guessed that letter")
			else:
				guessed_letters.append(guess_letter)
				if count==0:
					tries-=1
					print("\nTries Left: ",tries)
					if tries == 0:
						game_over = True
						print("\n",random.choice(lost_reactions))
					
			if '_' not in letters:
				game_over = True
				print("\n",random.choice(win_reactions))
				print("You Saved the Man!")
			print(stages[tries])
		option = input("\nDo you want to play again " + play_again + "(y/n): ")
		if option != 'y':
			play = False
		else:
			start_game()

start_game();
