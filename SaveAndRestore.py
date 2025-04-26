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
import zipfile
from zipfile import ZipFile
import datetime
import pathlib
from glob import glob
import json
from pathlib import Path

import Standard_Functions_SaveAndRestore as Standard_Functions

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

            def LoadDialog():
                self.LoadDialog()

            Button.connect(Button, SIGNAL("triggered()"), LoadDialog)

            # Add the button to the tools menu
            for action in MenuBar.children():
                if action.objectName() == "&Tools":
                    action.addAction(Button)

        except Exception:
            pass
        return

    def LoadDialog(self=None):
        UserConfig = App.getUserConfigDir() + "user.cfg"
        SystemConfig = App.getUserConfigDir() + "system.cfg"

        Files = [UserConfig, SystemConfig]

        now = datetime.datetime.now()
        Prefix = now.strftime("%Y_%m_%d_%H_%M_%S")

        # Define the filename
        FileName = f"{Prefix} - FreeCAD Settings.zip"

        # assume onedrive is present, desktop will be one layer below
        # something like "C:/Users/username/Onedrive - company name/Desktop"
        desktop = find_cloud_path()
        # if no Onedrive revert to standard Desktop
        # location: i.e. "C:/Users/username/Desktop
        if len(desktop) == 0:
            desktop = pathlib.Path.home() / "Desktop"
        Fullname = os.path.join(desktop, FileName)

        with ZipFile(Fullname, "w") as zipObj:
            for File in Files:
                zipObj.write(File, File.split(os.sep)[-1])

        return


def find_cloud_path():
    if platform.system().lower() == "windows":
        command = r'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v "Desktop"'
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        desktop = result.stdout.splitlines()[2].split()[2]

        return desktop
    else:
        return ""


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
