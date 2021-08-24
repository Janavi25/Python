# if name is less than 3 character long
#    name must be at least 3 characters
# otherwise if it's not more than 10 characters long
#    name can be a maximum of 10 characters
# otherwise
#    name looks good

name = input("Enter your Name: ")

if len(name) < 3:
    print(' name must be at least 3 characters')
elif len(name) > 10:
    print('name must be a maximum of 10 characters')
else:
    print('name looks good')
