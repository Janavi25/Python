def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("enter a no you want to fact of that:"))
print(fact(n))