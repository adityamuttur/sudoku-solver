import re
import os
import random
import logging
import copy
import signal, os

def handler(signum, frame):
	signal.alarm(0)
	raise Exception("Couldn't Solve")

logger = logging.getLogger(__name__)

class Solution(object):
	def __init__(self, input_grid=None):
		if input_grid is None:
			input_grid = [
							'.', '.', '.', '.', '.', '.', '.', '.', '.', 
							'.', '.', '.', '.', '.', '.', '.', '.', '.', 
							'.', '.', '.', '.', '.', '.', '.', '.', '.',
							'.', '.', '.', '.', '.', '.', '.', '.', '.', 
							'.', '.', '4', '6', '2', '9', '5', '1', '8', 
							'1', '9', '6', '3', '5', '8', '2', '7', '4', 
							'4', '7', '3', '8', '9', '2', '6', '5', '1', 
							'6', '8', '.', '.', '3', '1', '.', '4', '.', 
							'.', '.', '.', '.', '.', '.', '3', '8', '.'
						]
		self.input_grid = input_grid
		self.grid_size = 81
		self.grid = copy.deepcopy(self.input_grid)

	def isFull(self):
		return self.grid.count('.') == 0

	def getTrialCelli(self):
		for i in xrange(self.grid_size):
			if self.grid[i] == '.':
				logger.info('trial cell %s' % i)
				return i

	def isLegal(self, trialVal, trialCelli):
		cols = 0
		for eachSq in xrange(9):
			trialSq = [ x+cols for x in xrange(3) ] + [ x+9+cols for x in xrange(3) ] + [ x+18+cols for x in xrange(3) ]
			cols +=3
			if cols in [9, 36]:
				cols +=18
			if trialCelli in trialSq:
				for i in trialSq:
					if self.grid[i] != '.':
						if trialVal == int(self.grid[i]):
							logger.info('SQU')
							return False

		for eachRow in xrange(9):
			trialRow = [ x+(9*eachRow) for x in xrange (9) ]
			if trialCelli in trialRow:
				for i in trialRow:
					if self.grid[i] != '.':
						if trialVal == int(self.grid[i]):
							logger.info('ROW')
							return False

		for eachCol in xrange(9):
			trialCol = [ (9*x)+eachCol for x in xrange (9) ]
			if trialCelli in trialCol:
				for i in trialCol:
					if self.grid[i] != '.':
						if trialVal == int(self.grid[i]):
							logger.info('COL')
							return False
		logger.info('is legal cell %s set to %s ' % (trialCelli, trialVal))
		return True

	def setCell(self, trialVal, trialCelli):
		self.grid[trialCelli] = trialVal
		return self.grid

	def clearCell(self, trialCelli ):
		self.grid[trialCelli] = '.'
		logger.info('clear cell %s' % trialCelli)
		return self.grid

	def _hasSolution(self):
		if self.isFull():
			logger.info('SOLVED')
			return True
		else:
			trialCelli = self.getTrialCelli()
			trialVal = 1
			solution_found = False
			while ( solution_found != True) and (trialVal < 10):
				logger.info('trial value %s' % trialVal)
				if self.isLegal(trialVal, trialCelli):
					self.grid = self.setCell(trialVal, trialCelli)
					if self._hasSolution() == True:
						solution_found = True
						return True
					else:
						self.clearCell( trialCelli )
				trialVal += 1
			return solution_found

	def hasSolution(self):
		try:
			signal.signal(signal.SIGALRM, handler)
			signal.alarm(5)
			return self._hasSolution()
		except:
			signal.alarm(0)
			return False

	def returnGrid(self=None):
		if not self.hasSolution():
			logger.error("No Solution")
			return False
		i = 0
		solution_grid = []
		solution_row = []
		for val in self.grid:
			solution_row.append(int(val))
			i +=1
			if i in [ (x*9) for x in xrange(10)]:
				solution_grid.append(solution_row)
				solution_row = []

		return solution_grid
