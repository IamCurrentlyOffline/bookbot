def count_chars(text):
    counter = {}
    for char in text:
        char = char.lower()
        if char.isalpha():  # Only count alphabetic characters
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_char_count(char_dict):
    # Create a list of dictionaries from the char_dict
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    # Define a function to get the count for sorting
    def sort_on(dict):
        return dict["count"]

    # Sort the list by count (descending)
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
