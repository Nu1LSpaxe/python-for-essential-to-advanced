file = open("example.txt", 'r')
output = open("output.txt", 'w')
line = file.readline()

while line:
    content = line.replace(" ", "")
    output.write(content)
    line = file.readline()
file.close()
output.close()