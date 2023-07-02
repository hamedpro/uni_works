import tkinter 

window = tkinter.Tk()
window.geometry('500x500')
enrty_value = tkinter.StringVar(window , "22")
e1 = tkinter.Entry(window , textvariable=enrty_value)
enrty_value.set('33')
e1.grid(row = 1 , column=1)
window.mainloop()