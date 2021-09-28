# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

a = int(input("Enter a number: "))

temp = str(a)

n1 = temp
n2 = temp + temp
n3 = temp+temp+temp

add = int(n1) + int(n2) + int(n3)
print(f"n+nn+nnn = {add}")
