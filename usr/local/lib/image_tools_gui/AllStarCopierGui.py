#!/usr/bin/python
from image_tools.AllStarCopier import AllStarCopier
from ImageToolsSharedGui import ImageFileInfoToolGui

class AllStarCopierGui(AllStarCopier):

    def doRunSteps(self):
        imageTool = ImageFileInfoToolGui(self.out, self.system)
        super(AllStarCopierGui, self).doRunSteps(imageTool)

if __name__ == '__main__':
    from py_base.Job import runMockJob
    from image_tools.ImageToolsShared import getTestFilePaths
    runMockJob(AllStarCopierGui, arguments={'path':getTestFilePaths()})
