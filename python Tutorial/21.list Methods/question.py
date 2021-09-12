# Write a program to remove the duplicates in a list

numbers = [1, 2, 2, 3, 4, 5, 6]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
