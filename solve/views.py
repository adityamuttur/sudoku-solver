from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError, Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from solution import Solution
from django.core.context_processors import csrf

def input_sudoku(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('solve/input.html', c)

def no_solution(request):
	return render(request, 'solve/unsolvable.html')

def solve_sudoku(request):
	sudoku_input = []
	for i in range(0, 81):
		input_character = request.POST[str(i)]
		if len(input_character) == 0:
			sudoku_input.append('.')
		else:
			sudoku_input.append(input_character)

	sudoku_solution = Solution(sudoku_input).returnGrid()
	request.session['sudoku_solution'] = repr(sudoku_solution)

	if not sudoku_solution:
		return HttpResponseRedirect(reverse('solve:no_solution'))
	else:
		return HttpResponseRedirect(reverse('solve:display'))

def display_sudoku(request):
	sudoku_solution = request.session.get('sudoku_solution', None)

	if sudoku_solution is not None:
		sudoku_solution = eval(sudoku_solution)
	else:
		return HttpResponseRedirect(reverse('solve:no_solution'))

	return render(request, 'solve/display.html', {"grid":sudoku_solution})
