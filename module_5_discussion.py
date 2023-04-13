def calculations(num1, num2, operation): # Defines a function with 3 inputs
    '''Takes two numbers and either adds, subtracts, multiplies or divides them.
    Valid operation values are add, sub, mult, div'''

    if operation.lower() == 'add': # Converts the case of the input and compares it to the string
        return num1 + num2 # Returns the result of appropriate math operation 
    elif operation.lower() == 'sub':
        return num1 - num2
    elif operation.lower() == 'mult':
        return num1 * num2
    elif operation.lower() == 'div':
        return num1 / num2
    else: # Catches invalid operation parameters
        return "Invalid operation value. Use 'add', 'sub', 'mult', 'div'" # Returns help information

answer = calculations(1, 2, 'add') # Instantiates the function and assigns the return value to the variable
print(answer) # Prints the variable containing the return value
answer = calculations(1, 2, 'sub')
print(answer)
answer = calculations(1, 2, 'mult')
print(answer)
answer = calculations(1, 2, 'div')
print(answer)
answer = calculations(1, 2, 'sqrt') # Tests the invalid parameter
print(answer)

