from operator import attrgetter
from tkinter import *
from .add_change_window import createNewWindow, start_read_notes
from .class_notes import NotesSave


#********************************** FIND BY TEXT ********************************


def find_by_article():
    name = find_article.get(1.0, END+"-1c")
    notes_list = []
    a = ""

    for note in notes_save.values():
        if name in note.article.value:
            notes_list.append(f'{("").join(note.article.value)}\n ' )
    i = 1
    for item in notes_list:
        a += f"> " + "".join(item)
        i += 1
    text.configure(state="normal")
    text.delete("0.1", END)
    text.insert("1.0", a)
   
    return  text.configure(state='disabled')

def finde_by_text_note():
    name = find_article.get(1.0, END+"-1c")
    notes_list = []
    a = ""
    for note in notes_save.values():
        if name in note.text_note.value:
            notes_list.append(f'{("").join(note.article.value)} \n' )
    i = 1
    for item in notes_list:
        a += f"> " + "".join(item)
        i += 1
    text.configure(state="normal")
    text.delete("0.1", END)
    text.insert("1.0", a)
    return  text.configure(state='disabled')

def finde_by_key_words():
    name = find_article.get(1.0, END+"-1c").strip().split(" ")
    notes_list = []
    a = ""
    
    for note in notes_save.values():
        for tags in name:
            if tags in note.key_words.value:
                notes_list.append(f'{("").join(note.article.value)} \n' )
    i = 1
    for item in notes_list:
        a += f"> " + "".join(item)
        i += 1
    text.configure(state="normal")
    text.delete("0.1", END)
    text.insert("1.0", a)
    return  text.configure(state='disabled')

def show_all():
    notes_list = []
    a = ""
    for note in notes_save.values():
        notes_list.append(f'{("").join(note.article.value)}' )
        i = 1
    for item in notes_list:
        a += "".join(item)
        i += 1
    text.configure(state="normal")
    text.delete("0.1", END)
    text.insert("1.0", "\n".join(notes_list))
    return  text.configure(state='disabled')

 
#************************************* SORTER FUNCTIONS **************************************

clic_alfavit = 0
def sort_click_alfavit():
    global clic_alfavit
    if clic_alfavit == 1:
        sorted_alfavit(reverse=True)
        clic_alfavit = 0
    else:
        sorted_alfavit(reverse=False)
        clic_alfavit += 1

def sorted_alfavit(reverse):
    name = text.get(1.0, END+"-1c").strip().split("\n")
    sorted_list = sorted(name, reverse=reverse)

    text.configure(state="normal")
    text.delete("0.1", END)
    text.insert("1.0", "\n".join(sorted_list))
    return  text.configure(state='disabled')


clic_date = 0
def sort_click_date():
    global clic_alfavit
    if clic_alfavit == 1:
        sorted_by_date(reverse=True)
        clic_alfavit = 0
    else:
        sorted_by_date(reverse=False)
        clic_alfavit += 1

def sorted_by_date(reverse):
    name_article = text.get(1.0, END+"-1c").strip().split("\n")
    new_sort_list = []
    for name in name_article:
        new_sort_list.append(notes_save[name])

    sort = sorted(new_sort_list, key=attrgetter('date_note.value'), reverse=reverse)

    sorted_list = []
    for i in sort:
        sorted_list.append(i.article.value)
    text.configure(state="normal")
    text.delete("0.1", END)
    text.insert("1.0", "\n".join(sorted_list))
    return  text.configure(state='disabled')


#********************************** MAIN WINDOW FIELDS and BUTTON ********************************

def main_windw():
    global main_window
    global a

    main_window = Tk()
    main_window.title("Заметка")
    notes_form = Frame(relief=SUNKEN, borderwidth=5)
    a = notes_form
    main_window.geometry("+750+300")   
    notes_form.pack()
    main_input(notes_form)
    main_print(notes_form)
    print_find_text(notes_form)
    find_input(notes_form)
    btn_new_notes(notes_form)
    btn_exit(notes_form)
    main_window.mainloop()

def main_input(notes_form):
    global find_article
    pass_lbl = Label(master=notes_form, text="", height=2)
    pass_lbl.grid(row=0, rowspan=2, column=0, columnspan=3)
    leblel_article = Label(master=notes_form, text="Введите текст для поиска:")
    find_article = Text(master=notes_form, width=37, height= 6)

    find_article.insert("1.0", article_incert)

    btn_find_article = Button(master=notes_form, text="По артикулам", width=15, command=find_by_article)
    btn_find_tegs = Button(master=notes_form, text="По тегам", width=15, command=finde_by_key_words)
    btn_find_text = Button(master=notes_form, text="По тексту", width=15, command=finde_by_text_note)
    btn_show_all = Button(master=notes_form, text="Показать все записи", width=15, command=show_all)

    leblel_article.grid(row=2, column=0)
    find_article.grid(row=2, column=1, rowspan=4)
    btn_find_article.grid(row=3,column=0)
    btn_find_tegs.grid(row=4,column=0)
    btn_find_text.grid(row=5,column=0)
    btn_show_all.grid(row=6,column=0)

