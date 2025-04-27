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
import json
from PySide.QtCore import Qt, QTimer, QSize, QSettings, SIGNAL
from PySide.QtGui import QGuiApplication, QAction
from PySide.QtWidgets import QMainWindow, QLabel, QSizePolicy, QApplication, QToolButton, QStyle, QMenuBar, QMenu
from time import sleep

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
        # try:
        # get the menubar
        MenuBar: QMenuBar = mw.menuBar()

        # Add a button for the Save and Restore dialog
        Button = QAction(mw)
        Button.setText(translate("FreeCAD SaveAndRestore", "Save and restore..."))
        Button.setObjectName("SaveAndRestore")
        Button.setToolTip(translate("FreeCAD SaveAndRestore", "Save and restore FreeCAD's setting files"))

        def LoadDialog():
            LoadDialog_SaveAndRestore.main()

        Button.connect(Button, SIGNAL("triggered()"), LoadDialog)

        # Add the button to the tools menu
        def addMenu():
            for child in MenuBar.children():
                if child.objectName() == "&Tools":
                    isPresent = False
                    for action in child.actions():
                        if action.text() == "Save and restore...":
                            isPresent = True

                    if isPresent is False:
                        child.addAction(Button)

        mw.workbenchActivated.connect(addMenu)

        def runStartup(name):
            # Do not run when NoneWorkbench is activated because UI isn't yet completely there
            if name != "NoneWorkbench":
                # Run macro only once by disconnecting the signal at first call
                Gui.getMainWindow().workbenchActivated.disconnect(runStartup)

                self.WriteResetList()
                self.DetectAddOnChange()

        # # Connect the function that runs the macro to the appropriate signal
        mw.workbenchActivated.connect(runStartup)

        # except Exception as e:
        #     print(e)
        return

    def DetectAddOnChange(self):
        # Get the folder with add-ons
        path = os.path.dirname(__file__)
        # Get the folder with add-ons
        for i in range(2):
            # Starting point
            path = os.path.dirname(path)

        FileName = os.path.join(path, "SaveAndRestore", "ResetList.json")
        WB_ResetList = []
        with open(FileName, "r") as file:
            WB_ResetList = json.load(file)
        file.close()

        ToolBarReset = False

        # Go through the sub-folders and add them to the list
        CurrentAddOnList = []
        for root, dirs, files in os.walk(path):
            # remove the path from the root and split the remaining path so that only the add-on folder remains
            # Add this to a list if it is not in yet
            subdir = root.replace(path + os.sep, "").split(os.sep, 1)[0]
            # Add the path again to get a full path
            subdir = os.path.normpath(path + os.sep + subdir)

            # Check if the sub directory is already in the addon list
            isInList = False
            for AddOn in CurrentAddOnList:
                if AddOn == subdir:
                    isInList = True
                    break
            # Add the subdirectory to the current addon list
            if isInList is False and os.path.exists(subdir):
                CurrentAddOnList.append(subdir)

        # If there is already a WBlist, read it to compare
        FileName = os.path.join(path, "SaveAndRestore", "WBList.json")
        if os.path.exists(FileName):
            PreviousAddOnList = []
            with open(FileName, "r") as file:
                PreviousAddOnList = json.load(file)
                file.close()

            # Check if an add-on is removed
            for PreviousAddon in PreviousAddOnList:
                isInList = False
                for AddOn in CurrentAddOnList:
                    if AddOn == PreviousAddon:
                        isInList = True

                if isInList is False:
                    for WB in WB_ResetList:
                        if WB in PreviousAddon:
                            ToolBarReset = True
                            break

        # Check if a WB is installed that is present in the resetList
        if ToolBarReset is False:
            for AddOn in CurrentAddOnList:
                for WB in WB_ResetList:
                    if WB in AddOn:
                        # Check if the Addon is disabled
                        for name in os.listdir(AddOn):
                            if name == "ADDON_DISABLED":
                                ToolBarReset = True
                                WB_ResetList.remove(AddOn.rsplit(os.sep, 1)[1])
                                with open(os.path.join(path, "SaveAndRestore", "ResetList.json"), "w") as outfile:
                                    json.dump(WB_ResetList, outfile, indent=4)
                                outfile.close()
                                break
                        break

        # Write the current addon list
        with open(os.path.join(path, "SaveAndRestore", "WBList.json"), "w") as outfile:
            json.dump(CurrentAddOnList, outfile, indent=4)
        outfile.close()

        if ToolBarReset is True:
            text = translate(
                "FreeCAD SaveAndRestore",
                """an add-on is disabled or uninstalled. Do you want to open the "Save and restore" dialog to restore all toolbars or restore to previous saved settings?
            """,
            )
            Anwser = Standard_Functions.Mbox(text=text, title="", style=1, IconType="Question")

            if Anwser == "yes":
                LoadDialog_SaveAndRestore.main()
        return

    def WriteResetList(self):
        # Get the folder with add-ons
        path = os.path.dirname(__file__)

        # The list with add-ons for which this applies
        WbToLookFor = ["FreeCAD-Ribbon"]

        # Get the folder with add-ons
        for i in range(2):
            # Starting point
            path = os.path.dirname(path)

        # Go through the sub-folders and add them to the list
        CurrentAddOnList = []
        for root, dirs, files in os.walk(path):
            # remove the path from the root and split the remaining path so that only the add-on folder remains
            # Add this to a list if it is not in yet
            subdir = root.replace(path + os.sep, "").split(os.sep, 1)[0]
            # Add the path again to get a full path
            subdir = os.path.normpath(path + os.sep + subdir)

            # Check if the sub directory is already in the addon list
            isInList = False
            for AddOn in CurrentAddOnList:
                if AddOn == subdir:
                    isInList = True
                    break
            # Add the subdirectory to the current addon list
            if isInList is False and os.path.exists(subdir):
                CurrentAddOnList.append(subdir)

            # If there is already a WBlist, read it to compare
            FileName = os.path.join(path, "SaveAndRestore", "WBList.json")
            if os.path.exists(FileName):
                PreviousAddOnList = []
                with open(FileName, "r") as file:
                    PreviousAddOnList = json.load(file)
                    file.close()

                # Check if an add-on is installed
                for AddOn in CurrentAddOnList:
                    isInList = False
                    for PreviousAddon in PreviousAddOnList:
                        if AddOn == PreviousAddon:
                            isInList = True

                    if isInList is False:
                        if WbToLookFor.__contains__(AddOn):
                            # Write the reset list
                            with open(os.path.join(path, "SaveAndRestore", "ResetList.json"), "w") as outfile:
                                json.dump(CurrentAddOnList, outfile, indent=4)
                            outfile.close()


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
