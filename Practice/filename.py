# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print(f"The file Extension is: {repr(f_extns[-1])}")
