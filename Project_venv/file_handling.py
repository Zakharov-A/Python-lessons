import os

# with open('myfile.txt', 'a', encoding='utf-8') as myfile:
#     myfile.write("\nHi girls!")

# with open('myfile.txt', 'w', encoding='utf-8') as myfile:
#     myfile.write("Hi boys!")  

# with open('myfile.txt', 'r', encoding='utf-8') as myfile:
#     content = myfile.read()
#     print(content)

with open('abs.txt', 'r', encoding='utf-8') as myfile:
    for line in myfile:
        # line = line.upper()
        line = line.replace("\n", "")
        print(line)


os.rename("abs.txt", "myfile.txt")

