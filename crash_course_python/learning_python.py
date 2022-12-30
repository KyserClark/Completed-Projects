with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents + '\n')

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())
    print('\n')

learn_python = []
with open('learning_python.txt') as cool_text:
    for line in cool_text:
        learn_python.append(line)

for index in learn_python:
    print(index.strip())


