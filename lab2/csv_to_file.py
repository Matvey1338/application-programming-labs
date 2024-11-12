import csv
import os

csv_file = "file.csv"


def convert_to_csv(where_images: str, csv_filename: str = csv_file) -> str:
    """
     Function to convert files in directory to csv file with list of links.

    Parameters:
        where_images (str): where the images are located
        csv_filename (str): the csv file, where paths are located
    """

    with open(csv_filename, "w", newline="") as csvfile:
        image_dir = os.path.abspath(where_images)
        names = ("Real.path", "Absolute.path")

        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(names)

        for file in os.listdir(where_images):
            absolute_path = os.path.join(image_dir, file)
            real_path = os.path.relpath(absolute_path, start=csv_filename)
            print(real_path, absolute_path)

            csv_writer.writerow((real_path, absolute_path))

    return csv_filename
