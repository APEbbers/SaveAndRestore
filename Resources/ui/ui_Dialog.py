# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogWllHrN.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(275, 212)
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveSettings = QPushButton(Dialog)
        self.saveSettings.setObjectName(u"saveSettings")
        self.saveSettings.setMinimumSize(QSize(100, 50))

        self.gridLayout.addWidget(self.saveSettings, 0, 0, 2, 1)

        self.IncludeUser_Save = QCheckBox(Dialog)
        self.IncludeUser_Save.setObjectName(u"IncludeUser_Save")
        self.IncludeUser_Save.setChecked(True)

        self.gridLayout.addWidget(self.IncludeUser_Save, 0, 1, 1, 1)

        self.IncludeSystem_Save = QCheckBox(Dialog)
        self.IncludeSystem_Save.setObjectName(u"IncludeSystem_Save")
        self.IncludeSystem_Save.setChecked(True)

        self.gridLayout.addWidget(self.IncludeSystem_Save, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.IncludeUser_Restore = QCheckBox(Dialog)
        self.IncludeUser_Restore.setObjectName(u"IncludeUser_Restore")
        self.IncludeUser_Restore.setChecked(True)

        self.gridLayout_2.addWidget(self.IncludeUser_Restore, 0, 1, 1, 1)

        self.restoreToolbars = QPushButton(Dialog)
        self.restoreToolbars.setObjectName(u"restoreToolbars")

        self.gridLayout_2.addWidget(self.restoreToolbars, 3, 0, 1, 1)

        self.restoreSettings = QPushButton(Dialog)
        self.restoreSettings.setObjectName(u"restoreSettings")
        self.restoreSettings.setMinimumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.restoreSettings, 0, 0, 2, 1)

        self.IncludeSystem_Restore = QCheckBox(Dialog)
        self.IncludeSystem_Restore.setObjectName(u"IncludeSystem_Restore")
        self.IncludeSystem_Restore.setChecked(True)

        self.gridLayout_2.addWidget(self.IncludeSystem_Restore, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.CloseButton = QPushButton(Dialog)
        self.CloseButton.setObjectName(u"CloseButton")

        self.gridLayout_3.addWidget(self.CloseButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.CloseButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.saveSettings.setText(QCoreApplication.translate("Dialog", u"Save settings", None))
        self.IncludeUser_Save.setText(QCoreApplication.translate("Dialog", u"Include user settings", None))
        self.IncludeSystem_Save.setText(QCoreApplication.translate("Dialog", u"Include system settings", None))
        self.IncludeUser_Restore.setText(QCoreApplication.translate("Dialog", u"Include user settings", None))
        self.restoreToolbars.setText(QCoreApplication.translate("Dialog", u"Restore toolbars", None))
        self.restoreSettings.setText(QCoreApplication.translate("Dialog", u"Restore settings", None))
        self.IncludeSystem_Restore.setText(QCoreApplication.translate("Dialog", u"Include system settings", None))
        self.CloseButton.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

