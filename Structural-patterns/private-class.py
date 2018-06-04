"""
Control write access to class attributes.
Separate data from methods that use it.
Encapsulate class data initialization.
"""


class DataClass:
    """
    Hide all the attributes.
    this class is implemented by python descriptors.
    """

    def __init__(self):
        print("init")
        self.value = None

    def __get__(self, instance, owner):
        print("get value")
        return self.value

    def __set__(self, instance, value):
        print("set value")
        if self.value is None:
            self.value = value


class MainClass:
    """
    Initialize data class through the data class's constructor.
    """

    attribute = DataClass()

    def __init__(self, value):
        self.attribute = value


def main():
    m = MainClass(True)
    m.attribute = False


if __name__ == "__main__":
    main()
