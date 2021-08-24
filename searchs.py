import math, copy
from item import Item, cost_read
from coordinate import Coordinate

global count_search, path_distance
count_search = 0
path_distance = math.inf

def is_present(vet, new_coordinate):
	for coordinate in vet:
		if((coordinate.get_x()== new_coordinate.get_x()) and (coordinate.get_y()== new_coordinate.get_y())):
			return True 
	return False

# Method used to return the path of Uniform Search
def uniform_search(root, mat_paint, mat_read, destination_location_x, destination_location_y):
	q = []  # declaring the queue
	visited_positions = [] 
	q.append(root)
	global count_search, path_distance

	current_position = q.pop(0)
	count_search = 1
	visited_positions.append(current_position.get_item_coordinate())
	current_position.update_vet(Coordinate(current_position.item_coordinate.get_x(), current_position.item_coordinate.get_y()))

	while True:
		mat_paint[current_position.item_coordinate.get_x()][current_position.item_coordinate.get_y()].paint_search()

		if current_position.item_coordinate.get_x() == destination_location_x and current_position.item_coordinate.get_y() == destination_location_y:
			if current_position.get_total_cost() < path_distance:
				path_distance = current_position.get_total_cost()
				path_travelled = copy.copy(current_position.get_vet())
				print("Custo do caminho encontrado: ", path_distance)
				break		
		else:
			if current_position.item_coordinate.get_x() > 0 : # Search Up			
				next_position = Item((current_position.item_coordinate.get_x() - 1), current_position.item_coordinate.get_y()) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)		

			if current_position.item_coordinate.get_x() < 41 : # Search Down
				next_position=Item((current_position.item_coordinate.get_x() + 1), current_position.item_coordinate.get_y()) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)
														
			if current_position.item_coordinate.get_y() > 0 : # Search Left	
				next_position=Item((current_position.item_coordinate.get_x()), current_position.item_coordinate.get_y() - 1) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)

			if( current_position.item_coordinate.get_y() < 41): # Search Right
				next_position = Item((current_position.item_coordinate.get_x()), current_position.item_coordinate.get_y() + 1) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)
			q.sort(key=lambda x: x.get_total_cost()) # Sorts the queue in relation to cost vector

		while(is_present(visited_positions, current_position.get_item_coordinate())):
			current_position = q.pop(0)
			count_search += 1
			mat_paint[current_position.item_coordinate.get_x()][current_position.item_coordinate.get_y()].paint_search()
		
		visited_positions.append(current_position.get_item_coordinate())
		
	print("Quantidade de nos que o algoritmo buscou: ", count_search)
	return path_travelled

# Method used to return the path of A*
def uniform_search_manhattan(root, mat_paint, mat_read, destination_location_x, destination_location_y):
	q = []  # declaring the queue 
	visited_positions = []
	q.append(root)
	global count_search, path_distance

	current_position = q.pop(0)
	count_search = 1
	visited_positions.append(current_position.get_item_coordinate())
	current_position.update_vet(Coordinate(current_position.item_coordinate.get_x(), current_position.item_coordinate.get_y()))
 
	while True:
		mat_paint[current_position.item_coordinate.get_x()][current_position.item_coordinate.get_y()].paint_search()
		if current_position.item_coordinate.get_x() == destination_location_x and current_position.item_coordinate.get_y() == destination_location_y:
			if current_position.get_total_cost() < path_distance:
				path_distance = current_position.get_total_cost_manhattan()
				path_travelled = copy.copy(current_position.get_vet())
				print("Custo do caminho encontrado: ", path_distance)
				break	
		else:
			if current_position.item_coordinate.get_x() > 0 : # Search Up			
				next_position = Item((current_position.item_coordinate.get_x() - 1), current_position.item_coordinate.get_y()) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_total_cost_manhattan(next_position.get_total_cost() + manhattan_distance_calculation(mat_read, next_position.get_item_coordinate(), destination_location_x, destination_location_y))
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)		

			if current_position.item_coordinate.get_x() < 41 : # Search Down		
				next_position=Item((current_position.item_coordinate.get_x() + 1), current_position.item_coordinate.get_y()) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_total_cost_manhattan(next_position.get_total_cost() + manhattan_distance_calculation(mat_read,next_position.get_item_coordinate(), destination_location_x, destination_location_y))
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)
														
			if current_position.item_coordinate.get_y() > 0 : # Search Left	
				next_position=Item((current_position.item_coordinate.get_x()), current_position.item_coordinate.get_y() - 1) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_total_cost_manhattan(next_position.get_total_cost() + manhattan_distance_calculation(mat_read,next_position.get_item_coordinate(), destination_location_x, destination_location_y))
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)

			if( current_position.item_coordinate.get_y() < 41): # Search Right
				next_position = Item((current_position.item_coordinate.get_x()), current_position.item_coordinate.get_y() + 1) # Add next position
				mat_paint[next_position.item_coordinate.get_x()][next_position.item_coordinate.get_y()].paint_search_bord() # Paint the desired position of the matrix of orange
				next_position.set_total_cost(current_position.get_total_cost() + cost_read(mat_read,next_position.item_coordinate.get_x(), next_position.item_coordinate.get_y())) # Set the total cost so far
				next_position.set_total_cost_manhattan(next_position.get_total_cost() + manhattan_distance_calculation(mat_read,next_position.get_item_coordinate(), destination_location_x, destination_location_y))
				next_position.set_vet(current_position.get_vet())
				next_position.update_vet(next_position.get_item_coordinate())
				q.append(next_position)
			
			q.sort(key=lambda x: x.get_total_cost_manhattan()) # Sorts the queue in relation to cost vector
		
		if len(q) == 0:
			break
			
		while(is_present(visited_positions, current_position.get_item_coordinate())):
			current_position = q.pop(0)
			count_search += 1
			mat_paint[current_position.item_coordinate.get_x()][current_position.item_coordinate.get_y()].paint_search()

		visited_positions.append(current_position.get_item_coordinate())

	print("Quantidade de nos que o algoritmo buscou: ", count_search)
	return path_travelled

# Calculates manhattan distance
def manhattan_distance_calculation(mat_read, coordinate, goal_x, goal_y):
	return abs(coordinate.get_x()-goal_x) + abs(coordinate.get_y()-goal_y)