from abc import ABC, abstractmethod

class Expresion(ABC):

    def __init__(self, value: any):
        self.value = value

    @abstractmethod
    def accept(self, visitor):
        pass

    def getValue(self):
        return self.value
