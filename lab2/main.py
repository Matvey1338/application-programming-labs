import argparse
from argparse import Namespace

from image_to_dir import download_images, base_dir
from csv_to_file import convert_to_csv, csv_file


def _parse_arguments() -> Namespace:
    """
    Parse arguments from stdin in execution moment.
    Returns:
    list: list of the arguments
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Download target images",
    )
    parser.add_argument("keyword", type=str, help="Keyword for image search.")
    parser.add_argument("-c", "--csv", type=str, default=csv_file, help="Path to csv file.")
    parser.add_argument("-d", "--dir", type=str, default=base_dir, help="Path to directory where images store.")
    parser.add_argument("-n", "--number", type=int, default=50, help="Number of downloading files.")

    return parser.parse_args()


def main():
    args = _parse_arguments()
    images_dir = download_images(args.keyword, args.number, save_dir=args.dir)
    csv_paths = convert_to_csv(images_dir, csv_filename=args.csv)


if __name__ == "__main__":
    main()
