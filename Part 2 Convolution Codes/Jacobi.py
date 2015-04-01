import numpy as np
import sys
import pprint
from numpy import linalg as LA


def jacobi(file_name, tolIn):

    if file_name is None:
        exit()

#Turns file into one big matrix
    A = np.genfromtxt(file_name,delimiter=" ")
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])
    bdim = (aRows, 1)
    b = np.zeros(bdim)

    s = raw_input("Please provide list of your guess values separated by spaces, e.g. 1 2 3: ")
    guess = np.matrix(s)

#Creates nx1 b matrix
    for j in range(0, aRows):
       b[j,0] = A[j, aCols-1]


#Creates A matrix
    elim = [aCols-1]
    N = np.delete(A, elim, 1)
    A = N

    print(A)
    print ('\n')
    print(b)

#Sets tolerance
    tol = float(tolIn)

#Sets intial previous guess so loop does not stop first try
    prevGuess = np.zeros((1, aRows))
    for i in range (0, aRows):
        prevGuess[0,i] = 1000

#Establishes variables
    guess2 = np.zeros((1, aRows))
    limit = 0
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])

#Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
#reached.
    while ((np.linalg.norm(guess - prevGuess) > tol) and limit < 100):
        for j in range (0, aRows):
            guess2[0,j] = b[j,0]
            for i in range (0, aCols):
                if (i != j):

                    guess2[0,j] = guess2[0,j] -(A[j,i]) * (guess[0,i])
            guess2[0,j] = guess2[0,j] / A[j,j]

        for i in range(0, aCols):
                prevGuess[0,i] = guess[0,i]
        for i in range(0, aCols):
                guess[0,i] = guess2[0,i]
        guess2 = np.zeros((1, aCols))
        limit = limit + 1

    #answers mod 2 to get real answers
    for i in range(0,aCols):
        guess[0,i] = guess[0,i]%2

    #print ('\n')
    #print(limit)
    #print ('\n')
    #print (guess)
    #print ('\n')




    if limit >= 100:
        statement = ("Did not converge after 100 iterations")
        return statement
    else:
        statement = ("Took " + str(limit) + " iterations to converge")
        return limit, guess, statement

# This is only or when jacobi is used as a stand-alone module
# Read command line argument. Must be exactly two arguments.
# It outputs on the console
if __name__ == '__main__':
    limit, guess, statement = jacobi(sys.argv[1], sys.argv[2])
    np.set_printoptions(precision=6, suppress=True)

    print ('\n')
    print ("iterations:")
    print(limit)
    print ('\n')
    print ("Final answer:")
    print (guess)
    print ('\n')
    print(statement)
#jacobi("c.dat", 1e-8)

