# Name: Danny Caperton
# Assignment Name: CTA1 - Option #2: Create a Python Application
# Assignment Instructions:
#   Read two integers and print two lines. The first line should contain integer division, //, 
#       the second line should contain float division, /, and 
#       the third line should contain modulo division, %. 
#   You do not need to perform any rounding or formatting operations.
#   Input Format The first line contains the first integer. The second line contains the second integer.
#   Output Format Print the three lines as described above.
#   Sample Input43
#   Sample Output11.33333333333333331

num1 = int(input('Enter the first number: ')) # Prompts for input
num2 = int(input('Enter the second number: ')) # Prompts for input

print(num1 // num2) # Integer division
print(num1 / num2) # Float division
print(num1 % num2) # Modulo division