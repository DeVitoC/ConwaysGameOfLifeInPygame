import pygame
import sys
import random
import pygame_gui

from pygame.locals import (
	K_1,
	K_2,
	K_3,
	K_4,
	K_5,
	K_q,
	K_p,
	K_MINUS,
	K_EQUALS,
	QUIT,
)


class GameOfLife:
	def __init__(self, screen_width = 800,
						screen_height = 700,
						cell_size = 10,
						alive_color = "turquoise",
						dead_color = "white",
						speed = 4,
						preset = "random"):
		self.cell_size = cell_size
		self.alive_color = alive_color
		self.dead_color = dead_color

		self.num_cols = screen_width // cell_size
		self.num_rows = (screen_height - 100) // cell_size
		self.current_game_board = []
		self.inactive_board = []

		self.is_paused = False
		self.did_quit = False
		self.speed = speed
		self.last_update_time = 0

		self.preset = preset
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.setup_game_board()
		self.set_board()

		pygame.init()
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		self.clear_screen()
		# self.manager = pygame_gui.UIManager((800, 700), 'button_theme.json')
		pygame.display.flip()

	#######################
	# View methods:
	#######################

	def setup_game_board(self):
		self.current_game_board = self.create_2d_board()
		self.inactive_board = self.create_2d_board()

	def draw_board(self):
		self.clear_screen()
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				if self.current_game_board[row][col] == 1:
					color = self.alive_color
				else:
					color = self.dead_color
				pygame.draw.circle(self.screen,
										color,
										(col * self.cell_size + (self.cell_size // 2),
										row * self.cell_size + (self.cell_size // 2)),
										self.cell_size // 2,
										0)
		self.setup_button("Random", 25, 625, action = self.set_random)
		self.setup_button("Gosper Gun", 130, 625, action = self.set_option1)
		self.setup_button("Constructor", 235, 625, action = self.set_option2)
		self.setup_button("Stable Shapes", 340, 625, action = self.set_option3)
		self.setup_button("Spaceships", 445, 625, action = self.set_option4)
		if not self.is_paused:
			self.setup_button("Pause", 550, 625, width = 50, action = self.toggle_pause)
		self.setup_button("Quit", 725, 625, width = 50, action = self.quit)
		self.setup_button("Faster", 660, 625, width = 50, height = 25, action = self.faster)
		self.setup_button("Slower", 660, 650, width = 50, height = 25, action = self.slower)
		pygame.display.flip()


	def setup_button(self, msg, xcoord, ycoord, width = 100, height = 50, inactive_color = 'turquoise', active_color  = "light green", action = None):
		# self.hello_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((25, 625), (100, 50)), text = "Say Hello", manager = self.manager)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if xcoord + width > mouse[0] > xcoord and ycoord + height > mouse[1] > ycoord:
			pygame.draw.rect(self.screen, active_color, (xcoord, ycoord, width, height))

			if click[0] == 1 and action != None:
				action()
		else:
			pygame.draw.rect(self.screen, inactive_color, (xcoord, ycoord, width, height))
		smallText = pygame.font.Font("freesansbold.ttf", 12)
		textSurf, textRect = self.text_objects(msg, smallText)
		textRect.center = ((xcoord + (width / 2)), (ycoord + (height / 2)))
		self.screen.blit(textSurf, textRect)

	######################
	# Helper Methods
	######################

	def text_objects(self, text, font):
		textSurface = font.render(text, True, 'black')
		return textSurface, textSurface.get_rect()


	def create_2d_board(self):
		board = []
		for row in range(self.num_rows):
			cols = [0] * self.num_cols
			board.append(cols)
		return board

	def set_board(self):
		if self.preset == "random":
			for row in range(self.num_rows):
				for cols in range(self.num_cols):
					cell = random.choice([0, 1])
					self.current_game_board[row][cols] = cell
		elif self.preset == "option1":
			self.option1()
		elif self.preset == "option2":
			self.option2()
		elif self.preset == "option3":
			self.option3()
		elif self.preset == "option4":
			self.option4()

	def clear_screen(self):
		self.screen.fill(self.dead_color)

	def alternate_boards(self):
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				next_cell_state = self.check_surrounding_cells(row, col)
				self.inactive_board[row][col] = next_cell_state
		self.current_game_board, self.inactive_board = self.inactive_board, self.current_game_board

	def check_surrounding_cells(self, row_number, col_number):
		if self.preset == "option1" and (col_number == self.num_cols - 1 or row_number == self.num_rows - 1):
			return 0
		current_cell = (col_number, row_number)
		prev_col = self.set_prev_col(col_number)
		next_col = self.set_next_col(col_number)
		prev_row = self.set_prev_row(row_number)
		next_row = self.set_next_row(row_number)

		num_alive_neighbors = 0
		current_cell_value = 0
		for col in [prev_col, current_cell[0], next_col]:
			for row in [prev_row, current_cell[1], next_row]:
				if col == current_cell[0] and row == current_cell[1]:
					current_cell_value = self.current_game_board[row][col]
				elif self.current_game_board[row][col] == 1:
					num_alive_neighbors += 1
		return self.test_alive_state(current_cell_value, num_alive_neighbors)

	def set_prev_col(self, col):
		if col == 0:
			return self.num_cols - 1
		else:
			return col - 1

	def set_next_col(self, col):
		if col == self.num_cols - 1:
			return 0
		else:
			return col + 1

	def set_prev_row(self, row):
		if row == 0:
			return self.num_rows - 1
		else:
			return row - 1

	def set_next_row(self, row):
		if row == self.num_rows - 1:
			return 0
		else:
			return row + 1

	@staticmethod
	def test_alive_state(current_cell, num_alive_neighbors):
		# Cell dies
		if num_alive_neighbors > 3:
			return 0
		elif num_alive_neighbors < 2:
			return 0
		# Dead Cells come to life
		elif current_cell == 0 and num_alive_neighbors == 3:
			return 1
		# Staying alive
		elif current_cell == 1:
			return 1
		# All cases should be accounted for, but just in case,
		# return dead since cell won't have 2 or 3 live neighbors or be dead with 3 live neighbors
		else:
			return 0

	def handle_events(self):
		for event in pygame.event.get():
			# User has closed the window manually
			if event.type == QUIT:
				sys.exit()

			# if event.type == pygame.USEREVENT:
			# 	if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
			# 		if event.ui_element == self.hello_button:
			# 			print("Hello World")
			# self.manager.process_events(event)

			# User pressed a button
			# elif event.type == KEYDOWN:
		pressed_keys = pygame.key.get_pressed()
				# user can press "q" to quit
		if pressed_keys[K_q]:
			self.quit()
		# user can press "p" to toggle between play and pause
		elif pressed_keys[K_p]:
			self.toggle_pause()
		# user chooses preset 1 with "1"
		elif pressed_keys[K_1]:
			self.set_random()
		# user chooses preset 2 with "2"
		elif pressed_keys[K_2]:
			self.set_option1()
		# user chooses preset 3 with "3"
		elif pressed_keys[K_3]:
			self.set_option2()
		# user chooses preset 4 with "4"
		elif pressed_keys[K_4]:
			self.set_option3()
		# user chooses preset 5 with "5"
		elif pressed_keys[K_5]:
			self.set_option4()
		# User can press "-" to slow the game
		elif pressed_keys[K_MINUS]:
			self.slower()
		# uset can press "+" to speed up the game
		elif pressed_keys[K_EQUALS]:
			self.faster()


	def reset_screen(self):
		self.current_game_board = []
		self.inactive_board = []
		self.current_game_board = self.create_2d_board()
		self. inactive_board = self.create_2d_board()


	def set_random(self):
		self.preset = "random"
		self.reset_screen()
		self.set_board()

	def set_option1(self):
		self.preset = "option1"
		self.reset_screen()
		self.set_board()

	def set_option2(self):
		self.preset = "option2"
		self.reset_screen()
		self.set_board()

	def set_option3(self):
		self.preset = "option3"
		self.reset_screen()
		self.set_board()

	def set_option4(self):
		self.preset = "option4"
		self.reset_screen()
		self.set_board()

	def toggle_pause(self):
		self.is_paused = not self.is_paused

	def quit(self):
		self.did_quit = True

	def faster(self):
		self.speed += 1

	def slower(self):
		if self.speed < 2:
			return
		self.speed -= 1

	####################
	# Premade Patterns
	####################

	def option1(self):
		# set alive cells for Gosper glider gun
		self.current_game_board[2][26] = 1
		self.current_game_board[3][24] = 1
		self.current_game_board[3][26] = 1
		self.current_game_board[4][14] = 1
		self.current_game_board[4][15] = 1
		self.current_game_board[4][22] = 1
		self.current_game_board[4][23] = 1
		self.current_game_board[4][36] = 1
		self.current_game_board[4][37] = 1
		self.current_game_board[5][13] = 1
		self.current_game_board[5][17] = 1
		self.current_game_board[5][22] = 1
		self.current_game_board[5][23] = 1
		self.current_game_board[5][36] = 1
		self.current_game_board[5][37] = 1
		self.current_game_board[6][2] = 1
		self.current_game_board[6][3] = 1
		self.current_game_board[6][12] = 1
		self.current_game_board[6][18] = 1
		self.current_game_board[6][22] = 1
		self.current_game_board[6][23] = 1
		self.current_game_board[7][2] = 1
		self.current_game_board[7][3] = 1
		self.current_game_board[7][12] = 1
		self.current_game_board[7][16] = 1
		self.current_game_board[7][18] = 1
		self.current_game_board[7][19] = 1
		self.current_game_board[7][24] = 1
		self.current_game_board[7][26] = 1
		self.current_game_board[8][12] = 1
		self.current_game_board[8][18] = 1
		self.current_game_board[8][26] = 1
		self.current_game_board[9][13] = 1
		self.current_game_board[9][17] = 1
		self.current_game_board[10][14] = 1
		self.current_game_board[10][15] = 1


	def option2(self):
		for col in range(2, 10):
			self.current_game_board[self.num_rows // 2][col] = 1
		for col in range(11, 16):
			self.current_game_board[self.num_rows // 2][col] = 1
		for col in range(19, 22):
			self.current_game_board[self.num_rows // 2][col] = 1
		for col in range(28, 35):
			self.current_game_board[self.num_rows // 2][col] = 1
		for col in range(36, 40):
			self.current_game_board[self.num_rows // 2][col] = 1


	def option3(self):
		# Block
		self.current_game_board[2][2] = 1
		self.current_game_board[2][3] = 1
		self.current_game_board[3][2] = 1
		self.current_game_board[3][3] = 1

		# Bee-hive
		self.current_game_board[6][3] = 1
		self.current_game_board[6][4] = 1
		self.current_game_board[7][2] = 1
		self.current_game_board[7][5] = 1
		self.current_game_board[8][3] = 1
		self.current_game_board[8][4] = 1

		# Loaf
		self.current_game_board[11][3] = 1
		self.current_game_board[11][4] = 1
		self.current_game_board[12][2] = 1
		self.current_game_board[12][5] = 1
		self.current_game_board[13][3] = 1
		self.current_game_board[13][5] = 1
		self.current_game_board[14][4] = 1

		# Boat
		self.current_game_board[17][2] = 1
		self.current_game_board[17][3] = 1
		self.current_game_board[18][2] = 1
		self.current_game_board[18][4] = 1
		self.current_game_board[19][3] = 1

		# Tub
		self.current_game_board[22][3] = 1
		self.current_game_board[23][2] = 1
		self.current_game_board[23][4] = 1
		self.current_game_board[24][3] = 1

		# Blinker
		for col in range(15, 18):
			self.current_game_board[2][col] = 1

		# Toad
		for col in range(16, 19):
			self.current_game_board[6][col] = 1
		for col in range(15, 18):
			self.current_game_board[7][col] = 1

		# Beacon
		self.current_game_board[13][15] = 1
		self.current_game_board[13][16] = 1
		self.current_game_board[14][15] = 1
		self.current_game_board[14][16] = 1
		self.current_game_board[15][17] = 1
		self.current_game_board[15][18] = 1
		self.current_game_board[16][17] = 1
		self.current_game_board[16][18] = 1

		# Pulsar
		for col in range(18, 21):
			self.current_game_board[23][col] = 1
			self.current_game_board[28][col] = 1
			self.current_game_board[30][col] = 1
			self.current_game_board[35][col] = 1
		for col in range(24, 27):
			self.current_game_board[23][col] = 1
			self.current_game_board[28][col] = 1
			self.current_game_board[30][col] = 1
			self.current_game_board[35][col] = 1
		for row in range(25, 28):
			self.current_game_board[row][16] = 1
			self.current_game_board[row][21] = 1
			self.current_game_board[row][23] = 1
			self.current_game_board[row][28] = 1
		for row in range(31, 34):
			self.current_game_board[row][16] = 1
			self.current_game_board[row][21] = 1
			self.current_game_board[row][23] = 1
			self.current_game_board[row][28] = 1


	def option4(self):
		# Light-weight Spaceship
		self.current_game_board[3][5] = 1
		self.current_game_board[3][6] = 1
		self.current_game_board[4][3] = 1
		self.current_game_board[4][4] = 1
		self.current_game_board[4][6] = 1
		self.current_game_board[4][7] = 1
		for col in range(3, 7):
			self.current_game_board[5][col] = 1
		self.current_game_board[6][4] = 1
		self.current_game_board[6][5] = 1

		# Middle-weight Spaceship
		for col in range(4, 9):
			self.current_game_board[11][col] = 1
		self.current_game_board[12][3] = 1
		self.current_game_board[12][8] = 1
		self.current_game_board[13][8] = 1
		self.current_game_board[14][3] = 1
		self.current_game_board[14][7] = 1
		self.current_game_board[15][5] = 1

		# Heavy-weight Spaceship
		self.current_game_board[20][7] = 1
		self.current_game_board[20][8] = 1
		for col in range(3, 7):
			self.current_game_board[21][col] = 1
		self.current_game_board[21][8] = 1
		self.current_game_board[21][9] = 1
		for col in range(3, 9):
			self.current_game_board[22][col] = 1
		for col in range(4, 8):
			self.current_game_board[23][col] = 1

		# Backwards
		# Light-weight Spaceship
		self.current_game_board[28][-5] = 1
		self.current_game_board[28][-6] = 1
		self.current_game_board[29][-3] = 1
		self.current_game_board[29][-4] = 1
		self.current_game_board[29][-6] = 1
		self.current_game_board[29][-7] = 1
		for col in range(-3, -7, -1):
			self.current_game_board[30][col] = 1
		self.current_game_board[31][-4] = 1
		self.current_game_board[31][-5] = 1

		# Middle-weight Spaceship
		for col in range(-4, -9, -1):
			self.current_game_board[36][col] = 1
		self.current_game_board[37][-3] = 1
		self.current_game_board[37][-8] = 1
		self.current_game_board[38][-8] = 1
		self.current_game_board[39][-3] = 1
		self.current_game_board[39][-7] = 1
		self.current_game_board[40][-5] = 1

		# Heavy-weight Spaceship
		self.current_game_board[45][-7] = 1
		self.current_game_board[45][-8] = 1
		for col in range(-3, -7, -1):
			self.current_game_board[46][col] = 1
		self.current_game_board[46][-8] = 1
		self.current_game_board[46][-9] = 1
		for col in range(-3, -9, -1):
			self.current_game_board[47][col] = 1
		for col in range(-4, -8, -1):
			self.current_game_board[48][col] = 1


	####################
	# Run loop
	####################

	def run(self):
		clock = pygame.time.Clock()
		while True:
			# needs to handle events
			self.handle_events()
			if self.did_quit:
				pygame.display.quit()
				break
			# handles pause condition while still listening to events
			if self.is_paused:
				clock.tick(self.speed)
				self.setup_button("Play", 550, 625, width = 50, action = self.toggle_pause)
				self.setup_button("Next", 605, 625, width = 50)
				pygame.display.flip()
				continue
			# Switch between current and inactive game boards
			self.alternate_boards()
			# Draw the current game board on the screen
			self.draw_board()
			clock.tick(self.speed)


if __name__ == '__main__':
	game = GameOfLife()
	game.run()
