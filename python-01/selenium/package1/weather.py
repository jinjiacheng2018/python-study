'''
    需求： 1.访问天气查询网站：http://www.weather.com.cn/jiangsu/index.shtml
           2.获取江苏所有城市的天气，找出每天最低气温最低的城市，显示出来，如：温度最低为9℃，城市有连云港、盐城
'''

from selenium import webdriver

# 访问天气网站
chrome = webdriver.Chrome(r'E:\Test\Selenimu\BrowserDriver\chromedriver.exe')
url = 'http://www.weather.com.cn/html/province/jiangsu.shtml'
chrome.get(url)


# 获取最低气温的城市
def get_minimum_temperature():
    # 封装数据
    weather_city_list = chrome.find_element_by_class_name('forecastBox')
    dl_list = weather_city_list.find_elements_by_tag_name('dl')
    big_list = []
    for i in range(len(dl_list)):
        text = dl_list[i].text.split('\n')
        small_list = []
        if text is not None:
            small_list.append(text[0])
            split = text[1].replace('℃', '').split('/')
            for j in range(len(split)):
                small_list.append(split[j])
        big_list.append(small_list)

    # 获取最小气温列表
    min_list = []
    for i in range(len(big_list)):
        min_list.append(int(big_list[i][2]))

    # 获取最小的气温
    small_qw = int(min(min_list))
    city_str = ''
    for i in range(len(big_list)):
        if int(big_list[i][2]) == small_qw:
            city_str += big_list[i][0] + " "
    return '温度最低为%d℃,城市有：%s'%(small_qw,city_str)

# 调用函数
print(get_minimum_temperature())

# 关闭浏览器
chrome.quit()
