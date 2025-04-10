def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    counter = {}
    for char in text:
        char = char.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    
    return counter