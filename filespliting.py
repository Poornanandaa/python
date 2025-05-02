file = open("Sample.txt", "x") 
file.close()
import os
if os.path.exists("Codingal.txt"):
    os.remove("Codingal.txt")
else: 
    print("The file does not exist")    
file = open("Codingal.txt", "w") 
file.write("Hi, I am a Poornanand and I am 12 yrs old.")
file.close()


