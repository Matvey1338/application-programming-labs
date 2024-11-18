import argparse
from argparse import Namespace

from Datafr import make_dataframe


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
    parser.add_argument("csv_path", type=str, help="path to csv file")
    return parser.parse_args()


def main():
    args = _parse_arguments()
    make_dataframe(args.csv_path)


if __name__ == "__main__":
    main()
