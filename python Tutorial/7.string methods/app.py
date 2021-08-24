course = 'Python for Begineers'
print(len(course))

print(course.upper())
print(course.capitalize())
print(course)
print(course.lower())

# find method is case sensetive soo if i type lower p here it will give -1
print(course.find('P'))
print(course.find('o'))
print(course.find('Begineers'))

print(course.replace('Begineers', 'Absolute Begineers'))

print('Python' in course)
print('python' in course)

print(course.title())
