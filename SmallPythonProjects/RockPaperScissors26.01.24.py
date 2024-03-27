import random

options = ["Rock", "Paper", "Scissors"]
options_RPSLS = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class menu:
	def contents():
		choice = character_print('''
		Here are your options:
		
		1. Play against machine
		2. Multiplayer
		3. 2player against machine
		4. Rock Paper Scissors Lizard Spock
		5. Help
		6. Exit

		''')
		return choice
		menu.choice(choice)

	def choice(choice):
		if choice == 1:
			play.single_player()
		elif choice == 2:
			play.multiplayer()
		elif choice == 3:
			play.two_player()
		elif choice == 4:
			play.RPSLS
		elif choice == 5:
			needs_help == character_print('What do you need help with? (1/2/3/4)')
			if needs_help == 1:
				help.help_sp()
		elif choice == 6:
			exit = character_print("Are you sure you want to quit the game? y/n ")
			if exit == "y":
				exit("Bye Bye!") 
			elif exit == "n":
				menu.contents()
			else:
				character_print("Invalid option")
				menu.contents()
		else:
			character_print("Invalid option, choose a number: ")
			menu.contents()


class help:
	def help_sp():
		character_print('''
		Rules:
		Rock beats Scissors (crushing)
		Scissors beats Paper (cuts)
		Paper beats Rock (covers) \n''')
		playing = character_print("Play? y/n ")
		if playing == "y":
			play.single_player()
		elif playing == "n":
			menu.contents()
		else: 
			character_print("Invalid option")
			help.help_sp()

	def help_mp():
		character_print('''
		Rules:
		Rock beats Scissors (crushing)
		Scissors beats Paper (cuts)
		Paper beats Rock (covers) \n
		
		Player one enters their option, then player two.
		Then we see who wins!''')
		playing = character_print("Play? y/n ")
		if playing == "y":
			play.multiplayer()
		elif playing == "n":
			menu.contents()
		else: 
			character_print("Invalid option")
			help.help_mp()
		

class play:
	def machine_choose():
		result = options[random.randint(0,3)]
		return result
	def single_player():
		player_score == 0
		machine_score == 0
		character_print("Welcome to Single Player mode!\n")
		player_option = character_print('''
		Your play options:\n
		R -- Rock
		P -- Paper
		S -- Scissors\n''')

		character_print("Round 1! (Best of 3 / First to 2)\n")
		r1choice = character_print("Enter your option: (R/P/S)")
		character_print("3...\n2...\n1...")
		character_print("computer chose ", play.machine_choose())


	def character_print(info):		# prints text one character at a time
		for char in info:			# this prints characters one by one to create a better ui
			sys.stdout.write(char)  # the sys module is used to do this
			sys.stdout.flush()
			time.sleep(0.010)
		return input()


menu.contents