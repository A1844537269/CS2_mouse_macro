import os
import time
from tool import get_guns_data, get_config_data, save_config_data
from GHUB import ghub_device


class ProcessClass:
    _config_data = None
    _ghub_device = ghub_device()
    
    def __init__(self):
        self._config_data = get_config_data()
        self.device_status = self._ghub_device.get_status()
        self.latency = self._config_data.get("latency", 0.8)
        self.Sensitivity = self._config_data.get("sensitivity", 1)
        self.StartFire = False
        self.mouse_one = False
        self.GUN_Name = None
    
    def get_config(self, mode: str):
        """
        获取配置
        :param mode:
            sensitivity:灵敏度
            guns_key_config: 压枪配置
        :return: 配置数据
        """
        return self._config_data[mode]
    
    def update_config(self):
        """
        更新配置
        :return:
        """
        self._config_data = get_config_data()
    
    def save_config(self, mode: int, data):
        """
        保存配置
        :param mode: 1:灵敏度  2: 压枪配置 3:延迟补偿
        :param data: 数据
        :return:
        """
        Old_data = self._config_data
        if mode == 0:
            Old_data["sensitivity"] = data
        elif mode == 1:
            Old_data["guns_key_config"] = data
        elif mode == 2:
            Old_data["latency"] = data
        self._config_data = Old_data
        save_config_data(Old_data)
    
    def Fire(self, emit):
        """
        压枪程序
        :param emit: 回调事件
        :return:
        """
        if not self.GUN_Name:
            return emit('l', ('请先选择武器',))
        file_path = f'./_internal/CS2_DATA/{self.GUN_Name}.json'
        if not os.path.exists(file_path):
            return emit('l', ('枪械数据不存在',))
        emit('l', ("开始压枪",))
        for data in get_guns_data(file_path):
            if not self.mouse_one:
                emit('l', ("停止压枪",))
                break
            self._ghub_device.mouse_R(round(data["x"] * self.Sensitivity), round(data["y"] * self.Sensitivity))
            time.sleep(data['d'] / 1000 * self.latency)
        return
