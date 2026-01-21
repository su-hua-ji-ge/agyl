# #列表：格式：列表名 = [元素1，元素2，元素3...](一个列表中的数据类型可以各不相同）
# li = [1,2,3,4,'a','b']
# print(li,type(li))
# #列表也可以切片操作
# print(li[1:3])#列表是可迭代对象，可以for循环遍历取值
# for i in li:
#     print(i)

#5.列表常见操作
# #5.1添加元素
# #append() extend() insert()
# li = ['one','two','three']
# li.append("four")#append可理解为追加,数字无需为字符串''，""
# print(li)
# li.extend('2134')#extend可理解为将要添加的字符串分开一个个添加(数字也要)
# print(li)
# li.insert(0,"five")#insert可以理解为以下标的逻辑在指定位置添加,数字无需为字符串'',""
# print(li)
#5.2修改
#格式：li=[1,2,3]
#  li[被修改值] = '修改后的值'
# li[2] = 'a'
# print(li)

#查找
#in:判断指定元素是否存在，存在：True,不存在：False
#not in: 与之相反
# 格式：print('要查找的值' in li)

#用户输入昵称，不可重复存在
#1.定义一个了列表，保存已经存在的昵称并输入新昵称之后，将新昵称录入列表
# while True:
#     name_list = ['bingtang','aili','maoyuo']
#     li = []
#     name = input('请输入昵称：')
#     if name in name_list:
#         print("您输入的昵称已被占用~，请重新命名呀~")
#     else:
#         print(f"昵称{name}已成功被你占有")
#         li.append(name)
#         a=input("是否继续输入备用昵称：(请输入y或n)")
#         if a == 'y':
#             continue
#         elif a == 'n':
#             print("结束")
#             break
#         else:
#             print("无效请重新输入y或n")

#index:返回指定数据所在位置的下标，如果查找的数据不存在时会包报错
#count:统计指定数据在当前列标表中出现的次数

#删除
#del:格式：del 列表名[下标位置]
#示例：
# li =[1,2,3,4,5,6,]
#del li #删除列表
# del li[4]
# print(li)
#pop:删除指定下标的数据，格式1：li.pop: #默认删除最后一个元素
#格式2：li.pop [下标位置]
#remove:指定元素的值删除
# #例：
# #li = ['one','two','three']
# # li.remove("指定元素的值")#删除没在列表中的元素的值时会报错，以及默认删除第一个出现的指定元素
# # print(li)
#
# #排序
# #sort:列
# # 列表重新排列（正序），默认从小到大
# #reverse:倒序，将列表反过来
# #例：
# #li = [1,2,34,545,12,9]
# # li.sort\reverse()#从小到大（sort识别不了中文）
# # print(li)
#
# #列表推导式
# #格式：[表达式 for 变量 in 列表]
# #in后可放列表、range()、可迭代对象
# #;i =[0,1,2,3,4,5,6,7,8,9,10]
# # #[print(i*5) for i in li] # 前面的是i表达式
# li=[] #创建一个空列表
# # for i in range(1,9): # range：生成一串固定范围的值
# #     li.append(i) # 将for中的被赋予的值i的内容输入到空列表
# # print(li)
# #写列表推导式时要清楚推导式和变量的分别
# #例：
# # 要写入值到一个列表内，核心在li.append(i)。所以它就是表达式
# [li.append(i) for i in range(1,9)] # 后面正常写出要写入的字符串
# print(li)
#
# #格式二:[表达式 for 变量 in 列表 of 条件]#多了一个条件
# li = []
# [li.append(i) for i in range(1,19) if i % 2 == 0]#逻辑推导，先把i元素用append放进表里，i元素做for 循环推出奇数
# print(li)

#5.7 列表嵌套
#[..[..]]
li = [1,2,3,[4,5,6]]
#print(li [3]) #外层列表仍以正常下标，到内列表时作为一个整体输出
print(li[1])
print(li[3][1])#只有第一个（外列表的下标的下一位是内列表的下标时才可以单独输出内列表里的下标（不分内外数））
