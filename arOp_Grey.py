#Operacje arytmetyczne na obrazach szarych
import numpy as np
import cv2

class ArOpGrey:
    def sumImageWithNumber(self, img, number):
        qMax = 0
        dMax = 0
        fMax = 0
        x = 0
        fMin = 255
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        width = img.shape[1]
        height = img.shape[0]

        normalizedImg = np.empty((height, width), dtype=np.uint8)
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                sum = np.ceil(img[i, j] + number)
                resultImg[i, j] = sum
                if fMax < sum:
                    if sum > 255:
                        fMax = 255
                    else:
                        fMax = sum

                if fMin > sum:
                    if sum < 0:
                        fMin = 0
                    else:
                        fMin = sum

        for i in range(height):
            for j in range(width):
                normalizedImg[i, j] = (255*(resultImg[i, j]-fMin))/(fMax-fMin)

        self.show(img, resultImg, normalizedImg)

    def show(self, img1, img2, img3):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.imshow("3", img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

