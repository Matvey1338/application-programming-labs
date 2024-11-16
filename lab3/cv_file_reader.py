import cv2
import matplotlib.pyplot as plt


def image_analyze(path: str):
    image = cv2.imread(path,  cv2.IMREAD_COLOR)
    height, width, channels = image.shape
    print("Image shape:", width, "x", height)

    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 6))

    for i, color in enumerate(colors):

        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])

        plt.plot(histogram, color=color, label=f"{color.upper()} channel")
        plt.xlim([0, 256])

    # Добавляем подписи и легенду
    plt.title("Гистограмма цветного изображения")
    plt.xlabel("Значение интенсивности пикселя")
    plt.ylabel("Количество пикселей")
    plt.legend()
    plt.grid()
    plt.show()

