filss = input("输入文件名(使用空格分割)：").split()
#input.split()请输入字符串按空格拆分为列表
#print(files.count(".log"))#它的匹配机器严格只会匹
#配完全相同的:count(所以不可以使用)
ass = sum(1 for file in filss if file.endswith(".log"))
#sum可以计算括号内输出的值累加(统计满足条件的元素数量)
#for file in files遍历files列表的给个元素(for 临时命名 in
#为固定格式)
#if flie.endswith("对应条件")
print(ass)
