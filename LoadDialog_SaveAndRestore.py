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
from PySide.QtCore import Qt, SIGNAL
import sys
from datetime import datetime
import Standard_Functions_SaveAndRestore as Standard_Functions
import zipfile
from zipfile import ZipFile
import Parameters_SaveAndRestore
import StyleMapping_SaveAndRestore
import pathlib

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
            StyleSheet = f"""background-color: {StyleMapping_SaveAndRestore.ReturnStyleItem("Background_Color")};color: {StyleMapping_SaveAndRestore.ReturnStyleItem("FontColor")};"""

            Standard_Functions.EnableToolbars(StyleSheet=StyleSheet, FinishMessage="Toolbars enabled")

        self.form.restoreToolbars.connect(
            self.form.restoreToolbars,
            SIGNAL("clicked()"),
            on_EnableToolbars_clicked,
        )

        # Connect the clear button
        def on_ClearSettings_clicked():
            self.ClearSettings()

        self.form.clearSettings.connect(
            self.form.clearSettings,
            SIGNAL("clicked()"),
            on_ClearSettings_clicked,
        )

        return

    def SaveSettings(self):
        # Define the paths for the config files
        UserConfig = App.getUserConfigDir() + "user.cfg"
        SystemConfig = App.getUserConfigDir() + "system.cfg"

        # If checked, add the config files to the list
        Files = []
        if self.form.IncludeUser_Save.checkState() == Qt.CheckState.Checked:
            Files.append(UserConfig)
        if self.form.IncludeSystem_Save.checkState() == Qt.CheckState.Checked:
            Files.append(SystemConfig)

        # If the file list is not empty, continue
        if len(Files) > 0:
            # Define a prefix
            now = datetime.now()
            Prefix = now.strftime("%Y_%m_%d_%H_%M_%S")

            # Define the filename
            FileName = f"{Prefix} - FreeCAD Settings.zip"

            # Get the file and location were the zip file must be saved wit a saveas dialog
            Fullname = Standard_Functions.GetFileDialog(
                Filter="Archive (*.zip)",
                parent=self.form,
                DefaultPath=os.path.join(Parameters_SaveAndRestore.SAVE_DIRECTORY, FileName),
                SaveAs=True,
            )
            if Fullname is not None and Fullname != "":
                # Create the zipfile with the config files
                with ZipFile(Fullname, "w") as zipObj:
                    for File in Files:
                        zipObj.write(File, File.split(os.sep)[-1])

                # Write the path to preferences
                Parameters_SaveAndRestore.Settings.SetStringSetting("SaveDirectory", os.path.dirname(Fullname))
                Parameters_SaveAndRestore.SAVE_DIRECTORY = os.path.dirname(Fullname)

                print(
                    translate(
                        "FreeCAD SaveAndRestore", f'Settings saved as "{FileName}" to "{os.path.dirname(Fullname)}"'
                    )
                )
        else:
            Standard_Functions.Mbox(translate("FreeCAD SaveAndRestore", "Please select at least one config file!", "Warning"))
        return

    def RestoreSettings(self):
        # Define the paths for the config files
        UserConfig = "user.cfg"
        SystemConfig = "system.cfg"

        # If checked, add the config files to the list
        Files = []
        if self.form.IncludeUser_Restore.checkState() == Qt.CheckState.Checked:
            Files.append(UserConfig)
        if self.form.IncludeSystem_Restore.checkState() == Qt.CheckState.Checked:
            Files.append(SystemConfig)

        # If at least one config file is checked, select the zipfile with the config files via a file open dialog
        if len(Files) > 0:
            Fullname = Standard_Functions.GetFileDialog(
                Filter="Archive (*.zip)",
                parent=self.form,
                DefaultPath=Parameters_SaveAndRestore.SAVE_DIRECTORY,
                SaveAs=False,
            )
            
            # Extract the zipfile and place the config files
            if Fullname is not None and Fullname != "":
                # loading the temp.zip and creating a zip object
                with ZipFile(Fullname, "r") as zipObj:
                    # Extracting all the members of the zip
                    # into a specific location.
                    counter = 0
                    for File in Files:
                        try:
                            zipObj.extract(File, App.getUserConfigDir())
                        except Exception:
                            counter = counter + 1
                            Standard_Functions.Print(f"{File} not present in archive", "Warning")
                            continue
                    if counter == len(Files):
                        Standard_Functions.Print("There were no files to restore.", "Error")
                        return

                    # Write the path to preferences
                    Parameters_SaveAndRestore.Settings.SetStringSetting("SaveDirectory", os.path.dirname(Fullname))
                    Parameters_SaveAndRestore.SAVE_DIRECTORY = os.path.dirname(Fullname)

                    # print a message
                    print(translate("FreeCAD SaveAndRestore", f'Settings restored from "{Fullname}"'))

                    # Show the restart dialog
                    answer = Standard_Functions.RestartDialog(includeIcons=True)
                    if answer == "yes":
                        Standard_Functions.restart_freecad()
        else:
            Standard_Functions.Mbox(translate("FreeCAD SaveAndRestore", "Please select at least one config file!", "Warning"))

        return

    def ClearSettings(self):
        # Define the paths for the config files
        UserConfig = App.getUserConfigDir() + "user.cfg"
        SystemConfig = App.getUserConfigDir() + "system.cfg"

        # If checked, add the config files to the list
        Files = []
        if self.form.IncludeUser_Clear.checkState() == Qt.CheckState.Checked:
            Files.append(UserConfig)
        if self.form.IncludeSystem_Clear.checkState() == Qt.CheckState.Checked:
            Files.append(SystemConfig)

        if len(Files) > 0:
            # Remove the file(s)
            for File in Files:
                pathlib.Path.unlink(File)

            # Show the restart dialog
            answer = Standard_Functions.RestartDialog(includeIcons=True)
            if answer == "yes":
                Standard_Functions.restart_freecad()
        else:
            Standard_Functions.Mbox(translate("FreeCAD SaveAndRestore", "Please select at least one config file!", "Warning"))

        return


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
