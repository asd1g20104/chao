# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from mysql import connector
from chao.work.project.common.peizhiwenjian import ReadConfig
from chao.work.project.common import project_path


class Do_Mysql():
    def do_mysql(self,query,flag=1):
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')
        cnn=connector.connect(**db_config)#建立连接
        cursor=cnn.cursor()#第二步，获取游标，获取操作数据库的权限
         #第三步，操作数据表
        cursor.execute(query)

        #打印结果
        if flag==1:
            res=cursor.fetchone()#拿到第一行的数据，返回的是元组
        else:
            res=cursor.fetchall()#拿到所有数据，返回的是列表，嵌套元组
        #光标是会动的，读完一条后读下一条
        print('数据库的查询结果为：{}'.format(res))

        return res

        #增删改 updata，查select
        #cursor.execute('commit')#做增删改操作需要这个提交的步骤
if __name__ == '__main__':

    query='select max(id) from loan where memberid=1197'
    c=Do_Mysql().do_mysql(query=query)
    a=(209078,)
    print(a[0])