from ssl import Options
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import color


from click import option
from matplotlib.pyplot import text
root =Tk()
root.title("Absen otomatis")
root.geometry("600x600")

# def comboclick(event):
#     if myCombo=='Manajemen Jaringan':
#         import MANAJEMEN_JARINGAN
#     else:
#         mylabe= Label(root,text=myCombo.get()).pack()
def selected():
    if myCombo.get()=='Manajemen Jaringan':
        import MANAJEMEN_JARINGAN
    elif myCombo.get()=='Routing & Switching':
        import ROUTING_d_SWITCHING_ESSENTIAL
    elif myCombo.get()=='Manajemen Jaringan':
        import MANAJEMEN_JARINGAN
    elif myCombo.get()=='Interaksi Manusia Komputer':
        import imk
    elif myCombo.get()=='Pembelajaran mesin':
        import Pembelajaran_mesin
    elif myCombo.get()=='Mobile Commerce':
        import Mobile_commerce
    elif myCombo.get()=='Kecerdasan Buatan':
        import ai
    else:
        mylabe= Label(root,text=myCombo.get()).pack()

options =[
    "Manajemen Jaringan",
    "Routing & Switching",
    "Manajemen Jaringan",
    "Interaksi Manusia Komputer",
    "Pembelajaran mesin",
    "Mobile Commerce",
    "Kecerdasan Buatan",
]
# clicked = StringVar()
# clicked.set(options[0])
# drop= OptionMenu(root,clicked, *options)
# drop.pack(pady=20)

myCombo = ttk.Combobox(root, values=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>")
myCombo.pack()


# myButton = tkinter.Button(root, text="absen", command=absen)
# myButton.pack()
B =Button(root, text ="Absen", command=selected)
B.pack( pady=20)
root.mainloop()

