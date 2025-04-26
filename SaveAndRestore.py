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
import subprocess
from PySide6.QtCore import Qt, QTimer, QSize, QSettings, SIGNAL
from PySide6.QtGui import QGuiApplication, QAction
from PySide6.QtWidgets import QMainWindow, QLabel, QSizePolicy, QApplication, QToolButton, QStyle, QMenuBar, QMenu

import Standard_Functions_SaveAndRestore as Standard_Functions
import LoadDialog_SaveAndRestore

translate = App.Qt.translate

# Get the main window of FreeCAD
mw: QMainWindow = Gui.getMainWindow()


class SaveAndRestore:

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

        self.ApplicationMenus()

    def ApplicationMenus(self):
        try:
            # get the menubar
            MenuBar: QMenuBar = mw.menuBar()

            # Add a button for the Save and Restore dialog
            Button = QAction(mw)
            Button.setText(translate("FreeCAD SaveAndRestore", "Save and restore..."))
            Button.setToolTip(translate("FreeCAD SaveAndRestore", "Save and restore FreeCAD's setting files"))
            # Button.connect(Button, SIGNAL("triggered()"), self.loadDialog)
            Button.triggered.connect(self.loadDialog)

            # Add the button to the tools menu
            for action in MenuBar.children():
                if action.objectName() == "&Tools":
                    action.addAction(Button)

        except Exception:
            pass
        return

    def loadDialog(self):
        print("got here")
        LoadDialog_SaveAndRestore.main()
        return


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
