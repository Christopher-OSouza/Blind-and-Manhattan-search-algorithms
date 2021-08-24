import pygame, threading, time
from position import Positions_And_Colors, WHITE, RED, BACKGROUND
import searchs

global is_empty
is_empty = False

# Color of the grids
DARK_GREY = (105, 105, 105)

# Create the grids
def create_grid(rows, width):
	grid = []
	gap = width // rows
	for row in range(rows):
		grid.append([])
		for col in range(rows):
			position = Positions_And_Colors(row, col, gap, rows)
			grid[row].append(position)
	return grid

# Draw and paint the grids
def draw_and_pain_grid(main_window, rows, width):
	gap = width // rows
	for row in range(rows):
		pygame.draw.line(main_window, DARK_GREY, (0, row * gap), (width, row * gap))
		for col in range(rows):
			pygame.draw.line(main_window, DARK_GREY, (col * gap, 0), (col * gap, width))

# Draw, paint and update the map with a thread
def draw_map_and_update(main_window, grid, rows, width, height):	
	while not is_empty:	
		for row in grid:
			for position in row:
				position.draw(main_window)

		draw_and_pain_grid(main_window, rows, width)
		draw_borders(main_window, width, height)
		pygame.display.update()

# Creating the thread responsible for drawing
def thread_draw_map_and_update(main_window, grids, rows, width, height):
	threading.Thread(target = draw_map_and_update, args = (main_window, grids, rows, width, height)).start()

# Draw and paint the initial map on the window
def drawing_map_on_the_screen(file, grid, rows, mat_paint, mat_read):
	count=2 
	while(count < (rows+2)):
		file[count] = file[count].strip()
		row = 0
		pos = None
		line = file[count].split(",")
		mat_paint.append([])
		mat_read.append([])
		for typesOfTerrains in line:
			typesOfTerrains = int(typesOfTerrains)
			mat_read[count-2].append(typesOfTerrains)
			pos = grid[row][count-2]
			if typesOfTerrains == 1:
				pos.paint_solid_and_flat()
			elif typesOfTerrains == 2:
				pos.paint_mountainous()
			elif typesOfTerrains == 3:
				pos.paint_swamp()
			else:
				pos.paint_fire()
			mat_paint[count-2].append(pos)
			row += 1
		count += 1	

# Buildind the found path "Origin - destination"
def building_path(file, grids, rows, mat_paint, mat_read, path_travelled, root, end, main_window):
	#time.sleep(1)
	drawing_map_on_the_screen(file, grids, rows, mat_paint, mat_read)
	count_path = 1

	mat_paint[root.item_coordinate.get_x()][root.item_coordinate.get_y()].paint_start_localization()
	mat_paint[end.item_coordinate.get_x()][end.item_coordinate.get_y()].paint_destination_location()
	
	while(count_path < len(path_travelled)-1):
		mat_paint[path_travelled[count_path].get_x()][path_travelled[count_path].get_y()].paint_path()
		count_path += 1
		time.sleep(0.01)

	time.sleep(1)
	
	draw_informative_footer(main_window, searchs.count_search, searchs.path_distance)

	global is_empty
	is_empty = True

def draw_informative_footer(main_window, count_search, path_distance):
	main_window.fill(BACKGROUND)
	font_default = pygame.font.get_default_font()

	write_on_the_screen(main_window, 'QUANTIDADE DE NÓS VISITADOS: ', font_default, 30, 35, 900, WHITE, False)
	write_on_the_screen(main_window, 'CUSTO DO CAMINHO: ', font_default, 30, 585, 904, WHITE, False)
	write_on_the_screen(main_window, str(count_search), font_default, 40, 385, 899, RED, True)
	write_on_the_screen(main_window, str(path_distance), font_default, 40, 810, 899, RED, True)

def write_on_the_screen(screen, message, font, size, x, y, color, underline):
	myFont = pygame.font.SysFont(font, size)
	if(underline):
		myFont.set_underline(True)
	else:
		myFont.set_underline(False)
	text = myFont.render(message, False, color) 
	screen.blit(text, (x, y)) 

def draw_borders(main_window, width, height):
	pygame.draw.line(main_window, DARK_GREY, (0, width-2), (width, width-2), 5)
	pygame.draw.line(main_window, DARK_GREY, (0, height-3), (height, height-3), 5)
	pygame.draw.line(main_window, DARK_GREY, (0, 3), (width, 3), 5)
	pygame.draw.line(main_window, DARK_GREY, (3, 0), (3, height), 5)
	pygame.draw.line(main_window, DARK_GREY, (width-3, 0), (width-3, height), 5)