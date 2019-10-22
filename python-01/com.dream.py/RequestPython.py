import http.client
import json
from pprint import pprint


# 定义函数
def get_response(method, ip, port, header, url, bodyJson):
    """功能：请求接口返回接口响应的json对象"""
    conn = http.client.HTTPConnection(ip, port)
    conn.request(method, url, bodyJson, header)
    response = conn.getresponse()
    result = response.read().decode("utf-8")
    return json.loads(result)

# 函数第一行有注释，打印函数文档
help(get_response)

# 基本url前缀
ip = "118.31.7.33"
port = 8292

# 1.请求登录接口
url = "/iot/opsweb/login"
header = {
    "Content-Type": "application/json"
}
jsonStr = json.dumps({
    "userName": "admin",
    "passWord": "admin"
})
# # 获取连接对象请求得到相应
# conn = http.client.HTTPConnection(ip, port)
# conn.request("POST", url, jsonStr, header)
# response = conn.getresponse()
# result = response.read().decode("utf-8")
# jsonObj = json.loads(result)
# pprint(jsonObj["data"]["token"])
responseJson = get_response("POST", ip, port, header, url, jsonStr)
pprint(responseJson["data"]["token"])

token = ""
if responseJson is None:
    print("登录接口失败，无法获取token...")
else:
    token = responseJson["data"]["token"]

print("= " * 40)

# 获取厂商列表信息
url = "/iot/opsweb/api/company/listCompany"
header = {
    "Content-Type": "application/json",
    "Authorization": token
}
jsonStr = json.dumps({
    "pageNo": "1",
    "pageSize": "5",
    "companyName": ""
})
responseJson = get_response("POST", ip, port, header, url, jsonStr)
pprint(responseJson["data"]["list"])