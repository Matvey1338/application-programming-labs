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
    try:
        sd = make_dataframe(args.csv_path)
        print(f"New data frame\n{sd}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    try:
        sd = additional_columns(sd)
        print(f"Make new columns shape\n{sd}")
    except Exception as e:
        print(f"Error: {e}")
        return None

    print(f"calculate shape\n{calculate_stat(sd)}")

    max_width = 1000
    max_height = 1000
    print(f"Filtered dataframe\n{filter_images_by_size(sd, max_width, max_height)}")

    sd = make_area_column(sd)
    print(f"Dataframe with area column{sd}")

    sd = sort_area(sd)
    print(f"Sorted Dataframe:\n{sd}")

    make_histogram(sd)


if __name__ == "__main__":
    main()
