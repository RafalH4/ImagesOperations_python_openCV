from normalize import Normalize as norm
from arOp_Grey import ArOpGrey as ar
from geometricsOperations import GeometricsOperations as geo
from arOp_Color import ArOpColor as arC

e = geo()
n = norm()
ar = ar()
arC = arC()
#n.rasterGreyNormalize("temp_img/raster_grey.png", "temp_img/raster_grey_2.png")
#e.sumImageWithNumber("temp_img/zdj1.jpg", -40)
#e.sumImageWithImage("temp_img/2/1.jpg", "temp_img/2/2.jpg")
#e.moveImage("temp_img/2/1.jpg", 60, 60)
#e.turnImage("temp_img/2/1.jpg", 10)
#ar.multiplyImgWithNumber("temp_img/zdj1.jpg", 100)
#ar.mixImagesWithRate("temp_img/2/1.jpg", "temp_img/2/2.jpg", 0.4)
#ar.escalateImg("temp_img/2/1.jpg", 2)
#ar.divideImgByNumber("temp_img/2/2.jpg", 50)
#ar.divideImgByImg("temp_img/2/1.jpg", "temp_img/2/2.jpg")
#ar.extractImg("temp_img/2/1.jpg", 3)
#ar.logImg("temp_img/2/1.jpg")

#arC.sumImgWithNumber("temp_img/cukierki.tiff", 20)
#arC.sumImgWithImg("temp_img/2/1.jpg", "temp_img/2/2.jpg")
#arC.multiplyImgWithNumber("temp_img/2/1.jpg", 150)
#arC.multiplyImgWithImg("temp_img/2/1.jpg", "temp_img/2/2.jpg")
#arC.mixImagesWithRate("temp_img/2/1.jpg", "temp_img/2/2.jpg", 0.4)
#arC.escalateImg("temp_img/2/1.jpg", 2)
#arC.divideImgByNumber("temp_img/2/1.jpg", 300)
#arC.divideImgByImg("temp_img/2/1.jpg", "temp_img/2/2.jpg")
#arC.extractImg("temp_img/2/1.jpg", 3)
#arC.logImg("temp_img/2/1.jpg")

#e.homoScalingImg("temp_img/2/1.jpg", 2)
#e.inHomoScalingImg("temp_img/2/1.jpg", 2, 1)
#e.turn("temp_img/2/1.jpg", -30)
#e.cutFragImg("temp_img/2/1.jpg", 10,190, 60, 220)
e.copyFragImg("temp_img/2/1.jpg", 10,190, 60, 220)