/* TASK 3 */

character(jim).
character(jenny).
character(habib).
character(michael).
character(cindy).

charater_type(jim, prince).
character_type(jenny, princess).
character_type(habib, explorer).
character_type(michael, boyfriend).
character_type(cindy, girlfriend).

has_skill(jim, fly).
has_skill(jenny, invisiblility).
has_skill(habib, time_travel).
has_skill(michael, kiss).
has_skill(cindy, kiss).
has_skill(X, Y) :- 
	character(X),skill(Y).

has_pet(jim, horse).
has_pet(jenny, bird).
has_pet(habib, fish).
has_pet(michael, dog).
has_pet(cindy, cat).
has_pet(C, P) :-
	character(C),animal(P).

animal(horse).
animal(bird).
animal(fish).
animal(dog).
animal(cat).

skill(fly).
skill(invisibility).
skill(time_travel).
skill(kiss).


