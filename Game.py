from CustomMaze import maze, agent, COLOR
# from pyamaze import maze
from tkinter import *

def startGame():
    root.destroy()
    m = maze(9, 9)
    m.CreateMaze()
    a = agent(m, 4, 4, type="ghost",color=COLOR.blue)
    m.enableArrowKey(a)
    m.run()

root = Tk()
canvas = Canvas(root, width= 350)
root.title("A-maze-ing Chase")
root.geometry("600x300")
Label(canvas, font="cmr 40 bold", text="A-maze-ing Chase").pack(pady= 30)
Button(canvas, text="START", width=15, pady=10, font="cmr 15 bold", bg="gray11", borderwidth=0, foreground='white', command=lambda:startGame()).pack()
canvas.pack()

root.mainloop()


