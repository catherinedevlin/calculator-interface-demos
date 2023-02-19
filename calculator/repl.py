from cmd import Cmd

from . import core


class Calculator(Cmd):
    def _parse_args(self, arg):
        args = [float(n) for n in arg.split()]
        assert len(args) == 2, "Need two numbers"
        return args

    def do_add(self, raw_arg):
        "Adds two numbers together"
        args = self._parse_args(raw_arg)
        result = core.add(args[0], args[1])
        print(f"{result=}")

    def do_subtract(self, raw_args):
        "Subtracts second number from first"
        args = self._parse_args(raw_args)
        result = core.subtract(args[0], args[1])
        print(f"{result=}")

    def do_multiply(self, raw_args):
        "Multiplies two numbers together"
        args = self._parse_args(raw_args)
        result = core.multiply(args[0], args[1])
        print(f"{result=}")

    def do_divide(self, arg):
        "Divides first number by second"
        args = self._parse_args(arg)
        result = core.multiply(args[0], args[1])
        print(f"{result=}")

    def do_7(self, arg):
        print(f'{arg=}')

    def default(self, line):
        args = line.split()
        assert len(args) == 3, "Need number, then operator, then number"
        (x, raw_op, y) = (float(args[0]), core.Operator(args[1]), float(args[2]))
        op_function = core.operator(raw_op)
        result = op_function(x, y)
        print(f"{result=}")


def main():
    Calculator().cmdloop()
