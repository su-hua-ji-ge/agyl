def ip_to_int(ip_str):
    parts = ip_str.split('.') #.split字符串方法，按照指定分隔符切分成列表（便于以后分成32位整数）
    #接下来开始判断用户输入的IP是否符合IP的条件（判断是否为正确的IP）
  # 这个是判断IP是否
  # 为4段条件（以'.'为分割符）
    if len(parts) != 4: #len:返回对象长度，这里也可以返回列表中元素的个数,
        #这里!=代表不等于4，这里判断是否为等于4段IP地址198.168.23.23
        
        raise ValueError("IP地址必须有四段数字组成（用点分隔）") #raise:主动抛出异常，并结束程序进程
    #判断IP内容（是否都为整数（int）和范围），这里嵌套了一个for来判断
    mun_parts = [] #被嵌套的函数组mun_parts地址的4段整数
    for part in parts:
        if not part.isdigit(): #isdigit可以判断是否为全数字的字符串
            raise ValueError(f"IP段{part}包含非数字字符")
        num = int(part) #这里将第一次检查后的值（字符串形态）转化成整数让其可以被以后转化成32位整数
        if num < 0 or num > 255:  #这里开始判断该IP字段内是否有超过255或小于0的值
            raise  ValueError(f"该IP字段{part}内有超过有效范围的值（1 ~ 255包含首尾）")
        mun_parts.append(num) #.append将通过的整数添加到mun_parts
    #接下来开始将mun_parts中的整数转化成32位整数
    return (mun_parts[0] << 24) + (mun_parts[1] << 16) + (mun_parts[2] << 8) + mun_parts[3]
    #return:返回32位整数，这里利用了位运算符（<<）将每个整数左移24位、16位、8位、0位，最后将它们相加
    #这里利用了位运算符的优先级，先左移24位，再左移16位，再左移8位，最后左移0位，最后将它们相加

ip_input = input("请输入目标ip地址（如198.168.1.1）:").strip()#移除用户输入的首尾空格，避免用户输入时首尾有空格导致的错误
try:
    ip_int = ip_to_int(ip_input) #这里将用户输入的IP地址转化成32位整数，，并用ip
#_to_int函数进行转化
    print(ip_int)
except ValueError as e:
        print(f"IP地址转化失败原因：{e}")
        exit()

