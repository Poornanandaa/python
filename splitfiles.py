with open('Sample.txt', 'w') as f:
    f.write("Hi, I am Penguin and I am 10 yrs old.")
f.close()
with open('Sample.txt', 'r') as f:
    g = f.readlines()
    print(g)
    for i in g:
        j = i.split()
        print(j)
f.close()        

     