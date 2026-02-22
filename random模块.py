#random，随机模块
import random  #导入random模块
#作用：用于各种分步的伪随机数生成器，可以格局不同的实数来随机生成值
#1，random.random()  产生大于0且小于1的小数
print(random.random())
#2.random.uniform() 生成指定范围的随机小数
print(random.uniform(12,34)) #uniform包含首位的浮点数，包前不包后
#3.random.randint()  随机产生指定范围的整数，包括开头结尾
print(random.randint(33,456)) #包含开头结尾
#4.random.randrange(start()(开始),stop(结束),[step(步长)])  产生start,stop范围内的整数，包含开头不包含结尾
#srep：指定的随机步长，随机指定一个数据(步长表示随机数字的间隔，绝对为指定的步长可以整除的数除了开头)
print(random.randrange(2,44,4))
