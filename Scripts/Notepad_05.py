""" БЛОКНОТ (оконное приложение)
 - загружаем файл в многострочное поле
 - сохраняем файл
 - очищаем текст (файл)
 - сепаратор в меню
 - выходим из программы
 - сохраняем файл
 - инфо-поле внизу (число символов и слов в тексте (файйле)
 - транслитерируем русский текст
 - НЕ переводим с русского на английский язык (goog-Translator) <- не получилось!
 """

from tkinter import *  # Оконное приложение
from tkinter import messagebox as mb
from tkinter import filedialog as fd
# from transliterate import translit, get_available_language_codes
from transliterate import translit
# from transliterate import translit
# from googletrans import Translator, LANGUAGES
# from googletrans import Translator


def delete():
    text.delete('1.0', END)
    update_status()


def transliter():
    # global t_text
    try:
        source_text = text.get('1.0', END)
        t_text = translit(source_text, 'ru', reversed=True)
        text.delete('1.0', END)
        text.insert('1.0', t_text)
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибкаЖ {e}')
    update_status()


# def translate_():
#     # global t_text
#     try:
#         source_text = text.get('1.0', END)
#         translator = Translator()
#         t_text = translator.translate(source_text, src='ru', dest='en').text
#         text.delete('1.0', END)
#         text.insert('1.0', t_text)
#     except Exception as e:
#         mb.showerror('Ошибка', 'Произошла ошибка перевода {e}')


def insert():
    try:
        file = fd.askopenfilename()
        if file:  # Если файл есть
            with open(file, 'r') as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    update_status()


def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("All files:", "*.*")))
        if file:  # Если файл есть
            with open(file, 'w') as f:
                s = text.get('1.0', END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def quit_():
    window.destroy()


def update_status():  # Обновляем содержимое
    content = text.get('1.0', END)
    char_count = len(content)
    wird_count = len(content.split())
    status_bar.config(text=f'Символов: {char_count} Слов: {wird_count}')


window = Tk()

window.title("БЛОКНОТ")

frame = Frame()
frame.pack()

text = Text(frame, width=30, height=8,
            bg='gray', fg='black',
            wrap=WORD)  # Команда на создание текстового поля
text.pack(side=LEFT)
text.bind("<Key>", lambda event: update_status())
scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.configure(yscrollcommand=scroll.set)

status_bar = Label(text='Проба', anchor=W)
status_bar.pack(fill=X)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label='Открыть', command=insert)
file_menu.add_command(label='Сохранить', command=save)
file_menu.add_command(label='Очистить', command=delete)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_)


process_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Обработка', menu=process_menu)
process_menu.add_command(label='Транслитерация', command=transliter)
# process_menu.add_command(label='Перевод на английский', command=translate)


update_status()
window.mainloop()  # В окне основной цикл
