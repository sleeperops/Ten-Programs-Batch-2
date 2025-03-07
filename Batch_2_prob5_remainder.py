first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

try:
    first_input = int(first_input)
    second_input = int(second_input)
except:
    print('>>Not a number')
# ===============================================

def remainder_r(input1,input2):
    return input1 % input2

print(f'remainder: {remainder_r(first_input, second_input)}')