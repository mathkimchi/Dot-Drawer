#update log
'''This update occured because I finally figured out what the Frame widget does... hopefully
The update will be to go from using a Canvas called Board (for the main things) and 
Frame called Interface (for the minor things) at the core to using a 
main Frame (WRITING THIS JUST MADE ME REALISE WHAT MAINFRAME MEANT) 
containing a board and other things like possibly another frame called interface'''

'''I'm thinking of having the Mainframe have all the calculations, things, everything.'''

#imports
from tkinter import *
from tkinter import ttk

#math/basic custom functions
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
def betterList2String(l):
    s=''
    for element in l:
        s+=element
        s+='\n'
    s=s[:-1]
    return s


class Mainframe(Frame):
    def __init__(self, parent, dots=[], dotDrawer=defaultDotDrawer, **kwargs):
        #parent
        self.parent=parent
        self.kwargs=kwargs
        super().__init__(parent, **kwargs)

        #create canvas
        self.canvas=Canvas(self, width=600, height=600, background='black')
        self.canvas.grid(column=0, row=0)

        self.dots=dots
        self.dotDrawer=lambda dot, fill='gray', outline='green': dotDrawer(root=self.canvas, dot=dot, fill=fill, outline=outline)
        for dot in dots:
            self.dotDrawer(dot)

        #create interface
        self.interface=Frame(self, width=300, height=600, background='white')
        self.interface.grid(column=1, row=0, sticky=(N, W, E, S))
        
        self.labelThatSaysCommandsUsed=ttk.Label(self.interface, text='Commands Used:')
        self.labelThatSaysCommandsUsed.grid(column=0, row=0, sticky=(W, E))

        self.commands_used=[]
        self.commandsLabel=ttk.Label(self.interface, text='')
        self.commandsLabel.grid(column=0, row=1, sticky=(W, E))

        self.command=StringVar()
        self.command_entry=ttk.Entry(self.interface, textvariable=self.command)
        self.command_entry.grid(column=0, row=2, sticky=(W, E))

        self.commandButton=ttk.Button(self.interface, text='Run Command', command=self.runCommandButton)
        self.commandButton.grid(column=0, row=3, sticky=(E))

        #bindings
        self.easyBindings()

    def easyBindings(self):
        self.canvas.bind('<Button-1>', self.createDot)
        self.canvas.bind('')
        self.parent.bind('<Key>', self.keyEvents)

    def keyEvents(self, event): #need to make it so it only happens when event is in canvas 
        if event.char=='p':
            self.squarePerimeter()
        elif event.char=='w':
            self.web()
        elif event.char=='z':
            self.avgCircleAnimation1()
        elif event.char==' ':
            self.manualCommand()

    def runCommandButton(self):
        exec(self.command.get())
        self.commands_used.append(self.command.get())
        self.commandsLabel.configure(text=betterList2String(self.commands_used[-5:]))

    def manualCommand(self):
        command=input('Type your command: ')
        exec(command)

    def createDot(self, event):
        print('sus')
        if event.widget==self.canvas:
            dot=self.saveDot(event)
            self.dotDrawer(dot)
            print(self.dots)
        
    def saveDot(self, event):
        dot=[event.x, event.y]
        self.dots.append(dot)
        return dot

    def squarePerimeter(self, outline='green'):
        X, Y=extractDims(self.dots)
        x0=min(X)
        x1=max(X)
        y0=min(Y)
        y1=max(Y)
        self.canvas.create_rectangle(x0, y0, x1, y1, outline=outline, fill='')

    def web(self, fill='green'):
        dotPairs=ngroupFinder(self.dots, 2)
        for pair in dotPairs:
            self.canvas.create_line(pair[0][0], pair[0][1], pair[1][0], pair[1][1], fill=fill) #pair[0] 0th dot, pair[0][1] 0th dot y coords

    def averagePoint(self, fill='orange'):
        X, Y=extractDims(self.dots)
        avgX=sum(X)/len(X)
        avgY=sum(Y)/len(Y)
        self.dotDrawer([avgX, avgY], fill=fill)
        print('Average: [%s, %s]'%(avgX, avgY))
        return [avgX, avgY]

    def avgCircleAnimation1(self, outline='orange'):
        avgPoint=self.averagePoint()
        self.zoomingCircle=self.canvas.create_oval(avgPoint[0], avgPoint[1], avgPoint[0], avgPoint[1], outline=outline, fill='')
        dotsInCircle=[]
        zoomingOut=True
        while len(dotsInCircle)<=len(self.dots):
            self.enlargeShape(self.zoomingCircle, 1)
            self.canvas.update()
            for dot in self.dots:
                xDist=avgPoint[0]-dot[0]
                yDist=avgPoint[1]-dot[1]
                dist=((xDist**2)+(yDist**2))**(1/2)
            



    def enlargeShape(self, shape, step):
        x0, y0, x1, y1 = self.canvas.coords(shape) #x0 is smallest x 
        x0-=step
        y0-=step
        x1+=step
        y1+=step
        self.canvas.coords(shape, x0, y0, x1, y1)

    def dimFinder(self, shape):
        x0, y0, x1, y1 = self.canvas.coords(shape)
        xDim=x1-x0
        yDim=y1-y0
        return xDim, yDim






































def startEverything():
    root=Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    mainframe=Mainframe(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


    root.mainloop()

startEverything()