def main_print(notes_form):
    pass_lbl = Label(master=notes_form, text="", height=2)
    pass_lbl.grid(row=6, rowspan=2, column=0, columnspan=3)
    leblel_article = Label(master=notes_form, text="Найденые статьи: ", width=15)
    leblel_sort = Label(master=notes_form, text="Сортировка: ", width=15)
    
    btn_sort_alfavit = Button(master=notes_form, text="По алфавиту", width=15, command=sort_click_alfavit)
    btn_sort_date = Button(master=notes_form, text="По дате изменения", width=15, command=sort_click_date)


    leblel_article.grid(row=8, column=0)
    leblel_sort.grid(row=9,column=0)

    btn_sort_alfavit.grid(column=0)
    btn_sort_date.grid(column=0)


def print_find_text(notes_form):
    global text
    a.pack(side=LEFT)
    text = Text(master=a, width=37, height=8)
    text.configure(state='disabled')
    text.grid(row=8,column=1, rowspan= 6)

    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)

def find_input(notes_form):
    global text_input
    pass_lbl = Label(master=notes_form, text="", height=2)
    pass_lbl.grid(row=14, rowspan=2, column=0, columnspan=3)
    pass_lbl_2 = Label(master=notes_form, text="", height=2)
    pass_lbl_2.grid(row=20, rowspan=2, column=0, columnspan=3)
    
    leblel_find_input = Label(master=notes_form, text="Введите название статьи для:")
    text_input = Text(master=notes_form, width=37, height=6)
    btn_read = Button(master=notes_form, text="Прочтения", width=15, command=read_notes)
    btn_change = Button(master=notes_form, text="Изменения", width=15, command=change_chose_notes)
    btn_delete = Button(master=notes_form, text="Удаления", width=15, command=confirm_chose)

    text_input.insert("1.0", tags_incert)

    leblel_find_input.grid(row=16, column=0)

    text_input.grid(row=15, column=1, rowspan= 6)

    btn_read.grid(row=17, column=0)
    btn_change.grid(row=18, column=0)
    btn_delete.grid(row=19, column=0)

#********************************** CREATE NEW NOTES functions and BUTTON ********************************

def btn_new_notes(notes_form):
    pass_lbl_2 = Label(master=notes_form, text="", width=25)
    pass_lbl_2.grid(row=1, rowspan=1, column=3)
    btn_new_notes = Button(notes_form, text="Добавить новую статью", width=20, height=5, command=new_window)
    btn_new_notes.grid(row=2, rowspan=5, column=3)

def change_chose_notes():

    name = text_input.get(1.0, END+"-1c")
    try:
        notes_save[name]
    except KeyError:
        error_wind()
        return
    createNewWindow(notes_save, name)

def new_window():
    createNewWindow(notes_save, new_notes_flag="")

article_incert = "---Текст для поиска---"
tags_incert = "---Теги---"

#************************************* ERROR and AXIT ***************************


def error_wind(*_):
    global error_glob
    error_glob = Toplevel()
    error_glob.geometry("+1000+500") 
    
    btn_submit = Button(master=error_glob, text="Неверное название статьи", width=20, height=3,command=exit_menu)
    btn_submit.pack(padx=10, ipadx=10)

    error_glob.mainloop()





#***************************************** Confirm window *********************

def confirm_chose(*_):
    global error_glob
    error_glob = Toplevel()
    error_glob.geometry("200x60+900+450") 

    btn_submit = Button(master=error_glob, text="Подтвердить", width=8, command=delete_note)
    btn_submit.pack(side=RIGHT, padx=10, ipadx=10)

    btn_clear = Button(master=error_glob, text="Отменить", width=8, command=exit_menu)
    btn_clear.pack(side=RIGHT, padx=10, ipadx=10)
    error_glob.mainloop()
    



def exit_menu():
    notes_save.save_data()
    error_glob.destroy()

def confirm_exit(*_):
    global error_glob
    error_glob = Toplevel()
    error_glob.geometry("+850+500") 

    btn_submit = Button(master=error_glob, text="Выйти", command=exit, width=10)
    btn_submit.pack(side=RIGHT, ipadx=10, padx=10, pady=7, ipady=7)

    btn_clear = Button(master=error_glob, text="Отменить", command=exit_menu, width=10)
    btn_clear.pack(side=RIGHT, ipadx=10, padx=10, pady=7, ipady=7)

    error_glob.mainloop()

#********************************* Delete article *******************************
def confirm_chose(*_):
    global error_glob
    error_glob = Toplevel()
    error_glob.geometry("200x60+900+450") 

    btn_submit = Button(master=error_glob, text="Подтвердить", width=8, command=delete_note)
    btn_submit.pack(side=RIGHT, padx=10, ipadx=10)

    btn_clear = Button(master=error_glob, text="Отменить", width=8, command=exit_menu)
    btn_clear.pack(side=RIGHT, padx=10, ipadx=10)
    error_glob.mainloop()

def delete_note():
    key_note = text_input.get(1.0, END+"-1c")
    try:
        del notes_save[key_note]
    except KeyError:
        error_wind()  
        return
    exit_menu()

#********************************** EXIT functions and BUTTON ********************************
def btn_exit(notes_form):
    
    btn_exit = Button(master=notes_form, text="Выход с заметок", width=20, height=4, command=confirm_exit)
    btn_exit.grid(row=17, rowspan=3, column=3)

def exit_save():
    notes_save.save_data()
    main_window.destroy()
def exit_save():
    main_window.destroy()
def start_bot():
    global notes_save
    notes_save = NotesSave()
    notes_save.load_data()
    main_windw()


def read_notes():
    name = text_input.get(1.0, END+"-1c").strip()
    try:
        notes_save[name]
    except KeyError:
        error_wind()
        return
    start_read_notes(notes_save, name)


