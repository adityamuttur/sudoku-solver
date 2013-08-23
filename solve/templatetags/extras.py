from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
	# Returns product of the 2 digits
	return value*arg

@register.filter(name='addition')
def addition(value, arg):
	# Returns sum of the 2 digits
	return value+arg

@register.filter(name='range_list')
def range_list(string_value):
	# Accepts string form of an integer to produce list
	# Returns list of the string form of integers from "0" to "value-1"
	# Eg: "3"|range_list => ["0", "1", "2"]
	value = int(string_value)
	list_ = []
	for i in xrange(0, value):
		list_.append(str(i))
	return list_
