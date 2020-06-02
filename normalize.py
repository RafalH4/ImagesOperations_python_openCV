import numpy as np
import cv2

class Normalize:
    #Ujednolicanie obrazów szarych geometrycznie
    def geometricGreyNormalize(self, photo1, photo2):
        img1 = cv2.imread(photo1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(photo2, cv2.IMREAD_GRAYSCALE)

        widthImg1 = img1.shape[1]
        heightImg1 = img1.shape[0]

        widthImg2 = img2.shape[1]
        heightImg2 = img2.shape[0]

        width = widthImg1 if widthImg1 >= widthImg2 else widthImg2
        height = heightImg1 if heightImg1 >= heightImg2 else heightImg2

        resultImg1 = np.empty((height, width), dtype=np.uint8)
        resultImg2 = np.empty((height, width), dtype=np.uint8)

        print("width" + str(width))
        print("height" + str(height))
        startWidth = int(round((width - widthImg1) / 2))
        startHeight = int(round((height - heightImg1) / 2))


        for i in range(height):
            for j in range(width):
                resultImg1[i, j] = 1

        for i in range(heightImg1):
            for j in range(widthImg1):
                resultImg1[i + startHeight, j + startWidth] = img1[i, j]

        startWidth = int(round((width - widthImg2) / 2))
        startHeight = int(round((height - heightImg2) / 2))

        for i in range(height):
            for j in range(width):
                resultImg2[i, j] = 1

        for i in range(heightImg2):
            for j in range(widthImg2):
                resultImg2[i + startHeight, j + startWidth] = img2[i, j]

        self.show(resultImg1, resultImg2)

    #Ujednolicanie obrazów szarych rozdzielczościowe
    def rasterGreyNormalize(self, photo1, photo2):
        img1 = cv2.imread(photo1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(photo2, cv2.IMREAD_GRAYSCALE)

        widthImg1 = img1.shape[1]
        heightImg1 = img1.shape[0]

        widthImg2 = img2.shape[1]
        heightImg2 = img2.shape[0]

        widthScale = widthImg1/widthImg2
        heightScale = heightImg1/heightImg2

        resultImg1 = np.empty((heightImg1, widthImg1), dtype=np.uint8)
        resultImg2 = np.empty((heightImg1, widthImg1), dtype=np.uint8)
        tmp = np.empty((heightImg1, widthImg1), dtype=np.uint8)

        for i in range(heightImg1):
            for j in range(widthImg1):
                resultImg1[i, j] = img1[i, j]

        counter = 0
        for i in range(heightImg2):
            for j in range(widthImg2):
                if counter == 0:
                    resultImg2[int(heightScale*i), int(round(widthScale*j))+1] = img2[i, j]
                    counter += 1
                if counter == 1:
                    resultImg2[int(round(heightScale*i))+1, int(widthScale*j)] = img2[i, j]
                    counter = 0

        for i in range(heightImg1):
            for j in range(widthImg1):
                value = 0
                n = 0
                tmp[i, j] = resultImg2[i, j]
                if resultImg2[i, j] < 1:
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            if (i + iOff) > (heightImg1 - 2) or (i + iOff) < 0:
                                iSafe = i
                            else:
                                iSafe = i + iOff

                            if (j + jOff) > (widthImg1 - 2) or (j + jOff) < 0:
                                jSafe = j
                            else:
                                jSafe = j + jOff

                            if resultImg2[iSafe, jSafe] > 0:
                                value += resultImg2[iSafe, jSafe]
                                n += 1
                    tmp[i, j] = value / n
                    resultImg2[i, j] = tmp[i, j]
        self.show(resultImg1, resultImg2)
        

    #Ujednolicanie obrazów RGB geometrycznie
    def geometricColorNormalize(self, photo1, photo2):
        img1 = cv2.imread(photo1, cv2.IMREAD_COLOR)
        img2 = cv2.imread(photo2, cv2.IMREAD_COLOR)

        widthImg1 = img1.shape[1]
        heightImg1 = img1.shape[0]

        widthImg2 = img2.shape[1]
        heightImg2 = img2.shape[0]

        width = widthImg1 if widthImg1 >= widthImg2 else widthImg2
        height = heightImg1 if heightImg1 >= heightImg2 else heightImg2

        resultImg1 = np.empty((height, width, 3), dtype=np.uint8)
        resultImg2 = np.empty((height, width, 3), dtype=np.uint8)

        print("width" + str(width))
        print("height" + str(height))
        startWidth = int(round((width - widthImg1) / 2))
        startHeight = int(round((height - heightImg1) / 2))


        for i in range(height):
            for j in range(width):
                resultImg1[i, j] = 1

        for i in range(heightImg1):
            for j in range(widthImg1):
                resultImg1[i + startHeight, j + startWidth] = img1[i, j]

        startWidth = int(round((width - widthImg2) / 2))
        startHeight = int(round((height - heightImg2) / 2))

        for i in range(height):
            for j in range(width):
                resultImg2[i, j] = 1

        for i in range(heightImg2):
            for j in range(widthImg2):
                resultImg2[i + startHeight, j + startWidth] = img2[i, j]

        self.show(resultImg1, resultImg2)

    #Ujednolicanie obrazów RGB rozdzielczościowe

    def show(self, img1, img2):
        cv2.imshow("Obraz nr 1", img1)
        cv2.imshow("Obraz nr 2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()