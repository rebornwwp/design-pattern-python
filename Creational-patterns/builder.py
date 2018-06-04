"""
Separate the construction of a complex object from its representation so
that the same construction process can create different representations.
"""

import abc


class Director(object):
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def _build_part_a(self, a=1):
        self.product.a = a
        print("build part a")
        return self

    def _build_part_b(self, b=2):
        self.product.b = b
        print("build part b")
        return self

    def _build_part_c(self, c=3):
        self.product.c = c
        print("build part c")
        return self

    def get_product(self):
        return self.product


class Product(object):
    """
    Represent the complex object under construction.
    """

    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product
    print(product.a)
    print(product.b)
    print(product.c)
    print("="*40)
    # 链式构建处理
    concrete_builder._build_part_a(10)._build_part_b(11)._build_part_c(12)
    product = concrete_builder.get_product()
    print(product.a)
    print(product.b)
    print(product.c)


if __name__ == "__main__":
    main()
