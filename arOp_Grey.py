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
        #normalizedImg = np.empty((height, width), dtype=np.uint8)
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

        normalizedImg = self.normalizeImg(resultImg, fMin, fMax)
        self.show(img1, img2, normalizedImg)

#To jest chyba poprawne
    def sumImageWithImage2(self, img1, img2):
        QMax = 0
        DMax = 0
        X=0
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
                L = int(img1[i, j]) + int(img2[i, j])

                if QMax < L:
                    QMax = L

        if QMax > 255:
            DMax = QMax - 255
            X = DMax/255

        for i in range(height):
            for j in range(width):
                L=(img1[i, j] - img1[i, j]*X) + (img2[i, j] - img2[i, j]*X)
                resultImg[i, j] = np.ceil(L)

                if fMin > L:
                    fMin = L
                if fMax < L:
                    fMax = L

        for i in range(height):
            for j in range(width):
                normalizedImg[i, j] = 255 * ((resultImg[i, j] - fMin)/(fMax - fMin))


        #self.show(img1, img2, normalizedImg)

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
        QMax = 0
        DMax = 0
        X=0
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

