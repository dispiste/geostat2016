# encoding: utf-8

import rlib
reload(rlib)
from rlib.process import *
import os

"""
Sample plugin for declaring R plugins using RExternal plugin

Note that it is CRUCIAL that each process (each class extending from 
RProcess) has a unique name (even across different plugins!!!!). Otherwise
Sextante history gets confused and some errors arise.

Author: Cesar Martinez Izquierdo
"""

class TestProcess1(RProcess):
    def __init__(self):
        """
        We'll define the script to execute and the working directory on this method.

        Note that it's not mandatory to have a __init__ method, as it is
        also possible to define rscript and wd in the defineChracteristics
        method by using:
        self.rscript = "/path/to/my/script.r"
        self.wd = "/my/working/directory"
        """
        baseDir = os.path.dirname(os.path.abspath(__file__))
        rscript = os.path.join(baseDir, "rscript.r")
        RProcess.__init__(self, rscript, baseDir)

    def defineCharacteristics(self):
        # Process name
        self.setName("Test R process1")
        # Process group
        self.setGroup("Geostat course")
        params = self.getParameters() 
        # Define an input vector parameter, named IN_VECTOR, of type polygon and make it mandatory
        params.addInputVectorLayer("IN_VECTOR","Input vector layer", SHAPE_TYPE_POLYGON, True)

        # Define an input raster parameter named IN_RASTER and make it mandatory
        params.addInputRasterLayer("IN_RASTER","Input raster layer", True)

        # Define an output raster layer, name "OUT_RASTER"
        self.addOutputRasterLayer("OUT_RASTER", "Output raster")
        
    def callRProcess(self, *args):
        """
        Calls the main method of the defined R script
        """
        self.R.call("load_libraries")
        self.R.call("doalmostnothing", *args)

        """
        Alternative way: directly access params by name

        # this gets a gvSIG/Sextante layer object:
        in_vector_layer = self.getParamValue("IN_VECTOR")
        in_raster_layer = self.getParamValue("IN_RASTER")
        # we use rlib to convert the layer to an OGR DSN and an OGR layer name
        in_vector_dsn = rlib.getLayerPath(in_vector_layer)
        in_layer_name = rlib.getLayerName(in_vector_layer)
        in_raster_dsn = rlib.getLayerPath(in_raster_layer)

        # for output layers, getOutputValue directly returns a path, as the layer does not exist yet
        outRaster = self.getOutputValue("OUT_RASTER")
        self.R.call("doalmostnothing", in_vector_dsn, in_layer_name, in_raster_dsn, outRaster)
        """

        """
        Alternative way: individually access each parameter

        in_vector_dsn = args[0]
        in_layer_name = args[1]
        inRaster = args[2]
        outRaster = args[3]
        self.R.call("doalmostnothing", in_vector_dsn, in_layer_name, inRaster, outRaster)
        """

def main(*args):
        process = TestProcess1()
        process.selfregister("Scripting")
        process.updateToolbox()
