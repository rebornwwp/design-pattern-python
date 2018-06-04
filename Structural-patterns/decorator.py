#!/usr/bin/env python3
"""
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending
functionality.
"""

import abc


class Component(metaclass=abc.ABCMeta):
    """
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """
    @abc.abstractmethod
    def operation(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        # do before
        print("A doing before")
        self._component.operation()
        # do after
        print("A doing after")


class ConcreteDecoratorB(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        # do before
        print("B doing before")
        self._component.operation()
        # do after
        print("B doing after")


class ConcreteComponent(Component):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def operation(self):
        print("concreate Component doing")


def main():
    concrete_component = ConcreteComponent()
    concrete_component_a = ConcreteDecoratorA(concrete_component)
    concrete_component_b = ConcreteDecoratorB(concrete_component_a)
    concrete_component_a.operation()
    print("="*40)
    concrete_component_b.operation()
    print("="*40)


if __name__ == '__main__':
    main()
