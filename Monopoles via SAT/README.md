# monosat, unmonosat
CS 441/541 Fall 2020 class

Mi Yon Kim / HW #2 - Monopoles via SAT

monosat: This program generates a SAT encoding for a monopoles instance in DIMACS format for use with the minisat SAT solver.
unmonosat: This program decodes minisat's SAT solution to obtain a monopoles instance solution.
Read DIMACS format SAT solver output http://www.satcompetition.org/2009/format-benchmarks2009.html to solve a monopole instance.

Things to do to develop this code.
  * I reviewed the sudokugen.py and sudokusolve.py (https://github.com/pdx-cs-ai/sudoku-sat-py).
  * I reviewed the 'Monopole Formal Description' to get the idea of how to generate a SAT encoding in DIMACS format.
  * From the linux box, 
    - ./monosat m n should generate a DIMACS-format SAT instance on its standard output.
    - minisat SAT solver will find a satisfying assignment.
    - ./unmonosat m n should decode minisat's SAT solution to obtain a monopoles instance solution.

How to run the code:
  * For example: m = 8 and n = 2 (m should be a number of monopoles and n should a number of rooms) 
  * ./monosat 8 2 > test.sat
  * minisat test.sat test.soln
  * ./unmonosat 8 2 < test.soln
  
Result:
  * The result should print the solution monopoles in each room on a single line in increasing order. 
  * For the example above where m=8 and n=2 the program might print\
    3 4 6 7\
    1 2 4 8\
    When m=9 and n=2 your program should print\
    unsat