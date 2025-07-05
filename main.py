import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    words = get_book_text(path).split()
    words_int = len(words)

    chars = get_book_chars(path)
    char_list = sort_chars(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_int} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ==============")

main()
