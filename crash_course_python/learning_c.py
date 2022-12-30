with open('learning_python.txt') as text_file:
    old_text = text_file.read()
    new_text = old_text.replace('Python', 'C')

print(new_text)
