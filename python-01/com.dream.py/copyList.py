import copy

# 直接赋值
aList = [10,20,[100,200]]
bList = aList

# 改变原列表的外层列表，赋值的列表内层列表同步变化
aList.append(30)
print(aList)    # 10, 20, [100, 200], 30]
print(bList)    # 10, 20, [100, 200], 30]

# 改变原列表的内层列表，赋值的列表内层列表同步变化
aList[2].append(300)
print(aList)    # [10, 20, [100, 200, 300], 30]
print(bList)    # [10, 20, [100, 200, 300], 30]

'''
# 浅拷贝
aList = [10,20,[100,200]]
bList = copy.copy(aList)

# 改变原列表的外层列表，浅拷贝的列表外列表不受影响
aList.append(30)
print(aList)    # [10, 20, [100, 200], 30]
print(bList)    # [10, 20, [100, 200]]

# 改变原列表的内层列表，浅拷贝的列表内层列表同步变化
aList[2].append(300)
print(aList)    # [10, 20, [100, 200, 300], 30]
print(bList)    # [10, 20, [100, 200, 300]]
'''

'''
# 深拷贝
aList = [10,20,[100,200]]
bList = copy.deepcopy(aList)

# 改变原列表的外层列表，深拷贝的列表外列表不受影响
aList.append(30)
print(aList)    # [10, 20, [100, 200], 30]
print(bList)    # [10, 20, [100, 200]]

# 改变原列表的内层列表，深拷贝的列表内层列表不受影响
aList[2].append(300)
print(aList)    # [10, 20, [100, 200, 300], 30]
print(bList)    # [10, 20, [100, 200]]
'''

