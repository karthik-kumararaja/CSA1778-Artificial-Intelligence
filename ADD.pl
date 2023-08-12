sum(1,1).
sum(1,R):-
    N1=N-1,
    sum(N1,R1),
    R=R1+N.
