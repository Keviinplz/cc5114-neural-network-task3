from lib.ast.operations import Sum, Mul, Div, Sub
from lib.ast.leaf import Constant, Variable
from lib.ast.visitor import StringExpresionVisitor, EvaluateExpresionVisitor

expresion = Div(
        Mul(
            Sum(
                Variable("y"),
                Constant(5)
            ),
            Sum(
                Variable("x"),
                Constant(1)
            )
        ),
        Sub(
            Constant(8),
            Variable("x")
        )    
)   
x = 3
y = 5

print(f"x={x}, y={y}")
evaluateExpresion = EvaluateExpresionVisitor(x=x, y=y)
stringExpresion = StringExpresionVisitor()
expresion.accept(evaluateExpresion)
expresion.accept(stringExpresion)
print(stringExpresion.getResult())
print(evaluateExpresion.getResult())
