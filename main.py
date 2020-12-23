from lib.ast.operations import Sum, Mul, Div, Sub
from lib.ast.leaf import Constant, Variable
from lib.ast.visitor import StringBuilderExpresion

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
stringExpresion = StringBuilderExpresion()
expresion.accept(stringExpresion)

print(stringExpresion.getResult())
