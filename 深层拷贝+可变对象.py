#拷贝分为：（只针对可变对象）
# 浅拷贝：拷贝最外层的对象，内部元素只拷贝了一个引用
# 深拷贝：把对象的深层和浅层的元素都拷贝了一遍
#赋值
li = [1,2,3,4,5]
print(li)
li2 = li #将li赋值给li2
print('li2',li2)
print('li',li)
li.append(9)
print('新增后的li',li)
print('新增后的li2',li2)
#赋值：等于完全共享资源，一个值的变化会完全被另一个值共享

#2.2浅拷贝
#会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
#格式：列表名 = copy.copy(被拷贝的的列表名)
import copy  #导入copy模块#前一个Copy代表模块名，后一个copy代表模块中点函数
li = [1,2,3,4,[23,34,54],5] #定义一个嵌套列表
li2 = copy.copy(li)  #浅拷贝#一个是copy库，一个是copy库里面的copy方法，调用方法要声明库名，第一个模块名，第二个函数名
print('li2',li2)
print('li',li)
print('li内存地址：',id(li)) #查看对象的内存地址可以判断是否为同一个对象
#基本格式：id(列表名)
#当使用了copy模块后输入对应的列表名并输入（append）后不会完全共享资源
li.append(6)
print('li',li)
print('li2',li2)
#这就是浅拷贝
# 向嵌套列表内添加元素
# li[下标].append(要添加的元素)
li[4].append(7)
print('li2',li2)
print('li',li)  #浅拷贝只能拷贝第一层的数据，而嵌套层还是在原来的地址
#使用场景做对象备份，改太多时回去有备份。但太长时可用import copy调出copy备份

#深拷贝：数据完全不共享
#从里到外的元素都拷贝
#格式：列表名 = copy.deepcopy(被拷贝的的列表名)
import copy
li = [1,2,3,4,[23,34,54],5]
li2 = copy.deepcopy(li)
print('li2',li2)
print('li',li)
print('li2',id(li2))
print('li',id(li))
li.append(2)
li[4].append(1)
print('li',li)
print('li2',li2)
print('li的嵌套列表的内存地址',id(li[4])) #查找嵌套列表的内存地址
print('li2的嵌套列表的内存地址',id(li2[4]))

#可变对象：存储空间的数据允许被修改，这种数据就是可变类型
#大致有：list(列表),dict(字典),set(集合)内存地址均不会改变
dic = {'name':'suhuan','age':18}
print(dic,id(dic))
dic['name'] = 'suhuajige' #修改元素可以直接用键名改

set ={1,2,23,9}
print(set,id(set))
set.remove(23) #删除元素
print(set,id(set))

#不可变对象，修改会生成一个新的值（包含新的内存空间）
#常见类型：
# 1.int(整型“1，2)
n=1
print(n,id(n))
n=3
print(n,id(n))#int中改变对象的值会生成新的值，并重新赋值给n
#字符串（str）：同int（整型）
#元组（dict）:本来就不可修改，增加减少且只可查看，只能新定义一个元组（所以内存地址当然不一样）