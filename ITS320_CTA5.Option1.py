# Name: Danny Caperton
# Assignment Name: CTA5 - Option #1: String Values in Reverse Order
# Assignment Instructions:
#   Write a Python function that will work on three strings. The function will return to the user a concatenation of the string values in reverse order. 
#   The function is to be called from the main program.
#   In the main program, prompt the user for the three strings and pass these values to the function.

input_strings = [] # A place to store the input strings
count = 3 # Sets the number of input strings

def reverse_string_order(string_1, string_2, string_3):
    return string_3 + string_2 + string_1

while count > 0: # Loops the number of count to prompt for user input
    input_strings.append(input('Enter a word: ')) # Prompts for a string
    count -= 1 # Decrements count

print(reverse_string_order(input_strings[0], input_strings[1], input_strings[2])) # Prints the return results from the function