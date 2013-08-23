from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
	return value*arg

@register.filter(name='addition')
def addition(value, arg):
	return value+arg

@register.filter(name='range_list')
def range_list(string_value):
	value = int(string_value)
	list_ = []
	for i in xrange(0, value):
		list_.append(str(i))
	return list_
