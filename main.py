from normalize import Normalize as norm
from arOp_Grey import ArOpGrey as ar
from geometricsOperations import GeometricsOperations as geo

e = geo()
#e.sumImageWithNumber("temp_img/zdj1.jpg", -40)
#e.sumImageWithImage("temp_img/2/1.jpg", "temp_img/2/2.jpg")
e.moveImage("temp_img/2/1.jpg", 60, 60)
