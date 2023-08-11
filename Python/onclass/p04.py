with open("example.txt", 'r') as file:
    with open("output.txt", 'w') as output:
        while line := file.readline():
            content = line.replace(" ", "")
            output.write(content)
file.close()
output.close()