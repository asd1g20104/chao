from chao.work.project.common.peizhiwenjian import ReadConfig
from chao.work.project.common import project_path
import re
config=ReadConfig(project_path.conf_path)

class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIE=None
    loanid=None
    normal_user=config.get_data('data','normal_user')
    normal_pwd=config.get_data('data','normal_pwd')
    normal_memberid=config.get_data('data','normal_memberid')
    print(normal_pwd)

    def replace(self,target):
        p2 = '#(.*?)#'
        while re.search(p2, target):
            m = re.search(p2, target)
            key = m.group(1)
            value = getattr(GetData, key)
            target = re.sub(p2, value, target, count=1)  # 替换只能替换字符串
        return target

#类属性
#print(GetData.COOKIE)
#print(GetData().COOKIE)

# #利用反射的方法来拿值
# print(getattr(GetData,'COOKIE'))#第一个参数是类名 第二个是参数名，直接取值
# print(hasattr(GetData,'COOKIE'))#返回的是布尔值
# print(setattr(GetData,'COOKIE','123'))#设置你想要的值
#
# print(getattr(GetData,'COOKIE'))
