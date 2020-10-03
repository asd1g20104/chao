

#执行用例 生成测试报告
import unittest
from chao.work.project import HTMLTestRunnerNew #百度一下，下载这个模块

from chao.work.project.test_cases import test_register
from chao.work.project.test_cases import test_recharge
from chao.work.project.test_cases import test_loan

#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_loan))


#执行用例 生成测试报告


with open('test_report.html','wb') as file:

    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='超超自动化测试报告',description='超超自动化测试报告2',tester='超超自动化测试报告3')#此处需要安装东西才行
    runner.run(suite)#执行测试用例,suite是收集到的用例
