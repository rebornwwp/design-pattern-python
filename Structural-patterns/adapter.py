"""
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incopatible interfaces.
"""

import abc


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that client uses.
    """

    def __init__(self):
        self._adapter = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def request(self):
        self._adapter.specific_request()


class Adaptee(object):
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self):
        print("hello world")


def main():
    adaptee = Adaptee()
    adaptee.specific_request()
    print("="*40)
    adapter = Adapter()
    adapter.request()


if __name__ == '__main__':
    main()
