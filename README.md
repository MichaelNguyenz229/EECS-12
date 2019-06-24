from Tkinter import *


def printMessage1():
    x = "a"
    return x

def printMessage2():
    x = "b"
    return x

def printMessage3():
    x = "c"
    return x

def printMessage4():
    x = "d"
    return x

GUI = Tk()
GUI.title("Project X")

def ButtonPress(word):
    e.delete(0, END)
    e.insert(0, word)


e = Entry(GUI, width = 100, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 40, pady = 10)

initial0 = Button(GUI, text = "Intro", padx = 20, pady = 20, command=lambda: ButtonPress("a"))

button1 = Button(GUI, text = "Title A", padx = 20, pady = 20, command=lambda: ButtonPress("b"))

button2 = Button(GUI, text = "Title B", padx = 20, pady = 20, command=lambda: ButtonPress("c"))

button3 = Button(GUI, text = "Title C", padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button4 = Button(GUI, text = "Title D",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button5 = Button(GUI, text = "EndMessage 1",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button6 = Button(GUI, text = "EndMessage 2",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button7 = Button(GUI, text = "EndMessage 3",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button8 = Button(GUI, text = "EndMessage 4",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button9 = Button(GUI, text = "EndMessage 5",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button10 = Button(GUI, text = "EndMessage 6",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button11 = Button(GUI, text = "EndMessage 7",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button12 = Button(GUI, text = "EndMessage 8",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button13 = Button(GUI, text = "EndMessage 9",padx = 20, pady = 20, command=lambda: ButtonPress("d"))

button14 = Button(GUI, text = "EndMessage 10",padx = 20, pady = 20, command=lambda: ButtonPress("d"))


initial0.grid(row = 3, column = 0)
button1.grid(row = 4, column = 0)
button2.grid(row = 5, column = 0)
button3.grid(row = 6, column = 0)
button4.grid(row = 7)
button5.grid(row = 3, column = 1)
button6.grid(row = 4, column = 1)
button7.grid(row = 5, column = 1)
button8.grid(row = 6, column = 1)
button9.grid(row = 7, column = 1)
button10.grid(row = 3, column = 2)
button11.grid(row = 4, column = 2)
button12.grid(row = 5, column = 2)
button13.grid(row = 6, column = 2)
button14.grid(row = 7, column = 2)



#
# def printName():
#     print("MOOOOOOOOO")
#
# button_function = Button(GUI, text="Cows go", command=printName)
# button_function.pack()
#
# def printBob(event):
#     for i in range(0, 10):
#         print("BJORN SUCKS WIENERS")
#
# button_function2 = Button(GUI, text="Bjorns go")
# button_function2.bind("<Button-1>", printBob)
# button_function2.pack()
#




# frame = Frame(GUI, width = 600, height = 500)
# frame.pack(fill = X)
#
# title = Label(GUI, text = "TITLE",fg = "red",bg = "black")
# title.pack(side = TOP)
#
# button1 = Button(GUI, text = "Title A", command = printMessage1,bg = "red",fg = "black")
# button1.pack(fill = X, side = TOP)
#
# button2 = Button(GUI, text = "Title B", command = printMessage2)
# button2.pack(fill = X,side = TOP)
#
# button3 = Button(GUI, text = "Title C", command = printMessage3)
# button3.pack(fill = X,side = TOP)
#
# button4 = Button(GUI, text = "Title D", command = printMessage4)
# button4.pack(fill = X,side = TOP)





# class Test1:
#
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text="print message", command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text="Quit", command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self):
#         print("DONE")
#
#
#
# GUI = Tk()
# b = Test1(GUI)

GUI.mainloop()
