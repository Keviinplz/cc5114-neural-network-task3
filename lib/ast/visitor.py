"""
Visitor Module

Module that has all Visitor to AST.

"""


from .operations import Sum, Mul, Div, Sub, BinaryOperator
from .expresion import Constant, Variable

class Visitor():
    """
    Class Visitor

    This class is parent of all visitors classes bassed on AST.
    """

    def __init__(self, result):
        """
        Class Visitor

        This class is parent of all visitor classes bassed on AST.

        Parameters:
        
        result: any
            Result after visit an AST structure
            Can be any type, depends of the objetive of the visitor.
        """

        self.result = result

    def getResult(self) -> any:
        """
        getResult

        Return result of Visitor

        returntype: any
            Result of visitor after visit an AST structure
        """

        return self.result
    
    def setResult(self, newValue: any) -> None:
        """
        setResult

        Setter result.

        """

        self.result = newValue
    
    def visitBinaryOperator(self, op: BinaryOperator, function) -> None:
        """
        visitBinaryOperator

        Handle a Binary Operator visit, updating result with
        a function that depends of operator.

        Parameters:

        op: BinaryOperator
            A binary Operator object

        function: function
            Function that apply to new value, to set result.
        """


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
        if v.getValue() not in self.variableSet.keys():
            raise KeyError(f"Free ocurrency of {v.getValue()}. Please declare it in Visitor Constructor")
        value = self.variableSet[v.getValue()]
        if type(value) != float or type(value) != int:
            raise SyntaxError(f"{value} must to be Float or Integer, {type(value)} is not allowed")

        self.setResult(value)
        
    def visitConstant(self, c: Constant) -> None:
        self.setResult(float(c.getValue()))


