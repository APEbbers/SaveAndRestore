"""
MIT License

Copyright (c) 2025 Paul Ebbers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import os
import FreeCAD as App
import FreeCADGui as Gui
import shutil
import sys
import platform
from PySide6.QtCore import Qt, QTimer, QSize, QSettings
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QLabel, QSizePolicy, QApplication, QToolButton, QStyle, QMenuBar, QMenu

import Standard_Functions_SaveAndRestore as Standard_Functions

translate = App.Qt.translate

# Get the main window of FreeCAD
mw = Gui.getMainWindow()


class SaveAndRestore:

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def ApplicationMenus(self):
        # Define a placeholder for the tools menu
        ToolsMenu = QMenu()

        # get the menubar
        MenuBar: QMenuBar = mw.menuBar()

        # Get the tools menu
        for child in MenuBar.actions():
            if child.objectName() == "&Tools":
                ToolsMenu = child
                break

        # Add a button for the Save and Restore dialog
        Button = ToolsMenu.addAction(translate("FreeCAD SaveAndRestore", "Save and restore..."))
        Button.setToolTip("FreeCAD SaveAndRestore", "Save and restore FreeCAD's setting files")

        Button.triggered.connect(self.LoadDialog)

        return

    def LoadDialog(self):
        UserConfig = App.getUserConfigDir() + "user.cfg"
        SystemConfig = App.getUserConfigDir() + "system.cfg"

        Text = f"""
        User config file is:    {UserConfig}\n
        System config file is:  {SystemConfig}|n
        """

        Standard_Functions.Mbox(Text, "", 0)


class run:
    """
    Activate SaveAndRestore.
    """

    def __init__(self, name):
        """
        Constructor
        """
        disable = 0
        if name != "NoneWorkbench":
            mw: QMainWindow = Gui.getMainWindow()
            # Disable connection after activation
            mw.workbenchActivated.disconnect(run)
            if disable:
                return

        SaveAndRestore()
