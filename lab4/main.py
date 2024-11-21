import argparse
from argparse import Namespace

from Datafr import *


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
    sd = make_dataframe(args.csv_path)
    print(f"New data frame\n{sd}")

    sd = additional_columns(sd)
    print(f"Make new columns shape\n{sd}")

    print(f"calculate shape\n{calculate_stat(sd)}")

    max_width = 1000
    max_height = 1000
    print(f"Filtered dataframe\n{filter_images_by_size(sd, max_width, max_height)}")

    sd = make_area_column(sd)
    print(f"Dataframe with area column{sd}")

    make_histogram(sd)


if __name__ == "__main__":
    main()
