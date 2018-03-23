/* mode */
/* 0 is the result of mod(X,2) */
even(X) :- 0 is mod(X,2).
odd(X) :- not(even(X)).

/* Recursion */
factorial(0, 1).
factorial(N, F) :- 
	X is N - 1
	factorial(X, Y), 
	F is N * Y.
