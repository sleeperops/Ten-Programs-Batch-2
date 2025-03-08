first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

try:
    first_input = int(first_input)
    second_input = int(second_input)
except:
    print('>>Not a number')
 # ===============================================
 
def smaller_number(first_num, second_num):
    if first_num < second_num:
        return first_num
    elif second_num < first_num:
        return second_num
    else:
        return 'equal'

print(smaller_number(first_input, second_input))
