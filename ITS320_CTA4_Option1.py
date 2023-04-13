#Option #1: Repetition Control Structure - Five Floating Point Numbers

from time import sleep # Imported sleep from time

user_input = [] # List to hold the entered values
count = 5 # Counter for the while loop

print('\nYou are required to enter 5 numbers.\n') # Instructions to the user

while count > 0: # Checks the count to see how many enteries are left to enter
    user_input.append(float(input('Enter any number: '))) # Converts the user input to a fload and adds the value to the list
    count -= 1 # Decrements the count number so we don't have an infinite loop situation
    if count > 0: # This tells the user how many enteries they have left
        print('You have', count, 'entries remaining.\n') # Prints information for the user
    else: # Allows the program to skip telling the user the have 0 entries left to enter 
        print('\nCalculating data...\n') # Prints user information
        sleep(2) # Used sleep for dramatic effect

print('\nThe following values have been calculated:\n') # Prints users information
print('The sum total of values you entered is:  ', sum(user_input)) # The sum method is used for this calculation
print('The average of values you entered is:    ', sum(user_input) / len(user_input)) # The sum and len methods are used to find the average
print('The maximum value you entered is:        ', max(user_input)) # The max method is used to find the maximum value entered
print('The minimum value you entered is:        ', min(user_input)) # The min method is used to find the minimum value entered

print('The values with a 20% interest increase:') # Prints information for the user
for i in user_input: # Iterates through the list of user entered values
    print('                                         ', i * 1.2) # Prints the value with a 20% increase. I hope it's not a problem that
                                                                # I modified the formula from the instructions. I like this one better.
print('') # Prints a newline for formatting purposes