import cv2
import pandas as pd
import matplotlib.pyplot as plt


def make_dataframe(path):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print("There is not csv file to dataframe")
        return None

    pd.set_option('display.max_colwidth', None)
    df.columns = ['Relative Path', 'Absolute Path']

    return df


def additional_columns(df):
    def get_image_info_cv2(image_path):
        try:
            img = cv2.imread(image_path)
            if img is not None:
                height, width, channels = img.shape
                return height, width, channels
            else:
                print(f"Can't load image: {image_path}")
                return None, None, None
        except Exception as e:
            print(f"Error while compilating {image_path}: {e}")
            return None, None, None

    df[['Height', 'Width', 'Depth']] = df['Absolute Path'].apply(
        lambda image_path: pd.Series(get_image_info_cv2(image_path))
    )


def calculate_stat(df):
    # Вычисляем статистическую информацию для столбцов "Height", "Width" и "Depth"
    stats = df[['Height', 'Width', 'Depth']].describe()


def filter_images_by_size(df, max_width, max_height):
    """
    Фильтрует строки DataFrame на основе заданных максимальных значений ширины и высоты изображения.

    Параметры:
    - df (pd.DataFrame): DataFrame с колонками 'Height' и 'Width'.
    - max_width (int): Максимально допустимая ширина.
    - max_height (int): Максимально допустимая высота.

    Возвращает:
    - pd.DataFrame: Отфильтрованный DataFrame.
    """
    # Условие фильтрации
    filtered_df = df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]
    return filtered_df


def make_area_column(df):
    df['Area'] = df['Height'] * df['Width']
    df = df.sort_values(by='Area')


def make_histogram(df):
    plt.figure(figsize=(8, 6))
    plt.hist(df['Area'], bins=10, color='blue', edgecolor='black')

    # Подписи графика
    plt.title('Распределение площадей изображений', fontsize=14)
    plt.xlabel('Площадь изображения (пиксели)', fontsize=12)
    plt.ylabel('Частота', fontsize=12)

    # Отобразить график
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
