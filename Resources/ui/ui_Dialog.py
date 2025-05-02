# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_DialogbTWLyO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(419, 377)
        self.gridLayout_6 = QGridLayout(Dialog)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveSettings = QPushButton(self.groupBox)
        self.saveSettings.setObjectName(u"saveSettings")
        self.saveSettings.setMinimumSize(QSize(100, 50))

        self.gridLayout.addWidget(self.saveSettings, 0, 0, 2, 1)

        self.IncludeUser_Save = QCheckBox(self.groupBox)
        self.IncludeUser_Save.setObjectName(u"IncludeUser_Save")
        self.IncludeUser_Save.setChecked(True)

        self.gridLayout.addWidget(self.IncludeUser_Save, 0, 1, 1, 1)

        self.IncludeSystem_Save = QCheckBox(self.groupBox)
        self.IncludeSystem_Save.setObjectName(u"IncludeSystem_Save")
        self.IncludeSystem_Save.setChecked(True)

        self.gridLayout.addWidget(self.IncludeSystem_Save, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox1 = QGroupBox(Dialog)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout_2 = QGridLayout(self.groupBox1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.IncludeUser_Restore = QCheckBox(self.groupBox1)
        self.IncludeUser_Restore.setObjectName(u"IncludeUser_Restore")
        self.IncludeUser_Restore.setChecked(True)

        self.gridLayout_2.addWidget(self.IncludeUser_Restore, 0, 1, 1, 1)

        self.restoreSettings = QPushButton(self.groupBox1)
        self.restoreSettings.setObjectName(u"restoreSettings")
        self.restoreSettings.setMinimumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.restoreSettings, 0, 0, 2, 1)

        self.IncludeSystem_Restore = QCheckBox(self.groupBox1)
        self.IncludeSystem_Restore.setObjectName(u"IncludeSystem_Restore")
        self.IncludeSystem_Restore.setChecked(True)

        self.gridLayout_2.addWidget(self.IncludeSystem_Restore, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox1, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.IncludeUser_Clear = QCheckBox(self.groupBox_2)
        self.IncludeUser_Clear.setObjectName(u"IncludeUser_Clear")
        self.IncludeUser_Clear.setChecked(True)

        self.gridLayout_5.addWidget(self.IncludeUser_Clear, 0, 1, 1, 1)

        self.clearSettings = QPushButton(self.groupBox_2)
        self.clearSettings.setObjectName(u"clearSettings")
        self.clearSettings.setMinimumSize(QSize(100, 50))

        self.gridLayout_5.addWidget(self.clearSettings, 0, 0, 2, 1)

        self.IncludeSystem_Clear = QCheckBox(self.groupBox_2)
        self.IncludeSystem_Clear.setObjectName(u"IncludeSystem_Clear")
        self.IncludeSystem_Clear.setChecked(True)

        self.gridLayout_5.addWidget(self.IncludeSystem_Clear, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox2 = QGroupBox(Dialog)
        self.groupBox2.setObjectName(u"groupBox2")
        self.gridLayout_4 = QGridLayout(self.groupBox2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.restoreToolbars = QPushButton(self.groupBox2)
        self.restoreToolbars.setObjectName(u"restoreToolbars")
        self.restoreToolbars.setMinimumSize(QSize(120, 25))

        self.gridLayout_4.addWidget(self.restoreToolbars, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.StartSafeMode = QPushButton(self.groupBox2)
        self.StartSafeMode.setObjectName(u"StartSafeMode")
        self.StartSafeMode.setMinimumSize(QSize(170, 25))

        self.gridLayout_4.addWidget(self.StartSafeMode, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.CloseButton = QPushButton(Dialog)
        self.CloseButton.setObjectName(u"CloseButton")

        self.gridLayout_3.addWidget(self.CloseButton, 0, 2, 1, 1)

        self.HelpButton = QPushButton(Dialog)
        self.HelpButton.setObjectName(u"HelpButton")

        self.gridLayout_3.addWidget(self.HelpButton, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 5, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.CloseButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Save and restore", None))
#if QT_CONFIG(tooltip)
        self.saveSettings.setToolTip(QCoreApplication.translate("Dialog", u"Save \"user.cfg\" and \"system.cfg\" to a zipfile as backup.", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettings.setText(QCoreApplication.translate("Dialog", u"Save settings", None))
        self.IncludeUser_Save.setText(QCoreApplication.translate("Dialog", u"Include user settings", None))
        self.IncludeSystem_Save.setText(QCoreApplication.translate("Dialog", u"Include system settings", None))
        self.IncludeUser_Restore.setText(QCoreApplication.translate("Dialog", u"Include user settings", None))
#if QT_CONFIG(tooltip)
        self.restoreSettings.setToolTip(QCoreApplication.translate("Dialog", u"Restore \"user.cfg\" and \"system.cfg\" from a backup.", None))
#endif // QT_CONFIG(tooltip)
        self.restoreSettings.setText(QCoreApplication.translate("Dialog", u"Restore settings", None))
        self.IncludeSystem_Restore.setText(QCoreApplication.translate("Dialog", u"Include system settings", None))
        self.IncludeUser_Clear.setText(QCoreApplication.translate("Dialog", u"Include user settings", None))
#if QT_CONFIG(tooltip)
        self.clearSettings.setToolTip(QCoreApplication.translate("Dialog", u"Delete \"user.cfg\" and \"system.cfg\". FreeCAD creates new files after restart.", None))
#endif // QT_CONFIG(tooltip)
        self.clearSettings.setText(QCoreApplication.translate("Dialog", u"Clear settings", None))
        self.IncludeSystem_Clear.setText(QCoreApplication.translate("Dialog", u"Include system settings", None))
#if QT_CONFIG(tooltip)
        self.restoreToolbars.setToolTip(QCoreApplication.translate("Dialog", u"Restores all toolbars for every workbench.", None))
#endif // QT_CONFIG(tooltip)
        self.restoreToolbars.setText(QCoreApplication.translate("Dialog", u"Restore toolbars", None))
        self.StartSafeMode.setText(QCoreApplication.translate("Dialog", u"Start FreeCAD in SafeMode", None))
        self.CloseButton.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.HelpButton.setText(QCoreApplication.translate("Dialog", u"Help", None))
    # retranslateUi

