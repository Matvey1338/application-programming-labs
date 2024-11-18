import pandas as pd


def make_dataframe(path):
    df = pd.read_csv(path)
    pd.set_option('display.max_colwidth', None)
    print(df.head())
