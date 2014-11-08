import arcpy

from arcpy import env
from arcpy.sa import *
env.workspace = "F:/EsriPress/Python/Data/Exercise09"
env.overwriteOutput = True
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    elev = arcpy.Raster("elevation")
    land = arcpy.Raster("landcover.tif")
    slope = Slope(elev)
    aspect = Aspect(elev)
    sloperange = ((slope > 5) & (slope < 20))
    aspectrange = ((aspect > 150) & (aspect < 270))
    forest = ((land == 41) | (land == 42) | (land == 43))
    outraster = (sloperange & aspectrange & forest)
    outraster.save("F:/EsriPress/Python/Data/Exercise09/Results/chal_1_ans")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
    
