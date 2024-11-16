import argparse
from argparse import Namespace

from cv_file_reader import image_analyze


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
    parser.add_argument("pth1image", type=str, help="path to first image")
    parser.add_argument("pth2image", type=str, help="path to second image")
    return parser.parse_args()


def main():
    args = _parse_arguments()
    image_analyze(args.pth1image)


if __name__ == "__main__":
    main()
