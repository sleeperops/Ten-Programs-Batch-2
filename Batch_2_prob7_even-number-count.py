def even_number_count():
    total_even = 0
    counter = 10  # countdown, for auxillary purposes
    for _ in range(10):
        number = int(input(f'Input a number ({counter}): '))
        if number % 2 == 0:
            total_even += 1      
        
        counter -= 1 # countdown, for auxillary purposes
    return total_even


print(f'Total number of even numbers: {even_number_count()}')