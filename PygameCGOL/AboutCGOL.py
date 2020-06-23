import tkinter as tk
import tkinter.font as tkfont

class AboutCGOL:

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Conway's Game of Life")
		self.window.geometry("800x600")
		self.setup_title()
		self.setup_game_description()
		self.setup_exit_button()


	def setup_title(self):
		frm_game_name = tk.Frame(master = self.window)
		title_font = tkfont.Font(size = 60)
		lbl_game_name = tk.Label(master = frm_game_name, text = "Conway's Game \nOf Life", font = title_font, anchor = 'center')

		frm_game_name.pack()
		lbl_game_name.pack()


	def setup_game_description(self):
		frm_game_description = tk.Frame(master = self.window)
		description = ""
		with open("game_description.txt") as file:
			for line in file:
				description += line
		lbl_game_description = tk.Label(master = frm_game_description, text = description, justify = tk.LEFT)

		frm_game_description.pack()
		lbl_game_description.pack()


	def setup_exit_button(self):
		frm_exit = tk.Frame(master = self.window)
		exit_button = tk.Button(master = frm_exit, text = "OK", command = self.exit_window, padx = 10, pady = 10, relief = tk.RAISED)

		frm_exit.pack()
		exit_button.pack()


	def exit_window(self):
		self.window.destroy()


	def run(self):

		self.window.mainloop()