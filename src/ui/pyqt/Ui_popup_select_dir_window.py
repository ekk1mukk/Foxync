# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/qt-designer/foxync_popup_select_dir.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_select_dir_window(object):
    def setupUi(self, popup_select_dir_window):
        popup_select_dir_window.setObjectName("popup_select_dir_window")
        popup_select_dir_window.resize(600, 150)
        self.label = QtWidgets.QLabel(popup_select_dir_window)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_save = QtWidgets.QPushButton(popup_select_dir_window)
        self.button_save.setGeometry(QtCore.QRect(465, 100, 121, 34))
        self.button_save.setObjectName("button_save")
        self.textbox_synchronized_directory = QtWidgets.QLineEdit(popup_select_dir_window)
        self.textbox_synchronized_directory.setGeometry(QtCore.QRect(10, 100, 351, 32))
        self.textbox_synchronized_directory.setObjectName("textbox_synchronized_directory")
        self.button_select = QtWidgets.QPushButton(popup_select_dir_window)
        self.button_select.setGeometry(QtCore.QRect(364, 100, 71, 34))
        self.button_select.setObjectName("button_select")
        self.label_wrong = QtWidgets.QLabel(popup_select_dir_window)
        self.label_wrong.setEnabled(True)
        self.label_wrong.setGeometry(QtCore.QRect(11, 75, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_wrong.setFont(font)
        self.label_wrong.setStyleSheet("color: red;")
        self.label_wrong.setWordWrap(False)
        self.label_wrong.setObjectName("label_wrong")

        self.retranslateUi(popup_select_dir_window)
        QtCore.QMetaObject.connectSlotsByName(popup_select_dir_window)

    def retranslateUi(self, popup_select_dir_window):
        _translate = QtCore.QCoreApplication.translate
        popup_select_dir_window.setWindowTitle(_translate("popup_select_dir_window", "First connection on device"))
        self.label.setText(_translate("popup_select_dir_window", "<html><head/><body><p align=\"center\">It appears that it is the first time you\'re connecting on this device. </p><p align=\"center\">Please, choose a directory to synchronize.</p></body></html>"))
        self.button_save.setText(_translate("popup_select_dir_window", "Save"))
        self.button_select.setText(_translate("popup_select_dir_window", "Select"))
        self.label_wrong.setText(_translate("popup_select_dir_window", "Password must have at least 6 characters"))