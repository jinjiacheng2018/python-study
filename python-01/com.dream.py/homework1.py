"""
现有一个游戏系统的日志文件，记录内容的字符串的格式,如下所示
A girl come in, the name is Jack, level 955;
其中包含的 the name is 后面会跟着人名，随后紧跟一个逗号， 这是固定的格式。
其它部分可能都是会变化的，比如，可能是下面这些
A old lady come in, the name is Mary, level 94454
A pretty boy come in, the name is Patrick, level 194

请大家实现一个函数，名为getName，如下所示
def getName(srcStr):
    函数体
该函数的参数srcStr 是上面所描述的格式字符串（只处理一行），该函数需要将其中的人名获取出来，并返回
比如 调用 getName('A old lady come in, the name is Mary, level 94454')
返回结果应该是 'Mary'
"""

def get_name(src_str):
    str_list = src_str.split(",")
    print(type(str_list))
    name_str = str_list[1].split(" ")[-1]
    print(type(name_str), name_str)
    return name_str


get_name("A old lady come in, the name is Mary, level 94454")
get_name("A pretty boy come in, the name is Patrick, level 194")
