from time import sleep

print('''
Let's play Nim Sum with marbles!

There are 21 marbles. You can take any number of marbles between 1 and 3.

The player that takes the last marble loses.

------------------------------------------------

You start!
''')

marbles = 21
play = True
while play == True:
    print('''
    How many marbles do you choose?
    1, 2, or 3
    ''')
    choice = int(input('>>> '))
    if choice < 4 and choice > 0:
        marbles = marbles - choice
        if marbles > 0:
            print('You chose to take', choice, 'marbles. There is now', marbles, 'marbles')

            computer_choice = 4 - choice
            print()
            sleep(1)
            marbles = marbles - computer_choice
            print('The computer takes away', computer_choice, 'marbles. There is now', marbles, 'marbles')
        else:
            print('You took the rest of the marbles')
            print('You lose')
            play = False
    elif choice >= 4:
        print('You can not pick more than 3 marbles')
        print('-'*16)
    else:
        print('You can not pick less than 1 marbles')
        print('-'*16)
