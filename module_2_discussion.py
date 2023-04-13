'''
Suppose you are building a Python application for storing the names, birthdates, and addresses of members of an extended family. 
Describe the strategy that you would use in order to determine the data types you would need for your application. 
Provide four data elements and the corresponding data types that you would use in your application.
Provide a rationale for your response and provide constructive feedback on strategies and rationales posted by your peers. 
Provide at least one reference to support your findings.
'''
import datetime

extented_family = {} # This is a dictionary and the database of information.

name = str(input('Enter a name: '))
print('The name you entered is', name)

birthday = int(input('Enter the birthday of ' + name +' in the proper month_day_year format. Example is 02271992: '))
print('The birthday you entered is', birthday)

street_address = str(input('Enter the street address of ' + name +' in the proper format. Example is 123 Main St.: '))
print('The street you entered is', street_address)

city = str(input('Enter the city of ' + name +' : '))
print('The city you entered is', city)

state = str(input('Enter the state of ' + name +' in the proper 2 digit abbreviated format. Example is CO for Colorado: '))
print('The street you entered is', street_address)

zip_code = str(input('Enter your 5 digit zip code. Example is 80924:'))
print('The zip code you entered is ' + '{:05}'.format(int(zip_code)))

