from tkinter import *
from class_notes import TextNote, KeyWords, Article, Notes, NotesSave

#********************************** Window config ****************************    

def article_field(notes_form):
    global ent_article
    lbl_article = Label(master=notes_form, text="Заголовок:")
    ent_article = Entry(master=notes_form, width=47)
    
    try:
        ent_article.insert(0, notes_save[find_article].article.value) 
    except KeyError:
        pass
    # ent_article.insert(1, "dioswolf")   ****************    ввод текста в поле заголовка(для восстановления)
    btn_article_insert = Button(master=notes_form, text="Записать", command=getArticleInput)
    # btn_article_delete = tk.Button(master=notes_form, text="Удалить", command=)
    lbl_article.grid(row=0, column=0, sticky="e")
    ent_article.grid(row=0, column=1)
    btn_article_insert.grid(row=0, column=2)
    # btn_article_delete.grid(row=0, column=3)

def text_fiel(notes_form):
    global text_form
    text_lbl = Label(master=notes_form, text="Заметка:")
    text_form = Text(master=notes_form, width=35, height=15)
    try:
        text_form.insert("1.0", notes_save[find_article].text_note.value) 
    except:
        pass
    btn_tags_insert = Button(master=notes_form, text="Записать", command=getTextInput)
    btn_tags_delete = Button(master=notes_form, text="Удалить", command=delete_text)
    text_lbl.grid(row=2, column=0, sticky="e")
    text_form.grid(row=2, column=1)
    btn_tags_insert.grid(row=2, column=2)
    btn_tags_delete.grid(row=2, column=3)

def keywords_field(notes_form):
    global ent_tags
    lbl_tags = Label(master=notes_form, text="Теги:")
    ent_tags = Entry(master=notes_form, width=47)
    try:
        ent_tags.insert(0, notes_save[find_article].key_words.value) 
    except:
        pass
    # ent_article.insert(1, "dioswolf")   ****************    ввод текста в поле тегов(для восстановления)
    btn_tags_insert = Button(master=notes_form, text="Записать", command=getKeywordsInput)
    btn_tags_delete = Button(master=notes_form, text="Удалить", command=delete_key_words)
    lbl_tags.grid(row=3, column=0, sticky="e")
    ent_tags.grid(row=3, column=1)
    btn_tags_insert.grid(row=3, column=2)
    btn_tags_delete.grid(row=3, column=3)

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
    for keys, item in notes_save.items():
        if result_artilce == item.article.value:
            return
    article = Article(result_artilce)
    text_note = TextNote("")
    key_words = KeyWords("")
    note = Notes(article, text_note, key_words)
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

    newWindow = _
    newWindow.geometry("+800+320")  
    article_field(newWindow)
    text_fiel(newWindow)
    keywords_field(newWindow)
    btn_exit(newWindow)
    newWindow.mainloop()

def createNewWindow(notes_data, article=None):
    global find_article
    find_article = article
    global notes_save
    notes_save = notes_data
    notes_save.load_data()
    global newWindow
    newWindow = Toplevel()
    
    start_window_notes(newWindow)

