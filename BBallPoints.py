'''
Basketball Points Python Script:
This a python script that asks the user for their name.

After they put in their name, they will be asked for how
many 2-point shots and 3-point shots that they made.

After they have put in the number for their 2-point and 
3-point shots, the total amount of points will be displayed.

Also, input validation is being used (must enter a name
and cannot be blank; points must be integers).
'''

#Ask the user for their name
name = None
while not name:
    name = input('Hello there, what is your name? ')
    print('A name is needed!')
    
print('Welcome, ' + name + '. I will ask you two more questions.')

while True:
    try:
        #Ask the user how many 2-point shots they made.
        two_point = int(input('How many 2-point shots did you make? '))

        #Ask the user how many 3-point shots they made.
        three_point = int(input('How many 3-point shots did you make? '))

        #Display the total amount of points the user scored
        total_points = two_point * 2 + three_point * 3
        print(f'{name}, you scored {total_points} points.')
        break

    except:
        print('Whoops. It looks like you entered the wrong input (Integers only!). Let\'s try again.')
        print()


