import datetime
from django.db import models
from django.utils import timezone


class Solution(models.Model):
	sudoku_input = models.CharField("Input Sudoku Grid", max_length=85)
	pub_date = models.DateTimeField('Date Added')
	unique_id = models.AutoField(primary_key=True)

	def __unicode__(self):
		return "Sudoku %s" % (self.pub_date, self.unique_id)
