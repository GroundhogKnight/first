# int：整数
# 整数的数据范围也是无限的，但是可以明确表示
# flot:浮点数
# 小数的数据范围是无限的，有误差
# bool:条件判断，在python中，所有表达空的,都是false(0,"",[])

# ---------基础数据类型转换-------------
# a="123"
# b=0
# print(type(a))
# a=int(a)
# print(type(a))
# a=bool(a)
# b=bool(b)
# print(type(a))
# print(a)
# print(b)

#------------死循环1----------
# while 1: #非0为true
#      print("死循环")

#---------------空字符串为false--------
# s=""
# print(bool(s))

# ------------------
# list=[0]
# print(bool(list))

#----------------------------
while 1:
    content=input("请输入:")
    if content:  #如果content有值
        print(content)
    else:       #如果content没值
        print("什么都没输入")