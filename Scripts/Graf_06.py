""" Графический редактор
- рисование мышкой разными цветами;
- загрузка картинок с обработкой ошибок;
- сохранение картинок;
+ меню
"""

from tkinter import *
from PIL import Image, ImageTk, ImageGrab
# from Pillow import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox as mb


pen_color = 'white'  # Предопределение переменной.
# Функции должны отбиваться (отделяться) в тексте программы двумя пустыми строками с обеех сторон!!!


def drow(event):  # Функция рисования кружочками
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files', '+.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось загрузить файл из-зи ошибки {e}')


def save_image():
    try:
        file_path = fd.asksaveasfilename(defaultextension='*.png', filetypes=[('PND files', '*.png')])
        if file_path:
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            x1 = x + 600
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)  # Грабим и сохраняем содержимое окна с рисунком
            mb.showinfo('Сохранено!',f'Изображение успешно сохранено!')
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось сохранить файл из-зи ошибки {e}')


def quit_():
    window.destroy()

window = Tk()  # Создаём окно
window.title('Графический редактор')  # Заголовок окна

canvas = Canvas(width=600, height=400, bg='grey')  # Создаём холст
canvas.pack()
canvas.bind("<B1-Motion>", drow)  # Создаём событие - рисуем по перемещению нажатой левой (основной) кнопки мыши.
# Сначала создадим список цветов, которые нам потребуются.
colors = ['white', 'brown', 'crimson', 'red', 'orange', 'yellow', 'yellow green', 'lime',  'green',
          'dark blue', 'blue', 'turquoise', 'light blue', 'violet', 'fuchsia', 'purple', 'black']
for color in colors:  # Будем делать это в цикле!
    ldl = Label(bg=color, width=4, height=2)  # Создание метки.
    ldl.pack(side=LEFT)
    ldl.bind("<B1-Motion>", lambda e, c=color:globals().update(pen_color=c))  # Изменим цвет  мышки
    # СПРАВКА
    # Лямбда-функции (или лямбда-выражения) — это анонимные (безымянные) функции,
    # которые позволяют писать короткие функции прямо в месте их использования,
    # без необходимости объявлять их отдельно с помощью def (в Python) или function (в JavaScript).
    # Они особенно удобны для передачи в качестве аргументов другим функциям,
    # например, в map(), filter() или sorted().
    # Синтаксис
    # lambda аргументы: выражение

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить изображение', command=load_image)
file_menu.add_command(label='Сохранить изображение', command=save_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_)

window.mainloop()  # В конце скрипта должна следовать одна пустая строка!
