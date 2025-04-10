from stats import get_num_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    char_counts = count_chars(book_text)

    for char, count in char_counts.items():
        print(f"'{char}': {count}")

main()

# define multiple things to get proper readabiltiy and function