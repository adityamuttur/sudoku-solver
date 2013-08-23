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
	return render(request, 'solve/input.html')

# Want to use the solve_sudoku view to receive post call with input grid and then have it
# redirected (HttpResponseRedirect) to the display_sudoku view (since its a good practice)
# But can't send context variables through HttpResponseRedirect so can't send the solved
# drid to the sudoku grid to the display_sudoku view.
# NOT sure how to go about it
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

	# returnGrid return a 'bool' if no solution or if function timesout.
	# then it takes it to so solution page
	# The timer has to be put in solution.py. NOT yet working
	# View currently working for valid inputs
	sudoku_solution = Solution(sudoku_input).returnGrid()
	if not sudoku_solution:
		return HttpResponseRedirect(reverse('solve:no_solution'))
	else:
		return render(request, 'solve/display.html', {"grid":sudoku_solution})
