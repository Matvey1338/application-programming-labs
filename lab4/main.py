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
    parser.add_argument("pth1image", type=str, help="path to first image")
    parser.add_argument("-p", "--pth2image", type=str, default=second_image, help="path to second image")
    parser.add_argument("-t", "--transparency", type=float, default=0.5, help="transparency modifier")
    return parser.parse_args()

