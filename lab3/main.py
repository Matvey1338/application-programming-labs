import argparse
from argparse import Namespace


def _parse_arguments() -> Namespace:
    """
    Parse arguments from stdin in execution moment.
    Returns:
    list: list of the arguments
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="path to file to convert",
    )
    parser.add_argument("path", type=str, help="path to file")

    return parser.parse_args()


def main():
    args = _parse_arguments()


if __name__ == "__main__":
    main()
