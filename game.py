#import the random package so we can generate a random choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

#adding lives when one or the other gets to 0 win/lose
player_lives = 5
computer_lives = 5

#let the AI make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting
player=False

while player is False:
	player=input("Choose rock, paper or scissors: \n")

	#start doing some logic and condition checking
	print("computer", computer, "player: ", player)

	#always check a breaking condition first
	if player == computer:
		#we have a tie, no pointin going any further
		print("tie, no one wins try again")

	elif player == "quit":
		print("you chose to quit, quitter")
		exit()	
	elif player =="rock":
		if computer == "paper":
			print("you lose!", computer, "covers", player, "\n")
        else:
        	print("you won!", player, "smashes", computer, "\n")
	elif player =="paper":
		if computer == "scisors":
			print("you lose!", computer, "cuts", player, "\n")
        else:
        	print("you won!", player, "covers", computer, "\n")
	elif player =="scissors":
		if computer == "rock":
			print("you lose!", computer, "smashes", player, "\n")
        else:
        	print("you won!", player, "cuts", computer, "\n")

        

	player = False
	computer=choices[randint(0,2)]