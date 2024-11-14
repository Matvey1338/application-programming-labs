import cv2


def image_analyze(path: str):
    image = cv2.imread(path)
    height, width = image.shape
    print("Image shape:", width, "x", height)
