"""
Module Expresion

Module that create Abstracts expresion to AST
"""
import random 

from abc import ABC, abstractmethod

class Expresion(ABC):
    """
    Abstract Class Expresion

    Abstract representation of being an expresion

    """
    def __init__(self, value: any):
        """
        Abstract Class Expresion

        Abstract representation of being an expresion

        Parameter:
        
            value: any
                Value of the expresion
        """
        self.value = value

    @abstractmethod
    def accept(self, visitor) -> None:
        """
        ABSTRACT METHOD
        accept

        Accept an visitor, a set this object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        pass

    def getValue(self) -> any:
        """
        getValue

        Return value of the expresion

        returntype: any
            Value of the expresion
        """
        return self.value
    def insert(self, tree)-> None:
        self = tree


class BinaryOperator(Expresion):
    """
    Class BinaryOperator

    Abstract a Binary Operator
    """    
    def __init__(self, left: Expresion, right: Expresion):
        """
        Class BinaryOperator

        Abstract a Binary Operator
        Apply an operator to the tuple left and right
        Parameters:

            left: Expresion
                Expresion object
            
            right: Expresion
                Expresion object
        
        """
        self.left = left
        self.right = right

    def getLeft(self) -> Expresion:
        """
        getLeft

        Return left expresion

        returntype: Expresion
            Left expresion of the operator
        """
        return self.left

    def getRight(self) -> Expresion: 
        """
        getRight

        Return right expresion

        returntype: Expresion
            Right expresion of the operator
        """
        return self.right
    
    def insert(self, tree: Expresion)-> None:
        if random.random() >=0.5:
            self.left = tree
        else:
            self.right = tree

class Constant(Expresion):
    """
    Class Constant

    Represent a constant value
    """

    def __init__(self, value: float):
        """
        Class Constant

        Represent a constant value

        Parameters:
            
            value: float
                Constant value
        """
        super(Constant, self).__init__(value)

    def accept(self, visitor) -> None:
        """
        accept

        Accept an visitor, a set a Constant object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        visitor.visitConstant(self)
    

class Variable(Expresion):
    """
    Class Variable

    Represent a Variable value
    """

    def __init__(self, value: str):
        """
        Class Variable

        Represent a variable value

        Parameters:
            
            value: str
                Variable value
        """
        super(Variable, self).__init__(value)

    def accept(self, visitor) -> None:
        """
        accept

        Accept an visitor, a set a Variable object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        visitor.visitVariable(self)


