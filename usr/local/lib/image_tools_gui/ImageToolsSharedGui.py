from os.path import basename, dirname, splitext

from image_tools.ImageToolsShared import ImageFileInfoTool
from py_base_gui.PySystemGui import InputDialog

class ImageFileInfoToolGui(ImageFileInfoTool):

    def askUserForNewFileName(self, fullPath):
        base = basename(fullPath)
        defaultValue, extension = splitext(base)
        dialog = InputDialog('Renaming %s' % defaultValue,
                             self.out,
                             self.system,
                             label='Name this file or forever hold your peace:',
                             defaultValue=defaultValue,
                             imageFileName=fullPath)
        response = dialog.show()
        if not response:
            result = fullPath
        else:
            result = '%s/%s%s' % (dirname(fullPath), response, extension.lower())
        return result

if __name__ == "__main__":
    from PySystemMock import PySystemMock
    from JobOutput import JobOutput

    out = JobOutput()
    system = PySystemMock(out)
    infoTool = ImageFileInfoToolGui(out, system)
    fullPath = '/home/luke/Public/AllStars/rome.jpg'

    fullPath = infoTool.askUserForNewFileName(fullPath)

    print "RETURNED: " + fullPath
