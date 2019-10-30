"""
    使用selenium通过ChromeDirver驱动进行Chrome自动化
"""
import time
from selenium import webdriver

# 1.通过路径操作浏览器驱动，以Chrome驱动为例（执行到这一步就会打开浏览器），任务管理器会打开一个Chromedriver应用
webdriver_chrome = webdriver.Chrome(r'E:\Test\Selenimu\BrowserDriver\chromedriver.exe')

# 2.通过驱动对象访问指定的网址（访问百度，搜索松勤）
webdriver_chrome.get('https://www.baidu.com/')

elements_kw = webdriver_chrome.find_element_by_id('kw') # 百度一下输入框元素
elements_kw.send_keys('松勤') # 输入框输入内容，'松勤\n'相当于按enter键，就不需要点击按钮
webdriver_chrome.find_element_by_id('su').click() # 百度一下按钮

# 3.判断第一行是否包含‘松勤网 - 松勤软件测试’,注意页面跳转需要时间加载，所以立马获取元素可能会报错，需要等待
time.sleep(2)
text = webdriver_chrome.find_element_by_id('1').text

# 使用逻辑判断
# if '松勤网 - 松勤软件测试' in text:
#     print('pass')
# else:
#     print('fail')

# 使用断言代替逻辑判断
assert '松勤网 - 松勤软件测试' in text

# 4.关闭浏览器
# webdriver_chrome.close()  # 只会关闭窗口,任务管理器不会关闭Chromedriver应用，quit会关掉浏览器，通常用quit
webdriver_chrome.quit()