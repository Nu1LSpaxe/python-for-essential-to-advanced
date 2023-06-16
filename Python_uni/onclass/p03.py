with open("example.txt", 'r') as file:
    output = open("output.txt", 'w')
    while line := file.readline():
        content = line.replace(" ", "")
        output.write(content)
output.close()