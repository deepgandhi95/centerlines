#### import the simple module from the paraview

from paraview.simple import *
import os
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
file = sys.argv[1]
#cwd = os.getcwd()
# create a new 'XML PolyData Reader'
out_000000_centerline_geoinfovtp = XMLPolyDataReader(FileName=['{}_centerline_geoinfo.vtp'.format(file)])
out_000000_centerline_geoinfovtp.CellArrayStatus = ['Length', 'Tortuosity']
out_000000_centerline_geoinfovtp.PointArrayStatus = ['MaximumInscribedSphereRadius', 'Curvature', 'Torsion', 'FrenetTangent', 'FrenetNormal', 'FrenetBinormal']
cwd = os.getcwd
# save data
SaveData('{}_centerline_geoinfo.vtk'.format(file), proxy=out_000000_centerline_geoinfovtp, FileType='Ascii')
