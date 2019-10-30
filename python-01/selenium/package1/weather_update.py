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
    city_weather_list = weather_city_list.text.split('℃\n')

    # 定义变量保存最低温度与城市
    lowest_weather = ''
    lowest_city = []

    for city_weather in city_weather_list:
        cw_list = city_weather.replace('℃','').split('\n')
        cw_lowest_city = cw_list[0]
        # 字符数组转成int类型
        cw_lowest_weather = min(map(int,cw_list[1].split('/')))

        if lowest_weather == '' or cw_lowest_weather < lowest_weather:
            # 温度相比，保留最低的温度
            lowest_weather = cw_lowest_weather
            lowest_city = [cw_lowest_city]
        elif cw_lowest_weather == lowest_weather:
            # 温度相等，最小温度与当前温度相等，添加城市
            lowest_city.append(cw_lowest_city)

    return f'温度最低为{lowest_weather}℃,城市有：{lowest_city}'

# 调用函数
print(get_minimum_temperature())

# 关闭浏览器
chrome.quit()
