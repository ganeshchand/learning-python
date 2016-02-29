# You want to change the output produced by printing or viewing instances to something more readable and sensible
# To change the string representation of an instance, define the __str__() and __repr__() methods.


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = x

    def __repr__(self):  # Object representation
        return "Pair({0.x!r},{0.y!r})".format(self)

    def __str__(self):  # String representation
        return "({0.x!s},{0.y!s})".format(self)


if __name__ == "__main__":
    p = Pair(1, 2)
    # When you just type class instance p, you would want to display in an object format. When you evaluate p, it calls __repr__()
    print(p.__repr__())
    print(p.__str__())
    print "Calling p.__str__() inside the print results in {}.".format(p.__str__())
    print "Calling p inside the print results in {}. It calls __str__()".format(p)


"""
Defining __repr__() and __str__() is often good practice, as it can simplify debugging
and instance output.
the format code {0.x} specifies the x-attribute of argument 0.The 0 is actually
the instance self
"""