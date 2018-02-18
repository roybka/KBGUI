from Tkinter import *
import Tkinter
master = Tk()

canvas_width = 1000
canvas_height = 800
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

def write_slogan():
    print("Tkinter is easy to use!")


frame = Frame(master)
frame.pack()
y = int(canvas_height / 2)
#w.create_line(0, y, canvas_width, y, fill="#476042")
w.create_oval(400,300,600,500)
slogan = Tkinter.Button(frame,
                 text="Hello",
                 command=write_slogan,
                 )
    
#slogan.place(x=.250, y=.250,in_=w)
#slogan.place(x=.5,y=.5,anchor="c")
#slogan.grid(row=7,column=3)
slogan.pack()
slogan.place(bordermode=INSIDE, height=100, width=100,x=10)
#b1 = DrawnButton(pane, (12, 12), launch_icon, command=self.launch)
#b1.place(relx=1, x=-2, y=2, anchor=NE)

mainloop()
