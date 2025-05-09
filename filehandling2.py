with open("Sample.txt", "a") as file:
	content = file.read()
words = content.split()
for word in words:
	print(word)
import os
if os.path.exists("My_File.txt"):
	print("File exists")
else:
    print("File does not exist")
    