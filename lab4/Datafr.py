import cv2
import pandas as pd


def make_dataframe(path):
    df = pd.read_csv(path)
    pd.set_option('display.max_colwidth', None)
    df.columns = ['Relative Path', 'Absolute Path']

    def get_image_info_cv2(image_path):
        try:
            img = cv2.imread(image_path)
            if img is not None:
                height, width, channels = img.shape
                return height, width, channels
            else:
                print(f"Не удалось загрузить изображение: {image_path}")
                return None, None, None
        except Exception as e:
            print(f"Ошибка при обработке {image_path}: {e}")
            return None, None, None

    df[['Height', 'Width', 'Depth']] = df['Absolute Path'].apply(
        lambda path: pd.Series(get_image_info_cv2(path))
    )
    # Вычисляем статистическую информацию для столбцов "Height", "Width" и "Depth"
    stats = df[['Height', 'Width', 'Depth']].describe()

    # Выводим статистику
    print(df)
    return df


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
