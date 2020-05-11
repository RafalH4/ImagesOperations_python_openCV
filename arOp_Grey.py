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
                pktValue = int(img[i, j] + number)
                qMax = qMax if qMax < pktValue else pktValue

        if qMax>255:
            dMax = qMax - 255
            x = dMax/255

        for i in range(height):
            for j in range(width):
                resultImg[i, j] = np.ceil((img[i, j] - img[i, j]*x) + (number - (number*x)))
                fMin = resultImg[i, j] if fMin > resultImg[i, j] else fMin
                fMax = resultImg[i, j] if fMax < resultImg[i, j] else fMax

        for i in range(height):
            for j in range(width):
                normalizedImg[i, j] = (255*(resultImg[i, j]-fMin))/(fMax-fMin)

        self.show(img, resultImg, normalizedImg)

    def normalizeImage(self, img, fMax, fMin):
        width = img.shape[1]
        height = img.shape[0]
        imageToReturn = np.empty((height, width), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                imageToReturn[i, j] = 255*((img[i, j] - fMin)/(fMax-fMin))
        return imageToReturn

    def show(self, img1, img2, img3):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.imshow("3", img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

