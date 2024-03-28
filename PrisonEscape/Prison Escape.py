# ----imports---------------------------------
from datetime import datetime  # to get the exact date and time
import csv  # module to read and edit csv files
import time  # for the sleep function - delay print
import sys  # gives more access to variables for the user to control
import pandas as pd  # way to read csv files

# ----classes-------------------------------


class MenuAndRelated:  # menu and all the choices that follow other than the actual game

    def menu():  # tells the user about all the options they could choose, intro to the game etc
        choice = character_print(''' 
Welcome to Prison Escape™, here are your options:
------------------------------
1. Play game
2. Leaderboard
3. Information
4. Exit
------------------------------
Choose which one you would like to do. \n\n''')
        MenuAndRelated.menu_choice(choice)

    def menu_choice(choice):  # directs the user to the right area depending on their choice
        while True:
            if choice == '1':
                Onboarding.before_play()
            elif choice == '2':
                MenuAndRelated.leaderboard()
                MenuAndRelated.menu()
            elif choice == '3':
                MenuAndRelated.information()
                MenuAndRelated.menu()
            elif choice == '4':
                exit = character_print('Are you sure? y/n ')
                if exit == 'y':
                    exit('bye sad to see you go...')
                elif exit == 'n':
                    character_print('returning to menu...')
                    time.sleep(2)  # example of the time module
                    MenuAndRelated.menu()
            else:
                character_print('unrecognised, choose again\n')

    def information():  # tells the user about what the premise of the game is and get them introduced to it
        character_print(''' 
*****************************************************************************************
* Welcome to Prison Escape™!                                                            *
* You are a criminal, who is locked up for 20 years because you stole the Crown Jules   *
* - or attempted to! The problem is, you were drunk and it was a dare from your         *
* friends [bedrinkaware.com] and you are not really a bad person - its time to escape!  *
*                                                                                       *
* You will go through a series of trials to test if you are worthy of escaping the      *
* prison, these will be very serious, logical word problems!                            *
*****************************************************************************************\n''')
        input()

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


