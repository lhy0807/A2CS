/* Family Knowledge Base */

male(fred).
male(jacky).
male(john).
male(tom).
male(abe).

female(cindy).
female(alex).
female(linda).
female(lily).
female(ariana).

/* (parent, child）*/
parent(fred, cindy).
parent(fred, jacky).
parent(alex, cindy).
parent(alex, jacky).

parent(john, lily).
parent(linda, lily).

parent(abe, fred).
parent(ariana, fred).
parent(abe, linda).
parent(ariana, linda).

/* Test if A is B's brother */
isBrother(A, B) :-
	male(A),( parent(P, A),parent(P, B) ).

/* Test if A is B's sister */
isSister(A, B) :-
	female(A),( parent(P, A),parent(P, B) ).

/* Test if A is B's son */
isSon(A, B) :- 
	male(A),parent(B, A).

/* Test if A is B's daughter */
isDaughter(A, B) :-
	female(A),parent(B, A).

/* Test if A and B are couple */
isMarried(A, B) :-
	parent(A, X),parent(B, X).

/* Test if A is B's ancestor */
isAncestor(A, B) :-
	parent(A, B);( parent(A, X),parent(X, B) ).
	

