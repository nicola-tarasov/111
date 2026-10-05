""" ЗАДАНИЕ 4
Выполнено на основе скрипта Graf_06.py из асинхронного занятия 7
"""
# Курс обучения: "АЦ. Программирование на языке Python от базового уровня до продвинутого_1"
# Преподаватель: Голиков Денис Владимирович
# Слушатель: Тарасов Николай Александрович
# Группа: ППБУ-1.1
# Добавьте в проект графического редактора возможность изменения толщины пера
# с помощью поля ввода (Entry) и кнопки.
# Это позволит пользователям вводить желаемую толщину пера.
# Добавьте поле ввода для задания толщины линии.
#
# 1. Добавьте кнопку установки толщины пера.
# 2. Создайте функцию для обновления толщины пера с обработкой исключения ValueError,
# которое может возникнуть, если в поле ввода толщины будет введено не целое число.
# 3. Обновите функцию draw, чтобы она использовала значение толщины, введенное пользователем.
# ////////////////////////////////////////////////////////
# //                Решение задания 4                   //
# ////////////////////////////////////////////////////////



""" Графический редактор
- рисование мышкой;
- выбор цвета из палитры;
- загрузка картинок с обработкой ошибок;
- сохранение картинок;
- меню "Файл" (загрузка, очистка, сохранение, выход);
- изменение толщины пера (линии).
"""


from tkinter import *
from PIL import Image, ImageTk, ImageGrab
# from Pillow import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
# Функции должны отбиваться (отделяться) в тексте программы двумя пустыми строками с обеех сторон!!!


def line_width():
    global num
    num = entry.get().strip()
    try:
        if int(num):
            num = abs(int(num))
    # except num is None:
    #     mb.showerror('Ошибка', f'Толщина линии не задана.')
    except ValueError:
        mb.showerror('Ошибка', f'Толщина линии не задана. \nЛибо "{num}" - не целое число. \nЛибо "{num}" не удалось преобразовать в число.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла непредвиденная ошибка: {e}')


def drow(event):  # Функция рисования
    global num
    x, y = event.x, event.y
    canvas.create_oval(x - int(num) // 2, y - int(num) // 2,
                       x + int(num) // 2, y + int(num) // 2,
                       fill=pen_color, outline=pen_color)  # Рисуем кружочками вокруг курсора


def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files', '+.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((800, 400))
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
            x1 = x + 800
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)  # Грабим и сохраняем содержимое окна с рисунком
            mb.showinfo('Сохранено!',f'Изображение успешно сохранено!')
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось сохранить файл из-зи ошибки {e}')


def quit_():
    window.destroy()

window = Tk()  # Создаём окно
window.title('Графический редактор')  # Заголовок окна

# Предопределение переменных
pen_color = 'white'  # Цвет пера по умолчанию

canvas = Canvas(width=800, height=400, bg='grey')  # Создаём холст
canvas.pack()
canvas.bind("<B1-Motion>", drow)  # Создаём событие - рисуем по перемещению нажатой левой (основной) кнопки мыши.
# Сначала создадим список цветов, которые нам потребуются.
colors = ['black', 'grey', 'white', 'brown', 'crimson', 'red', 'orange', 'yellow', 'yellow green', 'lime',  'green',
          'dark blue', 'blue', 'turquoise', 'violet', 'fuchsia', 'purple', 'indigo']
for color in colors:  # Будем делать это в цикле!
    ldl = Label(bg=color, width=3, height=1)  # Создание метки.
    ldl.pack(side=LEFT)
    ldl.bind("<B1-Motion>", lambda e, c=color:globals().update(pen_color=c))  # Изменим цвет пера
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
# Создаём поле с подписью (слева от поля ввода толщины линии)
lab = Label(text='Толщина линии', width=14, justify='center')
lab.pack(side=LEFT)

# Создаём поле ввода толщины линии
entry = Entry(text='20', width=12, justify='center')  # Само поле ввода толщины линии
num = entry.get().strip()  # Функция strip (обнажаться) сдирает (удаляет) начальные и конечные пробелы из строки.
entry.pack(side=LEFT)

# Создаём кнопку и привязываем к ней функцию смены толщины линии (справа от поля ввода толщины линии)
Button(text='Установить толщину', width=18, justify='center', command=line_width).pack(side=LEFT)

window.mainloop()  # В конце скрипта должна следовать одна пустая строка!
