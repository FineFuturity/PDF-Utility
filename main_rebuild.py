import header as prog

def create_canvas(parent, **kwargs):
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    relwidth = kwargs.pop('relwidth', None)
    relheight = kwargs.pop('relheight', None)
    canvas = prog.Canvas(parent, **kwargs)
    canvas.place(x=x, y=y)
    if relwidth is not None:
        canvas.place(relwidth=relwidth)
    if relheight is not None:
        canvas.place(relheight=relheight)
    return canvas

def resize_canvas(event, *args):
	for canvas in args:
	    canvas.config(height=event.height)
	    canvas.update_idletasks()

def resize_sidebar(event, sidebar_width, cnv_sidebar, cnv_for_pdf_view):
    sidebar_width = event.x+10
    cnv_sidebar.config(width=sidebar_width)
    cnv_for_pdf_view.place(x=sidebar_width+1, y=0, relwidth=1.0, relheight=1.0)

def set_resize_cursor(event, cnv_sidebar):
    cnv_sidebar.config(cursor="sb_h_double_arrow")
    
def set_default_cursor(event, cnv_sidebar):
    cnv_sidebar.config(cursor="")

window = prog.Tk()
window.title(prog.TITLE)
window.geometry(prog.GEOMETRY)
window.configure(bg = "#ECECEC")

# create the main canvas
canvas = prog.Canvas(window, bg="#000000", height=prog.Y_RES, width=prog.X_RES, bd=0, highlightthickness=0, relief="ridge")
# canvas.pack(fill="both", expand="yes")
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# create the sidebar canvas
sidebar_width = 179
cnv_sidebar = create_canvas(canvas, bg="#D0D0D0", height=canvas.winfo_height(), width=sidebar_width, bd=0, highlightthickness=0, relief="ridge", x=0, y=0)
cnv_sidebar.create_rectangle(0, -1.0, sidebar_width, canvas.winfo_height(), fill="#BCBEC0", outline="")

# # create the canvas for pdf view on window canvas
cnv_for_pdf_view = create_canvas(window, bg="red", bd=0, highlightthickness=0, relief="ridge", x=sidebar_width+1, y=0, relwidth=1.0, relheight=1.0)

sidebar_resize = sidebar_width
window.bind('<Configure>', lambda event, arg1=cnv_sidebar, arg2=cnv_for_pdf_view: resize_canvas(event, arg1, arg2))
cnv_sidebar.bind('<B1-Motion>', lambda event, arg1=sidebar_resize, arg2=cnv_sidebar, arg3=cnv_for_pdf_view:  resize_sidebar(event, arg1, arg2, arg3))
cnv_sidebar.bind("<Enter>", lambda event, arg1=cnv_sidebar: set_resize_cursor(event, arg1))
cnv_sidebar.bind("<Leave>", lambda event, arg1=cnv_sidebar: set_default_cursor(event, arg1))

window.mainloop()
