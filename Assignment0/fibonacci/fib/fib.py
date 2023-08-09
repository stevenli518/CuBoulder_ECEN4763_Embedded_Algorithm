"""This Fib Module can be used to modularize the fibonacci sequence."""


class Fib:
    """Class represents the fibonacci algorithm data structure."""

    def __init__(self):
        """Construct a new instance."""
        self.number = 0

    def calculate(self, number):
        """Calculate the final number of a fibonacci sequence value of number using loops."""
        if isinstance(number, int) and number >= 0:
            if number == 0:
                self.number = 0
            elif number in (1, 2):
                self.number = 1
            else:
                prev = 0
                curr = 1
                while number > 1:
                    prev, curr = curr, prev + curr
                    number -= 1
                self.number = curr
        else:
            self.number = None

    def get_fib(self, number):
        """Calculate the fibonacci number and return it."""
        self.calculate(number)
        return self.number


def calculate_fib(number):
    """Return the final number of a fibonacci sequence value of number using recursion."""
    if isinstance(number, int) and number >= 0:
        if number == 0:
            return 0
        if number in (1, 2):
            return 1
        return calculate_fib(number - 2) + calculate_fib(number - 1)
    return None
