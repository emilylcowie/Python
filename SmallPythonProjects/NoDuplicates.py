# code to output a list without any duplicates
numbers = [1, 4, 678, 4, 945, 1009, 1, 5, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
