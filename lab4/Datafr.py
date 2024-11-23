from typing import Optional

import cv2
import matplotlib.pyplot as plt
import pandas as pd


def make_dataframe(path: str) -> Optional[pd.DataFrame]:
    """
       Loads a CSV file and prepares a DataFrame with columns for relative and absolute paths.

       Parameters:
           path (str): The file path to the CSV file.

       Returns:
           Optional[pd.DataFrame]: A DataFrame with 'Relative Path' and 'Absolute Path' columns.
           Returns None if the file is not found.
       """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise

    pd.set_option('display.max_colwidth', None)
    df.columns = ['Relative_Path', 'Absolute_Path']

    return df


def additional_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds additional columns ('Height', 'Width', 'Depth') to the DataFrame based on image properties.

    Parameters:
        df (pd.DataFrame): The input DataFrame with an 'Absolute Path' column.

    Returns:
        pd.DataFrame: The updated DataFrame with the new columns.
    """
    def get_image_info_cv2(image_path):
        try:
            img = cv2.imread(image_path)
            if img is not None:
                height, width, channels = img.shape
                return height, width, channels
            else:
                print(f"Can't load image: {image_path}")
                return None, None, None
        except Exception:
            raise

    df[['Height', 'Width', 'Depth']] = df['Absolute_Path'].apply(
        lambda image_path: pd.Series(get_image_info_cv2(image_path))
    )
    return df


def calculate_stat(df: pd.DataFrame) -> pd.DataFrame:
    """
       Calculates descriptive statistics for the 'Height', 'Width', and 'Depth' columns.

       Parameters:
           df (pd.DataFrame): The input DataFrame with 'Height', 'Width', and 'Depth' columns.

       Returns:
           pd.DataFrame: A DataFrame containing descriptive statistics for these columns.
       """
    return df[['Height', 'Width', 'Depth']].describe()


def filter_images_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Filters images by maximum width and height.

    Parameters:
        df (pd.DataFrame): The input DataFrame with 'Height' and 'Width' columns.
        max_width (int): The maximum allowable width for images.
        max_height (int): The maximum allowable height for images.

    Returns:
        pd.DataFrame: A DataFrame containing only rows where the image dimensions
                      are within the specified limits.
    """
    filtered_df = df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]
    return filtered_df


def make_area_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a new column ('Area') to the DataFrame, calculates the area of each image,
    and sorts the DataFrame by area in ascending order.

    Parameters:
        df (pd.DataFrame): The input DataFrame with 'Height' and 'Width' columns.

    Returns:
        pd.DataFrame: The updated DataFrame with the new 'Area' column.
    """
    df['Area'] = df['Height'] * df['Width']
    return df


def sort_area(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(by='Area')
    return df


def make_histogram(df: pd.DataFrame) -> None:
    """
    Creates and displays a histogram of image areas.

    Parameters:
        df (pd.DataFrame): The input DataFrame with the 'Area' column.

    """
    plt.figure(figsize=(8, 6))
    plt.hist(df['Area'], bins=10, color='blue', edgecolor='black')

    plt.title('Распределение площадей изображений', fontsize=14)
    plt.xlabel('Площадь изображения (пиксели)', fontsize=12)
    plt.ylabel('Частота', fontsize=12)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
