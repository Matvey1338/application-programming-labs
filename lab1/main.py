import argparse
from argparse import Namespace


def parser_of_file() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Returns most count number codes",
    )
    parser.add_argument("filename", type=str, help="Path to file.")

    return parser.parse_args()
