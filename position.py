import pygame

# Start the colors used
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (128, 128, 128)
GREY = (192, 192, 192)
BROWN = (101, 67, 33)
BLUE_SWAMP = (0, 94, 184)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
BACKGROUND = [0, 127, 255]

# Define positions and colors of the matrix or main screen
class Positions_And_Colors:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.width = width

	# Getters #
	def is_grid_color(self):
		return self.color == GREY

	def is_start_localization(self):
		return self.color == WHITE

	def is_destination_location(self):
		return self.color == BLACK

	def is_search(self):
		return self.color == YELLOW

	def is_search_bord(self):
		return self.color == ORANGE

	def is_solid_and_flat(self):
		return self.color == GREEN
	
	def is_mountainous(self):
		return self.color == BROWN

	def is_swamp(self):
		return self.color == BLUE_SWAMP

	def is_fire(self):
		return self.color == RED

	# SETTERS
	def paint_start_localization(self):
		self.color = WHITE

	def paint_destination_location(self):
		self.color = BLACK

	def paint_search(self):
		self.color = YELLOW
	
	def paint_search_bord(self):
		self.color = ORANGE

	def paint_solid_and_flat(self):
		self.color = GREEN

	def paint_mountainous(self):
		self.color = BROWN

	def paint_swamp(self):
		self.color = BLUE_SWAMP

	def paint_fire(self):
		self.color = RED

	def paint_path(self):
		self.color = GREY

	def paint_bord_position_empty(self):
		self.color = WHITE

	# Draw the grids
	def draw(self, main_window):
		pygame.draw.rect(main_window, self.color, (self.x, self.y, self.width, self.width))