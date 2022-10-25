"""
File: evo.py

Description: an evolutionary computing framework
"""


class Environment:

    def __init__(self):
        self.pop = {}
        self.fitness = {}
        self.agents = {}

    def add_fitness_criteria(self, name, f):
        """
            Every new solution is evaluated wrt each fitness criteria
        :return:
        """
        self.fitness[name] = f

    def add_agent(self, name, op, k=1):
        """
            Register an agent with the framework
        :param name:
        :param op:
        :param k:
        :return:
        """
        self.agents[name] = (op, k)

    def add_solution(self, sol):
        """
            Register a solution with the framework
        :param sol:
        :return:
        """
        evaluate = tuple([(name, f(sol)) for name, f in self.fitness.items()])
        self.pop[evaluate] = sol

