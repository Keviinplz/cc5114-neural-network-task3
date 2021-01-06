import random

import numpy as np
import matplotlib.pyplot as plt

from lib.ga.ga import TargetNumberGA, GuessingTheFunctionGA
from lib.ast.visitor import EvaluateExpresionVisitor, StringExpresionVisitor

seed = 3
random.seed(seed)

def evaluate_model(ga):
    ga.train()
    
    eev = EvaluateExpresionVisitor()
    sev = StringExpresionVisitor()

    best = ga.getBestIndividual()
    best.accept(sev)
    expresion = sev.getResult()

    best.accept(eev)
    value = eev.getResult()

    return expresion, value

def evaluate_p2(ga, sev, x_list):
    ga.train()
    best = ga.getBestIndividual()

    best.accept(sev)
    expresion = sev.getResult()

    values = np.zeros(len(x_list))
    for index, value in enumerate(x_list):
        eev = EvaluateExpresionVisitor(x=value)
        best.accept(eev)
        values[index] = eev.getResult()

    return expresion, values

def transpose(l: list):
    return list(map(list, zip(*l)))


## GENERAL PARAMETERS FOR GENETIC ALGORITHM

## Problem 1
#number_list = [1, 1, 1, -2, -3, 7]
#target_number = 5
number_list = [3, 2, 5, 7 , -2]
target_number = 16

targetNumberGAParameters = {
    'numbers_list': number_list,
    'target_number' : target_number,
    'population_size': 100,
    'depth_range': 6,
    'selector_factor': 5,
    'mutation_prob': 0.8,
    'epochs': 1000
}

targetNumberGA = TargetNumberGA(**targetNumberGAParameters)
expresion, value = evaluate_model(targetNumberGA)
print("Problem 1")
print(expresion)
print(value)

## Problem 2

# f(x) = x working well
#
tuple_list = [[1,1], [2,2], [3,3], [4,4], [5,5]]

guessingTheFunctionGAParameters = {
    'tuple_list': tuple_list,
    'population_size': 50,
    'depth_range': 6,
    'selector_factor': 5,
    'mutation_prob': 0.8,
    'epochs': 500
}

guessingTheFunctionGA = GuessingTheFunctionGA(**guessingTheFunctionGAParameters)

expresion, values = evaluate_p2(guessingTheFunctionGA, StringExpresionVisitor(), transpose(tuple_list)[0])
print("Problem 2")
print(expresion)
print(values)

# Metrics
epochs_tn = np.arange(0, targetNumberGAParameters['epochs'] - targetNumberGA.epochs)
fitness_tn = targetNumberGA.getFitnessEpoch()

epochs_gf = np.arange(0, guessingTheFunctionGAParameters['epochs'] - guessingTheFunctionGA.epochs)
fitness_gf = guessingTheFunctionGA.getFitnessEpoch()

fig, axs = plt.subplots(1, 1)
axs[0].plot(epochs_tn, fitness_tn)
axs[0].set_title('Epochs v/s Fitness Function Problem 1')

axs[1].plot(epochs_gf, fitness_gf)
axs[1].set_title('Epochs v/s Fitness Function Problem 2')

for ax in axs.flat:
    ax.set(xlabel='Epochs', ylabel='Fitness Value')

plt.show()
