a = 0.1579 #attack
d = 0.1579 #defence
pl = 0.1053 #percentage life
pa = 0.1053 #percentage attack
pd = 0.1053 #percentage defence
b = 0.0789 #huixin
bs = 0.0789 #huixinshanghai
yc = 0.1053 #yuansuchongneng
yj = 0.1053 #jingtong

# # 实验
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
count32 = 0
count3 = 0
gailv3 = 0
lst2 = lst1[0:-1:]
for element in lst2:
    chouqu2 = element #chouqu2是第二次抽取的副词条概率
    lst1.remove(chouqu2) #将被抽取的副词条从总的副词条中分离
    count32 += 1
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


# quanbufucitiao1 = {"attack": 1.1579, "defence": 0.1579, "percentage life": 0.1053, "percentage attack": 0.1053,
#                   "percentage defence": 0.1053, "huixin": 0.0789, "huixinshanghai": 0.0789, "yuansuchongneng": 0.1053,
#                   "yuansujingtong": 0.1053}
# for k in quanbufucitiao1:
#     print(quanbufucitiao1[k])
#
# shengyuzhihepingjunliebiao = []
# quanbufucitiao = [a, d, pl, pa, pd, b, bs, yc,yj]
# quanbufucitiao1 = [a, d, pl, pa, pd, b, bs, yc]
#
# for ele in range(0, len(quanbufucitiao1)):
#     beipaichu = quanbufucitiao1[ele]
#     shengyuzhihe = 1-beipaichu
#     # print(shengyuzhihe)
#     shengyuzhihepingjunliebiao.append(shengyuzhihe)
#
# print(shengyuzhihepingjunliebiao)
# #
# xiaogailv = []
# for element in shengyuzhihepingjunliebiao:
#     xiaogailv.append(yj/element)
# print(xiaogailv)
#
# gailv = 0
# for k in range(0, len(xiaogailv)):
#     gailv += xiaogailv[k]
# print("二词条是元素精通:",gailv/8)



# shengyuzhihepingjunliebiao = []
# quanbufucitiao = [a, d, pl, pa, pd, b, bs, yc,yj]
# quanbufucitiao1 = [a, d, pl, pa, pd, b, bs, yc]
# n = 0
# j = 1
# k = 2
# for ele in range(n, len(quanbufucitiao1)-2):
#     # print(quanbufucitiao1[ele], "::")
#     chushi = quanbufucitiao1[ele]
#     for ele2 in range(ele+1, len(quanbufucitiao1)-1):
#         # print(quanbufucitiao1[ele2], ":")
#         chushi2 = quanbufucitiao1[ele2]
#         # print(quanbufucitiao1)
#         # print(quanbufucitiao1)
#         for ele3 in range(ele2+1, len(quanbufucitiao1)):
#             # print(quanbufucitiao1[ele3])
#             chushi3 = quanbufucitiao1[ele3]
#
#             beipaichu = chushi + chushi2 + quanbufucitiao1[ele3]
#             # print(beipaichu)
#             shengyuzhihe = 1-beipaichu
#             # print(shengyuzhihe)
#             shengyuzhihepingjunliebiao.append(shengyuzhihe)
#
# print(shengyuzhihepingjunliebiao)
# xiaogailv = []
# for element in shengyuzhihepingjunliebiao:
#     xiaogailv.append(yj/element)
# print(xiaogailv)
#
# gailv = 0
# for k in range(0, len(xiaogailv)):
#     gailv += xiaogailv[k]
# print("四词条是元素精通:",gailv/56)


# shengyuzhihepingjunliebiao = []
# quanbufucitiao = [a, d, pl, pa, pd, b, bs, yc,yj]
# quanbufucitiao1 = [a, d, pl, pa, pd, b, bs, yc]
# for ele in range(0, len(quanbufucitiao1)-1):
#     n = 0
#     # print(quanbufucitiao1[n], ":")
#     chushi = quanbufucitiao1[n]
#     del quanbufucitiao1[n]
#     for ele2 in range(0, len(quanbufucitiao1)):
#         # print(quanbufucitiao1[ele2])
#         beipaichu = chushi + quanbufucitiao1[ele2]
#         # print(beipaichu)
#         shengyuzhihe = 1-beipaichu
#         # print(shengyuzhihe)
#         shengyuzhihepingjunliebiao.append(shengyuzhihe)
#
# # print(shengyuzhihepingjunliebiao)
#
# xiaogailv = []
# for element in shengyuzhihepingjunliebiao:
#     xiaogailv.append(yj/element)
# print(xiaogailv)
#
# gailv = 0
# for k in range(0, len(xiaogailv)):
#     gailv += xiaogailv[k]
# print("三词条是元素精通:",gailv/28)










# quanbufucitiao1 = [a, d, pl, pa, pd, b, bs, yc, yj]
# i = 0
# n = quanbufucitiao1[i] #n是被删除的元素
# #第一个词条是yj的概率
# percentage1 = yj
# print(percentage1)
#
#
# #第二个词条是yj的概率
# gailv = 0
# percentage2 = 0
# shengyugailvzhihe = 0
#
# i = 0
# while i < 8 :
#     n = quanbufucitiao1[i] #n是被删除的元素
#     del quanbufucitiao[i]
#     for ele in quanbufucitiao:
#         shengyugailvzhihe = shengyugailvzhihe + ele
#     gailv = gailv + n*quanbufucitiao[-1]/shengyugailvzhihe
#     i += 1
# print(gailv)
