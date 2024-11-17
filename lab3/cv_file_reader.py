import cv2
import matplotlib.pyplot as plt

second_image = "Example2.jpg"


def image_analyze(path: str):
    """
       Analyzes the color image by generating and displaying its histogram.

       Args:
           path (str): The file path to the input image.

       Description:
           - Loads the input image in color mode.
           - Extracts and prints the dimensions of the image (width, height, and number of channels).
           - Computes the histogram for each color channel (Blue, Green, Red) using OpenCV.
           - Plots the histograms with Matplotlib, including proper labels, grid, and legends.
           - The x-axis represents pixel intensity values (0-255), while the y-axis shows the pixel count.

       Example:
           image_analyze("path/to/image.jpg")
       """
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
    """
      Blends two images together and displays the result alongside the original image.

      Args:
          og_image (str): The file path to the first (original) image.
          blend_image (str): The file path to the second image to blend with the original.

      Description:
          - Loads both images in color mode using OpenCV.
          - Resizes the second image to match the dimensions of the first image.
          - Blends the two images using the specified alpha (opacity) and beta values.
          - Displays both the original image and the blended image side by side using Matplotlib.
          - Saves the blended image to a file (`./lab3/blended_image.jpg`).

      Example:
          image_blend("path/to/image1.jpg", "path/to/image2.jpg")
      """
    image1 = cv2.imread(og_image)
    image2 = cv2.imread(blend_image)

    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    alpha = 0.5
    beta = 1 - alpha

    blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.axis('off')
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 2, 2)
    plt.title("Blended Image")
    plt.axis('off')
    plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
    plt.show()

    cv2.imwrite('./lab3/blended_image.jpg', blended_image)
