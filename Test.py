from tkinter import *
from tkinter import ttk

root = Tk()

root.title("METANIT.COM")
root.geometry("250x200")

canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(fill=BOTH, expand=1)

# размеры прямоугольника
size = (60, 60, 100, 100)
red = "red"
blue = "blue"
green = "green"


# обработчики событий
def make_red(event): canvas.coords(id, size, fill= red)


def make_green(event): canvas.coords(id, size, fill = green)


def make_blue(event): canvas.coords(id, size, fill = blue)


id = canvas.create_rectangle(size, fill="red")
# привязка событий к элементу с идентификатором id
canvas.tag_bind(id, "<Enter>", make_green)
canvas.tag_bind(id, "<Leave>", make_red)
canvas.tag_bind(id, "<Button-1>", make_blue)

root.mainloop()