"""
Module Utils


Utils functions that helps to use AST Objects
"""
import random
import copy

from .expresion import Expresion, Constant, Variable, BinaryOperator
from .operations import Sum, Mul, Div, Sub
from .visitor import StringExpresionVisitor, EvaluateExpresionVisitor, CountVisitor

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

def selectRandomTree(tree: Expresion)->Expresion:
    """
    selectRandomTree

    Select a random subtree in a given tree

    Parameters:
        tree: Expresion 
            Given tree expresion

        returntype: Expresion
            Return a subtree randomly selected
    """

    cv = CountVisitor()
    if not isinstance(tree, BinaryOperator):
        return copy.deepcopy(tree)
        

    tree.accept(cv)
    a = cv.getResult()
    tree.getLeft().accept(cv)
    b = cv.getResult() 

    
    rand_num = random.randint(1, a)
    
    if rand_num <= b: return selectRandomTree(tree.getLeft())
    elif rand_num == b + 1: return copy.deepcopy(tree)
    else: return selectRandomTree(tree.getRight())

def adhere(tree: Expresion, graft: Expresion):
    """
    adhere
        Adhere a graft to a given tree Expresion

    Parameters:
        tree: Expresion 
            Given tree expresion
        graft: Expresion 
            Subtree to graft

    """
    
    if random.random()<=0.5:
        tree.insert(graft)
    else:
        if isinstance(tree, BinaryOperator): # isinstance :o code smell 
            if random.random()<=0.5:
                adhere(tree.getLeft(), graft)
            else:
                adhere(tree.getRight(), graft)
        else:
            tree.insert(graft)




    




        
    
