from stats import *

def main():
    path = "books/frankenstein.txt"

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
