first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

try:
    first_input = int(first_input)
    second_input = int(second_input)
except:
    print('>>Not a number')
 # ===============================================
 
def not_equal(input_1, input_2):
    if input_1 != input_2:
        return 'Not Equal'
    else:
        return 'equal'

print(not_equal(first_input, second_input))
