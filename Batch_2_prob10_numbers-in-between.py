'''Numbers in between two numbers'''

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