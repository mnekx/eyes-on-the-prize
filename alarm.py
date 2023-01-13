#!/usr/bin/env

from tkinter import *
from tkinter import ttk
import os

os.environ['DISPLAY'] = ":0" 
os.environ['XAUTHORITY']="/home/mnekx/.Xauthority"

root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

frm = ttk.Frame(root, padding=10);

frm.grid()
ttk.Label(frm, text="HAVE FUNNNN", justify=CENTER).grid(column=0, row=0)
ttk.Label(frm, text="design patterns - java, js, python", justify=CENTER).grid(column=0, row=10)
ttk.Label(frm, text="leetcode - java, js, python", justify=CENTER).grid(column=0, row=20)
ttk.Label(frm, text="SWE Fundamentals - node.js, react.js", justify=CENTER).grid(column=0, row=30)
ttk.Label(frm, text="HAVE FUNNNN", justify=CENTER).grid(column=0, row=40)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1000)
root.mainloop()