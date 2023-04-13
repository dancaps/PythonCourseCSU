# Name: Danny Caperton
# Assignment Name: Portfolio Project - Option #2: Home Inventory Program
# Assignment Instructions:
# Final program:
#     Create a home inventory class that will be used by a National Builder to maintain inventory of available houses in the country.  
#     The following attributes should be present in your home class:
#     private int squarefeet
#     private string address
#     private string city
#     private string state
#     private int zipcode
#     private string Modelname
#     private string salestatus (sold, available, under contract)
# Your program should have appropriate methods such as:
#     constructor
#     add a new home
#     remove a home
#     update home attributes
#     At the end of your program, be sure that it allows the user to output all home inventory to a text file.
#     Be sure that your final program includes your source code and screenshots of the application, executing the application, 
#       and the results.


import home_functions


# The main function
def main():
    # Runs the home application
    homes = []

    print('\nWelcome to the home inventory application\n')
    print('-' * 50)

    while True:
        # Maintains a running program until the user is done working in it 
        print('\nDo you want to add a new home? [a]')
        print('Do you want to remove an existing home? [r]')
        print('Do you want to update values on an existing home? [u]')
        print('Download a file of all the houses. [d]')
        print('Show homes in the system. [s]')
        print('Quit the program. [q]')
        user_selection = input('\nEnter your selection: ')

        # Based on user input this section tells main what to run
        # [a] - Calls the add new home functions, which actually creates a new object so that it can be appended to the homes list
        if user_selection.lower() == 'a':
            new_home = home_functions.add_home()
            if new_home == None:
                continue
            else:
                homes.append(new_home)

        # [r] - Calls the remove home function and passes the homes list.
        # Reassigns the return list to the homes variable
        elif user_selection.lower() == 'r':
            homes = home_functions.remove_home(homes)

        # [u] - Calls the update home function and passes the homes list.
        # Reassigns the return list to the homes variable
        elif user_selection.lower() == 'u':
            homes = home_functions.update_home(homes)

        # [d] - Creates a local file and prints each home object to it
        elif user_selection.lower() == 'd':
            f = open('Homes_Application_Download.txt', 'w')
            for h in homes:
                f.write(str(h))
            f.close()
            print('The data has been downloaded to a file named Homes_Application_Download.txt on your local drive.')
        
        # [s] - Shows the current contents of the home list
        elif user_selection.lower() == 's':
            print('\nHere is a list of homes currently in the system:')
            for h in homes:
                print(h)
        
        # [q] - Allows the user to quit the program when they are finished
        elif user_selection.lower() == 'q':
            print('Thank you for using the program. Goodbye.\n')
            break

        # Catches invalid input from the user
        else:
            print('You have entered an incorrect option. Please try again.')


# Using the special variable to call the main function
if __name__ == "__main__":
    main()