from datetime import datetime
from tkinter import *
from class_notes import TextNote, KeyWords, Article, Notes, NotesSave, DateNote

#********************************** Window config ****************************    




def article_field(notes_form, flag = None):
    global ent_article
    if flag == None:
        ent_article = Entry(master=notes_form, width=47)
        ent_article.insert(0, notes_save[find_article].article.value) 
        ent_article.configure(state='disabled')
    else:   
        btn_article_insert = Button(master=notes_form, text="Записать", command=getArticleInput)
        ent_article = Entry(master=notes_form, width=47)
        btn_article_insert.grid(row=0, column=2)
    lbl_article = Label(master=notes_form, text="Заголовок:")

    try:
        ent_article.insert(0, notes_save[find_article].article.value) 
    except KeyError:
        pass

    lbl_article.grid(row=0, column=0, sticky="e")
    ent_article.grid(row=0, column=1)


def text_fiel(notes_form, flag = None):
    global text_form
    if flag == None:
        text_form = Text(master=notes_form, width=35, height=15)
        text_form.insert("1.0", notes_save[find_article].text_note.value) 
        text_form.configure(state='disabled')
    else:   
        text_form = Text(master=notes_form, width=35, height=15)
        btn_tags_insert = Button(master=notes_form, text="Записать", command=getTextInput)
        btn_tags_delete = Button(master=notes_form, text="Удалить", command=delete_text)
        btn_tags_insert.grid(row=2, column=2)
        btn_tags_delete.grid(row=2, column=3)

    text_lbl = Label(master=notes_form, text="Заметка:")
    
    try:
        text_form.insert("1.0", notes_save[find_article].text_note.value) 
    except:
        pass

    text_lbl.grid(row=2, column=0, sticky="e")
    text_form.grid(row=2, column=1)

def keywords_field(notes_form, flag = None):
    global ent_tags
    if flag == None:
        ent_tags = Entry(master=notes_form, width=47)
        ent_tags.insert(0, notes_save[find_article].key_words.value) 
        ent_tags.configure(state='disabled')
    else:   
        ent_tags = Entry(master=notes_form, width=47)
        btn_tags_insert = Button(master=notes_form, text="Записать", command=getKeywordsInput)
        btn_tags_delete = Button(master=notes_form, text="Удалить", command=delete_key_words)
        btn_tags_insert.grid(row=3, column=2)
        btn_tags_delete.grid(row=3, column=3)

    lbl_tags = Label(master=notes_form, text="Теги:")

    try:
        ent_tags.insert(0, notes_save[find_article].key_words.value) 
    except:
        pass
    # ent_article.insert(1, "dioswolf")   ****************    ввод текста в поле тегов(для восстановления)

    lbl_tags.grid(row=3, column=0, sticky="e")
    ent_tags.grid(row=3, column=1)

#********************************** Delete functions ****************************    

def delete_text():
    global new_text_notes
    new_text_notes = text_form.delete("0.1", END)
    
    key_note = ent_article.get()
    text_note = TextNote("")
    try:
        notes_save[key_note].text_note = text_note
        notes_save.save_data()
    except KeyError:
        error_wind()
    return new_text_notes

def delete_key_words():
    global new_tags_notes
    new_tags_notes = ent_tags.delete(0, END)
    
    key_note = ent_article.get()
    key_words = KeyWords("")
    try:
        notes_save[key_note].key_words = key_words
    except KeyError:
        error_wind()
    notes_save.save_data()
    return new_tags_notes

#********************************** Added functions ****************************   


def add_new_note(result_artilce: str):
    global old_name

    for keys, item in notes_save.items():
        if result_artilce == item.article.value:
            return error_wind
    
    article = Article(result_artilce)
    
    text_note = TextNote(text_form.get(1.0, END+"-1c"))
    key_words = KeyWords(ent_tags.get())

    time_add = DateNote(datetime.now())
    note = Notes(article, text_note, key_words, time_add)

    del notes_save[old_name]
    old_name = result_artilce


    return save_info(notes_save, note)

def save_info(notes_save: NotesSave, note : Notes):   
    notes_save.add_record(note)
    notes_save.save_data()



#********************************** Delete functions ****************************   

def write_text_notes_field(result_text):

    key_note = ent_article.get()

    text_note = TextNote(result_text)
    try:
        notes_save[key_note].text_note = text_note
    except KeyError:
        error_wind()
    notes_save.save_data()
    return 

def write_key_words_field(result_keys):
    
    key_note = ent_article.get()

    key_words = KeyWords(result_keys)
    try:
        notes_save[key_note].key_words = key_words
    except KeyError:
        error_wind()    
    notes_save.save_data()
    return 


#********************************** GET TEXT functions ********************************


def getArticleInput():
    global old_name
    result_artilce = ent_article.get()
    return add_new_note(result_artilce)

def getTextInput():
    result_text= text_form.get(1.0, END+"-1c")
    return write_text_notes_field(result_text)


def getKeywordsInput():
    result_keys = ent_tags.get()
    return write_key_words_field(result_keys)

#********************************** ERROR and EXIT functions ****************************   

def exit():
    newWindow.destroy()


def btn_exit(notes_form):
    pass_lbl = Label(master=notes_form, text="", height=2)
    pass_lbl.grid(row=4, rowspan=2, column=2)
    btn_exit = Button(master=notes_form, text="Выход с заметок", width=20, height=4, command=exit)
    btn_exit.grid(row=6, rowspan=4, column=3)


def error_wind(*_):
    global error_glob
    error_glob = Toplevel()
    labelExample = Label(error_glob, text = "New Window")
    buttonExample = Button(error_glob, text = "New Window button", command=exit_menu)
    labelExample.pack()
    buttonExample.pack()
    error_glob.mainloop()

def exit_menu():
    notes_save.save_data()
    error_glob.destroy()


#********************************** START functions ******************************** 


def start_window_notes(_):
    flag = ""
    newWindow = _
    newWindow.geometry("+800+320")  
    article_field(newWindow, flag)
    text_fiel(newWindow, flag)
    keywords_field(newWindow, flag)
    btn_exit(newWindow)
    newWindow.mainloop()

def createNewWindow(notes_data, article=None):
    global find_article
    global old_name
    old_name = article
    find_article = article
    global notes_save
    notes_save = notes_data
    notes_save.load_data()
    global newWindow
    newWindow = Toplevel()
    start_window_notes(newWindow)

def read(newWindow):
    newWindow.geometry("+800+320")  
    # text_form.configure(state='disabled')
    # ent_tags.configure(state='disabled')
    article_field(newWindow)
    text_fiel(newWindow)
    keywords_field(newWindow)
    btn_exit(newWindow)
    newWindow.mainloop()

def start_read_notes(notes_data, article=None):
    global find_article
    global old_name
    old_name = article
    find_article = article
    global notes_save
    notes_save = notes_data
    notes_save.load_data()
    global newWindow
    newWindow = Toplevel()
    read(newWindow)
