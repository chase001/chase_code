#封装成函数
url='http://127.0.0.1:8000/login/'
data={
 'username':'sun',
 'password':'123',
 'data':'test'
}
def send_post(url,data):
    #post->get就是get接口的，但是上面的测试数据的是post请求，get没有测试
    res=requests.post(url=url,data=data).json()
    #格式化json数据，indent=2是空格，sort是排序
    return json.dumps(res,indent=2,sort_keys=True)
def send_get(url,data):
    #post->get就是get接口的
    res=requests.get(url=url,data=data).json()
    #格式化json数据，indent=2是空格，sort是排序
    return json.dumps(res,indent=2,sort_keys=True)
def run_main(data,url,method):
    res=None
    if method=='GET':
        res=send_get(url,data)
    else:
        res=send_post(url,data)
    return res
def run_main01(url,method,data=None):#默认参数放在最后面的位置
    res = None
    if method == 'GET':
        res = send_get(url, data)
    else:
        res = send_post(url, data)
    return res
# print(send_post(url,data))
# print(run_main(data,url,'POST'))