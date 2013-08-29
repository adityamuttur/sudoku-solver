from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError, Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from solution import Solution
from django.core.context_processors import csrf

temp_context =  {
                    'grid' : Solution().returnGrid(),
                    'nothing':[]
                }
def input_sudoku(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('solve/input.html', c)

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
    request.session['sudoku_solution'] = repr(sudoku_solution)

    if not sudoku_solution:
        return HttpResponseRedirect(reverse('solve:no_solution'))
    else:
        return HttpResponseRedirect(reverse('solve:test'))

def test(request):
    #TODO: this could be used. The other option is to pass it as get parameters
    sudoku_solution = request.session.get('sudoku_solution', None)

    if sudoku_solution is not None: sudoku_solution = eval(sudoku_solution)
    else: return HttpResponse("asdasldhl")

    return render(request, 'solve/display.html', {"grid":sudoku_solution})
