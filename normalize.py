import numpy as np
import cv2

class Normalize:
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

        self.show(resultImg1 ,resultImg2)

    def show(self, img1, img2):
        cv2.imshow("Obraz nr 1", img1)
        cv2.imshow("Obraz nr 2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()