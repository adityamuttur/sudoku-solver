import copy
import threading

class FuncThread(threading.Thread):
	def __init__(self, func):
		threading.Thread.__init__(self)
		self.result = None
		self.func = func

	def run(self):
		self.result = self.func()

	def _stop(self):
		if self.isAlive():
			threading.Thread._Thread__stop(self)

class Solution(object):
	def __init__(self, input_grid):
		self.input_grid = input_grid
		self.grid_size = 81
		self.grid = copy.deepcopy(self.input_grid)
		self.is_solution = False

	def is_full(self):
		return self.grid.count('.') == 0

	def get_trial_cell_i(self):
		for i in xrange(self.grid_size):
			if self.grid[i] == '.':
				return i

	def is_legal(self, trial_value, trial_cell_i):
		cols = 0
		for each_square in xrange(9):
			trial_square = [x+cols for x in xrange(3)] + [x+9+cols for x in xrange(3)] + [x+18+cols for x in xrange(3)]
			cols +=3
			if cols in [9, 36]:
				cols +=18
			if trial_cell_i in trial_square:
				for i in trial_square:
					if self.grid[i] != '.':
						if trial_value == int(self.grid[i]):
							return False

		for each_row in xrange(9):
			trial_row = [ x+(9*each_row) for x in xrange (9) ]
			if trial_cell_i in trial_row:
				for i in trial_row:
					if self.grid[i] != '.':
						if trial_value == int(self.grid[i]):
							return False

		for each_col in xrange(9):
			trial_col = [ (9*x)+each_col for x in xrange (9) ]
			if trial_cell_i in trial_col:
				for i in trial_col:
					if self.grid[i] != '.':
						if trial_value == int(self.grid[i]):
							return False
		return True

	def set_cell(self, trial_value, trial_cell_i):
		self.grid[trial_cell_i] = trial_value
		return self.grid

	def clear_cell(self, trial_cell_i ):
		self.grid[trial_cell_i] = '.'
		return self.grid

	def _has_solution(self):
		if self.is_full():
			return True
		else:
			trial_cell_i = self.get_trial_cell_i()
			trial_value = 1
			solution_found = False
			while (solution_found != True) and (trial_value < 10):
				if self.is_legal(trial_value, trial_cell_i):
					self.grid = self.set_cell(trial_value, trial_cell_i)
					if self._has_solution() == True:
						solution_found = True
						self.is_solution = solution_found
						return True
					else:
						self.clear_cell( trial_cell_i )
				trial_value += 1
			self.is_solution = solution_found
			return solution_found

	def has_solution(self):
		it = FuncThread(self._has_solution)
		# starts the thread....
		it.start()
		# blocks the main thread for 5 seconds and then returns
		# parallel to the execution of the other function
		it.join(5)
		if it.isAlive():
			# if the thread is still alive after 5 secs, kill it
			# not sure of the after effects of terminating a thread like this
			# throws unhandled excecptions when the django-server is stopped
			it._stop()
			return False
		else:
			return it.result

	def return_grid(self=None):
		if not self.has_solution():
			# Calling has_solution not only checks if the sudoku has a solution
			# but is also responsible for setting the solution to the grid into 
			# self.grid list element
			# Thus has_solution() HAS TO BE called here in order to set the solution
			# Solution is set into a single list called self.grid
			return False
		i = 0
		solution_grid = []
		solution_row = []
		# The following for loop is only responsible for converting the linear
		# list into a 2d square grid type(nested list)
		for val in self.grid:
			solution_row.append(int(val))
			i +=1
			if i in [ (x*9) for x in xrange(10)]:
				solution_grid.append(solution_row)
				solution_row = []

		return solution_grid
