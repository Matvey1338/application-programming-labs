import csv
import os


class ImgIterator:
    """
    The iterator class, for read rows from csv
    """

    def __init__(self, name: str):
        """
        Init iterator.

        Parameters:
        name (str): name of csv-file.
        """
        self.csv_file = name if name.endswith(".csv") else f"{name}.csv"
        self.file_exist = os.path.exists(self.csv_file)

    def __iter__(self):
        """
        Iter method.
        If target file don't exist set self.file_exist as False.
        """

        if not self.file_exist:
            return iter([])

        self.file = open(self.csv_file, newline="")
        self.csvreader = csv.reader(self.file)
        return self

    def __next__(self):
        """
        Next method for iterations.
        If self.file_exist is not True, don't start the iteration.
        """

        if not self.file_exist:
            raise StopIteration

        try:
            return next(self.csvreader)
        except StopIteration:
            self.file.close()
            raise StopIteration
