#Operacje arytmetyczne na obrazach kolorowych
import numpy as np
import cv2

class ArOpColor:
    def sumImgWithNumber(self, img, number):
        img = cv2.imread(img)
        fMax = 0
        fMin = 255
        qMax = 0
        x = 0
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                redValue = int(img[i, j, 0] + number)
                greenValue = int(img[i, j, 1] + number)
                blueValue = int(img[i, j, 2] + number)

                maxValue = max([redValue, greenValue, blueValue])
                if qMax < maxValue:
                    qMax = maxValue

        if qMax > 255:
            x = (qMax - 255)/255

        for i in range(height):
            for j in range(width):
                redValue = (img[i, j, 0] - (img[i, j, 0]*x))+(number - (number*x))
                greenValue = (img[i, j, 1] - (img[i, j, 1] * x)) + (number - (number * x))
                blueValue = (img[i, j, 2] - (img[i, j, 2] * x)) + (number - (number * x))

                resultImg[i, j, 0] = np.ceil(redValue)
                resultImg[i, j, 1] = np.ceil(greenValue)
                resultImg[i, j, 2] = np.ceil(blueValue)

                minValue = min([redValue, greenValue, blueValue])
                maxValue = max([redValue, greenValue, blueValue])

                if fMin > minValue:
                    fMin = minValue
                if fMax < maxValue:
                    fMax = maxValue
        print(fMax)
        print(fMin)
        normalizedImg = self.normalizeImg(img, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def sumImgWithImg(self, img1, img2):
        img1 = cv2.imread(img1, cv2.IMREAD_COLOR)
        img2 = cv2.imread(img2, cv2.IMREAD_COLOR)
        fMax = 0
        fMin = 255
        qMax = 0
        x = 0
        if(img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                redValue = int(img1[i, j, 0]) + int(img2[i, j, 0])
                greenValue = int(img1[i, j, 1]) + int(img2[i, j, 1])
                blueValue = int(img1[i, j, 2]) + int(img2[i, j, 2])

                maxValue = max([redValue, greenValue, blueValue])
                if qMax < maxValue:
                    qMax = maxValue

        if qMax > 255:
            x = (qMax - 255)/255
        for i in range(height):
            for j in range(width):
                redValue = (img1[i, j, 0] - (img1[i, j, 0]*x)) + (img2[i, j, 0] - (img2[i, j, 0]*x))
                greenValue = (img1[i, j, 1] - (img1[i, j, 1] * x)) + (img2[i, j, 1] - (img2[i, j, 1] * x))
                blueValue = (img1[i, j, 2] - (img1[i, j, 2] * x)) + (img2[i, j, 2] - (img2[i, j, 2] * x))

                resultImg[i, j, 0] = np.ceil(redValue)
                resultImg[i, j, 1] = np.ceil(greenValue)
                resultImg[i, j, 2] = np.ceil(blueValue)

                maxValue = max([redValue, greenValue, blueValue])
                minValue = min([redValue, greenValue, blueValue])

                if fMin > minValue:
                    fMin = minValue
                if fMax < maxValue:
                    fMax = maxValue
        #normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, resultImg)

    def multiplyImgWithNumber(self, img, number):
        fMax = 0
        fMin = 255
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if int(img[i, j, k]) == 255:
                        tempValue = 255
                    elif int(img[i, j, k]) == 255:
                        tempValue = int(img[i, j, k])
                    else:
                        tempValue = (int(img[i, j, k])*number)/255
                    resultImg[i, j, k] = np.ceil(tempValue)

                    if fMin > tempValue:
                        fMin = tempValue
                    if fMax < tempValue:
                        fMax = tempValue

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def multiplyImgWithImg(self, img1, img2):
        fMax = 0
        fMin = 255
        img1 = cv2.imread(img1, cv2.IMREAD_COLOR)
        img2 = cv2.imread(img2, cv2.IMREAD_COLOR)

        if(img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if int(img1[i, j, k]) == 255:
                        tempValue = int(img2[i, j, k])
                    elif int(img1[i, j, k]) == 0:
                        tempValue = 0
                    else:
                        tempValue = (int(img1[i, j, k]) * int(img2[i, j, k])) / 255
                    resultImg[i, j, k] = np.ceil(tempValue)

                    if fMin > tempValue:
                        fMin = tempValue
                    if fMax < tempValue:
                        fMax = tempValue

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def mixImagesWithRate(self, img1, img2, rate):
        fMax = 0
        fMin = 255
        img1 = cv2.imread(img1, cv2.IMREAD_COLOR)
        img2 = cv2.imread(img2, cv2.IMREAD_COLOR)

        if(img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]

        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    resultImg[i, j, k] = np.ceil(float(img1[i, j, k])*rate + float(img2[i, j, k])*(1-rate))

                    if fMin > resultImg[i, j, k]:
                        fMin = resultImg[i, j, k]
                    if fMax < resultImg[i, j, k]:
                        fMax = resultImg[i, j, k]

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def escalateImg(self, img, number):
        fMax = 0
        fMin = 255
        fImgMax = 0
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if fImgMax < int(img[i, j, k]):
                        fImgMax = int(img[i, j, k])

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if int(img[i, j, k]) == 255:
                        resultImg[i, j, k] = 255
                    elif int(img[i, j, k]) == 0:
                        resultImg[i, j, k] = 0
                    else:
                        resultImg[i, j, k] = pow(int(img[i, j, k])/fImgMax, number)*255

                    if fMin > resultImg[i, j, k]:
                        fMin = resultImg[i, j, k]
                    if fMax < resultImg[i, j, k]:
                        fMax = resultImg[i, j, k]
                    resultImg[i, j, k] = np.ceil(resultImg[i, j, k])

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def divideImgByNumber(self, img, number):
        fMax = 0
        fMin = 255
        QMax = 0
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if QMax < int(img[i, j, k])+number:
                        QMax = int(img[i, j, k])+number

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    tempValue = ((int(img[i, j, k])+number)*255)/QMax
                    resultImg[i, j, k] = np.ceil(tempValue)
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
        img1 = cv2.imread(img1, cv2.IMREAD_COLOR)
        img2 = cv2.imread(img2, cv2.IMREAD_COLOR)

        if (img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]):
            print("Obraz musi być ujednolicony")
        width = img1.shape[1]
        height = img1.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if QMax < int(img1[i, j, k]) + int(img2[i, j, k]):
                        QMax = int(img1[i, j, k]) + int(img2[i, j, k])

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    tempValue = (int(img1[i, j, k]) + int(img2[i, j, k])*255)/QMax
                    resultImg[i, j, k] = np.ceil(tempValue)
                    if fMin > tempValue:
                        fMin = tempValue
                    if fMax < tempValue:
                        fMax = tempValue
        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img1, img2, normalizedImg)

    def extractImg(self, img, number):
        newNumber = 1 / number
        self.escalateImg(img, number)

    def normalizeImg(self, img, fMax, fMin):
        width = img.shape[1]
        height = img.shape[0]
        normalizedImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                normalizedImg[i, j, 0] = np.ceil(255 * ((img[i, j, 0] - fMin) / (fMax - fMin)))
                normalizedImg[i, j, 1] = np.ceil(255 * ((img[i, j, 1] - fMin) / (fMax - fMin)))
                normalizedImg[i, j, 2] = np.ceil(255 * ((img[i, j, 2] - fMin) / (fMax - fMin)))
        return normalizedImg

    def logImg(self, img):
        fMax = 0
        fMin = 255
        fImgMax = 0
        img = cv2.imread(img, cv2.IMREAD_COLOR)

        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if fImgMax < int(img[i, j, k]):
                        fImgMax = int(img[i, j, k])

        for i in range(height):
            for j in range(width):
                for k in range(0, 2):
                    if int(img[i, j, k]) == 0:
                        resultImg[i, j, k] = 0
                    else:
                        resultImg[i, j, k] = (np.log(1 + int(img[i, j, k])))/np.log(1 + fImgMax)*255

                    if fMin > resultImg[i, j, k]:
                        fMin = resultImg[i, j, k]
                    if fMax < resultImg[i, j, k]:
                        fMax = resultImg[i, j, k]
                    resultImg[i, j, k] = np.ceil(resultImg[i, j, k])

        normalizedImg = self.normalizeImg(resultImg, fMax, fMin)
        self.show(img, resultImg, normalizedImg)

    def show(self, img1, img2, img3):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.imshow("3", img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()