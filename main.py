import random

from lib.ast.operations import Sum, Mul, Div, Sub
from lib.ast.expresion import Constant, Variable, Expresion
from lib.ast.visitor import StringExpresionVisitor, EvaluateExpresionVisitor, CountVisitor
from lib.ast.utils import generateRandomAST

NUMBERS = 4
TARGET = 323
POPULATION = 500

constants = random.sample(range(0, 50), NUMBERS)

eev = EvaluateExpresionVisitor()
sev = StringExpresionVisitor()
cv = CountVisitor()

expresions = [generateRandomAST(constants=constants) for _ in range(POPULATION)]

representations = []
values = []
counts = []

for exp in expresions:
    exp.accept(eev)
    exp.accept(sev)
    exp.accept(cv)
    values.append(eev.getResult())
    counts.append(cv.getResult())
    representations.append(sev.getResult())

print(representations)
print(values)
print(counts)

