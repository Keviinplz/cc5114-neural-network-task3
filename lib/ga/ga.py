import random
import numpy as np

from ast.operations import Sum, Mul, Div, Sub
from ast.expresion import Constant, Variable
from ast.visitor import StringExpresionVisitor, EvaluateExpresionVisitor

class GA():
        """
    Define a Genetic Algorithm class to find a word

    Attributes
    -----------

    p_s: int
        Size of the Population
    d_r: list
        Depth range of the tree
    population: list
        List of all individual, each individual is an instance of BoardSet
    mut_chance: float
        mutation chance indicate how likely an individual is to be mutated, 0.8 bu default
    """
    operations = [Sum, Mul, Div, Sub]
    population = []
    ready = False

    def __init__(self, p_s: int, d_r: list, s_f: float, mut = 0.8):
        """
        Parameters
        -----------
        p_s: int
            The size of the Population
        d_r: list
            Depth range of the tree
        s_f: float
            Selection factor
        mut: float 
            Mutation chance 
        """
        self.p_s = p_s
        self.b_s = b_s
        self.s_f = s_f
        self.mut = mut

    def createPopulation(self) -> None:
        """
        Create a population of p_s boards with b_s size

        """
        pass

    def getPopulation(self) -> list:
        """
        Getter population
        """
        return self.population

    def setPopulation(self, population: list):
        """Set the population of the GA

        Args:
            population (list): [description]
        """
        self.population = population