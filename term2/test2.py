import tkinter

window = tkinter.Tk()
window.geometry('500x500')
a = [2345345,34,53245]
username = tkinter.StringVar(window , "hamedpro")


username_input = tkinter.Entry(window , textvariable=username)
username_clone = tkinter.Entry(window , textvariable=username)
username_input.grid(row = 1 ,column=1)
username_clone.grid(row = 2 ,column=2)

window.mainloop()