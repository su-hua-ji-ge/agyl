# print("Hell World")
#
# a2=23
# a5=565
# print(a2*a5+5)
# # aaa=3
# aab=0.2
# print(aab)
# print(aaa)
# #变量=占位符
# a='agyl'
# print("我的名字：%s" % a)
# mz='agyl'
# a=19
# print("我的名字：%s，年龄：%06d" % (mz,a))
# print(134/5)
# print(3//2)
# print(11%3)
# print(2**3*2+2)
# b=1
# print(b)
# b-=1
# print(b)
# b += 1
# print(2)
# #input(prompt)
# #a=input("你的姓名为：")
# #print("欢迎你%a" % a )
# #print("爱你%a\t\n原宇宙的梦想会成功的" % a )
# # #print("aass\r ssaa")
# age = 17
# if age <18:
#     print("未成年不可上网")
# a = input('请输入成绩：')
# if a > '80':
#     print('你很棒的呀！请维持呀~')
# if a <= '80':
#     print('请加油！不要掉队呀~')
# s =2
# if s == 2 or s == 4:
# #     print("结果")
# # print(not 3>99)
# # a=input("请输入序列号：")
# # b=input("请输入ID：")
# # if a>'10' and b>='34':
# #     print( " 通过 " )
# # else:
# #     print("未通过")
# # a=input("")
# # b=input("")
# # # print("a小于等于b") if a <= b else print("a比b大")
# # if a==2:
# #     print("6")
# # elif b==5:
# #     print("8")
# # elif a>b:
# #     print("9")
# # else:
# #     print("10")
#
# i=1
# s=0
# s1=0
# while i<=100:
#         #写True的话表示条件一直为真没限制条件的话会死循环！False则没有输出还有0
#     s1 += i
#     a=8
#     while a<=100:
#         s += a
#         a += 1
#         # 每次循环的计算结果加与i相加,这里的i代表的是所有打印数据的总和
#     i += 1    # 每循环一次，i的结果加1
# print('',a)
# print('计算结果：', s1)
# a=1
# while a<=100:
#     s += a
#     a += 1
# print('',a)
# str='abcdffg'
# for i in str:
# #     print(i)
# s = 0
# for i in  range(101):
#     s += i #每循环一次结果与i进行相加
# print(s)
# i=1
# while i <= 5:
#     print(f"吃第{i}个苹果")
#     if i==3:
#         print("吃饱")
#         break #没有break的话输出吃饱了之后还好继续循环
#     i += 1
i =1
while i<= 5:
    print(f"啊吃{i}苹果")
    if i==3:
        print(f"第{i}味道与颜色不对，不可吃！")
        i +=1 #在这里必须让计数加1，否则会一直将i的值重复从1-3的循环。（因为continue为直接结束循环没有计数加1的
    # 话会重新循环
        continue
    i += 1
