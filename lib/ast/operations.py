from .expresion import Expresion, BinaryOperator

class Sum(BinaryOperator):
    
    def __init__(self, left: Expresion, right: Expresion):
        super(Sum, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitSum(self)

class Mul(BinaryOperator):

    def __init__(self, left: Expresion, right: Expresion):
        super(Mul, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitMul(self)

class Div(BinaryOperator):
    
    def __init__(self, left: Expresion, right: Expresion):
        super(Div, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitDiv(self)

class Sub(BinaryOperator):

    def __init__(self, left: Expresion, right: Expresion):
        super(Sub, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitSub(self)
