import tkinter as tk
import tkinter.font as tkfont
import importlib

gol = importlib.import_module("GameOfLife")
about = importlib.import_module("AboutCGOL")
kc = importlib.import_module("KeyCommands")

window = tk.Tk()
window.title("Conway's Game of Life")
window.geometry("800x600")

speed = tk.IntVar()
speed.set(4)
alive_color = tk.StringVar()
alive_color.set("turquoise")
cell_size = tk.IntVar()
cell_size.set(10)
preset = "random"


frm_game_name = tk.Frame(master = window)
title_font = tkfont.Font(size = 60)
lbl_game_name = tk.Label(master = frm_game_name, text = "Conway's Game \nOf Life", font = title_font, anchor = 'center')

frm_game_name.pack()
lbl_game_name.pack()


def start_random():
	global preset
	preset = "random"
	start_game()


def start_opt1():
	global preset
	preset = "option1"
	start_game()


def start_opt2():
	global preset
	preset = "option2"
	start_game()


def start_opt3():
	global preset
	preset = "option3"
	start_game()


def start_opt4():
	global preset
	preset = "option4"
	start_game()


def start_game():
	game = gol.GameOfLife(cell_size = cell_size.get(),
							alive_color = alive_color.get(),
							speed = speed.get(),
							preset = preset)
	game.run()


frm_start_options = tk.Frame(master = window, pady = 20)
btn_random = tk.Button(master = frm_start_options, text = "Random", command = start_random, pady = 10)
btn_opt1 = tk.Button(master = frm_start_options, text = "Gosper Glider Gun", command = start_opt1, pady = 10)
btn_opt2 = tk.Button(master = frm_start_options, text = "Constructor", command = start_opt2, pady = 10)
btn_opt3 = tk.Button(master = frm_start_options, text = "Stable Shapes", command = start_opt3, pady = 10)
btn_opt4 = tk.Button(master = frm_start_options, text = "Spaceships", command = start_opt4, pady = 10)

frm_start_options.pack()
btn_random.grid(row = 1, column = 1, padx = 20)
btn_opt1.grid(row = 1, column = 2, padx = 20)
btn_opt2.grid(row = 1, column = 3, padx = 20)
btn_opt3.grid(row = 1, column = 4, padx = 20)
btn_opt4.grid(row = 1, column = 5, padx = 20)


frm_alive_color = tk.Frame(master = window, pady = 20, padx = 20)
rdb_turquoise = tk.Radiobutton(frm_alive_color, text= "Turquoise", variable=alive_color,
								value= "turquoise", fg = "turquoise")
rdb_red = tk.Radiobutton(frm_alive_color, text="Red", variable=alive_color, value="red", fg = "red")
rdb_blue = tk.Radiobutton(frm_alive_color, text="Blue", variable=alive_color, value="blue", fg = "blue")
rdb_green = tk.Radiobutton(frm_alive_color, text="Green", variable=alive_color, value="green", fg = "green")
rdb_orange = tk.Radiobutton(frm_alive_color, text="Orange", variable=alive_color, value="orange", fg = "orange")
rdb_purple = tk.Radiobutton(frm_alive_color, text="Purple", variable=alive_color, value="purple", fg = "purple")

frm_alive_color.pack(side = tk.LEFT)
rdb_turquoise.grid(row = 1, column = 1, sticky = 'w')
rdb_red.grid(row = 2, column = 1, sticky = 'w')
rdb_blue.grid(row = 3, column = 1, sticky = 'w')
rdb_green.grid(row = 1, column = 2, sticky = 'w')
rdb_orange.grid(row = 2, column = 2, sticky = 'w')
rdb_purple.grid(row = 3, column = 2, sticky = 'w')


frm_speed = tk.Frame(master = window, pady = 20, padx = 20)
rdb_fast_speed = tk.Radiobutton(frm_speed, text = "Fast", variable = speed, value = 15)
rdb_normal_speed = tk.Radiobutton(frm_speed, text = "Normal", variable = speed, value = 4)
rdb_slow_speed = tk.Radiobutton(frm_speed, text = "Slow", variable = speed, value = 1)

frm_speed.pack(side = tk.LEFT)
rdb_fast_speed.grid(row = 1, column = 1, sticky = 'w')
rdb_normal_speed.grid(row = 2, column = 1, sticky = 'w')
rdb_slow_speed.grid(row = 3, column = 1, sticky = 'w')


frm_size = tk.Frame(master = window, pady = 20, padx = 20)
rdb_large_size = tk.Radiobutton(frm_size, text = "Large", variable = cell_size, value = 20)
rdb_medium_size = tk.Radiobutton(frm_size, text = "Medium", variable = cell_size, value = 10, tristatevalue = 10)
rdb_small_size = tk.Radiobutton(frm_size, text = "Small", variable = cell_size, value = 6)

frm_size.pack(side = tk.LEFT)
rdb_large_size.grid(row = 1, column = 1, sticky = 'w')
rdb_medium_size.grid(row = 2, column = 1, sticky = 'w')
rdb_small_size.grid(row = 3, column = 1, sticky = 'w')


def display_about_cgol():
	about_cgol = about.AboutCGOL()
	about_cgol.run()


def display_commands():
	key_commands = kc.KeyCommands()
	key_commands.run()


frm_about = tk.Frame(master = window, pady = 20, padx = 20)
btn_about_cgol = tk.Button(master = frm_about, text = "About CGOL", command = display_about_cgol, pady = 10)
btn_about_commands = tk.Button(frm_about, text = "Key Commands", command = display_commands, pady = 10)

frm_about.pack(side = tk.LEFT)
btn_about_cgol.grid(row = 1, column = 1)
btn_about_commands.grid(row = 2, column = 1)


def exit_window():
	window.destroy()


frm_exit = tk.Frame(master = window)
exit_button = tk.Button(master = frm_exit, text = "OK", command = exit_window, padx = 10, pady = 10,
                        relief = tk.RAISED)

frm_exit.pack(side = tk.LEFT)
exit_button.pack()





window.mainloop()
