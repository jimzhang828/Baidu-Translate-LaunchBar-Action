# Baidu Translate LaunchBar Action
>  A LaunchBar Action to translate between Chinese and English via Baidu translation API

1. 首先需要在[百度翻译平台](https://api.fanyi.baidu.com/)注册账号，获取`APP ID`和`密钥`。

```
申请信息
APP ID：2019xxxxxxxxxxxxx
密钥：xxxxxxxxxxxxxxxxxxxx
```

2. 下载这个Action后，进入`Translate.lbaction/Contents/Scripts`，填写`suggestions.py`中的`APP ID`和`密钥`部分。

```
appid = ''  # 填写你的appid
secretKey = ''  # 填写你的密钥
```

3. 安装`Translate.lbaction`，在LaunchBar中输入关键词`TR`即可进行翻译。