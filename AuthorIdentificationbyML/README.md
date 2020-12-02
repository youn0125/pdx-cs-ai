
#features : Emit comma-separated line with paragraph identifier
CS 441/541 Fall 2020 class

Mi Yon Kim / HW #3 - Author Identification by Machine Learning

This program emits comma-separated line with paragraph identifier



What machine learner(s) you tried.

How the learners performed.

What decisions you made in constructing your instances.
  * I reviewed the crys.py(https://github.com/pdx-cs-ai/crys/blob/main/crys.py) to how I can adapt the architecture of crys.py to monodfs.py
  * I focused on architecture, data structure, and the constraints.
  * From the linux box, 
    - The program got(./monodfs 8 2) the solution in 0.04s.
    - ./monodfs 9 2: unsat in 0.04s
    - ./monodfs 23 3: the solution in 0.06s
    - ./monodfs 24 3: unsat in 2s
  * I am still trying to find an efficient way to improve the performance to get solution in a reasonable time when I increase the monopoles and the number of rooms.
   
How to run the code:
  * ./monodfs m n, for example
  * ./monodfs 5 2
  * m should be a number of monopoles and n should a number of rooms.

Result:
  * The result should print the solution monopoles in each room on a single line in increasing order. 
  * For the example above where m=5 and n=2 the program might print\
    1 3 5\
    2 4\
    When m=9 and n=2 your program should print\
    unsat
