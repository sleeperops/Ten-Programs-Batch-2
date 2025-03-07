'''Numbers from 0 - 100 not ending in 5 or 0'''

for num in range(100):
    if num % 5 == 0 or num % 10 == 0:
        continue
    else:
        print(num, end = ' ')