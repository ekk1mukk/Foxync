# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/qt-designer/foxync-about_modal.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(500, 314)
        self.label = QtWidgets.QLabel(about_window)
        self.label.setGeometry(QtCore.QRect(150, 14, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(about_window)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 261, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(about_window)
        self.label_3.setGeometry(QtCore.QRect(3, 7, 141, 141))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("src/ui/qt-designer/../medias/logo-foxync_no_background.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_version = QtWidgets.QLabel(about_window)
        self.label_version.setGeometry(QtCore.QRect(10, 170, 91, 18))
        self.label_version.setObjectName("label_version")
        self.label_5 = QtWidgets.QLabel(about_window)
        self.label_5.setGeometry(QtCore.QRect(150, 44, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(about_window)
        self.label_6.setGeometry(QtCore.QRect(150, 124, 91, 18))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_commit = QtWidgets.QLabel(about_window)
        self.label_commit.setGeometry(QtCore.QRect(10, 200, 491, 10))
        self.label_commit.setObjectName("label_commit")
        self.label_7 = QtWidgets.QLabel(about_window)
        self.label_7.setGeometry(QtCore.QRect(10, 263, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "Foxync - About"))
        self.label.setText(_translate("about_window", "<html><head/><body><p><span style=\" font-weight:400;\">Foxync</span></p></body></html>"))
        self.label_2.setText(_translate("about_window", "Copyright © Mathias Amato - CFPT - 2024"))
        self.label_version.setText(_translate("about_window", "Version 0.0.1"))
        self.label_5.setText(_translate("about_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Foxync is an open-source file synchronization </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tool using Bittorrent.</p></body></html>"))
        self.label_6.setText(_translate("about_window", "<html><head/><body><p><a href=\"https://gitlab.ictge.ch/mathias-amt/foxync\">Link to Gitlab</a></p></body></html>"))
        self.label_commit.setText(_translate("about_window", "Latest commit : 0"))
        self.label_7.setText(_translate("about_window", "<html><head/><body><p>Icons provided by Freepik, Pixel Perfect, Roundicons, hqrloveq and hadiii</p></body></html>"))
