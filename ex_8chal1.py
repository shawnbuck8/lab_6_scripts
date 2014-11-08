import arcpy
import fileinput
import string
import os
import turtle

from arcpy import env
env.workspace = "J:/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
#env.SpatialReference("WGS1984")
sides = int(raw_input("How many sides for this polygon? "))
length = int(raw_input("What length should the sides be? "))
window = turtle.Screen()
shawn = turtle.Turtle()
degrees = (180 - (180*(sides-2)/sides))
ptlist = []
for side in range(sides):
    shawn.forward(length)
    shawn.left(degrees)
    ptlist.append(shawn.pos())
 

outpath = "J:/EsriPress/Python/Data/Exercise08"
newfc = "Results/turtle_poly.shp"
sr = arcpy.SpatialReference("J:/EsriPress/Python/Data/Exercise08/Results/4326.prj")
arcpy.management.CreateFeatureclass(outpath, newfc, "Polygon", "", "", "", sr)

cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])

array = arcpy.Array()
for x, y in ptlist:
    pt = arcpy.Point(x,y)
    array.append(pt)
poly = arcpy.Polygon(array)
cursor.insertRow([poly])
del cursor

