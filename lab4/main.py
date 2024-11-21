import argparse
from argparse import Namespace

from  Datafr import *
#from Datafr import make_dataframe, filter_images_by_size, show_area_dist


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
    ds = filter_images_by_size(sd, 1000, 1000)
    print(ds)


if __name__ == "__main__":
    main()
