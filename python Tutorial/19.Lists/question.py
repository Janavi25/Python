# Write a program to find the largest number in a list

numbers = [1, 2, 3, 4, 5, 6, 7]

let_max = numbers[0]

for number in numbers:
    if number > let_max:
        let_max = number
print(let_max)
