import argparse
from argparse import Namespace

from cv_file_reader import *


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
    parser.add_argument("pth1image", type=str, help="path to first image")
    parser.add_argument("-p", "--pth2image", type=str, default=second_image, help="path to second image")
    parser.add_argument("-t", "--transparency", type=float, default=0.5, help="transparency modifier")
    return parser.parse_args()


def main():
    try:
        args = _parse_arguments()
        image = image_analyze(args.pth1image)
    except FileNotFoundError:
        print(FileNotFoundError)
        return None
    print(f"Размер полученного изображения, Высота: {image_shape(image)[0]}, Ширина: {image_shape(image)[1]}")

    print("Гистограмма полученного изображения")
    make_histogram(image)

    print("Накладываем изображение на другое...")
    blended_image = image_blend(args.pth1image, args.pth2image, args.transparency)

    print("Гистограмма смешанного изображения")
    make_histogram(blended_image)

    print("Сравнение оригинала и преобразованного экземпляра")
    show_comprasion(image, blended_image)

    print("Сохраняем изображение")
    save_image(blended_image)


if __name__ == "__main__":
    main()
