# 1.字符串格式化
# ------------我叫xxx,我住xxx,我今年xxx岁,我喜欢xxxxx----
# name = input("请输入名字:")
# address = input("请输入住址:")
# age = int(input("请输入年龄:"))
# hobby = input("请输入你喜欢的选手:")

# %s 字符串占位,整数,小数都可以
# %d 占位整数数字 %f 占位小数
# s="我叫%s,我住%s,我今年%d岁,我喜欢%s" % (name,address,age,hobby)
# print(s)
# 上面这个的简化版
# s1 = "我叫{},我住{},我今年{}岁,我喜欢{}".format(name,address,age,hobby)
# print(s1)
# f-string
# s2 = f"我叫{name},我叫{name},我叫{name},我叫{name},我今年{age}岁,我叫{name},"
# print(s2)

# 2.字符串的索引和切片
# 索引:按照位置提取元素
# s="大陆赛区的美丽传说"
# print(s[3])
#  print(s[-1]) #倒数
# 切片:从一个字符串中提前一部分
# s="乱世小帅天下第一!"
# print(s[3:6])  #3开始,6结束,左闭右开
# print(s[:5])
# print(s[2:])
# print(s[:])
# print(s[-3:-1])# 还是左闭右开,目前只能从左往右切,输出为:第一
# print(s[-1:-4])# 错误代码,因为是从前往后取,[-1,-4]是从后往前
# 添加步长控制切片方向
# s="87好帅我好爱~"
# print(s[:4:-1]) #-最后一位为-1:从右到左;在最后一位默认为1,从左到右
# print(s[:8:2])  # 最后一位是2:每间隔一个元素选取一个,输出:8好我爱
# print(s[-1:-8:-2]) # 因为从后往前取,所以可以[-1:-10]

# 3.字符串常规操作
# 字符串操作不会对原字符串产生影响,会产生新的字符串
# 3.1字符串大小写转换(*upper:转成大写)
# s="python is cold"
# s1=s.capitalize()   #capitalize()首字母变成大写
# print(s1)

# s="caption we are win"
# s1=s.title()      #title()每个单词首字母变成大写
# print(s1)

# s="I LOVE LUAN SHI XIAO SHUAI"
# s1=s.lower()      #lower()变成小写
# print(s1)

# s="i love luan shi xiao shuai"
# **s1=s.upper()      #upper()变成大写
# print(s1)

# ---------如何让忽略大小写?-----------
# code ="xAda"
# while 1:
#     user_input = input(f"请输入验证码({code}):")
#     if code.upper()==user_input.upper():
#      print("验证正确!!!!")
#     else:
#      print("验证失败")


# 3.2 字符串替换与切割
# s="   乱世  小帅天下第一!   "
# s1=s.strip()    #strip():去掉前后空格
# print(s1)
# 案例
while 1:
    username = input("输入用户名:")
    if username == "admin":
        password = input("输入密码:")
        if password == 123456:
            print("成功")
        else:
            print("密码错误")
    else:
        print("用户名错误")
