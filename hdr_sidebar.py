
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surface\Documents\Projects\PDFUtilityRedux\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("179x28")
window.configure(bg = "#DD3227")


canvas = Canvas(
    window,
    bg = "#DD3227",
    height = 28,
    width = 179,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    12.0,
    7.0,
    anchor="nw",
    text="Page Thumbnails",
    fill="#FFFFFF",
    font=("MontserratRoman SemiBold", 10 * -1)
)
window.resizable(False, False)
window.mainloop()