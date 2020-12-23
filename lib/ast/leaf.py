from .expresion import Expresion

class Constant(Expresion):

    def __init__(self, value: int):
        super(Constant, self).__init__(value)

    def accept(self, visitor):
        visitor.visitConstant(self)

class Variable(Expresion):

    def __init__(self, value: str):
        super(Variable, self).__init__(value)

    def accept(self, visitor):
        visitor.visitVariable(self)
