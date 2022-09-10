from Class import AdressBook, Iterable


def show_all(book:AdressBook):
    Iterable(book)
    print_cont = "\n"
    
    for _ in book:
        pass

    i = 1 
    for items in book:
        key_name, value = items
        print_cont += "".join(f"{i}) {value}") + "\n"
        i += 1
    
    print(print_cont)

def show(book:AdressBook):
    user_end_index = int(input("\n>>> 0: To enter the contact menu.\n\nHow many contacts do you want to show: ").strip())
    i = 1

    while user_end_index != 0:
        Iterable(book, user_end_index)
        print_cont = "\n"

        if len(book) < i:
            i = 1

        for items in book:
            key_name, value = items
            print_cont += "".join(f"{i}) {value}") + "\n"
            i += 1

        print(print_cont)
        user_end_index = int(input(">>> 0: To enter the contact menu.\n\nHow many contacts do you want to show: ").strip())

    Iterable(book)
    for _ in book:
        pass

def find(book:AdressBook):

    find_cont = input("\n>>> 0: To enter the contact menu.\n\nWrite the text to search in the contact book: ").strip()
    
    while find_cont != "0":
        Iterable(book)
        find_contacts = "\n"
        
        for _ in book:
            pass

        i = 1
        for items in book:
            key_name, value = items
            if find_cont in value:
                find_contacts += "".join(f"{i}) {value}") + "\n"
                i += 1

        if find_contacts == "\n":
            print("\nCan't find anything.\n")
        else:
            print(find_contacts)

        find_cont = input(">>> 0: To enter the contact menu.\n\nWrite the text to search in the contact book: ").strip()