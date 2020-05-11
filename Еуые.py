import tkinter as tk
from tkinter import NW

w = tk.Tk()
w.geometry("960x540")
w.resizable(False, False)
w.title("Wanderer")
c = tk.Canvas(w, width=960, height=540, bg="white")
c.pack()
image = tk.PhotoImage(file = "C:/Users/Admin/Desktop/ЫЫыыЫСаИ/pervayakomnata.png")
c.create_image(0, 0, image = image, anchor = NW)
plX = 400
plY = 300
player = c.create_rectangle(plX, plY, plX+40, plY+60, fill = "green")
vx = 1
vy = 30
def goX2(x):
    if c.coords(player)[0] > 60:
        c.move(player, x, 0)
def goX1(x):
    if c.coords(player)[2] < 900:
        c.move(player, x, 0)
a = 2
def X(d):
    global vy
    vy = d
    if c.coords(player)[3] >= 463:
        c.move(player, 0, -vy)
        goY()
def goY():
    global a, vy, player
    vy = vy - a
    c.move(player, 0, -vy)
    if c.coords(player)[1] < 75:
        vy = 0
        w.after(30, goY)
    elif c.coords(player)[3] < 463:
        w.after(30, goY)
    elif c.coords(player)[3] == 310 and 100 < c.coords(player)[0] < 200:
        vy = 0
        w.bind("<Up>", lambda event: X(30))
    else:
        w.bind("<Up>", lambda event: X(30))
pass
goY()
w.bind("<Left>", lambda event: goX2(-10))
w.bind("<Right>", lambda event: goX1(10))
w.mainloop()
