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
from PySide.QtGui import QColor
import os
import sys
import Standard_Functions_SaveAndRestore as Standard_Functions

# Define the translation
translate = App.Qt.translate

preferences = App.ParamGet("User parameter:BaseApp/Preferences/Mod/SaveAndRestore")


class Settings:

    # region -- Functions to read the settings from the FreeCAD Parameters
    # and make sure that a None type result is ""
    def GetStringSetting(settingName: str) -> str:
        result = preferences.GetString(settingName)

        if result.lower() == "none":
            result = ""
        return result

    def GetIntSetting(settingName: str) -> int:
        result = preferences.GetInt(settingName)
        if result == "":
            result = None
        return result

    def GetFloatSetting(settingName: str) -> int:
        result = preferences.GetFloat(settingName)
        if result == "":
            result = None
        return result

    def GetBoolSetting(settingName: str) -> bool:
        result = None
        settings = preferences.GetContents()
        exists = False
        for setting in settings:
            if setting[0] == "Boolean" and setting[1] == settingName:
                exists = True
                break
        if exists is True:
            result = preferences.GetBool(settingName)
        return result

    def GetColorSetting(settingName: str) -> object:
        # Create a tuple from the int value of the color
        result = QColor.fromRgba(preferences.GetUnsigned(settingName)).toTuple()

        # correct the order of the tuple and divide them by 255
        result = (result[3] / 255, result[0] / 255, result[1] / 255, result[2] / 255)

        return result

    # endregion

    # region - Functions to write settings to the FreeCAD Parameters
    #
    #
    def SetStringSetting(settingName: str, value: str):
        if str(value).lower() == "none":
            value = ""
        if value == "":
            value = DefaultSettings[settingName]
        preferences.SetString(settingName, str(value))
        return

    def SetBoolSetting(settingName: str, value: bool):
        if value is None:
            value = DefaultSettings[settingName]
        preferences.SetBool(settingName, value)
        return

    def SetIntSetting(settingName: str, value: int):
        if str(value).lower() == "":
            value = int(DefaultSettings[settingName])
        if str(value).lower() != "":
            preferences.SetInt(settingName, value)
        return

    # endregion

    def WriteSettings():
        Settings.SetStringSetting("SaveDirectory", SAVE_DIRECTORY)

        return


# region - Define the resources ----------------------------------------------------------------------------------------
ICON_LOCATION = os.path.join(os.path.dirname(__file__), "Resources", "icons")
UI_LOCATION = os.path.join(os.path.dirname(__file__), "Resources", "ui")
# endregion ------------------------------------------------------------------------------------------------------------

DefaultSettings = {
    "SaveDirectory": Standard_Functions.find_cloud_path(),
}

# region - Define the import location ----------------------------------------------------------------------------------
SAVE_DIRECTORY = Settings.GetStringSetting("SaveDirectory")
if SAVE_DIRECTORY == "":
    SAVE_DIRECTORY = DefaultSettings["SaveDirectory"]
    Settings.SetStringSetting("SaveDirectory", SAVE_DIRECTORY)
# endregion ------------------------------------------------------------------------------------------------------------
