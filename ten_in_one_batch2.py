def smaller_number(first_input, second_input):
    if first_input < second_input:
        return first_input
    elif second_input < first_input:
        return second_input
    else:
        return 'equal'

def not_equal(first_input, second_input):
    if first_input != second_input:
        return 'Not Equal'
    else:
        return 'Equal'

def difference(first_input, second_input):
    return first_input - second_input

def quotient_no_dec(first_input, second_input):
    return f'{first_input//second_input}'

def remainder_of(first_input,second_input):
    return first_input % second_input

def difference_ten_numbers():
    total = 0
    counter = 9  # countdown, for auxillary purposes
    first_input = int(input('Input the first number as the minuend (10): ')) # to divide the other numbers to
    for _ in range(9):
        number = int(input(f'Input the rest as a subtrahend ({counter}): '))
        total += number
        counter -= 1 # countdown, for auxillary purposes
    print(first_input - total)

def even_number_count():
    total_even = 0
    counter = 10  # countdown, for auxillary purposes
    for _ in range(10):
        number = int(input(f'Input a number ({counter}): '))
        if number % 2 == 0:
            total_even += 1      
        
        counter -= 1 # countdown, for auxillary purposes
    print(f'Answer: {total_even}')

def odd_numbers():
    counter = 0
    while counter != 100:
        counter += 1
        if counter % 2 == 1:
            print(counter, end = ' ')
def no_zero_and_five():
    for num in range(100):
        if num % 5 == 0 or num % 10 == 0:
            continue
        else:
            print(num, end = ' ')

def in_between():
    first_input = input('Enter the first number: ')
    second_input = input('Enter the second number: ')

    try:
        first_input = int(first_input)
        second_input = int(second_input)
    except:
        print('>>Not a number')
    # ===============================================

    if first_input < second_input: # if first input is smaller, make it as the minimum value
        floor_num = first_input
        ceiling_num = second_input
    elif first_input > second_input: # if first input is larger, make it as the maximum value
        ceiling_num = first_input
        floor_num = second_input
    else:
        floor_num = first_input
        ceiling_num = second_input    

    print(f'Numbers in between {floor_num} and {ceiling_num} are: ')
    for numbers_in_between in range(floor_num + 1, ceiling_num): # numbers between the first input and the second
        print(numbers_in_between, end = ' ')

# MAIN LOOP===================================================================================
# Function list-------------------------------------------------------------------------------
# > Seperated into two, with one containing the names of the function, the second one contains the function-
function_names = ['Prog 1: Print the smaller of 2 numbers',
                  'Prog 2: Check if 2 numbers are not equal',
                  'Prog 3: Difference of 2 Numbers:',
                  'Prog 4: Quotient of 2 Numbers without the decimal',
                  'Prog 5: Remainder of 2 numbers when divided',
                  'Prog 6: Ask for 10 numbers. Subtract the remaining 9 numbers to the first',
                  'Prog 7: Counts the amount of even numbers in a set of inputs',
                  'Prog 8: Prints all odd numbers from 0 - 100',
                  'Prog 9: Prints all numbers from 0 - 100 except those ending in 0 or 5',
                  'Program 10: Prints all the numbers in between 2 given numbers'] #( ! program(1-10) is (0-9) in index)

function_list = [smaller_number, not_equal, difference, quotient_no_dec,remainder_of,
                 difference_ten_numbers, even_number_count, odd_numbers, no_zero_and_five, in_between]

# Selection: part where the user selects a program to play------------------------------------
# Displays the function itself----
while True:
    for function in function_names:  # displays all the function
        print(function)
# Error handling------------------------------------------------------------------------------
    print('') # space
    user_input = input('Pick the number of the program of your choice (// to exit): ')
  
    # exits the program---
    if user_input == '//':
        break
      
    # check if input is a number --- 
    try:
        user_input = int(user_input)
    except:
        print('>>Not a number')
        continue
      
    # checks if the selected function is in range---
    if user_input > len(function_list) or user_input < 1:
        print('>>No such option')
        continue
# executes the selected function----------------------------------------------------------------
    user_input -= 1  # to deal with 0 base
    if user_input in range(0,5):  # for functions with special parameters ! index(0-5) is programs(1-5) (6 is excluded)
        try:
            first_input = int(input('Enter the first number: '))
            second_input = int(input('Enter the second number: '))
            
        except:
            print('>>Not numbers')
            continue
        print(f'Answer: {function_list[user_input](first_input, second_input)}')  # calls the function based on user input

    elif user_input in range(5,11):  # for functions with no special parameters ! index(5,11) is program(6-10) (11 is exluded)
        function_list[user_input]()  # calls the function without input from user

# exit / continue program-------------------------------------------------------------------------
    # exit / continue program
    to_continue = input("Continue? (any key or 'n' to exit): ")
    if to_continue.lower() == 'n':
        break
    else:
        continue


