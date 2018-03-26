
# -*- coding: utf-8 -*-
'''
Created on 2018-03-20

@author: wan qiangxin


'''

import sys
import os
import unittest
import httplib
import time
import hashlib

appkey="2c5d54de"
dev_key = "developer_key"
url = "10.0.2.94"
udid = "101:1234567890"
taskConfig = "task=recognize,intention=weather"
sdkVersion = "8.0.0"
postUrl = "/v2/nlu/recog/cn_common"



class Test(unittest.TestCase):
    def setUp(self):
        print '*********************************************************'
        print 'Start up'
        print '*********************************************************'
        pass

    def tearDown(self):
        print '*********************************************************'
        print 'Tear down'
        print '*********************************************************'
        pass

    def testCase1(self):
        requestDate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        sessionKey =  hashlib.md5(str(requestDate)+dev_key).hexdigest()
        headers = {
            "x-app-key" : appkey,
            "x-task-config" : taskConfig,
            "x-request-date" : requestDate,
            "x-session-key" : sessionKey,
            "x-udid" : udid,
            "x-sdk-version" : sdkVersion
        }
        body = "今天天气怎么样"
        self.post(url, body, headers)

    def post(self, url, body, header):
        httpClient = httplib.HTTPConnection(url+":8880")
        httpClient.request("POST", postUrl, body, header)
        response = httpClient.getresponse()
        responseBody = response.read().decode("utf-8")
        print responseBody

        if httpClient:
            httpClient.close()


if __name__ == "__main__":
#    sys.argv = ['', 'Test.testCase7']
    unittest.main()