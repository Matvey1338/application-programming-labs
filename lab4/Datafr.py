import pandas as pd



def make_dataframe(path):
    df = pd.read_csv(path)
    print(df)