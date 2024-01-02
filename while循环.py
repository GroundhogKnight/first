
# ----------死循环----------
# a=input("输入金币数：")
# a=int(a)
# while a<10:
#     print("金币不足哦")
#     a=a+1

# -----------1+2+3...+100=?___________
# i=input("输入数字：")
# i=int(i)
# s=0
# while i<=100:
#     s=s+i       #累加：s为i的总和
#     i=i+1
#     print(s)

# i        s
# 0        0
# 1        0+1=1
# 2        1+2=3
# 3        3+3=6

# ------------1-2+3-4...-100=?---------

# ---------------continue：停止本次循环，break:停止循环-----------
# while True:
#     content = input("输入金币数：")
#     content = int(content)
#     if content>=10:
#         print(content,"个金币可以买熊熊！")
#     else:
#         print("金币不足哦！")
#         content=10-content
#         b="还差{}个！"
#         print(b.format(content))
#     continue

#------------------------------------1~10，跳过4-------------
i=1
while i<=10:
    if i==4:
        i=i+1
        continue #终止本次循环，继续执行下一次循环，用于排除本次
    print(i)
    i=i+1





