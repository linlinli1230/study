from appium import webdriver
import unittest
import time
import logging
from HTMLTestRunner import HTMLTestRunner

import os

class set(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '0123456789ABCDEF'
        desired_caps['appPackage'] = 'com.huawei.HwMultiScreenShot'
        desired_caps['appActivity'] = 'com.android.systemui.flashlight.FlashlightActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
    def tearDown(self):
       self.driver.quit()
        
    def testt(self):
        n=0
        flag=True
        while flag:

            print('已经点击了 '+str(2*n)+'次！')
            el1 = self.driver.find_element_by_id("手电筒打开。")
            el1.click()
            time.sleep(1)
            el2 =self. driver.find_element_by_accessibility_id("手电筒关闭。")
            el2.click()
            time.sleep(1)

            n +=1
            if n>5:
                flag=False


if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(set('testt'))
    suite.addTest(set('testcase1'))
    fp=open('E:\\testresult.html','wb')

    runner = HTMLTestRunner(stream=fp,title='testreport:',description='testdiscrebe:')
    runner.run(suite)
    fp.close()  

# if __name__=='__main__':
#          unittest.main()


    
    
   

    
        
        
    
    
