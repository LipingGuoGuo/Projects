# coding = utf-8
import configparser

class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        '''
        :param file_name: 配置文件地址
        :param node: 节点名称
        '''
        if file_name == None:
            # 默认地址
            file_name = "F:/Projects/zhizhu/Active_account/config/LocalElement.ini"
        else:
            self.file_name = file_name
        if node == None:
            # 默认节点
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        # 创建管理对象
        cf = configparser.ConfigParser()
        # 读取ini文件
        cf.read(file_name)
        return cf

    # 获取value值
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data

if __name__ == "__main__":
    # 默认配置文件地址、节点
    read_init = ReadIni()
    # 传入key值，获取value值
    print(read_init.get_value("knowledge_number"))