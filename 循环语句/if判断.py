# -----------------if----------------------
# if 条件：
#     代码
# elif 条件：
#       代码
# else:
#     代码

# a=input("请投入你的金币:")
# a=int(a)
# b="{}个金币买不到熊熊!"
# if a<10:
#     print(b.format(a))
# else:
#     print("你得到了熊熊！")

# ----------------------if嵌套-------------------------------
# a=input("请投入你的金币:")
# a=int(a)
# b="{}个金币不可以哦"
#
# if a>10:
#     if a>100:
#         print("得到熊熊！")
#     else:
#         print("得到花花！")
# else:
#     print(b.format(a))

# ---------------elif--------------------
a=input("请投入你的金币:")
a=float(a)

if a<10:
    print("得到花花！")
elif a<20:
    print("得到熊熊！")
elif a<30:
    print("得到大号熊熊！")
else:
    print("得到全部啦！")
