import numpy as np
import cv2

class GeometricsOperations:
    def moveImage(self, img, x, y):
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        height = img.shape[0]
        width = img.shape[1]
        #x = -1*x
        y = -1*y
        newImg = np.full((height, width), 0, dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if (j + x) >= 0 and (i + y) >= 0 and (i + y) < height and (j + x) < width :
                    newImg[i+y, j+x] = img[i, j]

        self.show(img, newImg)

    def show(self, img1, img2):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
