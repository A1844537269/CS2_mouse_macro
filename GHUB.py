from ctypes import CDLL, c_char_p


# ↓↓↓↓↓↓↓↓↓ 调用ghub键鼠驱动 ↓↓↓↓↓↓↓↓↓
class ghub_device:
    _info = 0
    
    def __init__(self):
        try:
            self.gm = CDLL(r'./_internal/ghub_device.dll')  # ghubdlldir
            self.gm_ok = self.gm.device_open()
            self.gm.key_down.argtypes = [c_char_p]
            self.gm.key_up.argtypes = [c_char_p]
            if not self.gm_ok:
                self._info = 1
        except FileNotFoundError:
            self._info = 2
            self.gm_ok = 0
    
    def _mouse_event(self, fun, *args):
        if self.gm_ok:
            try:
                if hasattr(self.gm, fun):
                    return getattr(self.gm, fun)(*args)
                else:
                    return None
            except (NameError, OSError):
                self.info = '键鼠调用严重错误!!!'
    
    def mouse_R(self, x, y):
        return self._mouse_event('moveR', int(x), int(y))
    
    def mouse_To(self, x, y):
        return self._mouse_event('moveTo', int(x), int(y))
    
    def mouse_down(self, key=1):
        return self._mouse_event('mouse_down', int(key))
    
    def mouse_up(self, key=1):
        return self._mouse_event('mouse_up', int(key))
    
    def scroll(self, num=1):
        return self._mouse_event('scroll', int(num))
    
    def key_down(self, key):
        return self._mouse_event('key_down', key.encode('utf-8'))
    
    def key_up(self, key):
        return self._mouse_event('key_up', key.encode('utf-8'))
    
    def device_close(self):
        return self._mouse_event('device_close')
    
    def get_status(self):
        if self._info == 1:
            info = (False, '未安装ghub或者lgs驱动😱😱😱，请安装后重新启动程序')
        elif self._info == 2:
            info = (False, '重要键鼠文件缺失😨😨😨，请安装后重新启动程序')
        else:
            info = (True, '驱动初始化成功🤗🤗🤗')
        return info
