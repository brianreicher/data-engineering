"""
sorting.py
A demonstration of using evocomp to sort a list of numbers
"""
import random as rnd
import evo

def stepsdown(L):
    """ Measures the total magnitude of the steps down (larger to a smaller value) """
    return sum([x - y for x,y in zip(L, L[1:]) if y < x])

def sumratio(L):
    """ ratio of the sum of the first half values to the 2nd half values """
    """ Ratio of sum of first-half values to 2nd half values """
    sz = len(L)
    return round(sum(L[:sz//2]) / sum(L[sz//2+1:]), 5)


def swapper(solutions):
    """ Agent: Swap two random values """
    L = solutions[0]
    i = rnd.randrange(0, len(L))
    j = rnd.randrange(0, len(L))
    L[i], L[j] = L[j], L[i]
    return L

def main():


    # create population
    E = evo.Environment()

    # register the fitness criteria (objects)
    E.add_fitness_criteria("stepsdown", stepsdown)
    E.add_fitness_criteria("sumratio", sumratio)

    # register all agents
    E.add_agent("swapper", swapper, 1)


    # seed the population with an intial solution
    L = [rnd.randrange(1,99) for _ in range(20)]
    E.add_solution(L)

    # run the evolver
    E.evolve(5)

    # print result
    print(E)


if __name__ == '__main__':
    main()