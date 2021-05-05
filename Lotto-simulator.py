import random

numbers = []
n = 1
while n < 7:
    """Get 6 different numbers between 1 and 49.
    
    Try until user give all proper number.

    :rtype: int
    :given list with 6 numbers provide by user
    """
    try:
        numbers.append(input("Enter " + str(n) + " number: "))
        numbers[-1] = int(numbers[-1])
    except ValueError:
        print("It is not an integer")
        numbers.pop()
        continue
    n += 1
    if 50 > numbers[-1] > 0:
        pass
    else:
        print("The number is not in the range 1-49")
        numbers.pop()
        n -= 1
    for i in numbers[:-1]:
        if numbers[-1] == i:
            print("You have already given this number")
            numbers.pop()
            n -= 1
            break
        else:
            pass
"""Print given numbers with ascending order.

:param list numbers: list of numbers
"""
numbers.sort()
print("Your numbers are: ", ', '.join([str(i) for i in numbers]))
"""Chose 6 random numbers.

:rtype: list
:list with 6 random numbers
"""
lotto = list(range(1, 50))
random.shuffle(lotto)
lotto = lotto[0:6]
lotto.sort()
print("Lotto numbers are: ", ', '.join([str(i) for i in lotto]))
"""Main function of program."""
count = 0
for i in numbers:
    if i in lotto:
        count += 1

print("You hit ", str(count), " numbers")
