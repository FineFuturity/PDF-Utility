import header as prog

class App(prog.tk.Tk):
		def __init__(self):
			super().__init__()
			# load initial window properties from consts in header
			self.title(prog.TITLE + self.curr_file)
			self.geometry(prog.GEOMETRY)

			# custom window properties, widget and definition
			self.curr_file = "Untitled"
			self.mnbr = prog.tk.Menu(self)
			self.load_widgets()
			self.init_bindings()

		def load_widgets(self):
			self.make_base_mnbr()

		def make_base_mnbr(self):

			filemenu = prog.tk.Menu(self.mnbr, tearoff=0)
			# filemenu.add_command(label="New...", command=lambda: self.do_nothing, accelerator="Ctrl + N", underline=0)
			filemenu.add_command(label="Open...", command=lambda: self.open_file(), accelerator="Ctrl + O", underline=0)
			filemenu.add_command(label=prog.NOT_DONE_YET, command=lambda: self.CMD_STUB)
			filemenu.add_separator()
			filemenu.add_command(label="Save...", command=lambda: self.CMD_STUB, accelerator="Ctrl + S", underline=0)
			filemenu.add_command(label="Save As...", command=lambda: self.save_file_as(), accelerator="Ctrl + Shift + S")
			filemenu.add_separator()
			filemenu.add_command(label="Exit", command=self.quit, accelerator="Alt + F4")
			self.mnbr.add_cascade(label="File", underline=0, menu=filemenu)
			
			# self is confusing as it gets "overloaded" by the current object paradigm for a tkinter window
			self.config(menu=self.mnbr)

		def load_layout():


		def open_file(self, event=None):
			self.use_file(prog.fdlg.askopenfilename())

		def save_file_as(self, event=None):
			print(self.curr_file)

		def use_file(self, filepath):
			self.curr_file = filepath
			print(self.curr_file)

		def init_bindings(self):
			self.bind('<Alt-F4>', self.quit())
			self.bind('<Control-o>', lambda e: self.open_file(e))
			self.bind('<Control-S>', lambda e: self.save_file_as(e))

		def CMD_STUB(self):
			pass


if __name__ == "__main__":
		app = App()
		app.mainloop()