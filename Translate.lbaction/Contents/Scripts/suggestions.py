#!/usr/bin/env python
# coding=utf-8
#
# LaunchBar Action Script
#
import sys
import json
import http.client
import md5
import urllib
import random
import re

appid = ''  # 填写你的appid
secretKey = ''  # 填写你的密钥
salt = str(random.randint(32768, 65536))
query = sys.argv[1] # query
sign = appid + query + salt + secretKey  # calculate the signature
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()

def is_contains_chinese(s):
    for ch in s:
        if u'\u4e00' <= ch <= u'\u9fa5':
            return True
    return False

from_lang = 'auto'  #原文语种
to_lang = 'zh'      #译文语种
if is_contains_chinese(query.decode('utf-8')):  # 如果包含中文，就翻译成英文
    to_lang = 'en'

# 拼接query url
url = '/api/trans/vip/translate'
url += '?appid=' + appid + '&q=' + urllib.quote(query)
url += '&from=' + from_lang + '&to=' + to_lang 
url += '&salt=' + salt + '&sign=' + sign

items = []
if len(query) > 0:
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read()
        # result_all = response.read().encode('utf-8')
        result = json.loads(result_all)
        trans_result = result['trans_result']
        for r in trans_result:
            items.append({'title': r['dst']})
    except Exception as e:
        items.append({'title': str(e)})
    finally:
        if httpClient:
            httpClient.close()

print json.dumps(items)
