def count_the(book, word):
    with open(book, 'r', encoding='utf-8') as file:
        read_file = file.read()
        result = read_file.lower().count(word)
    print(f"'{word}' appears {result} times in {book}\n")

book_list = [
    'A Christmas Carol in Prose; Being a Ghost Story of Christmas.txt',
    'Frankenstein.txt',
    'Pride and Prejudice.txt',
    ]

for book in book_list:
    count_the(book,'the ')




        