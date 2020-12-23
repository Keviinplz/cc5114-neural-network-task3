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
    """
    Class StringExpresionVisitor

    A visitor operator that convert an AST to his representation
    in String.

    """
    def __init__(self):
        """
        Class StringExpresionVisitor

        A visitor operator that convert and AST to his representation
        in String.

        """
        super(StringExpresionVisitor, self).__init__("")

    def visitSum(self, s: Sum) -> None:
        """
        visitSum

        Set result to 'x + y' string
        when x is the left expresion of the sum
        and y is the right expresion of the sum

        """
        self.visitBinaryOperator(s, lambda x, y : f"({x} + {y})")

    def visitMul(self, m: Mul) -> None:
        """
        visitMul

        Set result to 'x * y' string
        when x is the left expresion of the multiplication
        and y is the right expresion of the multiplication

        """

        self.visitBinaryOperator(m, lambda x, y : f"({x} * {y})")

    def visitDiv(self, d: Div) -> None:
        """
        visitDiv

        Set result to 'x % y' string
        when x is the left expresion of the division
        and y is the right expresion of the division

        """
        self.visitBinaryOperator(d, lambda x, y : f"({x} % {y})")

    def visitSub(self, st: Sub) -> None:
        """
        visitSub

        Set result to 'x - y' string
        when x is the left expresion of the substract
        and y is the right expresion of the substract

        """
 
        self.visitBinaryOperator(st, lambda x, y : f"({x} - {y})")

    def visitVariable(self, v: Variable) -> None:
        """
        visitVariable

        Set result to the string representation of variable 
        
        """
 
        self.setResult(v.getValue())

    def visitConstant(self, c: Constant) -> None:
        """
        visitConstant

        Set result to the string representation of constant.

        """
        self.setResult(str(c.getValue()))


class EvaluateExpresionVisitor(Visitor):
    """
    Class EvaluateExpresionVisitor

    A visitor operator that convert an AST to a value representation.

    """

    def __init__(self, **kwargs):
        """
        Class EvalueExpresionVisitor

        A visitor operator that convert an AST to a value representation.

        Parameters:

        **kwargs:
            Values of Identifiers of AST
            Examples:
                -   ```html
                        ex = Div(Variable("x"), Constant(3))
                        eev = EvaluateExpresionVisitor(x=3)
                        ex.accept(eev)

                        eev.getResult()
                        >>> 1
                    ```

                -   ```html
                        ex = Div(Sum(Variable("x"), Variable("y")), Sub(Constant(3), Variable("z")))
                        eev = EvaluateExpresionVisitor(x=2, y=6, z=1)
                        ex.accept(eev)

                        eev.getResult()
                        >>> 4
                    ```
        """
        super(EvaluateExpresionVisitor, self).__init__(0)
        self.variableSet = kwargs

    def visitSum(self, s: Sum) -> None:
        """
        visitSum

        Set result to the sum of apply visit to left value and right value

        """
        self.visitBinaryOperator(s, lambda x, y : x + y)

    def visitSub(self, st: Sub) -> None:
        """
        visitSub

        Set result to the substract of apply visit to left value and right value

        """
        self.visitBinaryOperator(st, lambda x, y : x - y)

    def visitMul(self, m: Mul) -> None:
        """
        visitMul

        Set result to the multiplication of apply visit to left value and right value

        """
        self.visitBinaryOperator(m, lambda x, y : x * y)

    def visitDiv(self, d: Div) -> None:
        """
        visitDiv

        Set result to the division of apply visit to left value and right value

        """
        self.visitBinaryOperator(d, lambda x, y : x / y if y != 0 else 1)
   
    def visitVariable(self, v: Variable) -> None:
        """
        visitVariable

        Set result to the real value of a Variable

        If visitor doesn't declare the value of the variable, raise KeyError

        If value of the variable if invalid (it's not Float or Integer), raise SyntaxError

        """
        if v.getValue() not in self.variableSet.keys():
            raise KeyError(f"Free ocurrency of {v.getValue()}. Please declare it in Visitor Constructor")
        value = self.variableSet[v.getValue()]
        if type(value) != float or type(value) != int:
            raise SyntaxError(f"{value} must to be Float or Integer, {type(value)} is not allowed")

        self.setResult(value)
        
    def visitConstant(self, c: Constant) -> None:
        """
        visitConstant
    
        Set result to the value of the Constant.
        Converts Constant to float.

        """
        self.setResult(float(c.getValue()))


