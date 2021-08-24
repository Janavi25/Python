course = "Python's for beginners"
print(course)

course_1 = 'Python for "beginners"'
print(course_1)

course_2 = '''
 Hi John,

 here is our first email to you.

 Thank you,
 The support team

 '''
print(course_2)

course_3 = 'python for beginners'

print(course_3[0])

# if we pass negative ...its the index of the last character
print(course_3[-1])

# if we pass 0:3 python interpretor will pass all the charaxters starting from the start index to second index (ie. index 0 - index 3) but exclude the character at index 3.
print(course_3[0:3])

# if we pass 1: python interpretor will pass all the characters starting from the  index 1 but exclude the character at index 1.
print(course_3[1:])

another = course_3[:]
print(another)  # this will clone the course_3

name = 'janavi'
print(name[1:-1])
