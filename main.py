import random

from lib.ast.operations import Sum, Mul, Div, Sub
from lib.ast.expresion import Constant, Variable, Expresion
from lib.ast.visitor import StringExpresionVisitor, EvaluateExpresionVisitor, CountVisitor
from lib.ast.utils import generateRandomAST, selectRandomTree, adhere

NUMBERS = 7
TARGET = 323
POPULATION = 1

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
print(expresions[0])
exp_c = selectRandomTree(expresions[0])
print(exp_c)
exp_c.accept(sev)
print(sev.getResult())
print(representations)
adhere(expresions[0], exp_c)
expresions[0].accept(sev)
print(sev.getResult())
#print(counts)

