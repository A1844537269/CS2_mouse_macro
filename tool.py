# -*- coding: utf-8 -*-
"""
@Time : 2024/2/1 3:07
@Author : hsxisawd
@File : tool.py
@Project : Code
@Des: 工具文件
"""
import ujson


def get_config_data():
    """
    读取配置文件数据
    :return: 配置数据 Dict数据
    """
    with open('./_internal/config.json', "r") as Config:
        return ujson.loads(Config.read())  # 使用ujson进行加载


def Read_Info():
    """
    读取通知文件数据，在线编辑器https://uutool.cn/ueditor/
    :return: html格式的数据
    
    """
    with open('_internal/Info.html', 'r', encoding='utf-8') as file:
        return file.read()


def save_config_data(data):
    """
    保存 数据到配置文件
    :param data: 保存数据
    """
    with open('./_internal/config.json', "w") as Config:
        Config.write(ujson.dumps(data))


def get_guns_data(path):
    """
    读取枪械文件数据
    :param path: 文件路径
    :return: 枪械数据 List数据
    """
    with open(path, "r") as Config:
        return ujson.loads(Config.read())


def is_numeric(string):
    """
    判断是否为数字
    :param string: 要判断的数据
    :return: 数字则返回 数字 || 非数字则返回 False
    """
    try:
        if '.' in string:
            return float(string)
        else:
            return int(string)
    except ValueError:
        return False
