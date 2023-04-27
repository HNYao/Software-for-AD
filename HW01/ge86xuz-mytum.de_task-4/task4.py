"""
Goal of Task 4:
    Implement a function that returns the n-th number of the Fibonacci Sequence.
"""


def fibonacci(n):
    """
    input:
        n (type: int)

    output:
        fibonacci_number (type: int)
    """

    # Task:
    # ToDo: Calculate the n-th number of the Fibonacci Sequence.
    #       The usage of python packages is not allowed for this task.
    # Hint: F_n = F_n-1 + F_n-2
    ########################
    #  Start of your code  #
    ########################
    if n > 2:
        fibonacci_number = fibonacci(n - 2) + fibonacci(n - 1)
    elif n > 0:
        return 1
    else:
        return 0
    ########################
    #   End of your code   #
    ########################

    return fibonacci_number


if __name__ == "__main__":
    assert fibonacci(9) == 34
