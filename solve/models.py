import datetime
from django.db import models
from django.utils import timezone


class Solution(models.Model):
	sudoku_input = models.CharField("Input Sudoku Grid", max_length=85)
	pub_date = models.DateTimeField('Date Added')
	unique_id = models.AutoField(primary_key=True)

	def __unicode__(self):
		return "Sudoku %s" % (self.pub_date, self.unique_id)
# Currently has no use. Thought that everytime a user gives a sudoku to solve,
# store that input state in the DB. So that if someone wants to see a random
# sudoku generated, one can be picked up at random from the ones that people
# have wanted solved :D
