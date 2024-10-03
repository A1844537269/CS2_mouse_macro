# -*- coding: utf-8 -*-
"""
@Time : 2024/2/22 0:07
@Author : hsxisawd
@File : CSGOKeyListener.py
@Project : Code
@Des:
"""
from PyQt5.QtCore import QThread, pyqtSignal
from pynput import keyboard
from pynput.keyboard import Key


class AppCSGOKeyListener(QThread):
    keyInfo = pyqtSignal(str, tuple)
    
    def __init__(self, PC):
        super().__init__()
        self.KeyHook = None
        self.PC = PC
    
    def on_key_pressed(self, key):
        Keys = str(key.name if isinstance(key, Key) else key.char)
        keybind = self.get_keys_bind_gun()
        if Keys in '1q':
            self.PC.StartFire = True
            self.keyInfo.emit('r', (self.PC.GUN_Name, self.PC.StartFire))
        elif Keys in keybind:
            self.PC.GUN_Name = keybind[Keys]
            self.PC.StartFire = True
            self.keyInfo.emit('r', (keybind[Keys], self.PC.StartFire))
        
        elif Keys in '234zxc':
            self.PC.StartFire = False
            self.keyInfo.emit('r', (self.PC.GUN_Name, self.PC.StartFire))
        elif Keys == "home":
            self.keyInfo.emit('t', ())
    
    def get_keys_bind_gun(self):
        guns = self.PC.get_config("guns_key_config")
        return {v: k for k, v in guns.items()}
    
    def run(self):
        self.rerun()
    
    def rerun(self):
        self.KeyHook = keyboard.Listener(on_press=self.on_key_pressed)
        self.KeyHook.start()
        self.keyInfo.emit('l', ("键盘监听已启动，等待键盘输入...",))
    
    def stop_listener(self):
        if self.KeyHook:
            self.KeyHook.stop()
            self.KeyHook = None
            self.keyInfo.emit('l', ("键盘监听已停止.....",))
