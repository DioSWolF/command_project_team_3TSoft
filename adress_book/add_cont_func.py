from Class import Record, AdressBook, Name, Phone, Birthday, Email, ArdessLive, Notes, Iterable


def add_contact(book:AdressBook):
    name_cont = input("\n>>> 0 to enter the menu.\nWrite contact name: ").strip()

    if name_cont == "0":
        return 

    if name_cont in book:
        return "\nYou have a contact with this name! Choose another name."

    name_cont = Name(name_cont)
    rec = Record(name_cont)
    
    book.add_record(rec)

    return write_in_field(book, rec)

def write_in_field(book:AdressBook, rec: Record):
    user_chose = ""

    while user_chose not in STOP_WORD:
        rec_list_print =  f"Phones: {', '.join(rec.phone)}", f"Email: {', '.join(rec.email)}", f"Adress: {'; '.join(rec.ardess_live)}", \
                            f"Birthday date: {rec.birthday}", f"Notes: {'; '.join(rec.notes)}"
        list_fiel_text = f"\nContact name: {rec.name.value}\n\nAdd to field:\n"
        
        i = 1
        for items in rec_list_print:
            list_fiel_text += f"{i}: {items}\n"
            i += 1

        list_fiel_text += f"\n>>> 0: Exit to main menu\n"

        print(list_fiel_text)

        user_chose = input("Select the field number to fill in: ").strip()
        user_chose = ADD_FUNC_DICT.get(str(user_chose), error_chose)
        user_chose = user_chose(rec)
        print(user_chose)
        book.add_record(rec)


def write_phone_field(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\nWrite phone number: ").strip()

    if user_input == "0":
        return 

    user_input = user_input.split(" ")

    if rec.phone == "":
        rec.phone = [Phone(ph).value for ph in user_input]
    else:
        rec.phone.extend([Phone(ph).value for ph in user_input])

def write_email_field(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\nWrite email number: ").strip()

    if user_input == "0":
        return

    if rec.email == "":
        rec.email = [Email(user_input).value]
    else:
        rec.email.append(Email(user_input).value)

def write_ardess_field(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\nWrite adress: ").strip()

    if user_input == "0":
        return

    if rec.ardess_live == "":

        rec.ardess_live = [ArdessLive(user_input).value]
    else:
        rec.ardess_live.append(ArdessLive(user_input).value)

def write_birthday_field(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\nWrite birthday: ").strip()

    if user_input == "0":
        return

    if rec.birthday == "":
        rec.birthday = Birthday(user_input).value.strftime('%d.%m.%Y')

def write_notes_field(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\nWrite notes: ").strip()

    if user_input == "0":
        return

    if rec.notes == "":

        rec.notes = [Notes(user_input).value]
    else:
        rec.notes.append(Notes(user_input).value)

def close_bot(*_):
    return "exit"

STOP_WORD = ("stop", "exit", "good bye")

ADD_FUNC_DICT = {   "0" : close_bot,
                    "1" : write_phone_field, 
                    "2" : write_email_field,
                    "3" : write_ardess_field,
                    "4" : write_birthday_field,
                    "5" : write_notes_field,
                }

def error_chose(*_):
    return "\n<<<You chose invalid. Try again>>>"