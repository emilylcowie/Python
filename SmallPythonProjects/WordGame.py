# Using lists and random module to randomly generate compliments/insults

import random
insults = ["I'll beat thee, but I would infect my hands", "The tartness of his face sours ripe grapes.",
           'I am sick when I do look on thee', 'Thine face is not worth sunburning', '*bites thumb*',
           "Thou art as fat as butter."]
compliments = ['Thou art wise as thou art beautiful', 'An angel is like you, and you are like an angel',
               'You are true-penny and straight-fingered', 'Your virtues have so strangely taken up my thoughts',
               'The brightness of your cheek would shame those stars', "You're a rudderish"]

while True:
    num = random.randint(0, 5)
    choice = input("Choose an (I)nsult, a (C)ompliment or to exit: ")
    choice = choice.upper()

    if choice == 'C':
        print(compliments[num])
    elif choice == 'I':
        print(insults[num])
    elif choice == 'EXIT':
        break
    else:
        print('I do not understand')
