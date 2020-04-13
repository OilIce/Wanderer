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
def go(a,b):
    c.move(player,a,b)
pass
i = 15
def jump(a,b):
    i-=1
    c.move(player,a,b*i)
w.bind("<Left>", lambda event: go(-10,0))
w.bind("<Right>", lambda event: go(10,0))
w.bind("<Up>", lambda event: jump(0,1))
w.mainloop()
