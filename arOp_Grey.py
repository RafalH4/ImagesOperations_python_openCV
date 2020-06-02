#Operacje arytmetyczne na obrazach szarych
import numpy as np
import cv2

class ArOpGrey:
    def sumImageWithNumber(self, img, number):
        fMax = 0
        fMin = 255
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        width = img.shape[1]
        height = img.shape[0]

        normalizedImg = np.empty((height, width), dtype=np.uint8)
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                resultImg[i, j] = np.ceil(img[i, j] + number)
                if fMax < resultImg[i, j]:
                    if resultImg[i, j] > 255:
                        fMax = 255
                    else:
                        fMax = resultImg[i, j]

                if fMin > resultImg[i, j]:
                    if resultImg[i, j] < 0:
                        fMin = 0
                    else:
                        fMin = resultImg[i, j]

        for i in range(height):
            for j in range(width):
                normalizedImg[i, j] = np.ceil((255*(resultImg[i, j]-fMin))/(fMax-fMin))

        self.show(img, resultImg, normalizedImg)

    def sumImageWithImage(self, img1, img2):
        fMax = 0
        fMin = 255
        img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

        if(img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                resultImg[i, j] = int(img1[i, j]) + int(img2[i, j])
                if fMax < resultImg[i, j]:
                    if resultImg[i, j] > 255:
                        fMax = 255
                    else:
                        fMax = resultImg[i, j]

                if fMin > resultImg[i, j]:
                    if resultImg[i, j] < 0:
                        fMin = 0
                    else:
                        fMin = resultImg[i, j]

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def multiplyImgWithNumber(self, img, number):
        fMax = 0
        fMin = 255
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width), dtype=np.uint8)
        normalizedImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if int(img[i, j]) == 255:
                    tempValue = 255
                elif int(img[i, j]) == 255:
                    tempValue = int(img[i, j])
                else:
                    tempValue = (int(img[i, j])*number)/255
                resultImg[i, j] = np.ceil(tempValue)

                if fMin > tempValue:
                    fMin = tempValue
                if fMax < tempValue:
                    fMax = tempValue

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def multiplyImgWithImg(self, img1, img2):
        fMax = 0
        fMin = 255
        img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

        if(img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]
        normalizedImg = np.empty((height, width), dtype=np.uint8)
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if int(img1[i, j]) == 255:
                    tempValue = int(img2[i, j])
                elif int(img1[i, j]) == 0:
                    tempValue = 0
                else:
                    tempValue = (int(img1[i, j]) * int(img2[i, j])) / 255
                resultImg[i, j] = np.ceil(tempValue)

                if fMin > tempValue:
                    fMin = tempValue
                if fMax < tempValue:
                    fMax = tempValue

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def mixImagesWithRate(self, img1, img2, rate):
        fMax = 0
        fMin = 255
        img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

        if(img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]

        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                resultImg[i, j] = np.ceil(float(img1[i, j])*rate + float(img2[i, j])*(1-rate))

                if fMin > resultImg[i, j]:
                    fMin = resultImg[i, j]
                if fMax < resultImg[i, j]:
                    fMax = resultImg[i, j]

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def escalateImg(self, img, number):
        fMax = 0
        fMin = 255
        fImgMax = 0
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if fImgMax < int(img[i, j]):
                    fImgMax = int(img[i, j])

        for i in range(height):
            for j in range(width):
                if int(img[i, j]) == 255:
                    resultImg[i, j] = 255
                elif int(img[i, j]) == 0:
                    resultImg[i, j] = 0
                else:
                    resultImg[i, j] = pow(int(img[i, j])/fImgMax, number)*255

                if fMin > resultImg[i, j]:
                    fMin = resultImg[i, j]
                if fMax < resultImg[i, j]:
                    fMax = resultImg[i, j]
                resultImg[i, j] = np.ceil(resultImg[i, j])

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def divideImgByNumber(self, img, number):
        fMax = 0
        fMin = 255
        QMax = 0
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if QMax < int(img[i, j]+number):
                    QMax = int(img[i, j]+number)

        for i in range(height):
            for j in range(width):
                tempValue = (int(img[i, j]+number)*255)/QMax
                resultImg[i, j] = np.ceil(tempValue)
                if fMin > tempValue:
                    fMin = tempValue
                if fMax < tempValue:
                    fMax = tempValue

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def divideImgByImg(self, img1, img2):
        fMax = 0
        fMin = 255
        QMax = 0
        img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

        if (img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if QMax < int(img1[i, j] + img2[i, j]):
                    QMax = int(img1[i, j] + img2[i, j])

        for i in range(height):
            for j in range(width):
                tempValue = (int(img1[i, j] + img2[i, j])*255)/QMax
                resultImg[i, j] = np.ceil(tempValue)
                if fMin > tempValue:
                    fMin = tempValue
                if fMax < tempValue:
                    fMax = tempValue
        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def extractImg(self, img, number):
        newNumber = 1/number
        self.escalateImg(img, number)

    def logImg(self, img):
        fMax = 0
        fMin = 255
        fImgMax = 0
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if fImgMax < int(img[i, j]):
                    fImgMax = int(img[i, j])

        for i in range(height):
            for j in range(width):
                if int(img[i, j]) == 0:
                    resultImg[i, j] = 0
                else:
                    resultImg[i, j] = (np.log(1 + int(img[i, j])))/np.log(1 + fImgMax)*255

                if fMin > resultImg[i, j]:
                    fMin = resultImg[i, j]
                if fMax < resultImg[i, j]:
                    fMax = resultImg[i, j]
                resultImg[i, j] = np.ceil(resultImg[i, j])

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def normalizeImg(self, img, fMax, fMin):
        width = img.shape[1]
        height = img.shape[0]
        normalizedImg = np.empty((height, width), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                normalizedImg[i, j] = 255 * ((img[i, j] - fMin)/(fMax - fMin))
        return normalizedImg

    def show(self, img1, img2, img3):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.imshow("3", img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

