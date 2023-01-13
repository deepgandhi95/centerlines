import os
import sys
import vtk
import vmtk

from vmtk import pypes
from vmtk import vmtkscripts

file = sys.argv[1]
filein = file +".stl"
fileout = file +"out.stl"

mySClipArg = 'vmtksurfaceclipper -ifile {} -interactive 1 -ofile {}'.format(filein, fileout)
mySClipPype = pypes.PypeRun(mySClipArg)

myScArg = 'vmtksurfacecapper -ifile {} -interactive 0 -ofile {}_closed.stl'.format(filein, file)
myScPype = pypes.PypeRun(myScArg)

mySsdArg = 'vmtksurfacesubdivision -method loop -ifile {} -ofile {}'.format(fileout, fileout)
mySsdPype = pypes.PypeRun(mySsdArg)

myCtlArg = 'vmtkcenterlines -seedselector pickpoint -resampling 1 -resamplingstep 1 -ifile {} -ofile {}_centerline.vtp'.format(fileout, file)
myCtlPype = pypes.PypeRun(myCtlArg)

myCtlGeoArg = 'vmtkcenterlinegeometry -ifile {}_centerline.vtp -smoothing 1 -iterations 30 -factor 0.2 -outputsmoothed 1 -ofile {}_centerline_geoinfo.vtp --pipe vmtkcenterlineattributes -ofile {}_geodata.dat'.format(file, file, file)
myCtlGeoPype = pypes.PypeRun(myCtlGeoArg)

os.popen('"C:/Program Files/ParaView 5.8.0-Windows-Python3.7-msvc2015-64bit/bin/pvpython" "C:/Users/GAN5EH/OneDrive - cchmc/Documents/MATLAB/CPIR codes/TrachealAnalysisCode/Convert_GeoinfovtpToVtk.py" {}'.format(file))
print("----------------------------------------------------------------------------------------------------------------------");
