<The Power Method, Part 3>

!---------------!
1. (6 points) Power method.
Run "python power_method.py arg1 arg2 arg3"
arg1 must be a .dat file containing a space-separated data of the N x N matrix, A
arg2 must be a float of error tolerance used to check convergence in the power method iteration
arg3 must be an initial approximation vector with the same number of rows as A
     Please input the vector as a string, separated by spaces
     Example: "2.1e5 1.9e5 1.8e5 2.1e5"

It will output the dominant eigenvalue, dominant eigenvector, and number of iterations
it took to converge. If it does not converge in a fixed number of iterations (100), it
will report that it did not converge on the console.

!---------------!
2. (9 points) Discussion.
Please see written_part3.docx

It should address the questions posted in the description of the project.

!---------------!
3. Additional program.
Written to find population distribution and total population of a certain decade.

Run "python population.py arg1 arg2 arg3"
arg1 must be a .dat file containing a space-separated data of the matrix, A
arg2 must be an initial approximation vector with the same number of rows as A
arg3 must be an integer of how many decades ahead you would like to see the population of
