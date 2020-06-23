import tkinter as tk
import tkinter.font as tkfont

class AboutCGOL:

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Conway's Game of Life")
		self.window.geometry("800x600")
		self.setup_title()

	def setup_title(self):
		frm_game_name = tk.Frame(master = self.window)
		title_font = tkfont.Font(size = 60)
		lbl_game_name = tk.Label(master = frm_game_name, text = "Conway's Game \nOf Life", font = title_font, anchor = 'center')

		frm_game_name.pack()
		lbl_game_name.pack()


	def run(self):

		self.window.mainloop()