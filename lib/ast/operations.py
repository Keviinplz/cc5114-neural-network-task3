"""
Module Operations

Operations that can be used in AST.
"""

from .expresion import Expresion, BinaryOperator

class Sum(BinaryOperator):
    """
    Class Sum

    Representation of sum of two values
    """
    def __init__(self, left: Expresion, right: Expresion):
        """
        Class Sum

        Representation of sum of two values

        Parameters:

            left: Expresion
                Left expresion of the sum
            
            right: Expresion
                Right expresion of the sum
        """
        super(Sum, self).__init__(left, right)

    def accept(self, visitor):
        """
        accept

        Accept an visitor, a set a Sum object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        visitor.visitSum(self)

class Mul(BinaryOperator):
    """
    Class Mul

    Representation of multiplication of two values
    """
    def __init__(self, left: Expresion, right: Expresion):
        """
        Class Mul

        Representation of multiplication of two values

        Parameters:

            left: Expresion
                Left expresion of the multiplication
            
            right: Expresion
                Right expresion of the multiplication
        """
        super(Mul, self).__init__(left, right)

    def accept(self, visitor):
        """
        accept

        Accept an visitor, a set a Mul object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        visitor.visitMul(self)

class Div(BinaryOperator):
    """
    Class Div

    Representation of division of two values
    """

    def __init__(self, left: Expresion, right: Expresion):
        """
        Class Div

        Representation of division of two values

        Parameters:

            left: Expresion
                Left expresion of the division
            
            right: Expresion
                Right expresion of the division
        """
        super(Div, self).__init__(left, right)

    def accept(self, visitor):
        """
        accept

        Accept an visitor, a set a Div object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        visitor.visitDiv(self)

class Sub(BinaryOperator):
    """
    Class Sub

    Representation of substract of two values
    """

    def __init__(self, left: Expresion, right: Expresion):
        """
        Class Sub

        Representation of substract of two values

        Parameters:

            left: Expresion
                Left expresion of the substract
            
            right: Expresion
                Right expresion of the substract
        """
        super(Sub, self).__init__(left, right)

    def accept(self, visitor):
        """
        accept

        Accept an visitor, a set a Div object visited

        Parameter:
        
            visitor: Visitor
                A visitor
        """
        visitor.visitSub(self)
