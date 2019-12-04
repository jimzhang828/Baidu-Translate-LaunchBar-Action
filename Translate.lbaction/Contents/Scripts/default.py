#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import urllib
import webbrowser

query = urllib.quote(sys.argv[1])
url = 'https://fanyi.baidu.com/translate?aldtype=16047&smartresult=dict&lang=auto2en&query=' + query
webbrowser.open(url)
