
import os

#文件的路径 放到这里

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)
#测试用例路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')#路径拼接
print(case_path)

#测试报告的路径
report_path=os.path.join(project_path,'test_result','test_report','test_resport.html')

#日志路径
log_path=os.path.join(project_path,'test_result','test_log','my_log')
print(log_path)

#配置文件路径
conf_path=os.path.join(project_path,'conf','case.conf')
print(conf_path)

