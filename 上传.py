import paramiko  # 导入paramiko库，用于SSH连接
import logging
from pathlib import Path  # 安全路径处理（避免字符串拼接风险）
import json
import sys
import subprocess

# 自动安装并导入包
def auto_install_and_import(package_name, import_name=None):
    """
    自动安装并导入包
    :param package_name: pip 包名（如 'paramiko'）
    :param import_name: 导入时的名称（通常与包名相同，可省略）
    """
    if import_name is None:
        import_name = package_name
    try:
        module = __import__(import_name)
        print(f"✅ {package_name} 已可用")
        return module
    except ImportError:
        print(f"⚠️ {package_name} 未安装，正在自动安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"✅ {package_name} 安装成功，重新导入")
        return __import__(import_name)

# 确保paramiko可用
paramiko = auto_install_and_import('paramiko')

# 日志配置：生产级脚本必备
logging.basicConfig( 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'  # 时间+级别+内容
) #配置日志记录器，设置日志级别为INFO，格式为时间+级别+内容
logger = logging.getLogger(__name__) #创建日志记录器，__name__是当前模块的名称


def secure_sftp_upload(host, port=22, username=None, key_file=None, password=None, local_path=None, remote_path=None,
                timeout=30): #格式化输出
    """
    安全上传文件到远程服务器
    :param host: 目标服务器IP（必填）
    :param key_file: 优先使用密钥（~/.ssh/id_rsa），比密码安全100倍
    :param password: 仅测试环境使用（生产环境禁用！）
    :param timeout: 防止脚本卡死（关键！）
    :return: True表示成功，False表示失败
    """
    # ssh = paramiko.SSHClient()
    # ⚠️ 安全警告：AutoAddPolicy仅用于测试！
    # 生产环境应：ssh.load_system_host_keys() + StrictHostKeyChecking
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 这里开始判断本地路径是否格式正确，正常以及判断，远程路径是否正常
    if not local_path:
        logger.error("本地路径不能为空")
        return False
    local_path_obj = Path(local_path).expanduser().resolve()  # 处理～和相对路径,以判断接下来的本地文件路径
    if not local_path_obj.exists():
        logger.error(f"本地文件不存在：{local_path_obj}")
        return False
    #检查远程路径是否正常
    if not remote_path:
        logger.error("远程路径不能为空")
        return False
    # 接下来他说是创建ssh客户端(要解释)
    ssh = paramiko.SSHClient() #创建ssh客户端对象
    # 生产环境应当使用ssh.load_system_host_keys()，这种需要对方提供密钥才能方式
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 检测使用生产环境中，请使用更安全的策略
    try:
        # 🔑 认证策略：密钥 > 密码（安全优先级）
        if key_file and Path(key_file).expanduser().exists():  
            # expanduser处理～和相对路径,resolve()处理符号链接，exists()判断文件是否存在，
            logger.info(f"🔑 使用密钥认证连接 {host}")
            ssh.connect(
                hostname=host,
                port=port,
                username=username,
                key_filename=key_file,
                timeout=timeout,
                look_for_keys=False,  # 禁用自动找密钥（明确指定更安全）
                allow_agent=False  # 禁用SSH代理（避免意外泄露）
            )
        elif password:
            logger.warning(f"⚠️ 密码认证风险高！仅限测试 {host}")
            ssh.connect(
                hostname=host,
                port=port,
                username=username,
                password=password,
                timeout=timeout
            )
        else:
            logger.error("❌ 必须提供密钥文件或密码")
            return False
        # 接下来是打开s FTP会话是什么意思？有啥用？
        sftp = ssh.open_sftp() #打开sftp会话，用于文件传输
        # 确保远程目录存在（可选：自动创建目录）
        remote_dir = '/'.join(remote_path.split('/')[:-1]) #获取远程目录部分.用split('/')将路径按/分割
        #‘/’是路径分隔符，[:-1]是去掉最后一个元素，即文件名，只保留目录部分
        #join是将列表中的元素用指定的分隔符连接起来，这里用/连接目录部分
        #如果remote_dir为空，说明是根目录，直接返回True
        if remote_dir:
            try:
                sftp.stat(remote_dir)  # 检查目录是否存在
            except FileNotFoundError:
                logger.info(f"远程目录 {remote_dir} 不存在，正在创建...")
                sftp.makedirs(remote_dir)  # 递归创建目录
                #mkdirakedirs是递归创建目录，如果目录不存在，会自动创建
        logger.info(f"上传中:{local_path_obj} -> {remote_path}")
        sftp.put(str(local_path_obj), remote_path)  # 核心上传操作
        sftp.chmod(remote_path,0o644)  # 核心上传操作，chmod是修改文件权限，0o644是只读权限
        logger.info(f"上传完成:{local_path_obj} -> {remote_path}")
        return True
    except Exception as e:
        logger.error(f"上传失败：{e}")
        return False
    finally:
        if 'sftp' in locals(): #判断是否有sftp对象
            sftp.close() #关闭sftp会话
        ssh.close()  # 关闭SSH会话


def ssh_execute(host, command, port=22, username=None, key_file=None, password=None, timeout=15):
    """
    在远程服务器上执行命令
    :param host: 目标服务器IP
    :param command: 要执行的命令字符串
    :param port: SSH端口，默认22
    :param username: 登录用户名
    :param key_file: 私钥文件路径（推荐）
    :param password: 密码（仅测试用）
    :param timeout: 命令执行超时（秒）
    :return: (stdout, stderr, exit_code)  # 标准输出、错误输出、退出码
    """
    ssh = paramiko.SSHClient()
    # ⚠️ 安全警告：AutoAddPolicy仅用于测试，生产环境请使用更严格的策略
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 认证连接
        if key_file and Path(key_file).expanduser().exists():
            logger.info(f"🔑 使用密钥认证连接 {host}")
            ssh.connect(
                hostname=host,
                port=port,
                username=username,
                key_filename=key_file,
                timeout=timeout,
                look_for_keys=False,
                allow_agent=False
            )
        elif password:
            logger.warning(f"⚠️ 密码认证连接 {host}（仅测试用）")
            ssh.connect(
                hostname=host,
                port=port,
                username=username,
                password=password,
                timeout=timeout
            )
        else:
            raise ValueError("必须提供密钥文件或密码")

        # 执行命令
        logger.info(f"执行命令: {command} @ {host}")
        stdin, stdout, stderr = ssh.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()  # 获取命令退出码

        # 解码输出
        return (
            stdout.read().decode('utf-8').strip(),
            stderr.read().decode('utf-8').strip(),
            exit_code
        )

    except Exception as e:
        logger.error(f"SSH执行失败: {type(e).__name__} - {str(e)[:100]}")
        return "", str(e), -1  # -1 表示连接或执行级错误

    finally:
        ssh.close()
        logger.debug(f"已断开 {host} 连接")


def safe_deploy(host,local_pkg,remote_pkg,deploy_cmd,**ssh_kwargs):#这里为基础格式
            #是默认有两个函数吗？（应该是有两个默认函数，直接传到那两个默认函数里）
            #local_pkg:本地要上传的文件或包路径
            #**ssh_kwargs:可变关键字参数 用于传递给默认的函数
    logger.info(f"启动部署：{local_pkg}→{host}:{remote_pkg}")
    
    # 上传文件
    if not secure_sftp_upload(
        host=host,
        local_path=local_pkg,
        remote_path=remote_pkg,
        **ssh_kwargs
    ):
#- 传递目标服务器地址 host| - 传递本地文件路径 local_pkg| - 传递远程文件路径 remote_pkg
#传递 SSH 连接参数 **ssh_kwargs （如用户名、密钥文件等），是的没错这就实现了上传文件到远程服务器的功能
        logger.critical("上传失败!熔断部署流程")
        return False, "UPLOAD_FAILED"
    
    # 执行部署命令
    logger.info(f"执行部署命令：{deploy_cmd}")
    stdout, stderr, code = ssh_execute(
        host=host,
        command=deploy_cmd,
        **ssh_kwargs
        )#code:是退出码，下面是先确定退出码是否为0（正确）
        #然后确定上传操作格式中deploy_cmd位置的执行命令是否正确并返回正确的如："OK"才会通过
            #stdout:为正确输出
            #stderr:为错误输出
    if code==0 and "OK" in stdout:
        logger.success(f"部署成功 ! 输出摘要:\n{stdout:[:100]}")
        return True,stdout
    else:
        logger.error(f"部署异常！| 退出码:{code} | 错误:{stderr[:80]}")
        return False, "DEPLOY_FAILED"
            
def deploy_with_Validation(host, local_pkg, remote_pkg, deploy_cmd, verify_cmd, **ssh_kwargs):
    """
    部署三部曲加验证
    :param host: 目标服务器IP
    :param local_pkg: 本地要上传的文件或包路径
    :param remote_pkg: 远程文件路径
    :param deploy_cmd: 部署命令
    :param verify_cmd: 验证命令
    :param ssh_kwargs: SSH连接参数
    :return: 部署结果字典
    """
    # 步骤1: 上传
    if not secure_sftp_upload(
        host=host,
        local_path=local_pkg,
        remote_path=remote_pkg,
        **ssh_kwargs
    ):
        return {"status": "FAIL", "step": "UPLOAD", "msg": "文件传输中断"}
    
    # 步骤2: 执行部署
    _, _, deploy_code = ssh_execute(host, deploy_cmd, **ssh_kwargs)
    if deploy_code != 0:
        return {"status": "FAIL", "step": "DEPLOY", "code": deploy_code, "msg": "部署命令异常"}
    
    # 步骤3: 验证服务状态
    v_out, v_err, v_code = ssh_execute(host, verify_cmd, timeout=10, **ssh_kwargs)
    if v_code == 0 and "OK" in v_out.upper():
        logger.info(f"验证通过,详细：{v_out.strip()}")
        return {
            "status": "SUCCESS", 
            "step": "VERIFY", 
            "service_status": "HEALTHY",
            "raw_output": v_out
        }
    else:
        logger.error(f"验证未通过,详细：{v_out.strip()}")
        return {
            "status": "FAIL", 
            "step": "VERIFY", 
            "service_status": "验证未通过",
            "raw_output": v_out,
            "建议": "检查服务日志或端口监听状态"
        }

def batch_deploy_form_config(config_path="deploy_config.json"): #这里deploy_config.json是默认部署配置文件的路径
    #批量部署函数如果输入没有配置文件路径，默认使用deploy_config.json
    #如果输入了配置文件路径，就使用输入的配置文件路径
    #如果配置文件路径不存在，就报错
    #如果配置文件路径存在，就读取配置文件，解析配置文件，部署配置文件中的所有应用
    
        #这里先用只读方式打开配置文件，然后读取配置文件内容并将文件内容解析（json.loads）为JSON格式给config
    with open(config_path,"r") as f:
        config = json.load(f)
        
    results = {"total":0,"success":0,"fail":0, "detail":{}} #total是总应用数，success是成功应用数，fail是失败应用数
        #因为没有应用部署，所以总应用数为0，成功应用数为0，失败应用数为0、
        #开始部署应用（遍历列表同时取出配置（config(目标)），并记录部署结果用数字success）
    for idx,server in enumerate(config["servers"],1): #idx:是次数,config["servers"]:提前配置的关于servers相关的配置
        #从配置中取出主机IP、用户名、密钥文件、本地包路径、远程包路径、部署命令、验证命令
        host = server["host"]
        username = server["username"]
        key_file = server["key_file"]
        local_pkg = server["local_pkg"]
        remote_pkg = server["remote_pkg"]
        deploy_cmd = server["deploy_cmd"]
        verify_cmd = server["verify_cmd"]
        results["total"] += 1 #总应用数加1
        logger.info(f"开始部署应用{idx}，主机IP：{host}")

        try:
            ssh_kwargs = {
                #这里用.items()方法，将server字典中的键值对，转换为元组，然后用k: v for v,
                #f for v 来判断是否为None，如果是None，就跳过（if v is not None）
                k: v for k, v in {
                    "port": server.get("port", 22), #没有配置端口，默认22
                    "username": server.get("username"), #这里直接从配置文件中取出用户名
                    "key_file": server.get("key_file"),
                    "timeout": 10,
                    "password": server.get("password")
                }.items() if v is not None #排除None值
            }

            #这里直接复用Day4的deploy_with_Validation函数
            res  = deploy_with_Validation(
                host=host,
                local_pkg=local_pkg,
                remote_pkg=remote_pkg,
                deploy_cmd=deploy_cmd,
                verify_cmd=verify_cmd,
                **ssh_kwargs #这里直接用ssh_kwargs，来传递所有参数
            )
            #让后这里先隐藏密码，登录使用密钥文件才安全，密码会暴露在日志中，不安全
            safe_res = {k: v for k, v in res.items() if k != "password"}
            results["detail"][host] = safe_res
            #这里将部署结果记录到results["detail"][host]中，host是主机IP，safe_res是部署结果（safe_res是一个提纯过后的字典）
            #开始判断部署结果是否成功
            if safe_res["status"] == "SUCCESS":
                logger.info(f"成功部署应用{idx}，主机IP：{host}，用户名：{server.get('username')}，密钥文件：{server.get('key_file')}")
                results["success"] += 1 #成功应用数加1
            elif safe_res["status"] == "FAIL":
                logger.error(f"部署应用{idx}，主机IP：{host}，用户名：{server.get('username')}，密钥文件：{server.get('key_file')}，部署失败")
                results["fail"] += 1 #失败应用数加1


        except Exception as e:
            logger.error(f"部署应用{idx}，主机IP：{host}，用户名：{server.get('username')}，密钥文件：{server.get('key_file')}，异常信息：{e}")
            results["fail"] += 1 #失败应用数加1
            continue #跳过当前应用，继续部署下一个应用


if __name__ == "__main__":
    # 调用ssh_execute函数并存储返回值
    upload_success = secure_sftp_upload(
        host="192.168.1.100",
        username="root",
        key_file="/home/user/.ssh/id_rsa",
        local_path="./test.txt",
        remote_path="/tmp/uploaded.txt"
    )
    # 检查返回值
    if upload_success:
        print("文件上传完成")
    else:
        print("文件上传失败，请查看日志")

    deploy_result, deploy_message = safe_deploy(
        host="192.168.1.100",
        local_pkg="./test.txt",
        remote_pkg="/tmp/test.txt",
        deploy_cmd="echo 'OK'",
        username="root",
        key_file="~/.ssh/id_rsa"
    )
    if deploy_result:
        print("部署成功！")
    else:
        print(f"部署失败：{deploy_message}")
