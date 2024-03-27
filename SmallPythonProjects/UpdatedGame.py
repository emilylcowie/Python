command = ""

start = False
stop = True

while True:
    command = input("> ")
    if command == 'help':
        print(''' 
start - to start the car
stop - to start the car
quit - to exit
speed - to control the speed (mph)
            ''')
    elif command == 'speed':
        if stop:
            print('you need to start your car')
        else:
            speed = int(input('what speed do you want the car to go at? '))
            if speed > 30:
                print('''
you're over the speed limit
the police are coming
you're in jail
''')
                choice = input('''
what do you choose to do? 

- do you choose to escape (a)
- do you try and make prisoner friends (b)
- do you do nothing and cry (c)
''')
                while choice:
                    if choice == 'a':
                        choice_2 = input('''
congrats you escaped, but you fell out a window.

what do you choose to do?

- use your parachute (a)
- plummet to your death (b)
- scream for help (c)
''')
                        while choice_2:
                            if choice_2 == 'a':
                                print('your parachute fails as your dog tore it. you die. you go back to the beginning')
                                break
                            elif choice_2 == 'b':
                                print('you obviously die. you have gone back to the beginning')
                                break
                            elif choice_2 == 'c':
                                choice_3 = input('''
someone miraculously runs out with a trampoline and catches you. you live.
you realise the person who saved you was a police officer and he chases you around the street

what do you choose to do?

- keep running (a)
- disguise yourself (b)
- go into somebody's house and hide (c)
''')
                                while choice_3:
                                    if choice_3 == 'a':
                                        print('he chases you down,he shoots you. you die. you go back to the beginning')
                                        break
                                    elif choice_3 == 'b':
                                        print('he does not fall for your tricks. you die. go back to the beginning')
                                        break
                                    elif choice_3 == 'c':
                                        choice_4 = input('''
he doesn't find you!
you decide to hang there for a while.
when you are about to leave, you see tons of police cars!

what do you choose to do?

- run out the back door (a)
- you go to sleep (b)
- you pretend they don't exist and watch tv
''')
                            else:
                                print('choose either a, b, or c.')

                    elif choice == 'b':
                        print('''
you annoyed a prisoner and got punched in the face, you die.
you have gone back to the beginning''')
                        break
                    elif choice == 'c':
                        print('''
you die of dehydration because of how many tears you lost. 
you have gone back to the beginning''')
                        break
                    else:
                        print('choose either a, b, or c. ')
            else:
                print('you are within the speed limit')
    elif command == 'start':
        if start:
            print('the car has already started')
        else:
            print('the car has started')
        start = True
        stop = False
    elif command == 'stop':
        if stop:
            print('car has already stopped')
        else:
            print('the car has stopped')
        stop = True
        start = False
    elif command == 'quit':
        break
    else:
        print('sorry, i did not understand that')
