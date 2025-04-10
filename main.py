def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

def count_words(text):
    words = text.split()
    return len(words)

main()

# define multiple things to get proper readabiltiy and function