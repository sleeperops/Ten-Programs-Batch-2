def difference_ten_numbers():
    total = 0
    counter = 9  # countdown, for auxillary purposes
    first_number = int(input('Input the first number as the minuend (10): ')) # to divide the other numbers to
    for _ in range(9):
        number = int(input(f'Input the rest as a subtrahend ({counter}): '))
        total += number
        counter -= 1 # countdown, for auxillary purposes
    return first_number - total
    
print(f'The first number minus the rest: {difference_ten_numbers()}')