import tkinter as tk



def draw_line(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y  # Запоминаем точку начала

def paint(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        # Рисуем линию от последней точки к текущей
        # canvas.create_line(last_x, last_y, event.x, event.y, fill="blue", width=200)
        canvas.create_oval(last_x, last_y, event.x, event.y, fill="blue", width=5)
        # canvas.create_rectangle(last_x, last_y, event.x, event.y, fill="blue", width=2)
        # canvas.create_polygon(last_x, last_y, event.x, event.y, last_x, event.y, fill="blue", width=2)
        last_x, last_y = event.x, event.y  # Обновляем последнюю точку


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Привязка событий
canvas.bind("<Button-1>", draw_line)  # Клик — начало линии
canvas.bind("<B1-Motion>", paint)    # Движение с зажатой кнопкой — рисование

root.mainloop()
