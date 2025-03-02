import random
import emoji

user_score = 0
computer_score = 0
def check_win(computer,user):
	global user_score
	global computer_score
	if( computer == user ):
		print(laughing," It's a Tie!")
	elif( (user== rock and computer == scissor) ):
		print(random.choice(win_reactions))
		user_score+=1
	elif(  (user == paper and computer == rock) ):
		print(random.choice(win_reactions))
		user_score+=1
	elif( (user ==  scissor and computer == paper) ):
		print(random.choice(win_reactions))
		user_score+=1
	else:
	 	print(random.choice(lost_reactions))
	 	computer_score+=1
	 	print()


rock = emoji.emojize(" :rock: ",language = 'alias')
paper = emoji.emojize(" :scroll: ",language = 'alias')
scissor = emoji.emojize(" :scissors: ",language = 'alias')
laughing = emoji.emojize(" :joy: ",language = 'alias')

win1 = emoji.emojize(" :partying_face: ",language = 'alias' )
win2 = emoji.emojize(":tada:",language = 'alias')
win3 = emoji.emojize(":confetti_ball:,",language = 'alias')
win4 = emoji.emojize(":fire:",language='alias')

win_reactions = [ win1 +"Yay! You Won The Game" ,
win2+" Congrats! You Crushed It ",
win3+" Victory dance time!",
win4+"You're on Fire"
]

lost1 = emoji.emojize(" :cry: ",language = 'alias')
lost2 = emoji.emojize(":pensive:",language = 'alias')
lost3 = emoji.emojize(":worried:",language = 'alias')

lost_reactions = [lost1+"You Lost! Try Again",
lost2+"Oops! Better Luck Next Time",
lost3+" Sad, Play Again!"
]

options = [ rock,paper,scissor ]

print("Play the Game")

print("1 : Rock "+ rock)
print("2:  Paper "+paper)
print("3:  Scissor "+scissor)

history_store = []
try:	
	play_again = 'y'
	while play_again =='y':
		user = options[  int(input("Enter Your Choice: [1,2 or 3] : ")) -1]
		computer = options[random.randint(0,2)]
		print("You: ", user)
		print("Computer: ", computer)
		check_win(computer, user)
		history_add = "Your choice: "+user +"| Computer Choice: "+computer
		history_store.append(history_add)
		print()
		play_again = input("Do You Want To Play Again:(y/n):  ")	
	print()	
	print("your Score: ",user_score)
	print("computer Score: ",computer_score)
	print("Game History: ")
	for eachtime in history_store:
		print(eachtime)
except IndexError:
	print("Invalid Choice")
print()

