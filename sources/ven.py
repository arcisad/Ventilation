from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import datetime as dt


def calculate(*args):
    try:
        value1 = float(FRC.get())
        value2 = float(TLC.get())
        VC.set(value2 - value1/2)
    except ValueError:
        pass


def deic(self):
    self.deiconify()
    self.protocol('WM_DELETE_WINDOW', lambda: self.withdraw()) #checks if the window is being closed to iconify it again
    root.update()
    return self


root = Tk()
root.title('The Ventilation Model')

FRC = StringVar()
TLC = StringVar()
VC = StringVar()


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

lv = Toplevel(root)
ttk.Button(mainframe, text="Specify the lung volumes", command=lambda: deic(lv)).grid(column=1, row=1, sticky=W)
lv.withdraw()

nw = Toplevel(root)
ttk.Button(mainframe, text="Input Pressure", command=lambda: deic(nw)).grid(column=1, row=2, sticky=W)
nw.withdraw()

vd = Toplevel(root)
ttk.Button(mainframe, text="Volume distribution", command=lambda: deic(vd)).grid(column=2, row=1, sticky=(N, W))
vd.withdraw()

ttk.Label(lv, text="Enter FRC: ").grid(column=1, row=1, sticky=(W, E))
FRC_entry = ttk.Entry(lv, width=7, textvariable=FRC)
FRC_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(lv, text="Litres").grid(column=3, row=1, sticky=W)
ttk.Label(lv, text="Enter TLC: ").grid(column=1, row=2, sticky=(W, E))
TLC_entry = ttk.Entry(lv, width=7, textvariable=TLC)
TLC_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(lv, text="Litres").grid(column=3, row=2, sticky=W)
ttk.Label(lv, text="Vital Capacity is: ").grid(column=1, row=3, sticky=W)
ttk.Button(lv, text="Calculate", command=calculate).grid(column=1, row=4, sticky=W)
ttk.Label(lv, textvariable=VC).grid(column=2, row=3, sticky=W)
ttk.Label(lv, text="Litres").grid(column=3, row=3, sticky=W)
FRC_entry.focus()
lv.bind('<Return>', calculate)

ttk.Label(nw, text="Please select the pressure type: ").grid(column=1, row=6, stick=(W, S))
p_type = StringVar()
passive = ttk.Radiobutton(nw, text='Passive', variable=p_type, value='Passive')
passive.grid(column=1, row=7, sticky=(W, S))
passive = ttk.Radiobutton(nw, text='Active', variable=p_type, value='Active')
passive.grid(column=1, row=8, sticky=(W, S))
passive = ttk.Radiobutton(nw, text='Input', variable=p_type, value='Input')
passive.grid(column=1, row=9, sticky=(W, S))
ttk.Button(nw, text="OK", command=lambda: nw.withdraw()).grid(column=1, row=10, sticky=W)

ttk.Label(vd, text="Enter Rmin: ").grid(column=1, row=1, sticky=(W, E))
Rmin_entry = ttk.Entry(vd, width=7)
Rmin_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(vd, text="Enter Rmax: ").grid(column=1, row=2, sticky=(W, E))
Rmax_entry = ttk.Entry(vd, width=7)
Rmax_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(vd, text="Enter COV: ").grid(column=1, row=3, sticky=(W, E))
COV_entry = ttk.Entry(vd, width=7)
COV_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Button(vd, text="OK", command=lambda: vd.withdraw()).grid(column=1, row=4, sticky=W)
Rmin_entry.focus()

dat = dt.datetime.now()
msb = ttk.Button(mainframe, text="Date/Time", command=lambda: msg.showinfo("Date and time", message=dat))
msb.grid(column=1, row=4, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
# Code to add widgets will go here...

root.geometry('{}x{}'.format(320, 240))
root.resizable(width=False, height=False)
root.mainloop()
