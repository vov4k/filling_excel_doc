# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(240, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(240, 200))
        MainWindow.setMaximumSize(QSize(240, 200))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 221, 174))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.settings_file = QPushButton(self.formLayoutWidget)
        self.settings_file.setObjectName(u"settings_file")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.settings_file)

        self.tmplate_file = QPushButton(self.formLayoutWidget)
        self.tmplate_file.setObjectName(u"tmplate_file")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.tmplate_file)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.data_base = QPushButton(self.formLayoutWidget)
        self.data_base.setObjectName(u"data_base")
        self.data_base.setAutoDefault(False)
        self.data_base.setFlat(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.data_base)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.Start = QPushButton(self.formLayoutWidget)
        self.Start.setObjectName(u"Start")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.Start)

        self.progressBar = QProgressBar(self.formLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.progressBar)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.save_dir = QPushButton(self.formLayoutWidget)
        self.save_dir.setObjectName(u"save_dir")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.save_dir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.data_base.setDefault(False)
        self.Start.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
        self.settings_file.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.tmplate_file.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.data_base.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.save_dir.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
    # retranslateUi

