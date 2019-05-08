import urllib.request
url= "http://hq.sinajs.cn/list=M0"
request= urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read())