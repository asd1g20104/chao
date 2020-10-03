import unittest
from ddt import ddt,data
from chao.work.project.common.do_excel import DoExcel
from chao.work.project.common.http_request import HttpRequest
from chao.work.project.common import project_path
from chao.work.project.common.my_log import MyLog


#测试数据




file_name = project_path.case_path
sheet_name = 'register'
test_data=DoExcel(project_path.case_path,'register').read_data('test_register')
my_log=MyLog()


print(test_data)
@ddt#装饰类
class testCases(unittest.TestCase):

    def setUp(self):
        print('测试开始')#执行用例之前要做的事情放进来


    def tearDown(self):
        print('测试结束')#执行用例之后要做的事情放进来

    #写用例
    @data(*test_data)#装饰用例*号脱外套,把测试数据放进来跑
    def test_cases(self,case):#把每一条用例（字典）存放到case里面

        global TestResult#全局变量
        method = case['Method']
        url = case['Url']
        param =eval(case['Params'])

         # 发起测试
        my_log.info('正在测试{}模块里的第{}条测试用例:{}'.format(case['Module'], case['CaseId'], case['Title']))

        resp = HttpRequest().http_request(method=method,url=url,data=param,cookies=None)#调用这个类来发送请求


        try:#监控断言
            self.assertEqual(eval(case['ExpectedResult']),resp.json())#对比最好用json字典
            TestResult='Pass'
        except Exception as e:#断言错误的话就会处理错误
            TestResult = 'Failed'
            my_log.error('http请求测试用例出错了,错误是:{}'.format(e))

            raise e#抛出异常，不抛出的话用例全是成功，没有失败
        finally:
            t = DoExcel(project_path.case_path, 'test_case')
            t.write_back(file_name,sheet_name,case['CaseId'] + 1, 8, str(resp.json()))
            t.write_back(file_name,sheet_name,case['CaseId'] + 1, 9, TestResult)


            my_log.info('实际结果:{}'.format(resp.json()))  # http发送请求拿到实际返回值

