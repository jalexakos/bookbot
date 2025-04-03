import sys
from stats import num_words_in_str, count_chars, sort_dict

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    count = num_words_in_str(book)
    chars = count_chars(book)
    sorted_chars = sort_dict(chars)

    # Found 75767 total words
    print(f"Found {count} total words")
    print(chars)
    print(sorted_chars)
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")


main()
# './books/frankenstein.txt'
