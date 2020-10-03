
import requests
from chao.work.project.common.learn_mysql import Do_Mysql
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


class HttpRequest:
    def http_request(self,method,url,data,cookies):

        if method.upper()=='GET':
            try:
                resp=requests.get(url,data=data,cookies=cookies)
            except Exception as e:
                print('get请求出错:{}'.format(e))

        if method.upper()=='POST':
            try:
                resp=requests.post(url,data=data,cookies=cookies)

            except Exception as e:
                print('post请求出错:{}'.format(e))

        else:
            print('不支持该方式')
            resp=0
        return resp


if __name__ == '__main__':
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    param = {'mobilephone':'18024172723','pwd':'123456'}
    method='POST'
    resp=HttpRequest().http_request(method=method,url=url,data=param,cookies=None)
    print(resp.text)
    print(resp.cookies)

    COOKIES=resp.cookies
    #
    # Url='http://test.lemonban.com/futureloan/mvc/api/loan/add'
    # Param = {'memberId': 1197, 'title': '拿去养蓓蓓', 'amount': 600,
    #          'loanRate': 12, 'loanTerm': 6, 'loanDateType': 4, 'biddingDays': 5,
    #          'repaymemtWay': 4}
    #
    #
    # resp=HttpRequest().http_request(method,Url,data =Param,cookies=COOKIES)
    # print(resp.json())
    #
    # url1='http://test.lemonban.com/futureloan/mvc/api/loan/audit'
    # Param1 = {'id':209154,'status':4}
    # resp1=HttpRequest().http_request(method,url1,data =Param1,cookies=COOKIES)
    # print(resp1.json())
    Param={'memberId': 406687, 'password':123456,'loanId':1198,'amount':200}
    url2='http://test.lemonban.com/futureloan/mvc/api/member/bidLoan'
    resp2=HttpRequest().http_request(method,url2,Param,cookies=COOKIES)
    print(resp2.json())
    money=Do_Mysql().do_mysql('select LeaveAmount from member where mobilephone=18024172723')[0]
    print(money)