import pygame
from searchs import uniform_search, uniform_search_manhattan, manhattan_distance_calculation, count_search
from draw_grid import create_grid, draw_map_and_update, thread_draw_map_and_update, drawing_map_on_the_screen, building_path, draw_informative_footer
from entry_screen_start import Entry_Screen_Start
from item import Item

from coordinate import Coordinate

def main():

	# width of the window dimension
	width = 882

	# height of the window dimension
	height = 940

	# Rows amount of square matrix
	rows = 42

	# Responsible to paint the desired position of the window
	mat_paint = []
	
	# Responsible to read the positions and calculate path cost in desired position
	mat_read = []

	# List with the final Path
	path_travelled = []
	
	# Responsible for graphic execution
	run = True
	
	# Start the Main Window
	# pylint: disable=maybe-no-member
	pygame.init()
	pygame.font.init()
	main_window = pygame.display.set_mode((width, height))
	pygame.display.set_caption("CHRISTOPHER AND MURILO - BLIND SEARCH FOR SHORTEST PATHS AND SEARCH WITH A*")

	# Creation of grids
	grids = create_grid(rows, width)

	# Read the file name and verify if the user wants the Uniform Search or Blind Search option 
	screen = Entry_Screen_Start()
	name = screen.inicializationName()
	name = name + '.txt'
	uniform_search_type =  screen.inicializationIsUniformSearch()

	# Verify if exist the file name and if the algorithm will read correctly
	try:
		myFile = open(name, "r")
		file = myFile.readlines()

		drawing_map_on_the_screen(file, grids, rows, mat_paint, mat_read)
		draw_informative_footer(main_window, 0, 0)
		
		# count to start and end
		count_positions = 0
		# Catch the positions start and end
		while count_positions < 2:	
			file[count_positions] = file[count_positions].strip()
			pos = file[count_positions].split(",")
			if count_positions == 0:
				start_localization_x = int(pos[0])
				start_localization_y = int(pos[1])
				mat_paint[start_localization_x][start_localization_y].paint_start_localization()
			else:
				destination_location_x = int(pos[0])
				destination_location_y = int(pos[1])
				mat_paint[destination_location_x][destination_location_y].paint_destination_location()
			count_positions += 1

		# Declaring the root the queue
		root = Item(start_localization_x, start_localization_y)
		end = Item(destination_location_x, destination_location_y)
		thread_draw_map_and_update(main_window, grids, rows, width, height)

		# Responsible for graphic execution
		while run:
			
			# If the user wants to quit the windows
			for event in pygame.event.get():
				# pylint: disable=maybe-no-member
				if event.type == pygame.QUIT:
					run = False

				# If the user presses enter
				if event.type == pygame.KEYDOWN:
					# pylint: disable=maybe-no-member
					if event.key == pygame.K_RETURN:
						if uniform_search_type:
							path_travelled = uniform_search(root, mat_paint, mat_read, destination_location_x, destination_location_y)
						else:
							path_travelled = uniform_search_manhattan(root, mat_paint, mat_read, destination_location_x, destination_location_y)

						building_path(file, grids, rows, mat_paint, mat_read, path_travelled, root, end, main_window)
						break
		# Close the file
		myFile.close()

	except:
		print("There is no file with this name!")

	# Close the pygame
	# pylint: disable=maybe-no-member	
	pygame.quit()
	pygame.font.quit()

main()