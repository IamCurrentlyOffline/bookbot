def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents
        
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = len(text.split())
    print(f"Found {num_words} total words")
    
main()