x = "is"
y = "my"
z = "name"
c = y + x + z
print(c)
d = y + " " + x + " " + z
print(d)
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

text1 = "my name is {}".format(fname)
print(text1)