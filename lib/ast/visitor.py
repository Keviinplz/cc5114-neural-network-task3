from .leaf import Constant, Variable
from .operations import Sum, Mul, Div, Sub, BinaryOperator

class StringBuilderExpresion():
    
    def __init__(self):
        self.result = ""

    def getResult(self) -> str:
        return self.result

    def setResult(self, newResult: str) -> None:
        self.result = newResult

    def visitVariable(self, v: Variable) -> None:
        self.setResult(v.getValue())

    def visitConstant(self, c: Constant) -> None:
        self.setResult(str(c.getValue()))

    def visitBinaryOperator(self, op: BinaryOperator, symbol: str) -> None:
        op.getLeft().accept(self)
        leftValue = self.getResult()

        op.getRight().accept(self)
        rightValue = self.getResult()

        newResult = f"({leftValue} {symbol} {rightValue})"
        self.setResult(newResult)

    def visitSum(self, s: Sum) -> None:
        self.visitBinaryOperator(s, '+')

    def visitMul(self, m: Mul) -> None:
        self.visitBinaryOperator(m, '*')

    def visitDiv(self, d: Div) -> None:
        self.visitBinaryOperator(d, '%')

    def visitSub(self, st: Sub) -> None:
        self.visitBinaryOperator(st, '-')
