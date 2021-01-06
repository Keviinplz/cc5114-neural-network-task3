import random
import numpy as np
from abc import ABC, abstractmethod

from ..ast.operations import Sum, Mul, Div, Sub
from ..ast.expresion import Constant, Variable, Expresion
from ..ast.visitor import StringExpresionVisitor, EvaluateExpresionVisitor
from ..ast.utils import generateRandomAST, adhere, selectRandomTree

class AbstractGeneticAlgorithm(ABC):
    """
    Define an Abstract Genetic Algorithm

    Attributes
    -----------

    population_size: int
        Size of the Population
    depth_range: list
        Depth range of the tree
    selector_factor: float
        Selection factor
    mutation: float
        mutation chance indicate how likely an individual is to be mutated, 0.8 by default
    """
    
    def __init__(
        self, 
        population_size: int, 
        depth_range: list, 
        selector_factor: float, 
        mutation_prob = 0.8,
        epochs = 100):
        """
        Parameters
        -----------

        population_size: int
            Size of the Population
        depth_range: list
            Depth range of the tree
        selector_factor: float
            Selection factor
        mutation: float
            mutation chance indicate how likely an individual is to be mutated, 0.8 by default
        """
        self.depth_range = depth_range
        self.selector_factor = selector_factor
        self.mutation_prob = mutation_prob
        self.population = self.createPopulation(population_size)
        self.epochs = epochs
        self.fitness_epoch = []

    def getPopulation(self) -> list:
        """
        Returns Populations

        returntype: list[PopulationObject]
            Population of GA
        """
        
        return self.population

    def getFitnessEpoch(self):
        return self.fitness_epoch

    def getEpochs(self) -> int:
        return self.epochs

    def discountEpochs(self) -> None:
        self.epochs -= 1
    
    def setPopulation(self, population):
        """
        Set Population

        Parameters:
        
        - population: list[PopulationObject]
            A list of populations objects
        """
        self.population = population

    @abstractmethod
    def createPopulation(self):
        """
        ABSTRACT METHOD

        Create a population of objects
        Using AST Library

        returntype: list[PopulationObject]
            A list of population objects
        """
        pass
    
    @abstractmethod
    def createRandomGen(self):
        """
        ABSTRACT METHOD

        Create a random gen 

        returntype: Expresion
            Random gen generated
        """
        pass

    @abstractmethod
    def fitness(self, tree: Expresion):
        pass

    @abstractmethod
    def isReady(self):
        """
        ABSTRACT METHOD

        Tells if the solution was reached

        Returns:
            boolean: true if the solution was reached 
        """
        pass

    def mutate(self, individual: Expresion) -> None:
        """
        Mutate a individual from Population
        With a random gen

        Parameters
        ----------

        - individual: Expresion
            A invidivual that gonna be mutated
        """
        random_gen = self.createRandomGen()
        adhere(individual, random_gen)

    def cross_over(self, ind1: Expresion, ind2: Expresion) -> None:
        """
        Generate a cross over between two individuals
        Extracting a random tree from both of them
        And finally graft each other

        Parameters:
        ----------

        - ind1: Expresion
            First individual

        - ind2: Expresion
            Second individual
        
        returntype: List
            List of children
        """
        random_subtree_ind1 = selectRandomTree(ind1)
        random_subtree_ind2 = selectRandomTree(ind2)
        adhere(ind1, random_subtree_ind2)
        adhere(ind2, random_subtree_ind1)
        return [ind1, ind2]

    def sortPopulation(self):
        """Sort the population in ascending order of fitness function


        """
        fitness_arr = [self.fitness(self.population[i]) for i in range(len(self.population))]
        
        sort_index = np.argsort(fitness_arr)
        np_population = np.array(self.population)
        self.population = np_population[sort_index].tolist()

    def selectParents(self)->list:
        """Order the population and select two parents such as
            the better fitness function are priorizated 

        Returns:
            parents: list of parents
        """
        self.sortPopulation()
        rand = np.random.uniform(0, 1, 2) # two parents
        random_index = (len(self.population) * rand**(self.selector_factor)).astype(int) # function to priorizate small values

        np_population = np.array(self.population)
        parents = np_population[random_index].tolist()
        return parents
        
    def randomMutate(self, individual):
        if random.random() <= self.mutation_prob:
            self.mutate(individual)
    
    def reproduce(self, parents:list)->list:
        """ Taking two given parents generate two children
            using the cross over process and the mutation of
            genes

        Args:
            parents: list of parents, every parent is an instance of BoardSet

        Returns:
            children: list of children 
        """
        firstParent = parents[0]
        secondParent = parents[1]
        children = self.cross_over(firstParent, secondParent)
        firstChild = children[0]
        secondChild = children[1]
        self.randomMutate(firstChild)
        self.randomMutate(secondChild)
        children = [firstChild, secondChild]
        return children

    def train(self):
        while (not self.isReady()):
            next_generation = []
            for i in range(int(len(self.population)/2)):
                parents = self.selectParents()
                children = self.reproduce(parents)
                next_generation.append(children[0])
                next_generation.append(children[1])
                self.setPopulation(next_generation)

            self.fitness_epoch.append(self.fitness(self.getBestIndividual()))
            self.discountEpochs()
            
    def getBestIndividual(self):
        self.sortPopulation()
        return self.population[0]

