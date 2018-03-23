/*
Name: Tianhe Zhang (Oscar)
Class: S3C2
Option: 3
*/

/* Bunny ears */
bunnyEars(0, 0).
bunnyEars(Input, Output) :-
	X is Input - 1,
	bunnyEars(X, Y),
	Output is Y + 2.

/* Fibonacci */
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(Input, Output) :-
	X is Input - 1,
	Y is Input - 2,
	fibonacci(X, Z),
	fibonacci(Y, A),
	Output is A + Z.

even(X) :- 0 is mod(X,2).
odd(X) :- not(even(X)).

/* Bunny ears 2 */
bunnyEars2(0, 0).
bunnyEars2(1, 2).
bunnyEars2(2, 5).
bunnyEars2(Input, Output) :-
	Pre is Input - 2,
	bunnyEars2(Pre, PreResult),
	Output is PreResult + 5.

/* triangle */
triangle(0, 0).
triangle(1, 1).
triangle(Row, Sum) :-
	PreRow is Row - 1,
	triangle(PreRow, PreSum),
	Sum is PreSum + Row.

/* sum digit */
sumDigits(0, 0).
sumDigits(N, S) :-
	PreN is div(N,10),
	sumDigits(PreN, PreS),
	S is PreS + mod(N,10).

/* count 7 */
isSeven(7).
countSeven(0, 0).
countSeven(N,C) :-
	D is mod(N,10),
	PreN is div(N,10),
	countSeven(PreN,PreS),
	( ( isSeven(D), C is PreS + 1 );
	( not(isSeven(D)), C is PreS + 0 ) ).








