# coding:utf-8
from __future__ import print_function

# 使用while循环打印九九乘法表
i = 1
while i <= 9 :
    j = 1
    while j <= i :
        print("%d*%d=%d "%(j,i,j*i),end="")
        j += 1
    print("")
    i += 1
