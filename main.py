path_to_file = 'books/frankenstein.txt'


def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    content = text.lower()
    r = {}
    for letter in content:
        if letter.isalpha():
            r[letter] = r.get(letter, 0) + 1
    r = dict(sorted(r.items(), key=lambda item: item[1], reverse=True))
    return r

def main():

    path_to_file = 'books/frankenstein.txt'

    file_contents = read_file(path_to_file)
    words_n = count_words(file_contents)
    letters_n = count_letters(file_contents)
    

    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{words_n} words found in the document")
    for i in letters_n:
        print(f"The '{i}' character was found {letters_n.get(i, 0)} times")

    print("--- End report ---")
if __name__ == "__main__":
    main()  