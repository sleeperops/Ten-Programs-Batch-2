first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

try:
    first_input = int(first_input)
    second_input = int(second_input)
except:
    print('>>Not a number')
# ===============================================
def quotient_no_dec(input1, input2):
    return f'{input1//input2}'

print(f'quotient: {quotient_no_dec(first_input,second_input)}')