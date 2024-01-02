#   for用来循环可迭代对象，字符串是可迭代的#
#   把可迭代的东西每一项内容拿出来，挨个赋值给变量，每次赋值后都执行一次
#   for循环计数，用range,range(n):从0到n,不包含n
#   range(m,n),从m到n,包含m，不包含n
#   range(m,n,s),从m到n,包含m，不包含n,间隔是s
#   for 变量 in 可迭代的东西：
#       代码
# ----------------------------
# s="乱世小帅天下第一！"
# for c in s:
#     print("大声说！：",c)

#-------------------------range(n)------------
# for age in range(20):
#     print(age)

#--------------range(m,n)--------------
# for age in range(18,30):
#     print(age)

#--------------------------range(m,n,s),输出1,3,5,7,9,11-------
# for age in range(1,12,2):
#     print(age)

#-------------1-2+3-4....-100=?---------
#   奇数相加偶数相减
a=0
for s in range(1,101):
    if s%2==0:
        a=a-s
    else:
        a=a+s
    print(a)

