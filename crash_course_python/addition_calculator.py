def read_file(filename):

    try:
        with open(filename) as file:
            full_file = file.read()

    except:
        pass

    else:
        print(full_file + '\n')

    
filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    read_file(file)
