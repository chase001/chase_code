import unittest
from base.demo import RunMain
import json

class TestMethod(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("类执行之前的方法")
    # @classmethod
    # def tearDownClass(cls):
    #     print("类执行之后的方法")
    def setUp(self):
        print('test ---> setup')
        self.run = RunMain()
    # # def tearDown(self):
    #     print('test -- > tearDown ')

    def test_01(self):
        print("这是第01个测试方法")
        url = 'https://m.gearbest.com/we/feed/group'
        data = {
            "group": 100,
            "page": 1,
            "pageSize": 10
        }
        res = self.run.run_main(url,'POST',data)

        a = 0
        for i in res:
            print(a,res[a])
            a = a + 1

        if res[2] == "SUCCESS":
            print('测试通过')

    # def test_02(self):
    #     #     print("这是第01个测试方法")
    #     #     url = 'https://m.gearbest.com/we/feed/group'
    #     #     data = {
    #     #         "group": 100,
    #     #         "page": 2,
    #     #         "pageSize": 10
    #     #     }
    #     #     res = self.run.run_main(url,'POST',data)
    #     #     print(res)

if __name__ == '__main__':
    unittest.main()