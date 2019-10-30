from selenium import webdriver

# 访问天气网站
chrome = webdriver.Chrome(r'E:\Test\Selenimu\BrowserDriver\chromedriver.exe')
url = 'http://www.weather.com.cn/html/province/jiangsu.shtml'
chrome.get(url)


# 关闭浏览器
chrome.quit()
