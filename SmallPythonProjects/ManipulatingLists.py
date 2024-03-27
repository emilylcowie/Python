import random
names = ['Ruhma', 'Palak', 'Emily', 'Cassandra']

print('''
    1. Generate random name
    2. Add name
    3. Remove name
    4. Print names
    5. Quit program
    ''')
print(names)

while True:
    num = len(names) - 1
    rand = random.randint(0, num)
    choice = int(input('Choose a number: '))

    if choice == 2:
        new_name = input('What name do you want to add in? ')
        names.append(new_name)
        print('DONE!')
    elif choice == 1:
        print(names[rand])
    elif choice == 3:
        bin_name = input('What name do you want to remove? ')
        names.remove(bin_name)
    elif choice == 5:
        exit('bye bye')
    elif choice == 4:
        print(names)
    else:
        print('Sorry I do not understand :(')
