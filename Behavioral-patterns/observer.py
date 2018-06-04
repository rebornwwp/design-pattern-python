#!/usr/bin/env python3
"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.
"""

import abc


class Subject(object):
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer(object, metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self, arg):
        self._observer_state = arg
        print(self, self._observer_state)


def main():
    subject = Subject()
    concrete_observer_A = ConcreteObserver()
    concrete_observer_B = ConcreteObserver()
    subject.attach(concrete_observer_A)
    subject.attach(concrete_observer_B)
    subject.subject_state = 123
    subject.subject_state = 234


if __name__ == '__main__':
    main()
