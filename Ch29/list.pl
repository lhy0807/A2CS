
/* 1.01 */
/* Find the last element of the list */
my_last([X], X).
my_last([_|B], Z) :-
	my_last(B, Z).

/* 1.02 */
/* */
my_last2([A,_], A).
my_last2([_|Tail], R) :-
	my_last2(Tail, R).

/* 1.03 */
findK([A|_],1,A).
findK([_|T], N, R) :-
	findK(T, X, R),
	N is X + 1.

/* 1.04 */
len([], 0).
len([_|T], L) :-
	len(T, X),
	L is X + 1.





