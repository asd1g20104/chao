

import re

from chao.work.project.common.get_data import GetData
#正则表达式的组成，原义字符和元字符
target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
p='normal_user'#原义字符的查找
p2='#(.*?)#'#圆括号代表正则表达式里面组的概念
m = re.search(p2,target)# 在目标字符串里根据正则表达式来查找，有匹配的字符串就返回对象
print(m)
print(m.group())# 不传参的时候返回的表达式是和匹配的字符串一起
print(m.group(1))# 传参就是只返回匹配的字符串，也就是当前组的匹配字符
mm=re.findall(p2,target)# 找到所有的匹配的字符，返回就是一个列表
print(mm)
target2=re.sub(p2,'18024172723',target,count=1)
print(target2)


def replace(target):
    p2 = '#(.*?)#'
    while re.search(p2,target):

        m=re.search(p2,target)
        key=m.group(1)
        value=getattr(GetData,key)
        target=re.sub(p2,value,target,count=1)#替换只能替换字符串
    return target


if __name__ == '__main__':
    target = "{'mobilephone':'#normal_user#','pwd':#normal_pwd#}"
    c=replace(target)
    print(c)

