import json
import os


def read_json(filename):
    '''
    :param filename: JSON文件的位置
    :return: 测试用例组成的字典
    '''
    filepath = os.path.join("D:/PyCharm Community Edition 2023.2.2/project/Web-Auto-Testing/data/", filename)
    with open(filepath,"r",encoding="utf-8") as f:
        return json.load(f)