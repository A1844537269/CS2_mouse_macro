import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from UI.CSGO_UI import Ui_CSGO
from Process import ProcessClass
from tool import is_numeric, Read_Info, get_config_data
from CSGOMouseListener import AppCSGOMouseListener
from CSGOKeyListener import AppCSGOKeyListener
from EditKeys import EditKeys


class AppManager(QWidget, Ui_CSGO):
    def __init__(self):
        super().__init__()
        self.chile_Win = None
        self.isHidden = None
        self.my_key_thread = None
        self.my_mouse_thread = None
        self.pauses = True
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.Init_UI_LOG("程序初始化中.....")
        self.Init_UI_Keys()
        self.Init_UI_Info()
        self.SensitivityText.setText(str(PC.get_config('sensitivity')))
        self.LatencySpinBox.setValue(PC.latency)
        if self.Init_UI_DeviceStatus():
            self.Init_UI_Button(True)
            self.Init_UI_LOG("程序初始化完成.....")
        else:
            self.StartBtn.setEnabled(False)
            self.PauseBtn.setEnabled(False)
            self.Init_UI_Button(False)
            self.Init_UI_LOG("程序初始化失败.....")

    def Init_UI_DeviceStatus(self):
        """
        初始化 驱动状态
        :return:
        """
        Status = PC.device_status
        self.Init_UI_LOG(Status[1])
        return Status[0]

    def Init_UI_Info(self):
        """
        初始化 通知信息
        :return:
        """
        self.Notifications.setText(Read_Info())

    def Init_UI_Keys(self):
        """
        初始化 按键配置
        :return:
        """
        keys = PC.get_config("guns_key_config")
        index = 1
        for k, v in keys.items():
            self.GunName.addItem(k, index)
            if index == 1:
                self.KeysName.setText(v)
            index += 1

    def Change_Keys_Text(self, value):
        """
        改变 按键配置 对应的按键
        :return:
        """
        keys = PC.get_config("guns_key_config")
        self.KeysName.setText(keys[value])

    def Init_UI_Button(self, status):
        """
        初始化 绑定按钮
        :return:
        """
        self.StopBtn.clicked.connect(self.StopRecognition)
        self.GunName.currentTextChanged.connect(self.Change_Keys_Text)
        self.KeyEditBtn.clicked.connect(self.OpenKeyEdit)
        if status:
            self.StartBtn.clicked.connect(self.StartRecognition)
            self.PauseBtn.clicked.connect(self.PauseRecognition)
            self.SensitivityBtn.clicked.connect(self.Save_Sensitivity)
            self.LatencySpinBox.textChanged.connect(self.Save_Latency)

    def OpenKeyEdit(self):
        """
        打开修改配置窗口
        :return:
        """
        keys = PC.get_config("guns_key_config")
        Edit.OpenWindow(keys)

    def StartRecognition(self):
        """
        启动主程序
        :return:
        """
        self.my_key_thread = AppCSGOKeyListener(PC)
        self.my_mouse_thread = AppCSGOMouseListener(PC)
        self.my_key_thread.start()
        self.my_mouse_thread.start()
        self.my_key_thread.keyInfo.connect(self.onKeyPressed)
        self.my_mouse_thread.mouseClicked.connect(self.onKeyPressed)
        self.SetStatus()

    def StopRecognition(self):
        """
        停止程序
        :return:
        """
        if self.my_key_thread and self.my_mouse_thread:
            self.my_key_thread.stop_listener()
            self.my_mouse_thread.stop_listener()
            self.my_mouse_thread.terminate()
            self.my_key_thread.terminate()
        QApplication.quit(5)

    def PauseRecognition(self):
        """
        暂停程序
        :return:
        """
        if self.pauses:
            self.my_key_thread.stop_listener()
            self.my_mouse_thread.stop_listener()
            self.PauseBtn.setText("继续")
            self.KeyEditBtn.setEnabled(True)
            self.Init_UI_LOG('程序暂停中....')
            self.pauses = False
        else:
            self.my_key_thread.rerun()
            self.my_mouse_thread.rerun()
            self.KeyEditBtn.setEnabled(False)
            self.PauseBtn.setText("暂停")
            self.Init_UI_LOG('程序运行中....')
            self.pauses = True

    def Save_Sensitivity(self):
        SensitivityText = self.SensitivityText.text()
        SensitivityText = is_numeric(SensitivityText)
        if not SensitivityText:
            self.message_Info("输入框只能输入数字！！", '警告')
            return
        PC.Sensitivity = SensitivityText
        PC.save_config(0, PC.Sensitivity)
        self.message_Info("保存灵敏度设置成功！！")

    def Save_Latency(self):
        Latency = self.LatencySpinBox.value()
        Latency = float("{:.1f}".format(Latency))
        PC.latency = Latency
        PC.save_config(2, Latency)

    def message_Info(self, message, title="提示信息"):
        """
        消息弹窗
        :param message: 消息
        :param title:  窗口标题
        :return:
        """
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowFlags(message_box.windowFlags() | Qt.WindowStaysOnTopHint)
        message_box.exec()

    def Init_UI_LOG(self, info):
        """
        UI上插入日志输出
        :param info:
        :return:
        """
        self.Info.append(info + "\n")

    def Init_UI_Resolution(self, GunsName, mode=False):
        """
        更新 UI 枪械数据
        :param mode:
            None    则更新开火模式
            非None  则更新枪械名字
        :return:
        """

        self.GunsName.setText(GunsName)
        if mode:
            info = "自动压枪模式"
        else:
            info = "手动压枪模式"
        self.KeyName.setText(info)

    def SetStatus(self):
        """
        设置启动、暂停、退出按钮状态
        :return:
        """
        self.StartBtn.setEnabled(False)
        self.PauseBtn.setEnabled(True)
        self.StopBtn.setEnabled(True)
        self.KeyEditBtn.setEnabled(False)

    def toggle_window(self):
        """
        显示与隐藏UI窗口
        :return:
        """
        if self.isHidden:
            self.show()
            self.isHidden = False
        else:
            self.hide()
            self.isHidden = True

    def Update_UI_keys(self, value):
        if value:
            PC.update_config()
            self.Change_Keys_Text(self.GunName.currentText())

    def onKeyPressed(self, key, value):
        """
        不同事件回调
        :param key:
        :param value:
        :return:
        """
        actions = {
            "l": self.Init_UI_LOG,
            "r": self.Init_UI_Resolution,
            "t": self.toggle_window
        }

        action = actions.get(key, None)
        if action:
            action(*value)


if __name__ == '__main__':
    app = QApplication([])
    PC = ProcessClass()
    Main = AppManager()
    Edit = EditKeys()
    Edit.Callback.connect(Main.Update_UI_keys)
    Main.show()
    sys.exit(app.exec_())
