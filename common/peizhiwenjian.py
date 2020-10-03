# -*- coding: utf-8 -*-
from configparser import ConfigParser
from chao.work.project.common import project_path
#创建对象:

class ReadConfig:
    global value
    def __init__(self,file_name):
        self.cf=ConfigParser()
        try:
            self.cf.read(file_name,encoding='utf-8')

        except Exception as e:
            print('文件打开报错:{}'.format(e))


        #cf=ConfigParser()
        #第一步：打开文件 read()
        #cf.read(file_name,encoding='utf-8')
        #第二步：读取内容 section option
        #res=cf.get('StudentName','stu_1')
        #res=cf['CASE']['case_id']
        #res=cf.getfloat('StudentName','stu_1')getint getboolean等等能拿到不同的数据类型
        #print(res)
        #通过配置文件读取出来的全部都是字符串
        #print(type(eval(res)))#eval()--把括号的里面的数据变成原本的数据类型

    def get_str(self, section, option):
        '''从配置文件中获取一个字符串'''
        try:
            value = self.cf.str(section, option)  # section option
        except Exception as e:
            print('取值报错:{}'.format(e))

        return value

    def get_data(self,section,option):
        '''从配置文件中获取一个元组 字典 列表等数据类型的数据'''
        try:
            value=self.cf.get(section,option)#section option
        except Exception as e:
            print('取值报错:{}'.format(e))

        return eval(value)
if __name__ == '__main__':
    res=ReadConfig(project_path.conf_path).str_data('data','normal_memberid')
    print(res)