class TargetNumberGA(AbstractGeneticAlgorithm):

    def __init__(
        self, 
        numbers_list: list,
        target_number: float,
        population_size: int, 
        depth_range: float, 
        selector_factor: float, 
        mutation_prob = 0.8,
        epochs = 200):

        self.numbers_list = numbers_list
        self.target_number = target_number
        super(TargetNumberGA, self).__init__(
            population_size, 
            depth_range, 
            selector_factor, 
            mutation_prob=mutation_prob, 
            epochs=epochs
        )
        
        
    
    def createPopulation(self, population_size: int):
        """
        Creates a random population 

        Parameters:
        
        - population_size: int
            size of populaton
        """
        return [generateRandomAST(constants=self.numbers_list) for _ in range(population_size)]

    def createRandomGen(self):
        """
        Create a random gen 

        returntype: Expresion
            Random gen generated
        """
        return generateRandomAST(constants=self.numbers_list, leafSize=len(self.numbers_list))
    
    def fitness(self, tree: Expresion):
        """
        fitness
            Calculate the diffence between the given tree value and the target number

        Parameters:
            tree: Expresion 
                Given tree expresion
        returntype: float
            Return fitness value
        """
        eev = EvaluateExpresionVisitor()
        tree.accept(eev)
        fit = eev.getResult()
        return abs(fit-self.target_number)

    def isReady(self) -> bool:     
        """
        isReady
            Returns the state of the 
        Parameters:
            none
        returntype: boolean
            return true or false depending on the reached fitness
        """
        self.sortPopulation()
        delta = 0.05
        if (self.fitness(self.population[0]) < delta) or self.epochs == 0:
            return True

        return False


class GuessingTheFunctionGA(AbstractGeneticAlgorithm):

    def __init__(
        self, 
        tuple_list: list,
        population_size: int, 
        depth_range: float, 
        selector_factor: float, 
        mutation_prob= 0.8,
        epochs = 200):

        self.tuple_list = tuple_list
        super(GuessingTheFunctionGA, self).__init__(
            population_size, 
            depth_range, 
            selector_factor, 
            mutation_prob=mutation_prob, 
            epochs=epochs
        )
        
    
    def createPopulation(self, population_size):
        """
        Creates a randoom population 

        Parameters:
        
        - population_size: int
            size of populaton
        """
        return [generateRandomAST(variables=['x']) for _ in range(population_size)]

    def createRandomGen(self):
        """
        Create a random gen, choosing if is with variables or not
        depending of random distribution value with 0.5 probability

        returntype: Expresion
            Random gen generated
        """
        return generateRandomAST(variables=['x'], leafSize=len(self.tuple_list)) if random.random() > 0.5 else generateRandomAST(leafSize=len(self.tuple_list))
    

    def fitness(self, tree: Expresion):
        """
        Evaluate the value of the given expression with respect to
        the tuples

        Parameters:
        ----------
        - tree: Expresion
            AST to evaluate

        returntype: float
            Mean difference between the tree results and the target 

        """
        fitness_list = []
        for i in range(len(self.tuple_list)):
            eev = EvaluateExpresionVisitor(x=self.tuple_list[i][0])
            tree.accept(eev)
            fitness_list.append(abs(eev.getResult()-self.tuple_list[i][1]))
        return np.mean(np.array(fitness_list))

    def isReady(self) -> bool:
        """
        isReady
            Returns the state of the 
        Parameters:
            none
        returntype: boolean
            return true or false depending on the reached fitness
        """     
        
        self.sortPopulation()

        delta = 0.05
        if (self.fitness(self.population[0]) < delta) or self.epochs == 0:
            return True 

        return False