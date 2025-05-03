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
from stat import S_IREAD, S_IRGRP, S_IROTH
from PySide.QtCore import Qt, SIGNAL, QProcess
from PySide.QtWidgets import QApplication, QLabel, QToolBar, QMenu
import sys
from datetime import datetime
import Standard_Functions_SaveAndRestore as Standard_Functions
import zipfile
from zipfile import ZipFile
import Parameters_SaveAndRestore
import StyleMapping_SaveAndRestore
import platform
import subprocess
import webbrowser
import shutil
import time
import stat

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

    ReproAdress: str = ""

    def __init__(self):
        super(LoadDialog, self).__init__()

        # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "ui_Dialog.ui"))

        self.form.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.CustomizeWindowHint)
        self.form.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, False)
        self.form.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
        self.form.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, True)

        # Get the address of the repository address
        PackageXML = os.path.join(os.path.dirname(__file__), "package.xml")
        self.ReproAdress = Standard_Functions.ReturnXML_Value(PackageXML, "url", "type", "repository")

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
            # Hide the dialog
            self.form.hide()

            StyleSheet = f"""background-color: {StyleMapping_SaveAndRestore.ReturnStyleItem("Background_Color")};color: {StyleMapping_SaveAndRestore.ReturnStyleItem("FontColor")};"""

            self.EnableToolbars(FinishMessage="Toolbars enabled", StyleSheet=StyleSheet)

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

        # Connect the help buttons
        def Help():
            self.on_Helpbutton_clicked()

        self.form.HelpButton.connect(self.form.HelpButton, SIGNAL("clicked()"), Help)

        # Get the icon from the FreeCAD help
        helpMenu = mw.findChildren(QMenu, "&Help")[0]
        helpAction = helpMenu.actions()[0]
        helpIcon = helpAction.icon()
        # Set the help icon
        if helpIcon is not None:
            self.form.HelpButton.setIcon(helpIcon)

        # Connect the safe mode button
        def on_StartSafeMode_clicked():
            self.StartSafeMode()

        self.form.startSafeMode.connect(
            self.form.startSafeMode,
            SIGNAL("clicked()"),
            on_StartSafeMode_clicked,
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
                # if not platform.system() == "Darwin":
                with ZipFile(Fullname, "w") as zipObj:
                    for File in Files:
                        zipObj.write(File, File.split(os.sep)[-1])
                # if platform.system() == "Darwin":
                # for File in Files:
                #     self.WriteZip_MacOS(Fullname, File)

            # Write the path to preferences
            Parameters_SaveAndRestore.Settings.SetStringSetting("SaveDirectory", os.path.dirname(Fullname))
            Parameters_SaveAndRestore.SAVE_DIRECTORY = os.path.dirname(Fullname)

            print(
                translate("FreeCAD SaveAndRestore", f'Settings saved as "{FileName}" to "{os.path.dirname(Fullname)}"')
            )
        else:
            Standard_Functions.Mbox(
                translate("FreeCAD SaveAndRestore", "Please select at least one config file!", "Warning")
            )
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
            answer = Standard_Functions.RestartDialog(
                translate("FreeCAD SaveAndRestore", "Do you really restore these settings?"),
                True,
                translate("FreeCAD SaveAndRestore", "Restore and restart"),
                translate("FreeCAD SaveAndRestore", "Cancel"),
            )
            if answer == "no":
                return
            if answer == "yes":
                # Set the wait cursor
                QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

                # Extract the zipfile and place the config files
                if Fullname is not None and Fullname != "":
                    if not platform.system() == "Darwin":
                        # loading the temp.zip and creating a zip object
                        with ZipFile(Fullname, "r") as zipObj:
                            # Extracting all the members of the zip
                            # into a specific location.
                            counter = 0
                            for File in Files:
                                # Delete the files first to be sure that the file will be from the zipfile.
                                if platform.system() == "Windows":
                                    subprocess.run(
                                        os.path.join(os.path.dirname(__file__), "DeleteFile.bat")
                                        + " "
                                        + App.getUserConfigDir()
                                        + File
                                    )
                                if platform.system() == "Linux" or platform.system() == "Darwin":
                                    subprocess.run(
                                        [
                                            "bash",
                                            os.path.join(os.path.dirname(__file__), "DeleteFile.sh"),
                                            App.getUserConfigDir() + File,
                                        ]
                                    )

                                # Extract the file from the zip file into the config directory
                                try:
                                    zipObj.extract(File, App.getUserConfigDir())

                                    # Set the file to read only to prevent from FreeCAD from overwrite the file after shutdown
                                    os.chmod(File, S_IREAD)
                                except Exception:
                                    counter = counter + 1
                                    Standard_Functions.Print(f"{File} not present in archive", "Warning")
                                    continue
                            if counter == len(Files):
                                Standard_Functions.Print("There were no files to restore.", "Error")
                                return

                    if platform.system() == "Darwin":
                        counter = 0
                        for File in Files:
                            self.extract_with_permission(
                                ZipFile(Fullname), os.path.basename(File), os.path.dirname(Fullname)
                            )
                            time.sleep(1)
                            try:
                                # Delete the current files
                                subprocess.run(["bash", "DeleteFile.sh", App.getUserConfigDir() + File])

                                # Move the extracted files to the config location
                                shutil.move(
                                    os.path.join(os.path.dirname(Fullname), os.path.basename(File)),
                                    App.getUserConfigDir() + File,
                                )
                                time.sleep(1)
                                # Set the file to read only to prevent from FreeCAD from overwrite the file after shutdown
                                # os.chmod(App.getUserConfigDir() + File, S_IREAD)

                            except Exception as e:
                                print(e)
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

                    # Return to the normal cursor
                    QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)

                    # Restart FreeCAD
                    Standard_Functions.restart_freecad()
            else:
                Standard_Functions.Mbox(
                    translate("FreeCAD SaveAndRestore", "Please select at least one config file!", "Warning")
                )

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
            # Show the restart dialog
            answer = Standard_Functions.RestartDialog(
                translate("FreeCAD SaveAndRestore", "Do you really clear the settings?"),
                True,
                translate("FreeCAD SaveAndRestore", "Clear and restart"),
                translate("FreeCAD SaveAndRestore", "Cancel"),
            )
            if answer == "yes":
                # Set the wait cursor
                QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
                # Remove the file(s)
                for File in Files:
                    if platform.system() == "Windows":
                        subprocess.run(os.path.join(os.path.dirname(__file__), "DeleteFile.bat") + " " + File)
                    if platform.system() == "Linux" or platform.system() == "Darwin":
                        subprocess.run(["bash", os.path.join(os.path.dirname(__file__), "DeleteFile.sh"), File])

                    # Create empty files, which will be filled at startup
                    with open(File, "w") as file:
                        pass

                    # Set the file to read only to prevent from FreeCAD from overwrite the file after shutdown
                    os.chmod(File, S_IREAD)

                # Return to the normal cursor
                QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)

                # Restart FreeCAD
                Standard_Functions.restart_freecad()
        else:
            QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
            Standard_Functions.Mbox(
                translate("FreeCAD SaveAndRestore", "Please select at least one config file!", "Warning")
            )

        return

    def EnableToolbars(self, FinishMessage="", StyleSheet=None):
        # Show the restart dialog
        answer = Standard_Functions.RestartDialog(
            translate("FreeCAD SaveAndRestore", "Do you really want to restore all toolbars?"),
            True,
            translate("FreeCAD SaveAndRestore", "Restore and restart"),
            translate("FreeCAD SaveAndRestore", "Cancel"),
        )
        if answer == "yes":
            lbl = QLabel(translate("FreeCAD SaveAndResore", "Loading workbench … (…/…)"))
            lbl.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowStaysOnTopHint)
            lbl.setMinimumSize(300, 20)
            lbl.setContentsMargins(3, 3, 3, 3)

            # Get the stylesheet from the main window and use it for this form
            if StyleSheet is not None:
                lbl.setStyleSheet(StyleSheet)

            lbl.show()
            lst = Gui.listWorkbenches()
            for i, wb in enumerate(lst):
                msg = (
                    translate("FreeCAD SaveAndResore", "Loading workbench ")
                    + wb
                    + " ("
                    + str(i + 1)
                    + "/"
                    + str(len(lst))
                    + ")"
                )
                print(msg)
                lbl.setText(msg)
                geo = lbl.geometry()
                geo.setSize(lbl.sizeHint())
                lbl.setGeometry(geo)
                lbl.repaint()
                Gui.updateGui()  # Probably slower with this, because it redraws the entire GUI with all tool buttons changed etc. but allows the label to actually be updated, and it looks nice and gives a quick overview of all the workbenches…
                try:
                    Gui.activateWorkbench(wb)
                    Workbench = Gui.activeWorkbench()
                    for ToolbarName in Workbench.listToolbars():
                        ToolBar = mw.findChild(QToolBar, ToolbarName)
                        ToolBar.setEnabled(True)
                        ToolBar.show()

                        preferences = App.ParamGet("User parameter:BaseApp/MainWindow/ToolBars")
                        preferences.SetBool(ToolbarName, True)
                        App.saveParameter()

                    Gui.updateGui()
                except Exception as e:
                    print(e)
                    pass

            # Print an message
            if FinishMessage != "":
                lbl.setText(FinishMessage)
                print(FinishMessage)

            # Restart FreeCAD
            Standard_Functions.restart_freecad()

        return

    def on_Helpbutton_clicked(self):
        if self.ReproAdress != "" or self.ReproAdress is not None:
            if not self.ReproAdress.endswith("/"):
                self.ReproAdress = self.ReproAdress + "/"

            Adress = self.ReproAdress + "wiki"
            webbrowser.open(Adress, new=2, autoraise=True)
        return

    def StartSafeMode(self):
        args = QApplication.arguments()[1:]
        args.append("--safe-mode")
        args.append(f"-P --{os.path.join(os.path.dirname(__file__), 'SaveAndRestore.py')}")

        if Gui.getMainWindow().close():
            QProcess.startDetached(QApplication.applicationFilePath(), args)

    def extract_all_with_permission(self, zipfile, target_dir, ZIP_SYSTEM=3):
        for info in zipfile.infolist():
            extracted_path = zipfile.extract(info, target_dir)

            if info.create_system == ZIP_SYSTEM:
                unix_attributes = info.external_attr >> 16
            if unix_attributes:
                os.chmod(extracted_path, unix_attributes)
        return

    def extract_with_permission(self, zipfile: ZipFile, filename: str, target_dir: str, ZIP_SYSTEM=3):
        print(zipfile.infolist())
        for info in zipfile.infolist():
            if filename in info.filename:
                extracted_path = zipfile.extract(info, target_dir)

                if info.create_system == ZIP_SYSTEM:
                    unix_attributes = info.external_attr >> 16
                if unix_attributes:
                    os.chmod(extracted_path, unix_attributes)

        return

    def WriteZip_MacOS(self, NewArchive_FullPath, FileToArchive):
        ZIP_MAC_SYSTEM = 7  # macOS
        zipInfo = zipfile.ZipInfo(os.path.basename(FileToArchive))
        zipInfo.create_system = ZIP_MAC_SYSTEM
        unix_st_mode = (
            stat.S_IFLNK
            | stat.S_IRUSR
            | stat.S_IWUSR
            | stat.S_IXUSR
            | stat.S_IRGRP
            | stat.S_IWGRP
            | stat.S_IXGRP
            | stat.S_IROTH
            | stat.S_IWOTH
            | stat.S_IXOTH
        )
        zipInfo.external_attr = unix_st_mode << 16

        mode = "w"
        if os.path.exists(NewArchive_FullPath):
            mode = "a"
        with ZipFile(NewArchive_FullPath, mode) as zipObj:
            zipObj.writestr(zipInfo, NewArchive_FullPath)

        return


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
