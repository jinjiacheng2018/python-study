"""
现有一个数据库记录文件（见附件0005_1.txt），保存了学生课程签到的数据库记录。 内容格式如下 ，
('2017-03-13 11:50:09', 271, 131),
('2017-03-14 10:52:19', 273, 131),
('2017-03-13 11:50:19', 271, 126),
每一行记录保存了学生的一次签到信息:每一次签到信息的记录，分为三个部分， 分别是签到时间、签到课程的id号、签到学生的id号,要求大家实现下面的函数。
其中参数fileName为数据库记录文件路径，输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：
    key 是各个学生的id号， value是该学生的签到信息,其中value里面保存着该学生所有签到的信息
    其中每个签到的信息是字典对象，有两个元素： key是lessonid的 记录课程id，key是checkintime的记录签到时间
    比如，对于上面的示例中的3条记录，相应的返回结果如下：
    {
        131: [
            {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
            {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
        ],
        126: [
            {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
        ],
    }
"""

import json


def put_info_to_dict(file_name):
    """函数功能：读取文件的内容清洗数据，得到需要的内容格式"""
    with open(file_name, "r+") as file_info:
        file_info_list = file_info.read().splitlines()

        # 定义外层字典
        big_dic = {}
        for info in file_info_list:
            # 字符串去除无用的字符转化列表
            str_split = info.replace("'", "").replace("\t", "").replace("\n", "") \
                .replace("(", "").replace("),", "").replace(";", "").split(",")

            ci_time = str_split[0].strip()
            lesson_id = int(str_split[1].strip())
            user_id = str_split[2]

            # 如果用户没有该用户存在则添加该用户列表
            if user_id not in big_dic:
                big_dic[user_id] = []

            # 如果存在该用户的信息列表，直接在原有的列表追加数据
            child_json = {'lesson_id': lesson_id, 'checkin_time': ci_time}
            big_dic[user_id].append(child_json)
        return big_dic


# 读取文件信息，使用相对路径，调用函数处理文件信息
file_name = "0005_1.txt"
# file_name = r"D:\\MyWorkspace\Python_Code\python-01\com.dream.py\0005_1.txt"
result_json = put_info_to_dict(file_name)
print(json.dumps(result_json, ensure_ascii=False))

# help(put_info_to_dict)