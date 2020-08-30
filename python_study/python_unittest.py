'''
Created on 2020年5月19日

@author: Administrator
'''
import unittest
from test.test_datetime import suit


class Calculator:
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
    #加法
    def add(self):
        return self.a + self.b
    #减法
    def sub(self):
         return self.a - self.b
    #乘法
    def mul(self):
        return self.a * self.b
    #除法
    def div(self):
        return self.a / self.b 

class LeapYear:
    #计算是否为闰年
    def __init__(self,year):
        self.year=int(year)
    def answer(self):
        year=self.year
        if year % 100 ==0:
            if year % 400 ==0:
                #整百年能被400整除的是闰年
                return "{0}是闰年".format(year) 
            else:
                return "{0}不是闰年".format(year) 
        else:
            if year % 4 ==0:
                #非整百年能被4整除的是闰年
                 return "{0}是闰年".format(year) 
            else:
                return "{0}不是闰年".format(year)

class TestCalcuator(unittest.TestCase):
    
    #测试用例前置动作：作用于每条用例的开始和结束之处
    def setUp(self):
        print('开始测试')
        
    #测试用例后置动作：每个用例后都会
    def tearDown(self):
        print('测试结束')
    
    def test_add(self):
        c=Calculator(3,5)
        result=c.add()
        self.assertEqual(result,8)
        
    def test_sub(self):
        c=Calculator(7,2)
        result=c.sub()
        self.assertEqual(result,4)
        
class TestLeapYear(unittest.TestCase):
    
    def test_2000(self):
        ly=LeapYear(2000)
        self.assertEqual(ly.answer(),'2000是闰年')
        
    def test_2001(self):
        ly=LeapYear(2001)
        self.assertEqual(ly.answer(),'2001不是闰年')
        
    def test_2849(self):
        ly=LeapYear(2849)
        self.assertEqual(ly.answer(),'2849是闰年')
if __name__=='__main__':
   
    '''main方法按照两个规则查找所有测试用例并执行，执行顺序和类及方法名称有关'''
    unittest.main() 
   
   #创建测试套件        '''只执行已添加用例且按添加顺序执行'''
    #suit=unittest.TestSuite()
        #增加用例           类名                                    用例名
    #suit.addTest(TestCalcuator("test_add"))
    #suit.addTest(TestCalcuator("test_sub"))
    
    #创建测试运行器
    #runner=unittest.TextTestRunner()
    #runner.run(suit)
    
    
    


