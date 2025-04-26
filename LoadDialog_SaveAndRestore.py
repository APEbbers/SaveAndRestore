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
    QCheckBox,
)
from PySide6.QtCore import Qt, SIGNAL, Signal, QObject, QThread, QSize
import sys
import json
from datetime import datetime
import Standard_Functions_SaveAndRestore as Standard_Functions
import pathlib
from zipfile import ZipFile
import Parameters_SaveAndRestore

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

        # Connect the save function
        def on_saveSettings_clicked():
            self.SaveSettings()

        self.form.saveSettings.connect(
            self.form.saveSettings,
            SIGNAL("clicked()"),
            on_saveSettings_clicked,
        )

        # Connect the restore function
        def on_RestoreSettings_clicked():
            self.RestoreSettings()

        self.form.restoreSettings.connect(
            self.form.restoreSettings,
            SIGNAL("clicked()"),
            on_RestoreSettings_clicked,
        )

        # Connect the restore ToolBars function
        def on_EnableToolbars_clicked():
            self.EnableToolbars()

        self.form.restoreToolbars.connect(
            self.form.restoreToolbars,
            SIGNAL("clicked()"),
            on_EnableToolbars_clicked,
        )
        return

    def SaveSettings(self):
        UserConfig = App.getUserConfigDir() + "user.cfg"
        SystemConfig = App.getUserConfigDir() + "system.cfg"

        Files = []
        if self.form.IncludeUser_Save.checkState() == Qt.CheckState.Checked:
            Files.append(UserConfig)
        if self.form.IncludeSystem_Save.checkState() == Qt.CheckState.Checked:
            Files.append(SystemConfig)

        if len(Files) > 0:
            now = datetime.now()
            Prefix = now.strftime("%Y_%m_%d_%H_%M_%S")

            # Define the filename
            FileName = f"{Prefix} - FreeCAD Settings.zip"

            # Get the file and location were the zip file must be saved
            Fullname = Standard_Functions.GetFileDialog(
                Filter="Archive (*.zip)",
                parent=self.form,
                DefaultPath=os.path.join(Parameters_SaveAndRestore.SAVE_DIRECTORY, FileName),
                SaveAs=True,
            )

            with ZipFile(Fullname, "w") as zipObj:
                for File in Files:
                    zipObj.write(File, File.split(os.sep)[-1])
            print(translate("FreeCAD SaveAndRestore", "Settings saved"))
        else:
            print(translate("FreeCAD SaveAndRestore", "No settings selected to save"))
        return

    def RestoreSettings(self):
        UserConfig = "user.cfg"
        SystemConfig = "system.cfg"

        Files = []
        if self.form.IncludeUser_Restore.checkState() == Qt.CheckState.Checked:
            Files.append(UserConfig)
        if self.form.IncludeSystem_Restore.checkState() == Qt.CheckState.Checked:
            Files.append(SystemConfig)

        Fullname = Standard_Functions.GetFileDialog(
            Filter="Archive (*.zip)",
            parent=self.form,
            DefaultPath=Parameters_SaveAndRestore.SAVE_DIRECTORY,
            SaveAs=False,
        )
        if Fullname is not None and Fullname != "":
            # loading the temp.zip and creating a zip object
            with ZipFile(Fullname, "r") as zipObj:
                # Extracting all the members of the zip
                # into a specific location.
                for File in Files:
                    zipObj.extract(File, App.getUserConfigDir())

                answer = Standard_Functions.RestartDialog(includeIcons=True)
                if answer == "yes":
                    Standard_Functions.restart_freecad()

        return

    def EnableToolbars(self):
        ToolBarGroup = App.ParamGet("User parameter:BaseApp/MainWindow/Toolbars")

        ToolBarStates = ToolBarGroup.getBools()

        for ToolBar in ToolBarStates:
            ToolBar.setBool(True)

        answer = Standard_Functions.RestartDialog(includeIcons=True)
        if answer == "yes":
            Standard_Functions.restart_freecad()

        return


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
