from tkinter import *
from tkinter import ttk

def commandList():
    print('''LMAO i'm to lazy to make this work''')
def defaultDotDrawer(root, dot, fill='gray', outline='green'):
    root.create_oval(dot[0]-5, dot[1]-5, dot[0]+5, dot[1]+5, fill=fill, outline=outline)
def tester1(event):
    print('test1')
def ngroupFinder(l, n):
    groups=[]
    if n==0:
        return [[]]
    
    for element in range(0, len(l)):
        newL=l[element+1:]
        smallGroups=ngroupFinder(newL, n-1)
        for smallGroup in smallGroups:
            groups.append([l[element]]+smallGroup)
    return groups
def extractDim(points, dimension):
    dimensions=[]
    for point in points:
        dimensions.append(point[dimension])
    return dimensions
def extractDims(points):
    allDimensions=[]
    for d in range(0, len(points[0])): 
        allDimensions.append(extractDim(points, d))
    return tuple(allDimensions)


class Board(Canvas):
    def __init__(self, parent, dots=[], dotDrawer=defaultDotDrawer, **kwargs):
        self.parent=parent
        self.kwargs=kwargs
        super().__init__(parent, **kwargs)
        parent.bind('<Button-1>', self.createDot)
        parent.bind('<Key>', self.key)
        self.dots=dots
        self.dotDrawer=lambda dot, fill='gray', outline='green': dotDrawer(root=self, dot=dot, fill=fill, outline=outline)

        for dot in dots:
            self.dotDrawer(dot)

    def createDot(self, event):
        if event.widget==self:
            dot=self.saveDot(event)
            self.dotDrawer(dot)
            print(self.dots)

    def saveDot(self, event):
        dot=[event.x, event.y]
        self.dots.append(dot)
        return dot

    def key(self, event):
        if event.char=='p':
            self.perimeter()
        if event.char=='w':
            self.web()
    
    def perimeter(self):
        X, Y=extractDims(self.dots)
        x0=min(X)
        x1=max(X)
        y0=min(Y)
        y1=max(Y)
        self.create_rectangle(x0, y0, x1, y1, outline='green', fill='')

    def web(self):
        dotPairs=ngroupFinder(self.dots, 2)
        for pair in dotPairs:
            self.create_line(pair[0][0], pair[0][1], pair[1][0], pair[1][1], fill='green') #pair[0] 0th dot, pair[0][1] 0th dot y coords

    def averagePoint(self, fill='orange'):
        X, Y=extractDims(self.dots)
        avgX=sum(X)/len(X)
        avgY=sum(Y)/len(Y)
        self.dotDrawer([avgX, avgY], fill=fill)
        print('Average: [%s, %s]'%(avgX, avgY))


class Interface(Frame):
    def __init__(self, parent, **kwargs):
        self.parent=parent
        self.kwargs=kwargs
        super().__init__(parent, **kwargs)

        self.command=StringVar()



root=Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

board=Board(root, width=600, height=400, background='black')

board.grid(column=0, row=0, sticky=(N, W, E, S))

interface=Interface(root, width=120, height=400, background='black')
interface.grid(column=1, row=0, sticky=(N, W, E, S))

root.mainloop()
