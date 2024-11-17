import cv2
import matplotlib.pyplot as plt

second_image = "Example2.jpg"


def image_analyze(path: str):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
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


def image_blend(og_image: str, blend_image: str):
    # Чтение изображений
    image1 = cv2.imread(og_image)
    image2 = cv2.imread(blend_image)

    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Установка параметра прозрачности (alpha)
    alpha = 0.5  # Прозрачность (0.0 полностью прозрачно, 1.0 полностью непрозрачно)
    beta = 1 - alpha

    # Наложение изображений
    blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

    # Показ результата
    plt.figure(figsize=(10, 6))
    plt.title("Blended Image")
    plt.axis('off')
    #plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
    plt.imshow(blended_image)
    plt.show()

    cv2.imwrite('./lab3/blended_image.jpg', blended_image)
