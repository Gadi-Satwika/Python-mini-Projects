import emoji

#Emoji module contains all frequently used emojis with predefined names

#Precautions
#Whenever we are working with emoji module we need take care of the word we need transition
#That is, if we need pizza emoji we need to enter correct word because it is case-sensitive. Even if you enter (Pizza) it will not give output
#For the word we need transition, the word should start with colon(:) and end with colon(:) i.e :pizza:
#So these are the two things that we need to remember

all_emojis = {"sad" : ":sob:",
	"happy" :":smiley:",
	"rock" :":rock:",
	"paper" : ":scroll:",
	"scissor" :":scissors:",
	"laugh" :":joy:",
	"Fire" :":fire:",
	"cool" : ":sunglasses:",
	"surprise" :":astonished:",
	"tired" :":sleeping:",
	"pizza" :":pizza:",
	"burger" :":hamburger:",
	"cake": ":birthday:",
	"coffee" : ":coffee:",
	"apple" : ":apple:",
	"fries" : ":fries",
	"sun" : ":sunny:",
	"moon" : ":crescent_moon:",
	"tree" : ":deciduous_tree:",
	"cat" : ":cat:",
	"dog" : ":dog:",
	"flower " : ":cherry_blossom:",
	"basketball" : ":basketball:",
	"chess " : "chess _pawn:",
	"won"  : ":trophy:",
	"win": ":trophy:",
	"car" :"car :",
	 "airplane" : ":airplane:",
	 "ship": ":ship:",
	  "bicycle" : ":bike:" ,
	  "bike" : ":bike:",
	  "check" : ":white_check_mark:",
	  "cross" :  ":x:",
	  "play " : ":arrow_forward:",
	  "stop" : ":stop_button:",
	  "warning": ":warning:",
	  "love" : ":heart:"
}
def start():
	sentence = input("Enter sentence in which you want to apply emoji transition:  ").split()
	new = []
	for i in sentence:
		word = emoji.emojize(":" +i+ ":" , language = 'alias')
		word1 = word[1:len(word)-1]
		if word1 != i:
			new.append(word)
		elif i.lower() in all_emojis:
			new.append( emoji.emojize(all_emojis[i.lower()], language = 'alias' ))
		else:
			new.append(i)
	
	new_sentence = '  '.join(new)
	print(new_sentence)
	
	again = input("Do you want to try again: (y/n): ")
	if again.lower() == 'y':
		start()

start()
