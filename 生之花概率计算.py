#生之花可能出现的副词条
a = 0.1579 #攻击力小数值
d = 0.1579 #防御力小数值
pl = 0.1053 #生命值百分比
pa = 0.1053 #攻击力百分比
pd = 0.1053 #防御力百分比
b = 0.0789 #暴击率
bs = 0.0789 #暴击伤害
yc = 0.1053 #元素充能
yj = 0.1053 #元素精通

#实验
# count = 0
# lst1 = [a, d, pl, pa, pd, b, bs, yc, yj]
# for i in lst1:
#     lst1.remove(i)
#     lst1.append(i)
#     count+=1
# print(count)

# 第一次选择
lst1 = [a, d, pl, pa, pd, b, bs, yc, yj]
gailv1 = lst1[-1]
print("第一次抽到元素精通的概率是", gailv1)

# 第二次选择
count2 = 0
gailv2 = 0
lst2 = lst1[0:-1:]
for element in lst2:
    chouqu2 = element
    lst1.remove(chouqu2)
    shengyugailv2 = 0
    for element2 in lst1:
        shengyugailv2+=element2 #剩余概率之和
    lst1.append(chouqu2)
    gailv2+=chouqu2*yj/shengyugailv2
    count2+=1
print("第二次抽到元素精通的概率是", gailv2) #运行8次


# 第三次选择
count3 = 0
gailv3 = 0
lst2 = lst1[0:-1:]
for element in lst2:
    chouqu2 = element #chouqu2是第二次抽取的副词条概率
    lst1.remove(chouqu2) #将被抽取的副词条从总的副词条中分离
    for element2 in lst1:
        chouqu3 = element2 #chouqu3是第三次抽取的副词条概率
        lst1.remove(chouqu3)
        shengyugailv3 = 0
        for element3 in lst1:
            shengyugailv3+=element3 #剩余概率之和
        lst1.append(chouqu3)
        gailv3+=chouqu2*chouqu3*yj/shengyugailv3
        count3+=1
    lst1.append(chouqu2) #恢复副词条被第二次抽取时的状态
print("第三次抽到元素精通的概率是", gailv3)
print(count3) #这里循环了64次，但是应该循环56次，不知哪里写错了
