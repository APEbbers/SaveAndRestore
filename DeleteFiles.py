import pathlib
import os
import FreeCAD as App
import FreeCADGui as Gui


def DeleteFile(File):
    pathlib.Path.unlink(App.getUserConfigDir() + "user.cfg")
    return
