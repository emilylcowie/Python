from random import randint
answer = 'yes'

while answer.lower() == 'yes':

    t = ['rock', 'paper', 'scissors']
    computer = t[randint(0, 2)]

    player = input('Rock, Paper or Scissors ')

    if computer == player:
        print(computer)
        print('Draw!')
        answer = input('Would you like to play again? ')

    elif computer == 'rock':
        if player == 'paper':
            print(computer)
            print('You win!')
            print('Paper beats rock! ')
            answer = input('Would you like to play again? ')
        else:
            print(computer)
            print(computer)
            print('You lose!')
            print('rock beats scissors')
            answer = input('Would you like to play again? ')

    elif computer == 'paper':
        if player == 'rock':
            print(computer)
            print('You lose!')
            print('Paper beats rock!')
            answer = input('Would you like to play again? ')
        else:
            print(computer)
            print('You win!')
            print('Scissors cut paper!')
            answer = input('Would you like to play again? ')

    elif computer == 'scissors':
        if player == 'rock':
            print(computer)
            print('You win!')
            print('rock beats scissors!')
            answer = input('Would you like to play again? ')
        else:
            print('You lose!')
            print(computer)
            print('Scissors beats paper!')
            answer = input('Would you like to play again? ')

    else:
        print('Your spelling seems incorrect, try again.')
