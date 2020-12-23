from .operations import Sum, Mul, Div, Sub, BinaryOperator
from .expresion import Constant, Variable

class Visitor():

    def __init__(self, result):
        self.result = result

    def getResult(self):
        return self.result
    
    def setResult(self, newValue):
        self.result = newValue
    
    def visitBinaryOperator(self, op: BinaryOperator, function) -> None:
        op.getLeft().accept(self)
        leftValue = self.getResult()

        op.getRight().accept(self)
        rightValue = self.getResult()

        newResult = function(leftValue, rightValue)
        self.setResult(newResult)

class StringExpresionVisitor(Visitor):
    
    def __init__(self):
        super(StringExpresionVisitor, self).__init__("")

    def visitSum(self, s: Sum) -> None:
        self.visitBinaryOperator(s, lambda x, y : f"({x} + {y})")

    def visitMul(self, m: Mul) -> None:
        self.visitBinaryOperator(m, lambda x, y : f"({x} * {y})")

    def visitDiv(self, d: Div) -> None:
        self.visitBinaryOperator(d, lambda x, y : f"({x} % {y})")

    def visitSub(self, st: Sub) -> None:
        self.visitBinaryOperator(st, lambda x, y : f"({x} - {y})")

    def visitVariable(self, v: Variable) -> None:
        self.setResult(v.getValue())

    def visitConstant(self, c: Constant) -> None:
        self.setResult(str(c.getValue()))


class EvaluateExpresionVisitor(Visitor):
    
    def __init__(self, **kwargs):
        super(EvaluateExpresionVisitor, self).__init__(0)
        self.variableSet = kwargs

    def visitSum(self, s: Sum) -> None:
        self.visitBinaryOperator(s, lambda x, y : x + y)

    def visitSub(self, st: Sub) -> None:
        self.visitBinaryOperator(st, lambda x, y : x - y)

    def visitMul(self, m: Mul) -> None:
        self.visitBinaryOperator(m, lambda x, y : x * y)

    def visitDiv(self, d: Div) -> None:
        self.visitBinaryOperator(d, lambda x, y : x / y if y != 0 else 1)
   
    def visitVariable(self, v: Variable) -> None:
        try:
            value = self.variableSet[v.getValue()]
            self.setResult(float(value))
        except KeyError:
            raise KeyError(f"Free ocurrency of {v.getValue()} in AST\nPlease declare it when initialice this visitor.")
        
    def visitConstant(self, c: Constant) -> None:
        self.setResult(float(c.getValue()))


