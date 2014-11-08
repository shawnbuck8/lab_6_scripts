import arcpy

from arcpy import env
file_path = "F:/EsriPress/Python/Data/Exercise09"
env.workspace = file_path
env.overwriteOutput = True
rastlist = arcpy.ListRasters()
arcpy.management.CreatePersonalGDB(file_path + "/Results", "rasters.gdb")
for raster in rastlist:
    desc = arcpy.Describe(raster)
    name = desc.baseName
    outraster = file_path + "/Results/rasters.gdb/" + name
    arcpy.CopyRaster_management(raster, outraster)
print "Done!"
    
