import home_class


def add_home():
    # Creates and returns a new home object
    try:
        home_id = int(input('Enter the ID for the home: '))
        address = str(input('Enter the street address: '))
        city = str(input('Enter the city: ' ))
        state = str(input('Enter the state: '))
        zip_code = int(input('Enter the zip code: '))
        model_name = str(input('Enter the model of the home: '))
        sqft = int(input('Enter the sqft of the home: '))
        status = str(input('Enter the current status (Sold, Available, Under Contract): '))
    except ValueError:
        print('\nThere was a problem with the type of data you entered. Please try again.')
        return None
    
    # Creats a new home object and returns it to main
    new_home = home_class.Home(home_id, address, city, state, zip_code, model_name, sqft, status)
    print('\nThe new home has been created. Verify the details by selecting the [s] option.')
    return new_home


def remove_home(homes):
    # Prompts the user for the existing home ID
    # Validates the data type
    # Searches a copy of the home list and removed the object if it's found
    new_list_of_homes = list(homes)
    try:
        remove_home_id = int(input('Enter the ID of the home you wish to remove: '))
    except ValueError:
        print('\nThere was a problem with the ID you entered. Please start over.')
        return new_list_of_homes

    for i in new_list_of_homes:
        if i.home_id == remove_home_id:
            new_list_of_homes.remove(i)
            print('The home with ID: %s has been removed from the system.' % (remove_home_id))
    
    # Returns the modied homes list
    return new_list_of_homes


def update_home(homes):
    # Updates the attributes of on any home object passed to the function
    # Returns an updated list of home objects
    new_list_of_homes = list(homes)
    attribute_legend = {1: 'home_id', 2: 'address', 3: 'city', 4: 'state', 
                        5: 'zip_code', 6: 'model_name', 7: 'sqft', 8: 'status'}
    home_exists = False

    # This section gets the ID from the user
    # Throws an error if the user input is not an integer
    # Changes the home exists flag if the id is found
    # Tells the user they entered the an invalid ID if it's not found
    try:
        update_home_id = int(input('Enter the ID of the home you wish to update: '))
    except ValueError:
        print('\nThere was a problem with the ID you entered. Please start over.')
        return new_list_of_homes
    for i in new_list_of_homes:
        if i.home_id == update_home_id:
            home_exists = True
    if home_exists == False:
        print('\nThere is no home with that ID in the system. Please start again.')
        return new_list_of_homes

    # This section asks the user to input a number associated with the attribute they want to change
    # Throws an error if it's not an integer
    # Checks to see if the integer is a valid attribute number
    print('\nHere is a list of attributes that can be changed')
    print('[1] Home ID\n[2] Address\n[3] City\n[4] State\n[5] Zip Code\n[6] Model Name\n[7] SQFT\n[8] Status')
    try:
        update_attribute = int(input('Enter the number for the attribute you wish to update: '))
    except ValueError:
        print('\nThere was a problem with the type of data you entered. Please start over.')
        return new_list_of_homes
    if update_attribute < 1 or update_attribute > 8:
        print('\nYou entered an incorrect attribute number. Please start over.')
        return new_list_of_homes

    # If the attribute is an integer then it prompts the user and throws an error if they supply the wrong type
    if update_attribute == 1 or update_attribute == 5 or update_attribute == 7:
        try:
            attribute_change = int(input('Enter the new value you want for the attribute: '))
        except ValueError:
            print('\nThere was a problem with the type of data you entered. Please start over.')
            return new_list_of_homes
    else:
        attribute_change = input('Enter the new value you want for the attribute: ')

    # Searches for the object with the matching ID and sends a dictionary with the update value
    for i in new_list_of_homes:
        if i.home_id == update_home_id:
            i.update({attribute_legend[update_attribute]:attribute_change})

    print('The home with ID: %s has been updated in the system.' % (update_home_id))
    return new_list_of_homes
