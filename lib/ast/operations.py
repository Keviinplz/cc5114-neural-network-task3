from .expresion import Expresion

class BinaryOperator(Expresion):
    
    def __init__(self, left: Expresion, right: Expresion):
        self.left = left
        self.right = right

    def getLeft(self) -> Expresion:
        return self.left

    def getRight(self) -> Expresion: 
        return self.right

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


