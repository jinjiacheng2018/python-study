"""
    使用selenium通过ChromeDirver驱动进行Chrome自动化
"""
import time
from selenium import webdriver

# 1.通过路径操作浏览器驱动，以Chrome驱动为例（执行到这一步就会打开浏览器），任务管理器会打开一个Chromedriver应用
webdriver_chrome = webdriver.Chrome(r'E:\Test\Selenimu\BrowserDriver\chromedriver.exe')

# 2.通过驱动对象访问指定的网址（访问百度，搜索松勤）
webdriver_chrome.get('https://w.whaleex.com.cn/')

elements_ant_input = webdriver_chrome.find_element_by_class_name('ant-input') # 币种輸入框
elements_ant_input.send_keys('99.9999')
text = webdriver_chrome.find_element_by_class_name('input-tips').text
assert "最小下单金额为100.00CNY" in text

time.sleep(2)
elements_ant_input.clear()
time.sleep(2)
elements_ant_input.send_keys('111')
elements_ant_input.clear()
time.sleep(2)
elements_ant_input.send_keys('55555555555')


# 4.关闭浏览器
# webdriver_chrome.close()  # 只会关闭窗口,任务管理器不会关闭Chromedriver应用，quit会关掉浏览器，通常用quit
time.sleep(3)
webdriver_chrome.quit()