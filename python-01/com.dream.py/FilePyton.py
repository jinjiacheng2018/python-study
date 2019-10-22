import pprint

# 文件读写
file_object = open(r'D:\MyDocuments\开发细节.txt', encoding='utf-8')
# print(file_object.readlines())
# print(file_object.read().splitlines())

# 读取指定的长度的文件内容，返回字符串类型
# read_str = file_object.read(10)
# print(read_str)

# 读取一行数据,返回字符串数据
# readline_str = file_object.readline()
# print(readline_str)

# 读取多行数据，返回列表类型，每一个元素都会带换行符


# for循环嵌套打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (j, i, i * j), end=" ")
#     print("")
#
# print()
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j <= i:
#             print("%d*%d=%d" % (j, i, i * j), end=" ")
#     print("")


# python排序
sort_list = [10,4,25,6,94,21,5,19]
# 升序，调用sort方法没有返回值
# sort_list.sort()

# 切片法
# list_2 = sort_list[::-1]
# print(sort_list)\

# 排序返还，reverse：True反转，False不反转
print(sorted(sort_list,reverse=False))
