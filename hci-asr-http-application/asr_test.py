#coding=utf-8
'''
Created on 2015-4-14

@author: 测试二组

该脚本用来测试发送的请求中HTTP头的各种情况
'''
import sys
import os
import unittest
import time
import json
import httplib
import hashlib
#import xml.etree.ElementTree as Etree
import random

appkey="2c5d54de"
dev_key = "developer_key"
url = "10.0.2.94"
sdk_version = "5.0"
udid = "101:1234567890"
tid = "49652372"
eid = "42072569"
capkey = "asr.cloud.freetalk"
#config = "capkey=asr.cloud.freetalk,audioformat=pcm8k16bit,modeltype=8k,identify=testAsr_Freetalk_case2426"
#config = "capkey=asr.cloud.freetalk,audioformat=pcm16k16bit"
#config = "addpunc=no,audioformat=speex,candnum=10,capkey=asr.cloud.dialog,context=yes,dialogmode=freetalk,identify=1134551,index=1,intention=tvChannels;videoControl;deviceControl;video;,needcontent=no,nettimeout=4,orderby=intention,realtime=yes,resver=2,vadhead=10000,vadmode=engine,vadseg=500,vadswitch=yes,vadtail=0,vadthreshold=20"
config = "addpunc=no,audioformat=pcm16k16bit,candnum=10,capkey=asr.cloud.dialog,context=yes,context_len=0,dialogmode=freetalk,identify=66660,index=-19,intention=weather;joke;calendar;deviceControl;tvChannels;video;videoControl,needcontent=yes,nettimeout=4,orderby=intention,realtime=yes,resver=2,vadhead=10000,vadmode=engine,vadseg=500,vadswitch=no,vadtail=0,vadthreshold=100,vadtime=405954"
#postUrl = "/v2/asr/freetalk/chinese_16k_common"
postUrl = "/asr/recognise"
body =  open("./res/sinovoice.pcm","rb").read()


class Test(unittest.TestCase):
    def setUp(self):
        print '**************************************************'
        print 'Start UP Test'
        pass

    def tearDown(self):
        print '**************************************************'
        print 'Tear Down Test'
        pass
    
    #########http头的功能用例#########
    #2.1测试HTTP头中x-app参数
    #2.1.1检测HTTP头中的x-app参数为正确的情况
    #2.2.1测试HTTP头中的x-sdk参数为8.0的情况
    #2.3.1测试HTTP头中的x-date参数传入格式如2014-6-18 10:10:11的情况
    #2.5.1测试HTTP头中的x-sess的值为正确的情况
    #2.6.1测试HTTP头中的x-udid的值为正确的情况
    #2.7.1测试HTTP头中的x-tid的值为开发手册提供值的情况
    #2.8.1测试HTTP头中的x-eid的值为开发手册提供值的情况
    def testCase1(self):
        import sys
        print sys.getdefaultencoding()
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        print "testCase1    2.1.1 检测HTTP头中的x-app参数为正确的情况"
        #time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准
        #time.time()：返回当前时间的时间戳
        #time.strftime(format[, t])： 把一个代表时间的元组或者struct_time（如由time.localtime()返回）转化为格式化的时间字符串。 
        request_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        identify = str(random.randint(1,20000))
        task_config = config + ",identify="+identify
        session_key = hashlib.md5(str(request_date)+dev_key).hexdigest()

        headers = {
                   "x-app-key" :appkey,
                   "x-sdk-version" : 5.0,
                   "x-request-date": request_date,
                   "x-task-config" : task_config,
                   "x-udid" : "101:1234567890",
                   "x-session-key" :  session_key
                    }
        print headers
        self.post(url,body,headers)
        
     ###### post http消息    ###############  
    def post(self,url,body,header):
        httpClient = httplib.HTTPConnection(url+":8880")
#        test=str(body)
#        httpClient.request("POST", postUrl, test.encode('utf-8'), header)
        httpClient.request("POST", postUrl, body, header)

        response = httpClient.getresponse()
        response_body = response.read().decode("utf-8")
        print response_body
#         print "---------------------------------"
        if httpClient:
            httpClient.close()

            
if __name__ == "__main__":
#    sys.argv = ['', 'Test.testCase7']
    unittest.main()
