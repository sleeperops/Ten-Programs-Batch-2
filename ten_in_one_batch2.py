
# MAIN LOOP===================================================================================
# Function list-------------------------------------------------------------------------------
# > Seperated into two, with one containing the names of the function, the second one contains the function-
function_names = ['Prog 1: Print the smaller of 2 numbers',
                  'Prog 2: Check if 2 numbers are not equal',
                  'Prog 3: Difference of 2 Numbers:',
                  'Prog 4: Quotient of 2 Numbers without the decimal',
                  'Prog 5: Quotient of 2 Numbers',
                  'Prog 6: First Number raised to the Second',
                  'Prog 7: Summation of 10 Numbers',
                  'Prog 8: Odd number counter',
                  'Prog 9: All even numbers from 0 - 100',
                  'Program 10: All numbers from 0-100 except those ending in zero']

function_list = [greater_number, compare_ab, sum_ab, product_ab, quotient_ab, exponent_ab, summate, odd_numbers,
                 all_even, no_zero]

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


