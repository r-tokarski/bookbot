def get_book_text(book):
    with open(book) as b:
       return b.read()

def main():
    path = "books/frankenstein.txt"
    words = get_book_text(path).split()
    words_int = len(words)
    print(f"{words_int} words found in the document")

main()