class CsvEdit:  # csv manipulation e.g. editing csv with new info
    def create_csv_users():  # creates the csv where all the user data will be stored and manipulated
        with open('users.csv', 'w', newline='') as csvfile:
            file = csv.writer(csvfile, delimiter=',',  # delimiter used to separate values
                              quotechar='|', quoting=csv.QUOTE_MINIMAL)  # quotechar is what is used to surround areas that contain thy delimiter characters
            # QUOTE_MINIMAL is saying only specifies areas are quoted
            file.writerow(['Username', 'Password'])

    def create_csv_scores():  # creates the csv where all the user score data will be stored and  manipulated
        with open('score.csv', 'w', newline='') as csvfile:
            file = csv.writer(csvfile, delimiter=',',
                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file.writerow(['Username', 'Level'])

    # inputting the new username into the database
    def update_csv_users(username, password):
        fields = ['Username', 'Password']
        with open('/workspaces/Prison-Escape/CSV Files/users.csv', 'a', newline='\n') as csvfile:
            # dict is now a dictionary, as required by writerow.
            dict = {'Username': username, 'Password': password}
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerow(dict)

    # inputting the users score into the database
    def update_csv_scores(username, level):

        # Read the existing CSV file into a Pandas DataFrame
        path = '/workspaces/Prison-Escape/CSV Files/score.csv'
        df = pd.read_csv(path)

        # Update the specific data in the DataFrame
        df.loc[df['Username'] == username, 'Level'] = level

        # Save the updated DataFrame back to the same CSV file
        df.to_csv(path, index=False)

    def add_date_to_leaderboard():
        def get_date():
            # Get the current date and time
            current_datetime = datetime.now()

            # Format the date and time as "xx:xx xx/xx/xx"
            formatted_datetime = current_datetime.strftime("%H:%M %m/%d/%y")

            return formatted_datetime

        # Example usage:
        current_date = get_date()
        print("Current Date and Time:", current_date)

        path = '/workspaces/Prison-Escape/CSV Files/score.csv'
        df = pd.read_csv(path)


class Onboarding:  # Onboarding - sign up, log in etc

    def before_play():  # once user selects play, they need to either sign up or log in
        account = character_print('Have you created an account? y/n   ')
        if account == 'n':
            Onboarding.sign_up()
        elif account == 'y':
            character_print('''
Welcome back!
To log in, press 'Enter'. 
Dont have an account? Sign up by pressing 'Esc'.\n ''')
        while True:
            key = sys.stdin.read(1)
            if key == '\x1b':  # Esc key
                Onboarding.sign_up()
                Play.intro_to_game()
                break
            elif key == '\n':  # Enter key
                Onboarding.sign_in()
            else:
                character_print("Unknown key pressed.")

    def sign_up():  # used to collect user data as they sign up
        username = character_print(
            '\nSign up for your new account! \n\nCreate new username:\n')
        # connects to the verification function
        Onboarding.verify_email(username)
        password = character_print('''\nCreate a new password:\n''')
        while True:  # to make sure the user is sure of=n their password
            verify = character_print('''Re-enter your password \n''')
            if verify == password:
                character_print('Welcome ' + username + "!\n")
                CsvEdit.update_csv_users(username, password)
                CsvEdit.update_csv_scores(username, level=0)
                Play.intro_to_game()
            else:
                character_print('Passwords do not match try again: \n')

    # this is verification used to check if their username exists in the database
    def verify_email(username):
        verified = False
        while not verified:
            # reading inside the csv file
            if username not in open('/workspaces/Prison-Escape/CSV Files/users.csv').read():
                verified = True
                print('Available!')
                return username
            else:
                username = character_print(
                    "This username is already taken choose another\nTry another username:/n")

    def sign_in():
        logged_in = False
        while not logged_in:
            username = character_print('Enter username:   ')
            password = character_print('Enter your password:   ')
            with open('/workspaces/Prison-Escape/CSV Files/users.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row[0] == username and row[1] == password:
                        logged_in = True
                        character_print('Logged in\nWelcome back ' + username)
                        Play.resume(username)
                    else:
                        continue
                character_print('''
Log in Failed
Your username or password is incorrect
Try again\n''')


class Play:  # actual game
    def intro_to_game(username):
        TextBasedImages.in_prison()
        choice = character_print(
            '\nHave you read the information section (why you are in prison)? y/n     ')
        if choice == 'y':
            character_print('Great, get ready to Play... ')
            Play.level1(username)
        elif choice == 'n':
            MenuAndRelated.information()
            Play.level1(username)

    def level1(username):
        CsvEdit.update_csv_scores(username, level=1)
        TextBasedImages.hot_soup()
        choice = character_print('''
A guard has given you a hot bowl of soup, what do you do?
                        
A - Throw the boiling soup in his face
B - Steal his keys without him noticing
C - Bribe him to set you free
D - Eat the food and do nothing               
                        
''').lower()
        while True:
            if choice == 'a':
                character_print(
                    'His face is severely burned and he gets angry, you are sentenced to another 10 years. ')
                Play.fail()
                Play.level1(username)
            elif choice == 'b':
                character_print(
                    'He notices - you are jailed for another year. ')
                Play.fail()
                Play.level1(username)
            elif choice == 'c':
                character_print(
                    'Turns out he loves bribes! When he helps to get you out, you promise to give him 1 million pounds!! ')
                Play.level2(username)
            elif choice == 'd':
                character_print(
                    "You don't get into trouble however you never get a shot at escaping, you die alone in your cell. ")
                Play.fail()
                Play.level1(username)
            else:
                choice = character_print('Please choose a valid option \n')

    def level2(username):
        CsvEdit.update_csv_scores(username, level=2)
        choice = character_print('''
He helps you to escape, but by doing so, you fall out a window!
What do you do?

A - Use your uniform as a parachute
B - Plummet to your death
C - Scream for help 
D - Use your uniform as a cape and fly to safety like superman
''').lower()
        TextBasedImages.superman()
        while True:
            if choice == 'a':
                character_print(
                    'The parachute idea fails but you do get stuck in a tree thanks your uniform being caught up in the branches!!')
                Play.level3(username)
            elif choice == 'b':
                character_print(
                    'Obviously you die. I have no idea why you chose this, were you trying to be clever? Perhaps this tells you something about your own life? ')
                Play.fail()
                Play.level2(username)
            elif choice == 'c':
                character_print(
                    'Bad idea, the guards hear you and sentence you for life. ')
                Play.fail()
                Play.level2(username)
            elif choice == 'd':
                character_print(
                    "I think you should go into an insane asylum, not a prison! Oh and you die :) ")
                Play.fail()
                Play.level2(username)
            else:
                character_print('Please choose a valid option \n').lower()

    def level3(username):
        CsvEdit.update_csv_scores(username, level=3)
        character_print('''
Someone miraculously runs out with a trampoline and catches you when you fall form the tree. 
You live.
You realise the person who saved your life was a police officer and he chases you around the street!''')
        TextBasedImages.police()
        choice = character_print('''
                        
What do you choose to do?

A - Keep running 
B - Turn yourself in
C - Disguise yourself
D - Go into somebody's house and hide
                        
''').lower()
        while True:
            if choice == 'a':
                character_print(
                    'The policeman chases you down, he shoots you. You die.')
                Play.fail()
                Play.level3(username)
            elif choice == 'b':
                character_print(
                    'You, obviously return to jail.\nBecause you chose so badly, you have to return to level 1!\n')
                character_print('Your score will also go back to 1.')
                CsvEdit.update_csv_scores(username, level=1)
                Play.condition_fail(level=1)
                Play.level1(username)
            elif choice == 'c':
                character_print(
                    'He does not fall for your tricks. You are arrested. Go back to level 1. ')
                Play.condition_fail(level=1)
                Play.level1(username)
            elif choice == 'd':
                character_print("Wow! Somehow that worked! ")
                Play.level4(username)
            else:
                choice = character_print(
                    'Please choose a valid option \n').lower()

    def level4(username):
        CsvEdit.update_csv_scores(username, level=4)
        TextBasedImages.cars()
        choice = character_print('''
He doesn't find you!
You decide to hang there for a while.
When you are about to leave, you see tons of police cars!

What do you choose to do?

A - You pretend they don't exist and watch tv
B - You go to sleep
C - Run out the back door
D - Turn yourself in
                        
''').lower()
        while True:
            if choice == 'a':
                character_print(
                    'It turns out the police cars are there for a robbery across the street! ')
                Play.level5(username)
            elif choice == 'b':
                character_print(
                    'It turns out the police cars are there for a robbery across the street! ')
                character_print(
                    'Although they wanted to interview you and you did not answer the door. They discover who you are and arrest you ')
                Play.fail()
                Play.level4(username)
            elif choice == 'c':
                character_print("Stop the running man, it's getting boring. ")
                character_print(
                    'Return to level 3 where you got chased by a police to remind you that this was an appaling choice. ')
                Play.condition_fail(level=3)
                Play.level3(username)
            elif choice == 'd':
                character_print(
                    'You, obviously return to jail\nBecause you chose so badly, you have to return to level 1!')
                character_print('Your score will also go back to 1.')
                CsvEdit.update_csv_scores(username, level=1)
                Play.condition_fail(level=1)
                Play.level1(username)
            else:
                choice = character_print(
                    'Please choose a valid option \n').lower()

    def level5(username):
        CsvEdit.update_csv_scores(username, level=5)
        character_print('''
However, they would like to interview you to see if you saw anything. 
You are worried that they might recognise you.
What do you do? ''')
        TextBasedImages.mustache()
        choice = character_print('''
A - Disguise yourself!
B - Say you saw nothing, then make them all coffee!
C - Act natural - you did nothing wrong ;)
D - You find a gun in the house, use it to send them away.
                    
''').lower()
        while True:
            if choice == 'a':
                character_print(
                    'Awful idea. Anyone can see through that neon pink wig and mustache!\n')
                character_print(
                    'You realise they know who you are and you run onto the roof, the house owner is there.')
                Play.condition_fail(level=2)
                Play.level2(username)
            elif choice == 'b':
                character_print(
                    'The police officvers love you! They are too focused on that amazing cup of coffee to realise who you are!')
                character_print(
                    'Except one! He is the man you bribed and he wants his money...')
                Play.level6(username)
            elif choice == 'c':
                character_print(
                    "Nope! Your so-called 'natural' is anything but!\n")
                character_print(
                    "You make a complete fool of yourself and actually end up confessing your love to one of the officers!")
                character_print(
                    'They do not recognise you but they arrest you for being suspicious! Back to jail (Level 1) you go!')
                Play.condition_fail(level=1)
                Play.level1(username)
            elif choice == 'd':
                character_print(
                    "Okay Okay calm down, the gun has no ammo anyway.\nBut this voilence shows you deserve to fail this level anyway.")
                Play.fail()
                Play.level5(username)
            else:
                choice = character_print(
                    'Please choose a valid option \n').lower()

    def level6():
        character_print('Level 6 coming soon!')

    def fail():
        choice = character_print('''
                        
DISCLAIMER: You are lucky you get the option to restart the level...
                        
1. Restart level
2. Restart whole game 
3. Menu
4. Exit \n \n ''')
        while True:
            if choice == '1':
                character_print('Restarting level...\n')
                break
            elif choice == '2':
                character_print('Restarting game...\n')
                Play.intro_to_game()
            elif choice == '3':
                MenuAndRelated.menu()
            elif choice == '4':
                character_print('Are you sure you want to exit? y/n')
                choice2 = input()
                if choice2 == 'y':
                    exit('Bye Bye')
                else:
                    continue
            else:
                choice = character_print('Please choose a valid option')

    def condition_fail(level):
        while True:
            character_print('''
    1. Restart level ''')
            sys.stdout.write(str(level))
            choice = character_print('''
    2. Restart whole game 
    3. Menu
    4. Exit \n \n ''')
            if choice == '1':
                character_print('Going back to level ')
                sys.stdout.write(str(level))
                character_print('... \n')
                break
            elif choice == '2':
                character_print('Restarting game...\n')
                Play.intro_to_game()
            elif choice == '3':
                MenuAndRelated.menu()
            elif choice == '4':
                choice2 = character_print('Are you sure you want to exit? y/n')
                if choice2 == 'y':
                    exit('Bye Bye')
                else:
                    continue
            else:
                choice = character_print('Please choose a valid option')

    def resume(username):
        path = '/workspaces/Prison-Escape/CSV Files/score.csv'
        df = pd.read_csv(path)
        level = df.loc[df['Username'] == username, 'Level']
        level = level.values[0]

        while True:
            character_print(
                '''\nWould you like to continue from where you left off?\nThat's level ''' + str(level))
            choice = character_print('y/n\n')
            if choice == 'y':
                character_print('Resuming from level ' + str(level))
                level_to_play = 'level'+str(level)
                getattr(Play.level_to_play)(username)
            elif choice == 'n':
                character_print(
                    '\nWould you like to restart? This will restart your score too? y/n')
                choice = input()
                if choice == 'y':
                    character_print('Restarting game... \n')
                    Play.intro_to_game()
                elif choice == 'n':
                    character_print('Returning to menu... \n')
                    MenuAndRelated.menu()
                else:
                    character_print('Please choose a valid option. ')
            else:
                character_print('Please choose a valid option. ')


class TextBasedImages:
    def hot_soup():
        print('''                                          
              @     @    @              
              @    @%    @              
              @%   @     @/             
                    &(                  
              ,/#@@@@@@&#/,             
   .@@#                           %@@   
  (@  @@@#                    .#@@& .@  
   @   /@@@@@@&#(*,,,,**(%&@@@@@@*   @  
   *@                               @   
    /@                             @    
      @                          ,@     
        @(                     @@       
           @@&@@@@@@@@@@@@@@@@          
                                   ''')

    def in_prison():
        character_print('''
 _________________________
      ||   ||     ||   ||
      ||   ||, , ,||   ||
      ||  (||/|/(\||/  ||
      ||  ||| _'_`|||  ||
      ||   || o o ||   ||
      ||  (||  - `||)  ||
      ||   ||  =  ||   ||
      ||   ||\___/||   ||
      ||___||) , (||___||
     /||---||-\_/-||---||\\
    / ||--_||_____||_--|| \\
   (_(||)-|Criminal |-(||)_)
 	''')

    def superman():
        character_print('''
            .=.,
            ;c =\\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \\
      /' _  [<_->] )  \\
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \\
      / | |   | \;  |  \ \\
     / /  | :/   \: \   \_\\
    /  |  /.'|   /: |    \ \\
    |  |  |--| . |--|     \_\\
    / _/   \ | : | /___--._) \\
   |_(---'-| >-'-| |       '-'
          /_/     \_\ ''')

    def police():
        character_print('''
              ,
     __  _.-"` `'-.
    /||\'._ __{}_(
    ||||  |'--.__\\
    |  L.(   ^_\^
    \ .-' |   _ |
    | |   )\___/
    |  \-'`:._]
    \__/;      '-.
                        ''')

    def cars():
        character_print('''
  ______
 /|_||_\`.__
(   _    _ _\\
=`-(_)--(_)-' ''')

    def mustache():
        character_print('''
⠀⢀⣠⣄⡀⠀⠀⠀⣠⣶⣾⣿⣿⣶⣦⣴⣾⣿⣿⣷⣦⣄⠀⠀⠀⢀⣠⣄⡀⠀
⣰⣿⠟⠛⢻⡆⣠⣾⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢰⠟⠛⢻⣿⡆
⢻⣿⣦⣀⣤⣾⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣦⣤⣀⣼⣿⡇
⠀⠛⠿⢿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⢿⣿⣿⡿⠿⠋⠀''')

# ----functions-------------------------------


def character_print(info):  # prints text one character at a time
    for char in info:  # this prints characters one by one to create a better ui
        sys.stdout.write(char)  # the sys module is used to do this
        sys.stdout.flush()
        time.sleep(0.010)
    return input()

# ----main program----------------------------


MenuAndRelated.menu()
