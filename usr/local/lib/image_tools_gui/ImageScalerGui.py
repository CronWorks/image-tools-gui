#!/usr/bin/python
from image_tools.ImageScaler import ImageScaler
from image_tools_gui.ImageToolsSharedGui import ImageFileInfoToolGui

class ImageScalerGui(ImageScaler):

    def doRunSteps(self):
        imageTool = ImageFileInfoToolGui(self.out, self.system)
        super(ImageScalerGui, self).doRunSteps(imageTool)

if __name__ == "__main__":
    from py_base.Job import runMockJob
    from image_tools.ImageToolsShared import getTestFilePaths
    runMockJob(ImageScalerGui, arguments={'path':getTestFilePaths()})
