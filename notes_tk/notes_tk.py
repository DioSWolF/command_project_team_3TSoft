#from tabnanny import check
import tkinter as tk


# Запись
new_article_notes = ""
new_text_notes = ""
new_tags_notes = ""

"""
тестовый комментарий
"""

"""
тестовый комментарий 2
"""


def record_article():

    global new_article_notes
    new_article_notes = ent_article.get()

    return new_article_notes


def record_text():

    global new_text_notes
    new_text_notes = text_form.get("0.1", tk.END)

    return new_text_notes


def record_tags():

    global new_tags_notes
    new_tags_notes = ent_tags.get()

    return new_tags_notes


# Удаление значения
def delete_article():

    global new_article_notes
    new_article_notes = ent_article.delete(0, tk.END)
    return new_article_notes


def delete_text():

    global new_text_notes
    new_text_notes = text_form.delete("0.1", tk.END)
    return new_text_notes


def delete_tags():

    global new_tags_notes
    new_tags_notes = ent_tags.delete(0, tk.END)
    return new_tags_notes


def check():
    text_check_form.insert("1.0", new_article_notes)
    text_check_form.insert("1.0", new_text_notes)
    text_check_form.insert("1.0", new_tags_notes)


def delete_check():
    text_check_form.delete("0.1", tk.END)


window = tk.Tk()
window.title("Заметка")

notes_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

notes_form.pack()

# ****************Article
lbl_article = tk.Label(master=notes_form, text="Заголовок:")
ent_article = tk.Entry(master=notes_form, width=47)
btn_article_insert = tk.Button(
    master=notes_form, text="Записать", command=record_article)
btn_article_delete = tk.Button(
    master=notes_form, text="Удалить", command=delete_article)

lbl_article.grid(row=0, column=0, sticky="e")
ent_article.grid(row=0, column=1)
btn_article_insert.grid(row=0, column=2)
btn_article_delete.grid(row=0, column=3)

# ****************Text
text_lbl = tk.Label(master=notes_form, text="Заметка:")
text_form = tk.Text(master=notes_form, width=35, height=15)

btn_text_insert = tk.Button(
    master=notes_form, text="Записать", command=record_text)
btn_text_delete = tk.Button(
    master=notes_form, text="Удалить", command=delete_text)

text_lbl.grid(row=1, column=0, sticky="e")
text_form.grid(row=1, column=1)
btn_text_insert.grid(row=1, column=2)
btn_text_delete.grid(row=1, column=3)

# *****************Tags
lbl_tags = tk.Label(master=notes_form, text="Теги:")
ent_tags = tk.Entry(master=notes_form, width=47)
btn_tags_insert = tk.Button(
    master=notes_form, text="Записать", command=record_tags)
btn_tags_delete = tk.Button(
    master=notes_form, text="Удалить", command=delete_tags)

lbl_tags.grid(row=2, column=0, sticky="e")
ent_tags.grid(row=2, column=1)
btn_tags_insert.grid(row=2, column=2)
btn_tags_delete.grid(row=2, column=3)


# *************** Поле проверки

text_check_lbl = tk.Label(master=notes_form, text="Проверка:")
text_check_form = tk.Text(master=notes_form, width=35, height=15)

btn_text_insert = tk.Button(master=notes_form, text="Проверить", command=check)
btn_text_delete = tk.Button(
    master=notes_form, text="Удалить", command=delete_check)

text_check_lbl.grid(row=3, column=0, sticky="e")
text_check_form.grid(row=3, column=1)
btn_text_insert.grid(row=3, column=2)
btn_text_delete.grid(row=3, column=3)


# Получение текста из переменных

article = "--Заголовок--- "
text = "--Текст--"
tags = "#Тег"
ent_article.insert(0, article)
text_form.insert("1.0", text)
ent_tags.insert(0, tags)


window.mainloop()
