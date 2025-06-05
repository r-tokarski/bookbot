def get_book_text(book):
    with open(book) as b:
       return b.read()

def get_book_chars(book):
    alphabet = {}
    text = get_book_text(book)
    for char in text:
        lower_case = char.lower()
        if lower_case in alphabet:
            alphabet[lower_case] += 1
        else:
            alphabet[lower_case] = 1

    return alphabet

def sort_on(dict):
    return dict["num"]

def sort_chars(book):
    alphabet = get_book_chars(book)
    list = []
    result = ""
    for alpha_char in alphabet:
        if alpha_char.isalpha() == True:
            string_char = f"{alpha_char}"
            value_char = alphabet[alpha_char]
            alpha_char = {}
            alpha_char["char"] = string_char
            alpha_char["num"] = value_char
            list.append(alpha_char)
    list.sort(reverse=True, key=sort_on)
    for dict in list:
        result = result + f"{dict["char"]}: {dict["num"]}\n"
        if dict == list[-1]:
            result = result + f"============= END ==============="
    return result
