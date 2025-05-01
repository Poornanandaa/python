file = open('Sample_File.txt', 'r')
first_ten_lines = file.readlines(10)
print(first_ten_lines)
first_line = file.readline()
print(first_line)
for i in range(4):
    line = file.readline()
    print(line.strip())
for line in file:
    print(line.strip())
file.close()
