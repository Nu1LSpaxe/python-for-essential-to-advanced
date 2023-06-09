with open("example.txt", 'r') as file:
    with open("output.txt", 'w') as output:
        line = file.readline()

        while line:
            content = line.replace(" ", "")
            output.write(content)
            line = file.readline()
file.close()
output.close()