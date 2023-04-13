# Name: Danny Caperton
# Assignment Name: CTA2 - Option #2: Create a Python Application
# Assignment Instructions:
#   Develop a Python application that incorporates using appropriate data types and provides program output in a logical manner.  
#   Your program should prompt a user to enter a car brand, model, year, starting odometer reading, 
#       an ending odometer reading, and the estimated miles per gallon consumed by the vehicle. 
#   Store your data in a dictionary and print out the contents of the dictionary.

car_infomation = {} # Stores the user input

# Prompts for user input
car_infomation['car_brand'] = input('Enter the brand of the car: ')
car_infomation['car_model'] = input('Enter the model of the car: ')
car_infomation['car_year'] = int(input('Enter the year of car: '))
car_infomation['starting_odometer'] = int(input('Enter the starting odometer reading of the car (without commas): '))
car_infomation['ending_odometer'] = int(input('Enter the ending odometer reading of the car (without commas): '))
car_infomation['est_mpg'] = int(input('Enter the estimated miles per gallon of the car: '))

# Prints the results
print('')
print('The car brand you entered was:                 ', car_infomation['car_brand'])
print('The car model you entered was:                 ', car_infomation['car_model'])
print('The car year you entered was:                  ', car_infomation['car_year'])
print('The starting odometer reading you entered was: ', car_infomation['starting_odometer'])
print('The ending odometer reading you entered was:   ', car_infomation['ending_odometer'])
print('The estimated miles per gallon you entered was:', car_infomation['est_mpg'], end='\n\n')