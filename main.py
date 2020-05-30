from normalize import Normalize as norm
from arOp_Grey import ArOpGrey as ar
from geometricsOperations import GeometricsOperations as geo

e = geo()
n = norm()
ar = ar()
#n.rasterGreyNormalize("temp_img/raster_grey.png", "temp_img/raster_grey_2.png")
#e.sumImageWithNumber("temp_img/zdj1.jpg", -40)
#e.sumImageWithImage("temp_img/2/1.jpg", "temp_img/2/2.jpg")
#e.moveImage("temp_img/2/1.jpg", 60, 60)
#e.turnImage("temp_img/2/1.jpg", 10)
#ar.multiplyImgWithNumber("temp_img/zdj1.jpg", 100)
ar.mixImagesWithRate("temp_img/2/1.jpg", "temp_img/2/2.jpg", 0.4)
 