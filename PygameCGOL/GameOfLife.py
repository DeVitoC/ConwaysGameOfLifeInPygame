import pygame
import sys
import random

class GameOfLife:
	def __init__(self, screen_width=800, screen_height=600, cell_size=10, alive_color=(255, 0, 255), dead_color=(0, 0, 0)):
		self.cell_size = cell_size
		self.alive_color = alive_color
		self.dead_color = dead_color

		self.num_cols = screen_width // cell_size
		self.num_rows = screen_height // cell_size

		pygame.init()
		self.screen = pygame.display.set_mode(pygame(screen_width, screen_height))
		pygame.display.flip()



	def run(self):
		while True:
			# needs to recognize a command to quit and when the app window is closed
			self.handle_events()

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