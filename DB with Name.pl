%Facts
dob(karthik, date(2003,09,20)).
dob(roshan, date(2004,09,08)).
dob(soorya, date(2003,10,13)).
dob(haemanth, dob(10,12,2004)).

%Queries
name(name) :- dob(name, _).
year(name,year):-
    dob(name,date(year, _, _)).
month(name, _,month, _).
day(name,day):-
    dob(name,date(_, _, day)).
