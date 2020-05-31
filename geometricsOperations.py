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

    def homoScalingImg(self, img, scale):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                if scale*i < height and scale*j < width:
                    resultImg[int(scale*i)][int(scale*j)] = img[i, j]

        normalizedImg = self.interpolation(resultImg)

        self.show(img, normalizedImg)

    def inHomoScalingImg(self, img, scaleX, scaleY):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                if scaleY*i < height and scaleX*j < width:
                    resultImg[int(scaleY*i)][int(scaleX*j)] = img[i, j]

        normalizedImg = self.interpolation(resultImg)
        self.show(img, normalizedImg)

    def turn(self, img, radius):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)
        correctRadius = np.radians(radius)
        for i in range(height):
            for j in range(width):
                newX = (j - width/2) * np.cos(correctRadius) - (i - height/2) * np.sin(correctRadius) + (width/2)
                newY = (j - width/2) * np.sin(correctRadius) + (i - height/2) * np.cos(correctRadius) + (height/2)
                if newY < height and newY >= 0 and newX >= 0 and newX < width:
                    resultImg[int(newY), int(newX)] = img[i, j]

        interpolatedImg = self.interpolation(resultImg)
        self.show(img, resultImg)

    def cutFragImg(self, img, startX, endX, startY, endY):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if i < height - startY and i > height - endY and j > startX and j < endX:
                    resultImg[i, j] = 0
                else:
                    resultImg[i, j] = img[i, j]
        self.show(img, resultImg)

    def copyFragImg(self, img, startX, endX, startY, endY):
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]
        resultImg = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(startY, endY):
            for j in range(startX, endX):
                newI = i - startY
                newJ = j - startX
                resultImg[i, j] = img[newI, newJ]
        self.show(img, resultImg)

    def interpolation(self, img):
        width = img.shape[1]
        height = img.shape[0]
        tempImg = np.empty((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                n = 1
                tempImg[i, j] = img[i, j]
                if (img[i, j][0] < 1) & (img[i, j][1] < 1) & (img[i, j][2] < 1):
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (height - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width - 2)) | ((j + jOff) < 0) else (j + jOff)
                            if (img[iSafe, jSafe][0] > 0) | (img[iSafe, jSafe][1] > 0) | (
                                    img[iSafe, jSafe][2] > 0):
                                r += img[iSafe, jSafe][0]
                                g += img[iSafe, jSafe][1]
                                b += img[iSafe, jSafe][2]
                                n += 1
                    tempImg[i, j] = (r / n, g / n, b / n)
                    img[i, j] = tempImg[i, j]
        return img

    def show(self, img1, img2):
        cv2.imshow("1", img1)
        cv2.imshow("2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
