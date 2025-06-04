def get_book_text(book):
    with open(book) as b:
       return b.read()
