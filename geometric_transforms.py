import cv2
import numpy

def rotate_image(img, angle, center=None, scale=1.0):
    """Поворачивает изображение."""
    h, w = img.shape[:2]
    angle = (angle + 180) % 360 - 180
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(img, M, (w, h))
    return rotated_img

if __name__ == "__main__":
    # Пример использования функции
    image = cv2.imread('input_image.jpg')
    rotated_image = rotate_image(image, 45)
    cv2.imshow('Rotated Image', rotated_image)  # Поворот на 45 градусов
    cv2.waitKey(0)
    cv2.destroyAllWindows()