from coordinate import Coordinate
import copy

# Objects itens or positions of the matrix or main screen
class Item:
	def __init__(self, x, y):
		self.__vet = []
		self.__total_cost=0
		self.item_coordinate = Coordinate(x,y)
		self.__total_cost_manhattan = 0

	def set_total_cost(self, cost):
		self.__total_cost = cost

	def set_total_cost_manhattan(self, cost):
		self.__total_cost_manhattan = cost
	
	def get_vet(self):
		return self.__vet

	def get_total_cost(self):
		return self.__total_cost

	def get_total_cost_manhattan(self):
		return self.__total_cost_manhattan
	
	def get_item_coordinate(self):
		return self.item_coordinate

	def update_vet(self, Coordinate):
		self.__vet.append(Coordinate)

	def is_present(self, new_coordinate):
		for coordinate in self.__vet:
			if((coordinate.get_x()== new_coordinate.get_x()) and (coordinate.get_y()== new_coordinate.get_y())):
				return True 
		return False
	
	def set_vet(self,coordinateList):
		self.__vet =  copy.copy(coordinateList)
	
def cost_read(mat, x, y):
	if mat[x][y] == 1:
		return 1
	elif mat[x][y] == 2:
		return 5
	elif mat[x][y] == 3:
		return 10
	else:
		return 15
