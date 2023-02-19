from enum import Enum


class Operator(Enum):
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDED_BY = "/"


def add(x, y) -> float:
    return x + y


def subtract(x, y) -> float:
    return x - y


def multiply(x, y) -> float:
    return x * y


def divide(x, y) -> float:
    return x / y


def operator(operator_inst: Operator):
    match operator_inst:
        case Operator.PLUS:
            op = add
        case Operator.MINUS:
            op = subtract
        case Operator.TIMES:
            op = multiply
        case Operator.DIVIDED_BY:
            op = divide

    return op
