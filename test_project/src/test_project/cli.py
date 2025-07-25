from argparse import ArgumentParser
from typing import Optional, Sequence
from test_project import __version__


def cli(args: Optional[Sequence[str]] = None) -> None:
    p = ArgumentParser(description="A test project", conflict_handler="resolve")
    p.add_argument(
        "-V",
        "--version",
        action="version",
        help="Show the conda-prefix-replacement version number and exit.",
        version="test_project %s" % __version__,
    )

    parsed, unknown = p.parse_known_args(args)

    # do something with the args
    print("CLI template - fix me up!")

    # No return value means no error.
    # Return a value of 1 or higher to signify an error.
    # See https://docs.python.org/3/library/sys.html#sys.exit


if __name__ == "__main__":
    import sys

    cli(sys.argv[1:])
