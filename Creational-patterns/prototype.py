"""
Specify the kinds of objects to create using prototypical instance,
and create new objects by copying this prototype.
"""

import copy


class Prototype(object):
    """
    Example class to be copied.
    """

    pass


def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)
    print(prototype_copy is prototype)


if __name__ == '__main__':
    main()
