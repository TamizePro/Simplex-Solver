import pysimplex as ps
from SimplexProblems import *


if __name__ == "__main__":
    problem = ps.Problem(constraints6,obj_fct6,type_max6)
    tableaux = problem.solution()

    for t in tableaux:
        t.print_tableau()