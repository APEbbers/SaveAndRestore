# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_DialogahyIKZ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QGridLayout,
    QGroupBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(419, 377)
        self.gridLayout_6 = QGridLayout(Dialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.saveSettings = QPushButton(self.groupBox)
        self.saveSettings.setObjectName("saveSettings")
        self.saveSettings.setMinimumSize(QSize(200, 50))

        self.gridLayout.addWidget(self.saveSettings, 0, 0, 2, 1)

        self.IncludeUser_Save = QCheckBox(self.groupBox)
        self.IncludeUser_Save.setObjectName("IncludeUser_Save")
        self.IncludeUser_Save.setChecked(True)

        self.gridLayout.addWidget(self.IncludeUser_Save, 0, 1, 1, 1)

        self.IncludeSystem_Save = QCheckBox(self.groupBox)
        self.IncludeSystem_Save.setObjectName("IncludeSystem_Save")
        self.IncludeSystem_Save.setChecked(True)

        self.gridLayout.addWidget(self.IncludeSystem_Save, 1, 1, 1, 1)

        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox1 = QGroupBox(Dialog)
        self.groupBox1.setObjectName("groupBox1")
        self.gridLayout_2 = QGridLayout(self.groupBox1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.IncludeUser_Restore = QCheckBox(self.groupBox1)
        self.IncludeUser_Restore.setObjectName("IncludeUser_Restore")
        self.IncludeUser_Restore.setChecked(True)

        self.gridLayout_2.addWidget(self.IncludeUser_Restore, 0, 1, 1, 1)

        self.restoreSettings = QPushButton(self.groupBox1)
        self.restoreSettings.setObjectName("restoreSettings")
        self.restoreSettings.setMinimumSize(QSize(200, 50))

        self.gridLayout_2.addWidget(self.restoreSettings, 0, 0, 2, 1)

        self.IncludeSystem_Restore = QCheckBox(self.groupBox1)
        self.IncludeSystem_Restore.setObjectName("IncludeSystem_Restore")
        self.IncludeSystem_Restore.setChecked(True)

        self.gridLayout_2.addWidget(self.IncludeSystem_Restore, 1, 1, 1, 1)

        self.gridLayout_6.addWidget(self.groupBox1, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.IncludeUser_Clear = QCheckBox(self.groupBox_2)
        self.IncludeUser_Clear.setObjectName("IncludeUser_Clear")
        self.IncludeUser_Clear.setChecked(True)

        self.gridLayout_5.addWidget(self.IncludeUser_Clear, 0, 1, 1, 1)

        self.clearSettings = QPushButton(self.groupBox_2)
        self.clearSettings.setObjectName("clearSettings")
        self.clearSettings.setMinimumSize(QSize(200, 50))

        self.gridLayout_5.addWidget(self.clearSettings, 0, 0, 2, 1)

        self.IncludeSystem_Clear = QCheckBox(self.groupBox_2)
        self.IncludeSystem_Clear.setObjectName("IncludeSystem_Clear")
        self.IncludeSystem_Clear.setChecked(True)

        self.gridLayout_5.addWidget(self.IncludeSystem_Clear, 1, 1, 1, 1)

        self.gridLayout_6.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox2 = QGroupBox(Dialog)
        self.groupBox2.setObjectName("groupBox2")
        self.gridLayout_4 = QGridLayout(self.groupBox2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.restoreToolbars = QPushButton(self.groupBox2)
        self.restoreToolbars.setObjectName("restoreToolbars")
        self.restoreToolbars.setMinimumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.restoreToolbars, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.startSafeMode = QPushButton(self.groupBox2)
        self.startSafeMode.setObjectName("startSafeMode")
        self.startSafeMode.setMinimumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.startSafeMode, 1, 0, 1, 1)

        self.gridLayout_6.addWidget(self.groupBox2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.CloseButton = QPushButton(Dialog)
        self.CloseButton.setObjectName("CloseButton")

        self.gridLayout_3.addWidget(self.CloseButton, 0, 2, 1, 1)

        self.HelpButton = QPushButton(Dialog)
        self.HelpButton.setObjectName("HelpButton")

        self.gridLayout_3.addWidget(self.HelpButton, 0, 0, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_3, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.CloseButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Save and restore", None)
        )
        # if QT_CONFIG(tooltip)
        self.saveSettings.setToolTip(
            QCoreApplication.translate(
                "Dialog",
                'Save "user.cfg" and "system.cfg" to a zipfile as backup.',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.saveSettings.setText(
            QCoreApplication.translate("Dialog", "Save settings", None)
        )
        self.IncludeUser_Save.setText(
            QCoreApplication.translate("Dialog", "Include user settings", None)
        )
        self.IncludeSystem_Save.setText(
            QCoreApplication.translate("Dialog", "Include system settings", None)
        )
        self.IncludeUser_Restore.setText(
            QCoreApplication.translate("Dialog", "Include user settings", None)
        )
        # if QT_CONFIG(tooltip)
        self.restoreSettings.setToolTip(
            QCoreApplication.translate(
                "Dialog", 'Restore "user.cfg" and "system.cfg" from a backup.', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.restoreSettings.setText(
            QCoreApplication.translate("Dialog", "Restore settings", None)
        )
        self.IncludeSystem_Restore.setText(
            QCoreApplication.translate("Dialog", "Include system settings", None)
        )
        self.IncludeUser_Clear.setText(
            QCoreApplication.translate("Dialog", "Include user settings", None)
        )
        # if QT_CONFIG(tooltip)
        self.clearSettings.setToolTip(
            QCoreApplication.translate(
                "Dialog",
                'Delete "user.cfg" and "system.cfg". FreeCAD creates new files after restart.',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.clearSettings.setText(
            QCoreApplication.translate("Dialog", "Clear settings", None)
        )
        self.IncludeSystem_Clear.setText(
            QCoreApplication.translate("Dialog", "Include system settings", None)
        )
        # if QT_CONFIG(tooltip)
        self.restoreToolbars.setToolTip(
            QCoreApplication.translate(
                "Dialog", "Restores all toolbars for every workbench.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.restoreToolbars.setText(
            QCoreApplication.translate("Dialog", "Restore toolbars", None)
        )
        self.startSafeMode.setText(
            QCoreApplication.translate("Dialog", "Start FreeCAD in safe mode", None)
        )
        self.CloseButton.setText(QCoreApplication.translate("Dialog", "Close", None))
        self.HelpButton.setText(QCoreApplication.translate("Dialog", "Help", None))

    # retranslateUi
