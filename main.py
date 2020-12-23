from lib.ast.operations import Sum, Mul, Div, Sub
from lib.ast.expresion import Constant, Variable
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

var = {
    "x" : x,
    "y" : y
}

print(f"x={x}, y={y}")

sev = StringExpresionVisitor()
eev = EvaluateExpresionVisitor(**var)

expresion.accept(sev)
expresion.accept(eev)

print(sev.getResult())
print(eev.getResult())
