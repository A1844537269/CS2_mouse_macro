# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KeyEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopWindow(object):
    def setupUi(self, PopWindow):
        PopWindow.setObjectName("PopWindow")
        PopWindow.resize(200, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/GHUB.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PopWindow.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(PopWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(PopWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GunsName = QtWidgets.QComboBox(self.widget_3)
        self.GunsName.setObjectName("GunsName")
        self.horizontalLayout_2.addWidget(self.GunsName)
        self.KeyText = QtWidgets.QLineEdit(self.widget_3)
        self.KeyText.setObjectName("KeyText")
        self.horizontalLayout_2.addWidget(self.KeyText)
        self.OKBtn = QtWidgets.QToolButton(self.widget_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/OK.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OKBtn.setIcon(icon)
        self.OKBtn.setObjectName("OKBtn")
        self.horizontalLayout_2.addWidget(self.OKBtn)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.KeySelectLabel = QtWidgets.QLabel(self.groupBox_4)
        self.KeySelectLabel.setText("")
        self.KeySelectLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.KeySelectLabel.setObjectName("KeySelectLabel")
        self.verticalLayout_3.addWidget(self.KeySelectLabel)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(PopWindow)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveBtn = QtWidgets.QPushButton(self.widget_2)
        self.SaveBtn.setObjectName("SaveBtn")
        self.horizontalLayout.addWidget(self.SaveBtn)
        self.CloseBtn = QtWidgets.QPushButton(self.widget_2)
        self.CloseBtn.setObjectName("CloseBtn")
        self.horizontalLayout.addWidget(self.CloseBtn)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(PopWindow)
        QtCore.QMetaObject.connectSlotsByName(PopWindow)

    def retranslateUi(self, PopWindow):
        _translate = QtCore.QCoreApplication.translate
        PopWindow.setWindowTitle(_translate("PopWindow", "修改按键配置"))
        self.OKBtn.setText(_translate("PopWindow", "..."))
        self.groupBox_4.setTitle(_translate("PopWindow", "可选按键"))
        self.SaveBtn.setText(_translate("PopWindow", "保存"))
        self.CloseBtn.setText(_translate("PopWindow", "取消"))
