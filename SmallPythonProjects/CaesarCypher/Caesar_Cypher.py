##########################
#~~~~~~~~~~~~~~~~~~~~~~~~#
#~ Name: Emily Cowie    ~#
#~ Date: 01/02/2024     ~#
#~ Title: Caesar Cypher ~#
#~~~~~~~~~~~~~~~~~~~~~~~~#
##########################


#----imports---------------------------------

import random 
import sys
import time

#----variables-------------------------------
final_en_message = ''
#----functions-------------------------------

class MenuAndRelated:  # menu and all the choices that follow other than the actual game

	def menu():
		choice = character_print(''' 
	Welcome to Ceaser Cypher™, here are your options:
	------------------------------
	1. Encode a message
	2. Decode a message
	3. Exit
	------------------------------
	Choose which one you would like to do. \n\n''')
		MenuAndRelated.menu_choice(choice)

	def menu_choice(choice):  # directs the user to the right area depending on their choice
		while True:
			if choice == '1':
				encrypt()
			elif choice == '2':
				decrypt()
			elif choice == '3':
				exit = character_print('Are you sure? y/n ')
				if exit == 'y':
					exit('Bye sad to see you go...')
				elif exit == 'n':
					character_print('Returning to menu...')
					time.sleep(2)  # example of the time module
					MenuAndRelated.menu()
			else:
				character_print('Unrecognised, choose again\n')



	def leaderboard():
		path = '/workspaces/Prison-Escape/CSV Files/score.csv'
		df = pd.read_csv(path)

		# sorts values and orders them by highest level
		df = df.sort_values(by='Level', ascending=False)

		# creates a column called rank showing the top player
		df['Rank'] = range(1, len(df) + 1)
		df = df[['Rank'] + [col for col in df.columns if col != 'Rank']]

		# 'index=False' hides index column
		character_print(df.to_string(index=False))

		# save to og file
		output_file_path = '/workspaces/Prison-Escape/CSV Files/sorted_leaderboard.csv'
		df.to_csv(output_file_path, index=False)
		input()


	
def character_print(info):			# prints text one character at a time
	for char in info:				# this prints characters one by one to create a better ui
		sys.stdout.write(char)		# the sys module is used to do this
		sys.stdout.flush()
		time.sleep(0.010)
	return input()


def encrypt():
	encoded = []
	text = character_print("Enter your message that you want to encode\n")
	shift = character_print("How many characters do you want to shift by? Or try random [ran]? \n")
	if shift == 'ran':
		shift = random.randint(0,26)
	elif int(shift) > 26 or int(shift) == 0:
		shift = int(character_print("Please enter a valid number between 1 and 27"))
	else:
		shift = int(shift)

	to_encode = [*text]									# splits the list into its characters e.g. ['123'] --> ['1', '2', '3']
	len_message = len(to_encode)						# 'len' gives the number of items in the list e.g. list = ['1', '2', '3'] // len(list) --> 3
	for i in range(0,len_message):						# goes through each item in the list
		encoded.append(chr(ord(to_encode[i])+shift))	# ord turns character into unicode , chr converts it back
	final_en_message = ''.join(encoded)
	character_print(final_en_message)
	return final_en_message -------------------------------------------------
	menu()


def decrypt():
	decoded = []
	choice = character_print("Decrypt custom message [custom] Or most recently encypted message? [recent]\n")
	while True:
		if choice == 'custom':
			text = character_print("Enter your message that you want to decode\n")
		elif choice == 'recent':
			character_print("Is this correct? [y/n]:\n")
			check = character_print(final_en_message)
			if check == 'y':
				continue
			elif check == 'n':
				character_print("Returning to custom message...")
				choice = 'custom'
	shift = int(character_print("What has the message been shifted by?"))
	to_decode = [*text]									# splits the list into its characters e.g. ['123'] --> ['1', '2', '3']
	len_message = len(to_decode)						# 'len' gives the number of items in the list e.g. list = ['1', '2', '3'] // len(list) --> 3
	for i in range(0,len_message):						# goes through each item in the list
		decoded.append(chr(ord(to_decode[i])-shift))	# ord turns character into unicode , chr converts it back
	final_de_message = ''.join(decoded)
	character_print(final_de_message)
	menu()


#----main program----------------------------
menu()
