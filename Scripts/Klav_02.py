from tkinter import Tk, Label
import time
from tkinter import messagebox as mb


def load_phrase():
    try:
        with open('phrase.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        mb.showerror('Ошибка!', 'Файл с фразой не найден')
        return 'quick brown fox'


def start():
    global i, t
    i = 0  # Интекс первой буквы
    t = time.time()  # Время старта
    label.config(text=phrase[i])  # Выводится подксказка с первой букваой фразы
    window.bind('<Key>', check)  # Первый вызов функции check,
    # чтобы узнать, что же ввёл пользователь


def check(event):
    global i
    if event.char == phrase[i]:
        i += 1
        if i == len(phrase):
            finish()
        else:
            label.config(text=phrase[i])
    else:
        label.config(text=f'Ошибка! Ожидалась буква {phrase[i]},\n '
                          f'нажмите любую клавишу для продолжения')
        window.bind('<Key>', cont)  # Перекличка между функциями


def finish():
    global i, t
    elapsed = time.time() - t
    time_allowed = len(phrase)
    if elapsed <= time_allowed:
        res = (f'Вы победили! Ваше время {elapsed:.1f} сек.\n '
               f'Надо было уложиться в {time_allowed} сек.')
        window.unbind('<Key>')
    else:
        res = f'Вы проиграли! Прошло {elapsed:.1f} сек.\n '\
              f'Надо было уложиться в {time_allowed} сек.'
        window.unbind('<Key>')
    mb.showinfo('Результат', res)
    if mb.askyesno('Повторить?', 'Хотите попробовать ещё раз?'):
        start()
    else:
        window.destroy()


def cont(event):
    global i
    label.config(text=phrase[i])
    window.bind('<Key>', check)  # Перекличка между функциями

i = 0
t = 0
phrase = load_phrase()  # Быстрая бурая лиса
# Это  фраза для отработки быстрого ввода


window = Tk()
window.title("Клавиатурный тренажёр")
window.geometry("800x100")

label = Label(font=('Helvetica', 24))
label.pack()

start()
window.mainloop()
