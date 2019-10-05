# The Travelling Salesman Problem
The Travelling Salesman Problem is a famous problem in CS. The premise is simple, given a
list of 'cities' find the best tour/route that visits all of them. It is in the NP-Complete
Class of problems, meaning there is no polynomial exact solution. The best we can do is
find optimizations instead of exact solutions. This project explores 2 algorithms to find
a tour. The first algorithm is the naive/brute force algorithm. It first finds all the permutations
of the routes and tries them all to find the most optimal one. This algorithm has O(N!) complexity, which
is not ideal. The second algorithm is a Genetic Algorithm. As the name suggests, it takes inspiration
from genetics in biology. First the algorithm selects a few tours from a 'population' of tours. It then performs
'mutations' on those few tours and creates a new population descendant from the mutations.
This algorithm arrives at an near optimal tour much faster than the brute force, especially if the
number of cities is large


# Demo
![](res/geneticDemo.gif)
