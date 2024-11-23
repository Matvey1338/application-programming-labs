import cv2
import matplotlib.pyplot as plt
import numpy

second_image = "Example2.jpg"


def image_analyze(path: str) -> numpy.ndarray:
    """
    Analyzes the image by loading it from the specified path.

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The loaded image in BGR format.
    """
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    return image


def image_shape(image: numpy.ndarray) -> tuple:
    """
       Returns the dimensions (height and width) of the input image.

       Args:
           image (np.ndarray): The input image.

       Returns:
           tuple[int, int]: A tuple containing the height and width of the image.
       """
    return image.shape[:2]


def make_histogram(image: numpy.ndarray) -> None:
    """
        Generates and displays a histogram of the input image, showing pixel intensity
        distributions for the blue, green, and red color channels.

        Args:
            image (np.ndarray): The input image in BGR format.

        Returns:
            None
        """
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


def image_blend(og_image: str, blend_image: str, transparency: float = 0.5) -> numpy.ndarray:
    """
      Blends two images together and displays the result alongside the original image.

      Args:
          og_image (str): The file path to the first (original) image.
          blend_image (str): The file path to the second image to blend with the original.
          transparency (float): The modifier of blend image

      Description:
          - Loads both images in color mode using OpenCV.
          - Resizes the second image to match the dimensions of the first image.
          - Blends the two images using the specified alpha (opacity) and beta values.

      Example:
          image_blend("path/to/image1.jpg", "path/to/image2.jpg")
      """
    image1 = cv2.imread(og_image)
    image2 = cv2.imread(blend_image)

    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    alpha = transparency
    beta = 1 - alpha

    blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)
    return blended_image


def show_comprasion(image1: numpy.ndarray, blended_image: numpy.ndarray) -> None:
    """
    Displays the original image and blended image side by side for comparison.

    Args:
        image1 (np.ndarray): The original image.
        blended_image (np.ndarray): The blended image.

    Returns:
        None
    """
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


def save_image(image: numpy.ndarray, path_to_save: str = './lab3/blended_image.jpg') -> None:
    """
    Saves the image to the specified file path.

    Args:
        image (np.ndarray): The image to save.
        path_to_save (str, optional): The path to save the image. Defaults to './lab3/blended_image.jpg'.

    Returns:
        None
    """
    cv2.imwrite(path_to_save, image)
