# #2.3 字典常见操作2
# dic = {'name':'agyl','age':20}
# print(len(dic))
# ziliao=[2,3,45,6]
# print("您的值还剩余",len(ziliao),"字符")
# #keys():返回字典里面包含的所有键名
# #格式：print(字典名.keys())
# dic = {'name':'agyl','age':20}
# print(dic.keys())
# #方法2
# for i in dic.keys():#使用for循环取出键名
#     print(i)

#values()；返回字典里的所有值
#格式：print(字典名.values())
dic = {'name':'agyl','age':20}
print(dic.values())
#同理也可以用for循环取出值:for i in 字典名.values()

 #items()：返回字典里的所以键值对（以元组形式返回）
# dic = {'name':'agyl','age':20}
# print(dic.items())
# # for i in dic.items():
#     print(i,type(i))

#字典的医用场景
#使用键值对保存描述一个物体的相关信息