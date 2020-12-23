from abc import ABC, abstractmethod

class Expresion(ABC):

    def __init__(self, value: any):
        self.value = value

    @abstractmethod
    def accept(self, visitor):
        pass

    def getValue(self):
        return self.value

class BinaryOperator(Expresion):
    
    def __init__(self, left: Expresion, right: Expresion):
        self.left = left
        self.right = right

    def getLeft(self) -> Expresion:
        return self.left

    def getRight(self) -> Expresion: 
        return self.right

class Constant(Expresion):

    def __init__(self, value: float):
        super(Constant, self).__init__(value)

    def accept(self, visitor) -> None:
        visitor.visitConstant(self)

class Variable(Expresion):

    def __init__(self, value: str):
        super(Variable, self).__init__(value)

    def accept(self, visitor) -> None:
        visitor.visitVariable(self)


