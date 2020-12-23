from .expresion import Expresion

class BinaryOperator(Expresion):
    
    def __init__(self, left: Expresion, right: Expresion):
        self.left = left
        self.right = right

    def getLeft(self) -> Expresion:
        return self.left

    def getRight(self) -> Expresion: 
        return self.right

    def evaluate(self) -> float:
        raise NotImplementedError("Method must be implemented by subclass")

class Sum(BinaryOperator):
    
    def __init__(self, left: Expresion, right: Expresion):
        super(Sum, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitSum(self)

    def evaluate(self) -> float:
        return self.getLeft().evaluate() + self.getRight().evaluate()

class Mul(BinaryOperator):

    def __init__(self, left: Expresion, right: Expresion):
        super(Mul, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitMul(self)

    def evaluate(self) -> float:
        return self.getLeft().evaluate() * self.getRight().evaluate()


class Div(BinaryOperator):
    
    def __init__(self, left: Expresion, right: Expresion):
        super(Div, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitDiv(self)

    def evaluate(self) -> float:
        leftValue = self.getLeft().evaluate()
        rightValue = self.getRight().evaluate()
        return leftValue / rightValue if rightValue == 0 else 1


class Sub(BinaryOperator):

    def __init__(self, left: Expresion, right: Expresion):
        super(Sub, self).__init__(left, right)

    def accept(self, visitor):
        visitor.visitSub(self)

    def evaluate(self) -> float:
        return self.getLeft().evaluate() - self.getRight().evaluate()
