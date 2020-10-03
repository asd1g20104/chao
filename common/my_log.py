import logging
from chao.work.project.common import project_path
class MyLog:




    def my_log(self,level,msg):

#日志收集器 root Logger  默认日志收集器 root looger
#日志输出渠道 handlers   控制台 console file txt


#1:定义一个日志收集器并且还要设置级别 getLogger

        my_logger=logging.getLogger('api-log')#定义收集器
        my_logger.setLevel('DEBUG')#收集INFO以上的级别


        #2:指定输出渠道还要设置级别 StreamHandler --控制台 FileHandbler 输出指定文件
        #定义日志的格式
        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(name)s]-日志信息：%(message)s')

        ch=logging.StreamHandler()#控制台
        ch.setLevel('DEBUG')#设置级别
        ch.setFormatter(formatter)#设置格式

        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')#输出到文件里面
        fh.setLevel('DEBUG')#设置级别
        fh.setFormatter(formatter)#设置格式



        #3:对接，输出的是两者的交集

        my_logger.addHandler(ch)#日志收集器收集到的信息要输出到ch里面
        my_logger.addHandler(fh)
        if level=='DEBUG':
            my_logger.debug(msg)
            my_logger.removeHandler(fh)
            my_logger.removeHandler(ch)
        elif level=='INFO':
            my_logger.info(msg)
            my_logger.removeHandler(fh)
            my_logger.removeHandler(ch)#用完一定要记得移除掉（移除的是对接渠道）
        elif level=='ERROR':
            my_logger.error(msg)
            my_logger.removeHandler(fh)
            my_logger.removeHandler(ch)
    def debug(self,msg):
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

if __name__ == '__main__':
    test_logger=MyLog()
    test_logger.debug('炸穿')

    test_logger.error('奔溃')

    test_logger.info('掉线')
