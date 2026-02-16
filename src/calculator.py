"""
Simple Calculator
Basic Arithmic operations

"""


def add(x: float, y: float) -> float:
    """
    Docstring for add

    :param x: Description
    :type x: float
    :param y: Description
    :type y: float
    :return: Description
    :rtype: float
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    Docstring for subtract

    :param x: Description
    :type x: float
    :param y: Description
    :type y: float
    :return: Description
    :rtype: float
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Docstring for multiply

    :param x: Description
    :type x: float
    :param y: Description
    :type y: float
    :return: Description
    :rtype: float
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    Docstring for divide

    :param x: Description
    :type x: float
    :param y: Description
    :type y: float
    :return: Description
    :rtype: float
    """
    if y == 0:
        raise ValueError("Cant divide by Zero")
    return x / y
