
# MAIN LOOP===================================================================================
# Function list-------------------------------------------------------------------------------


# Selection: part where the user selects a program to play------------------------------------
while True:
    for function in function_dict:  # displays all the function
        print(function)
    # function selection
    print('')
    user_input = input('Pick the number of the program of your choice (// to exit): ')
    if user_input == '//':  # exit program
        break
    try:
        user_input = int(user_input)
    except:
        print('>>Not a number')
        continue
#----------------------------------------------------------------------------------------------
    user_input -= 1  # to deal with 0 base
    if user_input >= 0 and user_input < 6:  # for functions with special parameters
        first_input = input('Enter the first number: ')
        second_input = input('Enter the second number: ')
        try:
            first_input = int(input('Enter the first number: '))
            second_input = int(input('Enter the second number: '))
            
        except:
            print('>>Not numbers')
            continue
        print(f'Answer: {function_list[user_input](input_a, input_b)}')  # calls the function based on user input

    elif user_input > 5 and user_input <= 10:  # for functions with no special parameters
        function_list[user_input]()  # calls the function based on user input

    else: # error in input
        print('>>Out of index')
#---------------------------------------------------------------------------------------
    # exit / continue program
    to_continue = input("Continue? (any key or 'n' to exit): ")
    if to_continue.lower() == 'n':
        break
    else:
        continue


