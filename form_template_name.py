# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_choose_template_name.ui'
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


class Ui_name_template(object):
    def setupUi(self, name_template):
        if not name_template.objectName():
            name_template.setObjectName(u"name_template")
        name_template.resize(390, 272)
        self.splitter = QSplitter(name_template)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(11, 11, 369, 251))
        self.splitter.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.listWidget = QListWidget(self.splitter)
        self.listWidget.setObjectName(u"listWidget")
        self.splitter.addWidget(self.listWidget)
        self.template_of_file_name = QLineEdit(self.splitter)
        self.template_of_file_name.setObjectName(u"template_of_file_name")
        self.template_of_file_name.setClearButtonEnabled(False)
        self.splitter.addWidget(self.template_of_file_name)
        self.buttonBox = QDialogButtonBox(self.splitter)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.splitter.addWidget(self.buttonBox)

        self.retranslateUi(name_template)
        self.buttonBox.accepted.connect(name_template.accept)
        self.buttonBox.rejected.connect(name_template.reject)

        QMetaObject.connectSlotsByName(name_template)
    # setupUi

    def retranslateUi(self, name_template):
        name_template.setWindowTitle(QCoreApplication.translate("name_template", u"\u0428\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("name_template", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u041d\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0446\u0438\u0444\u0440\u044b \u0432 \u0448\u0430\u0431\u043b\u043e\u043d\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u0430</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.template_of_file_name.setToolTip(QCoreApplication.translate("name_template", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u0448\u0430\u0431\u043b\u043e\u043d \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0432\u044b\u0448\u0435 (\u0434\u0432\u043e\u0439\u043d\u043e\u0439 \u0449\u0435\u043b\u0447\u043e\u043a), \u043e\u043d\u0438 \u0431\u0443\u0434\u0443\u0442 \u0437\u0430\u043c\u0435\u043d\u0435\u043d"
                        "\u044b \u043d\u0430 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0411\u0414</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.template_of_file_name.setInputMask("")
        self.template_of_file_name.setPlaceholderText(QCoreApplication.translate("name_template", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u0430", None))
    # retranslateUi

