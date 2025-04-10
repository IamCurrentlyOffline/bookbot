import sys
from stats import get_num_words, count_chars, sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    num_words = get_num_words(book_text)

    # Get character counts and sort them
    char_counts = count_chars(book_text)
    sorted_chars = sort_char_count(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")

    print("============= END ===============")


main()

# define multiple things to get proper readabiltiy and function
