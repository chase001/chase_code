import  requests
import json
import sys
sys.path.append(r'E:\chase_code\ImoocInterface')

# #封装成函数
# url='http://127.0.0.1:8000/login/'
# data={
#  'username':'sun',
#  'password':'123',
#  'data':'test'
# }

url = 'https://m.gearbest.net/community'
data = {
    "group":100,
    "page":1,
    "pageSize":10
}


class RunMain:
    def send_post(self,url,data):
        #post->get就是get接口的，但是上面的测试数据的是post请求，get没有测试
        res=requests.post(url=url,data=data).json()
        #格式化json数据，indent=2是空格，sort是排序
        return json.dumps(res,indent=2,sort_keys=True)

    def send_get(self,url,data):
        #post->get就是get接口的
        res=requests.get(url=url,data=data).json()
        #格式化json数据，indent=2是空格，sort是排序
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        res=None
        if method=='GET':
            res=self.send_get(url,data)
        else:
            res=self.send_post(url,data)
        return res

# a = RunMain().run_main(url,'POST',data)
# print(a)