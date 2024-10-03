# -*- coding: utf-8 -*-
"""
@Time : 2024/2/22 0:21
@Author : hsxisawd
@File : EditKeysLua.py
@Project : Code
@Des:
"""
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.KeyEdit_UI import Ui_PopWindow
from tool import save_config_data, get_config_data


class EditKeys(QWidget, Ui_PopWindow):
    Callback = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        self.Keys = {}
        self.KeysDict = {}
        self.KeysDefault = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '5', '6', '7',
                            '8', '9', '0', '""']
        self.usedKey = []
        self.IFUPDATE = False
        self.OLDKey = ""
        self.initUI()
        self.message_box = QMessageBox()
    
    def initUI(self):
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.CloseBtn.clicked.connect(self.close)
    
    def OpenWindow(self, KeysData):
        self.Keys = KeysData
        self.Init_UI_Keys()
        self.Init_UI_Label()
        self.GunsName.currentTextChanged.connect(self.Change_Keys_Text)
        self.OKBtn.clicked.connect(self.OKBtn_click)
        self.SaveBtn.clicked.connect(self.SaveBtn_click)
        self.show()
    
    def Init_UI_Keys(self):
        """
        初始化 按键配置
        :return:
        """
        self.KeysDict = {}
        self.usedKey = []
        self.GunsName.clear()
        index = 1
        for k, v in self.Keys.items():
            self.GunsName.addItem(k, index)
            self.KeysDict[v] = k
            self.usedKey.append(v)
            if index == 1:
                self.KeyText.setText(v)
                self.OLDKey = v
            index += 1
    
    def Change_Keys_Text(self, value):
        """
        改变 按键配置 对应的按键
        :return:
        """
        key = self.Keys.get(value, '')
        self.KeyText.setText(key)
        self.OLDKey = key
    
    def OKBtn_click(self):
        """
        确定修改单条
        :return:
        """
        key = self.KeyText.text()
        c_Name = self.GunsName.currentText()
        k_Name = self.KeysDict.get(key.lower(), "")
        KeyIndex = self.GunsName.currentIndex()
        if k_Name and c_Name != k_Name:
            self.message_Info(f"该按键已被{k_Name}使用,请先删除原配置", "提示信息")
            self.KeyText.setText(self.OLDKey)
        elif key.lower() not in self.KeysDefault:
            self.message_Info(f"该按键不是有效按键", "提示信息")
            self.KeyText.setText(self.OLDKey)
        else:
            self.Keys[c_Name] = key
            self.Init_UI_Keys()
            self.Init_UI_Label()
            self.IFUPDATE = True
            self.GunsName.setCurrentIndex(KeyIndex)
            self.message_Info(f"{c_Name}修改为{key}！", "提示信息")
    
    def SaveBtn_click(self):
        """
        保存数据
        :return:
        """
        oldData = get_config_data()
        if not self.IFUPDATE:
            self.message_Info(f"没有修改任何数据！", "提示信息")
            self.Callback.emit(False)
            self.close()
            return
        oldData["guns_key_config"] = self.Keys
        save_config_data(oldData)
        self.message_Info(f"保存成功！", "提示信息")
        self.Callback.emit(True)
        self.close()
    
    def Init_UI_Label(self):
        """
        初始化 按键提示
        :return:
        """
        Label = list(set(self.KeysDefault) - set(self.usedKey))
        self.KeySelectLabel.setText(', '.join(Label))
    
    def message_Info(self, message, title="提示信息"):
        """
        消息弹窗
        :param message: 消息
        :param title:  窗口标题
        :return:
        """
        if not self.message_box:
            self.message_box = QMessageBox()
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.setWindowFlags(self.message_box.windowFlags() | Qt.WindowStaysOnTopHint)
        self.message_box.exec()
        self.message_box.close()
