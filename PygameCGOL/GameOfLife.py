import pygame
import sys
import random


class GameOfLife:
	def __init__(self, screen_width = 1000,
						screen_height = 600,
						cell_size = 10,
						alive_color = "turquoise",
						dead_color = "black",
						speed = 4,
						preset = "random"):
		self.cell_size = cell_size
		self.alive_color = alive_color
		self.dead_color = dead_color

		self.num_cols = screen_width // cell_size
		self.num_rows = screen_height // cell_size
		self.current_game_board = []
		self.inactive_board = []

		self.is_paused = False
		self.speed = speed
		self.last_update_time = 0
		self.desired_time_between_updates = (1 / self.speed) * 1000

		self.preset = preset
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.setup_game_board()
		self.set_board()

		pygame.init()
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		self.clear_screen()
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
		pygame.display.flip()

	######################
	# Helper Methods
	######################

	def create_2d_board(self):
		board = []
		for row in range(self.num_rows):
			cols = [0] * self.num_cols
			board.append(cols)
		return board

	def set_board(self):
		print(self.preset)
		if self.preset == "random":
			for row in range(self.num_rows):
				for cols in range(self.num_cols):
					cell = random.choice([0, 1])
					self.current_game_board[row][cols] = cell
		elif self.preset == "option1":
			self.option1()
			print("option1")
		elif self.preset == "option1":
			print("this will be preset 2")
		elif self.preset == "option2":
			print("this will be preset 3")
		elif self.preset == "option3":
			print("this will be preset 4")

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

	def set_speed(self):
		now = pygame.time.get_ticks()
		time_since_last_update = now - self.last_update_time
		time_to_delay = self.desired_time_between_updates - time_since_last_update
		if time_to_delay > 0:
			pygame.time.delay(int(time_to_delay))
		self.last_update_time = now

	def handle_events(self):
		for event in pygame.event.get():
			# User has closed the window manually
			if event.type == pygame.QUIT:
				sys.exit()
			# User pressed a button
			elif event.type == pygame.KEYDOWN:
				# user can press "q" to quit
				if event.unicode == 'q':
					# pygame.quit()
					sys.exit()
				elif event.unicode == 'p':
					self.is_paused = not self.is_paused
				elif event.unicode == 'r':
					self.set_board()
				elif event.unicode == '-':
					if self.speed < 2:
						return
					self.speed -= 1
					self.desired_time_between_updates = (1 / self.speed) * 1000
				elif event.unicode == '+':
					self.speed += 1
					self.desired_time_between_updates = (1 / self.speed) * 1000

	####################
	# Premade Patterns
	####################

	def option1(self):
		# set board to all dead
		# for row in range(self.num_rows):
		# 	for cols in range(self.num_cols):
		# 		self.current_game_board[row][cols] = 0

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




	####################
	# Run loop
	####################

	def run(self):
		clock = pygame.time.Clock()
		while True:
			# needs to handle events
			self.handle_events()
			# handles pause condition while still listening to events
			if self.is_paused:
				continue
			# Switch between current and inactive game boards
			self.alternate_boards()
			# Draw the current game board on the screen
			self.draw_board()
			clock.tick(self.speed)
			# Control speed by waiting after each iteration
			# self.set_speed()


if __name__ == '__main__':
	game = GameOfLife()
	game.run()
