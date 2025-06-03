def get_book_text(book):
    with open(book) as b:
       return b.read()

def main():
    path = "books/frankenstein.txt"
    print(get_book_text(path))

main()
