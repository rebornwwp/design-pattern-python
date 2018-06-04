"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface for opration that create abstract product
    objects.
    """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Define a product object tobe created by the conresponding concrete
    factory.
    Implement the AbstractProducer interface.
    """

    def interface_a(self):
        print("conrete product a1")


class ConcreteProductA2(AbstractProductA):
    """
    Define a product object tobe created by the conresponding concrete
    factory.
    Implement the AbstractProducer interface.
    """

    def interface_a(self):
        print("conrete product a2")


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    """
    Define a product object tobe created by the conresponding concrete
    factory.
    Implement the AbstractProducer interface.
    """

    def interface_b(self):
        print("conrete product b1")


class ConcreteProductB2(AbstractProductB):
    """
    Define a product object tobe created by the conresponding concrete
    factory.
    Implement the AbstractProducer interface.
    """

    def interface_b(self):
        print("conrete product b2")


def main():
    for factory in [ConcreteFactory1(), ConcreteFactory2()]:
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()


if __name__ == '__main__':
    main()
