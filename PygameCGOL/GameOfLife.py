import pygame
import sys
import random

class GameOfLife:
	def __init__(self, screen_width=800, screen_height=600, cell_size=10, alive_color=(0, 255, 255), dead_color=(0, 0, 0)):
		self.cell_size = cell_size
		self.alive_color = alive_color
		self.dead_color = dead_color

		self.num_cols = screen_width // cell_size
		self.num_rows = screen_height // cell_size
		self.game_boards = []
		self.current_game_board = 0

		self.is_paused = False

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
		self.game_boards.append(self.create_2d_board())
		self.game_boards.append(self.create_2d_board())

	def draw_board(self):
		self.clear_screen()
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				if self.game_boards[self.current_game_board][row][col] == 1:
					color = self.alive_color
				else:
					color = self.dead_color
				pygame.draw.circle(self.screen,
				                   color,
				                   (col *  self.cell_size + (self.cell_size//2),
				                    row * self.cell_size + (self.cell_size//2)),
				                   self.cell_size//2,
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
		for row in range(self.num_rows):
			for cols in range(self.num_cols):
				cell = random.choice([0, 1])
				self.game_boards[self.current_game_board][row][cols] = cell

	def clear_screen(self):
		self.screen.fill(self.dead_color)

	def alternate_boards(self):
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				print("This is where the check for the 4 rules of the Game Of Life would happen - to be built)")
				# Temporarily just assigning a random value to make sure it's alternating correctly
				cell = random.choice([0, 1])
				self.game_boards[self.current_game_board][row][col] = cell
		self.current_game_board = (self.current_game_board + 1) % 2

	def handle_events(self):
		for event in pygame.event.get():
			# User has closed the window manually
			if event.type == pygame.QUIT:
				sys.exit()
			# User pressed a button
			elif event.type == pygame.KEYDOWN:
				# user can press "q" to quit
				if event.unicode == 'q':
					sys.exit()
				elif event.unicode == 'p':
					self.is_paused = not self.is_paused
				elif event.unicode == 'r':
					self.set_board()

	####################
	# Run loop
	####################

	def run(self):
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




if __name__ == '__main__':
	game = GameOfLife()
	game.run()