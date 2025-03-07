''' Odd numbers from 0 - 100 using while loop'''

counter = 0
while counter != 100:
    counter += 1
    if counter % 2 == 1:
        print(counter, end = ' ')
    