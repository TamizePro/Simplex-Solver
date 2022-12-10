import pysimplex as ps
from SimplexProblems import *


if __name__ == "__main__":
    problem = ps.Problem(constraints17,obj_fct17,type_max17)
    tableaux = problem.solution()

    for t in tableaux:
        t.print_tableau()