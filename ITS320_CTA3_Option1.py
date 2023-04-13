# Name: Danny Caperton
# Assignment Name: CTA3 - Option #1: Creating a Program to Calculate the Value of a Ferrari
# Assignment Instructions:
#   Implement a program that reads in a year and outputs the approximate value of a Ferrari 250 GTO in that year. 
#   Use the following table that describes the estimated value of a GTO at different times since 1962.
#   Year      | Value
#   1962-1964 | $18,500
#   1965-1968 | $6,000
#   1969-1971 | $12,000
#   1972-1975 | $48,000
#   1976-1980 | $200,000
#   1981-1985 | $650,000
#   1986-2012 | $35,000,000
#   2013-2014 | $52,000,000

year = int(input('Enter the year of your Ferrari 250 GTO: ')) # The data type is an integer

if year >= 1962 and year <= 1964:
    print('The value of your car is $18,500.')
elif year >= 1965 and year <= 1968:
    print('The value of your car is $6,000.')
elif year >= 1969 and year <= 1971:
    print('The value of your car is $12,000.')
elif year >= 1972 and year <= 1975:
    print('The value of your car is $48,000.')
elif year >= 1976 and year <= 1980:
    print('The value of your car is $200,000.')
elif year >= 1981 and year <= 1985:
    print('The value of your car is $650,000.')
elif year >= 1986 and year <= 2012:
    print('The value of your car is $35,000,000.')
elif year >= 2013 and year <= 2014:
    print('The value of your car is $52,000,000.')
else:
    print('You have entered an invalid year. Please try again.') # This is the catch all so that invalid numbers are handled.