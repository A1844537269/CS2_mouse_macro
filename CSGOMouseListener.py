# -*- coding: utf-8 -*-
"""
@Time : 2024/2/22 0:04
@Author : hsxisawd
@File : CSGOMouseListener.py
@Project : Code
@Des:
"""
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QThread
from pynput import mouse


class AppCSGOMouseListener(QThread):
    mouseClicked = pyqtSignal(str, tuple)
    
    def __init__(self, PC):
        super().__init__()
        self.listener = None
        self.data = []
        self.PC = PC
    
    def on_button_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            self.PC.mouse_one = pressed
            if pressed and self.PC.StartFire:
                Thread(target=self.PC.Fire, args=(self.mouseClicked.emit,)).start()
    
    def run(self):
        self.rerun()
    
    def rerun(self):
        self.listener = mouse.Listener(on_click=self.on_button_click)
        self.listener.start()
        self.mouseClicked.emit("l", ("鼠标监听已启动，等待鼠标响应...",))
    
    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
            self.mouseClicked.emit("l", ("鼠标监听已结束...",))
