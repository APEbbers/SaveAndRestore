# *************************************************************************
# *                                                                       *
# * Copyright (c) 2019-2024 Hakan Seven, Geolta, Paul Ebbers              *
# *                                                                       *
# * This program is free software; you can redistribute it and/or modify  *
# * it under the terms of the GNU Lesser General Public License (LGPL)    *
# * as published by the Free Software Foundation; either version 3 of     *
# * the License, or (at your option) any later version.                   *
# * for detail see the LICENCE text file.                                 *
# *                                                                       *
# * This program is distributed in the hope that it will be useful,       *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# * GNU Library General Public License for more details.                  *
# *                                                                       *
# * You should have received a copy of the GNU Library General Public     *
# * License along with this program; if not, write to the Free Software   *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# * USA                                                                   *
# *                                                                       *
# *************************************************************************

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
        if value.lower() == "none":
            value = ""
        if value == "":
            value = DefaultSettings[settingName]
        preferences.SetString(settingName, value)
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
