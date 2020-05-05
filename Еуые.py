import tkinter as tk
w = tk.Tk()
w.geometry("960x540")
w.resizable(False, False)
w.title("ЗапускайсяСволочь")
c = tk.Canvas(w, width=960, height=540, bg="white")
c.pack()
plX= 400
plY=300
player = c.create_rectangle(plX, plY, plX+40, plY+60)
vx = 1
vy = 30
def goX(x):
    c.move(player, x, 0)
a = 2
def X(d):
    vy = d
    return vy
def goY():
    global a, vy, player
    vy = vy - a
    c.move(player, 0, -vy)
    if c.coords(player)[3] < 440:
        w.after(30, goY)
pass
w.bind("<Left>", lambda event: goX(-10))
w.bind("<Right>", lambda event: goX(10))
w.bind("<Up>", lambda event: X(30))
goY()
w.mainloop()
