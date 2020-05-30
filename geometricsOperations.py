import numpy as np
import cv2

class GeometricsOperations:
    def moveImage(self, img, x, y):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        height = img.shape[0]
        width = img.shape[1]
        #x = -1*x
        y = -1*y
        newImg = np.full((height, width, 3), 0, dtype=np.uint8)


        for i in range(height):
            for j in range(width):
                if (j + x) >= 0 and (i + y) >= 0 and (i + y) < height and (j + x) < width :
                    newImg[i+y, j+x] = img[i, j]

        self.show(img, newImg)

    def turnImage(self, img, angle):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        height = img.shape[0]
        width = img.shape[1]
        newImg = np.full((height, width, 3), 0, dtype=np.uint8)

        radians = np.deg2rad(angle)
        for i in range(height):
            for j in range(width):
                newX = (j - width/2) * np.cos(radians) - (i - height/2) * np.sin(radians) + width/2
                newY = (j - width/2) * np.sin(radians) + (i - height / 2) * np.cos(radians) + height / 2
                if newX < width and newX >= 0 and newY < height and newY >= 0:
                    newImg[int(newY), int(newX)] = img[i, j]

        self.show(img, newImg)

    def show(self, img1, img2):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
