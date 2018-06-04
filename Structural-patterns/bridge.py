"""
Decouple an abstraction from its implementation so that the two can vary independently.
"""

import abc


class Abstraction(object):
    """
    Define the abstraction's interface.
    Maintain a reference to an object of type Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def operation(self):
        self._imp.operation_imp()


class Implementor(metaclass=abc.ABCMeta):
    """
    Define the interface for implementation classes. This interface
    doesn't have to correspond exactly to Abstraction's interface; in
    fact the two interfaces can be quite different. Typically the
    Implementor interface provides only primitive operations, and
    Abstraction defines higher-level operations based on these
    primitives.
    """
    @abc.abstractmethod
    def operation_imp(self):
        pass


class ConcreteImplementorA(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implement.
    """

    def operation_imp(self):
        print("Concrete implementor A")


class ConcreteImplementorB(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implement.
    """

    def operation_imp(self):
        print("Concrete implementor B")


def main():
    concrete_imp_a = ConcreteImplementorA()
    abstraction = Abstraction(concrete_imp_a)
    abstraction.operation()


if __name__ == '__main__':
    main()
