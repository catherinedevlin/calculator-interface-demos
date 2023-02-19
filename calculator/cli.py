from enum import Enum

import click

from . import core


@click.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.option(
    "-o",
    "--operation",
    type=core.Operator,
    default=core.Operator.PLUS,
    help="+, -, *, or /.  Escape `*` with backslash.",
)
def main(x, y, operation):
    op = core.operator(operation)
    result = op(x, y)
    print(f"{result=}")


if __name__ == "__main__":
    main()
