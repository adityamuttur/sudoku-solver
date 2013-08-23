from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError, Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from solution import Solution

temp_context =  { 
					'grid' : Solution().returnGrid(),
					'nothing':[]
				}
def input_sudoku(request):
	return render(request, 'solve/input.html', temp_context)

def solve_sudoku(request):
	pass

def no_solution(request):
	return render(request, 'solve/unsolvable.html')

def display_sudoku(request):
	sudoku_input = []
	for i in range(0, 81):
		input_character = request.POST[str(i)]
		if len(input_character) == 0:
			sudoku_input.append('.')
		else:
			sudoku_input.append(input_character)

	sudoku = Solution(sudoku_input)
	if not sudoku.hasSolution():
		return HttpResponseRedirect(reverse('solve:no_solution'))
	else:
		return render(request, 'solve/display.html', {"grid":sudoku.returnGrid()})
