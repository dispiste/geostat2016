# encoding: utf-8

import rlib
reload(rlib)
import os
from rlib.process import *

"""
Sample plugin for declaring R plugins using RExternal plugin

This plugin uses a more compact structure, as it declares all the
R processes in one file.

Note that it is CRUCIAL that each process (each class extending from 
RProcess) has a unique name (even across different plugins!!!!). Otherwise
Sextante history gets confused and some errors arise.

Author: Cesar Martinez Izquierdo
"""

class TestProcess2(RProcess):

    def defineCharacteristics(self):
        self.wd = os.path.dirname(os.path.abspath(__file__))
        self.rscript = os.path.join(self.wd, "rscript.r")
        
        # Process name
        self.setName("Test R process2")
        # Process group
        self.setGroup("Geostat course compact")
        params = self.getParameters() 
        # Define an input vector parameter, named IN_VECTOR, of type polygon and make it mandatory
        params.addInputVectorLayer("IN_VECTOR","Input vector layer", SHAPE_TYPE_POLYGON, True)

        # Define an input raster parameter named IN_RASTER and make it mandatory
        params.addInputRasterLayer("IN_RASTER","Input raster layer", True)

        # Define an output raster layer, name "OUT_RASTER"
        self.addOutputRasterLayer("OUT_RASTER", "Output raster")

class TestProcess3(RProcess):
    def defineCharacteristics(self):
        self.wd = os.path.dirname(os.path.abspath(__file__))
        self.rscript = os.path.join(self.wd, "rscript.r")

        # Process name
        self.setName("Test R process3")
        # Process group
        self.setGroup("Geostat course compact")
        params = self.getParameters() 
        # Define an input vector parameter, named IN_VECTOR, of type polygon and make it mandatory
        params.addInputVectorLayer("IN_VECTOR","Input vector layer", SHAPE_TYPE_POLYGON, True)

        # Define an input raster parameter named IN_RASTER and make it mandatory
        params.addInputRasterLayer("IN_RASTER","Input raster layer", True)

        # Define an output raster layer, name "OUT_RASTER"
        self.addOutputRasterLayer("OUT_RASTER", "Output raster")


def main():
    process = TestProcess2()
    process.selfregister("Scripting")
    process = TestProcess3()
    process.selfregister("Scripting")
    #process.updateToolbox() #not necessary at startup

main()
