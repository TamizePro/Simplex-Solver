from SimplexProblems import *


if __name__ == "__main__":
    tableaux = problem10.solve()

    for t in tableaux:
        t.print_tableau()