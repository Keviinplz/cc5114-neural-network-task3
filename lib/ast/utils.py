"""
Module Utils


Utils functions that helps to use AST Objects
"""
import random

from .expresion import Expresion, Constant, Variable
from .operations import Sum, Mul, Div, Sub

def generateRandomASTFromList(lst) -> Expresion:
    """
    generateRandomASTFromList

    Generate a Random AST from given List
    List must to have Constant or/and Variable objects

    Parameters:
        lst: list
            A list of Constant object and/or Variable objects

        returntype: Expresion
            An AST Expresion
    """
    operator = [Sum, Mul, Div, Sub]
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return random.choice(operator)(lst[0], lst[1])
    else:
        ix = random.randint(1, len(lst) - 1)
        retval = random.choice(operator)(generateRandomASTFromList(lst[:ix]), generateRandomASTFromList(lst[ix:]))
        return retval

def generateRandomAST(constants=[], variables=[], leafSize=20) -> Expresion:
    """
    generateRandomAST

    Generate a Random AST

    Parameters:
        constants: list[float] (Default: Empty List [])
            A list of numbers to fill AST.
        
        variables: list[string] (Default: Empty List[])
            A list of string that represents Variables in AST

        leafSize: int (Default: 20)
            Quantity of leafs that AST gonna have

        returntype: Expresion
            An AST Expresion
    """
    leafs = []
    leafSize = (len(constants) + len(variables)) if constants else leafSize
    quantityOfConstants = random.randint(1, leafSize - len(variables))
    quantityOfVariables =  leafSize - quantityOfConstants
    if not constants:
        while quantityOfConstants:
            value = random.randint(0, 20)
            leafs.append(Constant(value))
            quantityOfConstants -= 1
    else:
        for const in constants:
            leafs.append(Constant(const))
    if variables:
        while quantityOfVariables:
            var = random.choice(variables)
            leafs.append(Variable(var))
            quantityOfVariables -= 1
    
    random.shuffle(leafs)
    return generateRandomASTFromList(leafs)