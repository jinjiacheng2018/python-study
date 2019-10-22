# 字符串格式化
# %s不能联合format使用
# print('my name is %s'.format('Mike'))
# print('my name is %s' %'mike')
#
# print('my name is {}'.format('Mike'))
# print("my name is {}, I'm {} years old.".format('Mike', 5))

# 错误字符串格式化,报错
# print("my name is {}, I'm {} years old.".format(['Mike',5]))

# 可以使用索引，也可以不指定索引，使用{}当做占位符，也可以随便
print("my name is {},I'm {} years old!!!".format('Jack',5))
print("my name is {0},I'm {1} years old!!!".format('Jack',5))
print("my name is {1},I'm {0} years old!!!".format('Jack',5))