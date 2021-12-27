from CustomMaze import maze, agent, COLOR
# from pyamaze import maze
from tkinter import *
from queue import PriorityQueue

def manhattanDistance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x2-x1) + abs(y2-y1)

def aStar(m, start, goal):
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = manhattanDistance(start, goal)

    queue = PriorityQueue()
    queue.put((manhattanDistance(start, goal), manhattanDistance(start, goal), start))
    path = {}
    while not queue.empty():
        currCell = queue.get()[2]
        if currCell == goal:
            break
        for dir in 'ESNW':
            if m.maze_map[currCell][dir] == True:
                if dir == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if dir == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if dir == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if dir == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                temp_g = g_score[currCell] + 1
                temp_f = temp_g + manhattanDistance(childCell, goal)

                if temp_f < f_score[childCell]:
                    g_score[childCell] = temp_g
                    f_score[childCell] = temp_f
                    queue.put((temp_f, manhattanDistance(childCell, goal), childCell))
                    path[childCell] = currCell
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[path[cell]] = cell
        cell = path[cell]
    return fwdPath


def startGame():
    root.destroy()
    m = maze(9, 9)
    def moveAgent():
        path = aStar(m, b.position, a.position)
        nextCell = path[b.position]
        b.position = nextCell
        if (b.position == a.position):
            m.killAgent(a)
    m.CreateMaze(loopPercent=30)
    a = agent(m, 9, 9, type="cat", callback=lambda:moveAgent())
    b = agent(m, 1, 9, type="ghost")
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


