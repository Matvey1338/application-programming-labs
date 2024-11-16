import cv2


def image_analyze(path: str):
    image = cv2.imread(path,  cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
    print("Image shape:", width, "x", height)
