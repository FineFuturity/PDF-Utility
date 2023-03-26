from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os as ossrvcs
import PIL as pil
import pandas as pd
import pypdf as pdf

NAME = "PDF Utility"
VER = "1.0"
PHASE = "alpha"
BRANCH = "dev.main_refactor"
BUILD = "26032023-0419"
ALLCLIENTENV = ["dev", "client","prod"]
CLIENTENV = ALLCLIENTENV[0]

BUILD_TAG_FULL = NAME + "\nVer. " + VER + "." + BUILD + "." + BRANCH + " (" + PHASE + ")\nFor testing purposes only."

# program flags
DEV = True

# Window Title Strings
TITLE = NAME
if DEV:
    WIN_BRC_TITLE = " ( ver. " + VER + "." + BUILD + ", " + BRANCH + " branch )"
    TITLE = TITLE + WIN_BRC_TITLE

# Window Properties
X_RES = 800
Y_RES = 600
GEOMETRY = str(X_RES)+"x"+str(Y_RES)

# global strings
NOT_DONE_YET = "Not implemented yet..."