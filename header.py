# ATTEMPT PYTHON 3 IMPORTS
try:
    import tkinter as tk
    import tkinter.ttk as ttk
    import tkinter.messagebox as msgbox
    import tkinter.filedialog as fdlg
# FALL BACK TO PYTHON 2
except ImportError:
    import Tkinter as Tk
    import Tkinter.ttk as Ttk
    import Tkinter.messagebox as Msgbox
    import Tkinter.filedialog as Fdlg

import PIL as pil
import pandas as pd
import os as ossrvcs
import pypdf as pdf

NAME = "PDF Utility"
VER = "1.0"
PHASE = "alpha"
BRANCH = "main.dev_prev_code"
BUILD = "24032023-1126"
CLIENTENV = {"dev", 
    {
        "client": "prod",
    }
} #dev, client-test, client-prod

BUILD_TAG_FULL = NAME + "\nVer. " + VER + "." + BUILD + "." + BRANCH + " (" + PHASE + ")\nFor testing purposes only."

# program flags
DEV = True

# Window Title Strings
TITLE = NAME
if DEV:
    WIN_BRC_TITLE = " ( ver. " + VER + "." + BUILD + ", " + BRANCH + " branch )"
    TITLE = TITLE + WIN_BRC_TITLE

# Window Properties
GEOMETRY = "800x600"

# global strings
NOT_DONE_YET = "Not implemented yet..."