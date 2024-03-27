# code to output the largest number in a list
numbers = (5, 3, 6, 100, 3, 9, 10)
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
