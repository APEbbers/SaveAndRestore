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

import FreeCAD as App
import FreeCADGui as Gui
import os
from PySide6.QtGui import QIcon, QPixmap, QAction, QGuiApplication
from PySide6.QtWidgets import (
    QListWidgetItem,
    QTableWidgetItem,
    QListWidget,
    QTableWidget,
    QToolBar,
    QToolButton,
    QComboBox,
    QPushButton,
    QMenu,
    QWidget,
    QLineEdit,
    QSizePolicy,
    QRadioButton,
    QLabel,
)
from PySide6.QtCore import Qt, SIGNAL, Signal, QObject, QThread, QSize
import sys
import json
from datetime import datetime
import Standard_Functions_SaveAndRestore as Standard_Functions
import pathlib
from zipfile import ZipFile

# Get the resources
pathUI = os.path.join(os.path.dirname(__file__), "Resources", "ui")
pathIcons = os.path.join(os.path.dirname(__file__), "Resources", "icons")
sys.path.append(pathIcons)
sys.path.append(pathUI)

# import graphical created Ui. (With QtDesigner or QtCreator)
import ui_Dialog as ui_Dialog

# Define the translation
translate = App.Qt.translate

# Get the main window of FreeCAD
mw = Gui.getMainWindow()


class LoadDialog(ui_Dialog.Ui_Dialog):

    def __init__(self):
        super(LoadDialog, self).__init__()

        # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "ui_Dialog.ui"))

        self.form.saveSettings.connect(
            self.form.saveSettings,
            SIGNAL("clicked()"),
            self.on_saveSettings_clicked,
        )

    def on_saveSettings_clicked(self):
        self.SaveSettings()

    def SaveSettings(self=None):
        UserConfig = App.getUserConfigDir() + "user.cfg"
        SystemConfig = App.getUserConfigDir() + "system.cfg"

        Files = [UserConfig, SystemConfig]

        now = datetime.datetime.now()
        Prefix = now.strftime("%Y_%m_%d_%H_%M_%S")

        # Define the filename
        FileName = f"{Prefix} - FreeCAD Settings.zip"

        # assume onedrive is present, desktop will be one layer below
        # something like "C:/Users/username/Onedrive - company name/Desktop"
        desktop = Standard_Functions.find_cloud_path()
        # if no Onedrive revert to standard Desktop
        # location: i.e. "C:/Users/username/Desktop
        if len(desktop) == 0:
            desktop = pathlib.Path.home() / "Desktop"
        Fullname = os.path.join(desktop, FileName)

        with ZipFile(Fullname, "w") as zipObj:
            for File in Files:
                zipObj.write(File, File.split(os.sep)[-1])

        return


def main():
    print("tried to load the form")
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
