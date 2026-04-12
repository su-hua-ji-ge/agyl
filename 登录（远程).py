logger = logging.getLogger(__name__) #创建日志记录器，__name__是当前模块的名称
import subprocess #导入子进程模块，subprocess模块用于创建子进程，执行外部命令，获取命令输出等
from pathlib import Path #导入路径模块,现代路径操作自动处理～，斜杠兼容
from sys import executable #导入系统模块,获取当前Python解释器的路径,用于安装paramiko库时使用
#import ssl #导入SSL模块,用于加密SSH连接
try:
    import paramiko  # 纯Python代码实现ssh vr协议库
except ImportError:
    print("正在安装 paramiko 库...")
    subprocess.check_call([executable, "-m", "pip", "install", "paramiko"]) 
    #executable:当前Python解释器的路径,用于安装paramiko库,check_call:检查命令是否成功执行
    import paramiko  # 重新导入
import logging #结构化物质代替print环境追踪
#同时也可以设置日志的级别logger.对应的级别后面就是结构了
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(basicConfig:只会在程序开始时运行一次，后面不会再运行无效，除非之前没有调用) :一次性配置，日志系统更新(基本参数)
#level=loging.INFO:设置日志的级别为INFO
#format=(),这是在设置输出的格式
#%(asctime)s - %(levelname)s - %(message)s:分别的意思是日志的发生时间，日志的级别名称，日志的内容
def ssh_execute(host,port=22,username=None,key_file=None,password=None,command="uname -a",timeout=15): #host:目标或主机名,port:SSH端口名
#接下来是创建SSH客户端，使用了paramiko库
    ssh_a = paramiko.SSHClient() #创建SSH客户端对象，
    #paramiko.SSHClient()是paramiko库中的SSH客户端类，用于创建SSH客户端对象
    #这里使用了对应的库，SSHClient是作为建立连接，执行命令等
    ssh_a.set_missing_host_key_policy(paramiko.AutoAddPolicy())#主要作用是连接到一个不在本地文件中的地址是自动接收对方的主机密钥,AutoAddPolicy容易遭受中间人攻击。生产环境使用Reject Policy(纪为拒绝未知主机),并且同时要求用户实现手动添加密钥到known_hosts
        #set_missing_host_key_policy:设置缺失主机密钥策略,这里设置为AutoAddPolicy,即自动接收对方的主机密钥
    try:
        if key_file and Path(key_file).expanduser().exists():#expanduser:展开用户主目录
            #expanduser:展开用户主目录,例如~表示用户主目录
            #Path(key_file) .exists是用来检查该密钥是否存在
            logger.info(f"使用密钥认证连接{host}")
            #进行日志记录(提示),并同时将这个日志设置为info级别
            #接下来的这个就是内容了
            ssh_a.connect( #连接到远程主机
            hostname = host,port=port,username = username,
            key_filename = key_file,timeout=timeout, #
            look_for_keys = False, #禁止自动查找Ssh密钥避免意外使用错误密钥
            allow_agent = False #禁止用ssh代理确保使用指定密钥，以防止进行篡改和窃取机密
            
            )
        elif password: #如果密码密码存在
                logger.warning("密码登录有风险，建议改成ssh密钥")
                ssh_a.connect(hostname = host,port=port,username = username,
            password = password,timeout=timeout,
            look_for_keys = False, #禁止自动查找Ssh密钥避免意外使用错误密钥
            allow_agent = False #禁止用ssh代理确保使用指定密钥，以防止进行篡改和窃取机密
            
            )
        else:
             raise ValueError("密钥或密码不能为空")
             #如果密钥或密码都为空，就抛出异常
             #这里将三个类文件对象返回
        logger.info(f"执行命令{command}")
        #进行日志记录(提示),并同时将这个日志设置为info级别
        stdin,stdout,stderr = ssh_a.exec_command(command,timeout=timeout) #ssh执行命令
                 #大意为在远程主机上执行一个命令,这里command在之前已经被设置了默认的命令
                 #这里此时就是返回等于的那三个类文件对象
                 #即可以写入数据到命令的标准输入,读取命令的标准输入,读取命令的标准错误输入
        exit_code = stdout.channel.recv_exit_status() #stdout.channel:标准输出通道通道对象
                 #这里大意为获取退出码(即读取输出)
                 #channel.recv_exit_status：这个代码用于等待远程命令执行结束并返回命令的推出码状态整数（正确为零，错误为非零）
                 #这里如果exit_code为0，说明命令执行成功，否则说明命令执行失败
        return (stdout.read().decode("utf-8").strip(),stderr.read().decode("utf-8").strip(),exit_code)
                #stdout.read()这里是读取标准输出，decode()：解码为字符串，去掉首尾空格
                 #这里返回的是元组，分别是标准输出，标准错误输出，退出码
    #stdout.read().decode().strip()：这是标准输出，这里是读取标准输出，解码为字符串，去掉首尾空格
    #stderr.read().decode().strip()：这是标准错误输出，这里是读取标准错误输出，解码为字符串，去掉首尾空格
    #exit_code：这是退出码，这里是获取退出码
    except TimeoutError as e:
            logger.error(f"执行命令{command}时超时({timeout}秒):{e}")
            #这里如果执行命令时超时，就返回2,None,None
            #2：这是退出码，表示超时
            #None：这是标准输出，这里是返回None
            #None：这是标准错误输出，这里是返回None
            return (2,None,None)
    except Exception as e:
            logger.error(f"执行命令{command}时出错:{e}")
            #这里如果执行命令时出错，就返回1,None,None
            #1：这是退出码，这里是获取退出码
            #None：这是标准输出，这里是返回None
            #None：这是标准错误输出，这里是返回None
            return (1,None,None)
    finally:
            ssh_a.close()
            logger.info(f"连接已断开{host}")

if __name__ == "__main__":
    result = ssh_execute(
        host="192.0.2.1",
        username="root",
        key_file="~/.ssh/id_rsa",
        command="uname -a"
    )
    print(f"命令执行结果:{result},状态：{result[2]}")