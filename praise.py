import tkinter as tk
from tkinter import messagebox
import numpy

praiselist = [" is such a good boy!", " did it!", " looks nice today.", " is doing good lad"]
def PraiseUser(who = "User", which = 0, title = "get praised lol"):
    messagebox.showinfo(title, (who + praiselist[which]))