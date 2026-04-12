import paramiko
import logging
from pathlib import Path
import subprocess
from sys import executable

# 日志配置
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 检查并安装paramiko库
try:
    import paramiko
except ImportError:
    logger.info("正在安装paramiko库...")
    subprocess.check_call([executable, "-m", "pip", "install", "paramiko"])
    import paramiko

def secure_sftp_upload(host, port=22, username=None, key_file=None, password=None, local_path=None, remote_path=None, timeout=30):
    """
    安全上传文件到远程服务器
    """
    # 检查本地路径
    if not local_path:
        logger.error("本地路径不能为空")
        return False
    local_path_obj = Path(local_path).expanduser().resolve()
    if not local_path_obj.exists():
        logger.error(f"本地文件不存在：{local_path_obj}")
        return False

    # 检查远程路径
    if not remote_path:
        logger.error("远程路径不能为空")
        return False

    # 创建SSH客户端
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 认证策略：密钥 > 密码
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

        # 打开SFTP会话
        sftp = ssh.open_sftp()
        
        # 确保远程目录存在
        remote_dir = '/'.join(remote_path.split('/')[:-1])
        if remote_dir:
            try:
                sftp.stat(remote_dir)
            except FileNotFoundError:
                logger.info(f"远程目录 {remote_dir} 不存在，正在创建...")
                sftp.makedirs(remote_dir)

        # 核心上传操作
        logger.info(f"上传中:{local_path_obj} -> {remote_path}")
        sftp.put(str(local_path_obj), remote_path)

        logger.info("上传成功")
        return True
    except Exception as e:
        logger.error(f"错误！{e},上传失败")        
        return False
    finally:
        if 'sftp' in locals():
            sftp.close()
        ssh.close()
        logger.info("SSH连接已关闭")

def ssh_execute(host, port=22, username=None, key_file=None, password=None, command="uname -a", timeout=15):
    """
    安全执行远程命令
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # 认证策略：密钥 > 密码
        if key_file and Path(key_file).expanduser().exists():
            logger.info(f"使用密钥认证连接{host}")
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
            logger.warning("密码登录有风险，建议改成ssh密钥")
            ssh.connect(
                hostname=host, 
                port=port, 
                username=username,
                password=password, 
                timeout=timeout,
                look_for_keys=False,
                allow_agent=False
            )
        else:
            raise ValueError("密钥或密码不能为空")

        logger.info(f"执行命令{command}")
        stdin, stdout, stderr = ssh.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()
        
        return (stdout.read().decode("utf-8").strip(), stderr.read().decode("utf-8").strip(), exit_code)
    except Exception as e:
        logger.error(f"执行命令{command}时出错:{e}")
        return ("", str(e), 1)
    finally:
        ssh.close()
        logger.info(f"连接已断开{host}")

# 部署函数
def safe_deploy(host, local_pkg, remote_pkg, deploy_cmd, **ssh_kwargs):
    """
    安全部署文件到远程服务器
    :param host: 目标服务器IP
    :param local_pkg: 本地要上传的文件或包路径
    :param remote_pkg: 远程文件路径
    :param deploy_cmd: 部署命令
    :param ssh_kwargs: SSH连接参数
    :return: (成功标志, 消息)
    """
    logger.info(f"启动部署：{local_pkg}→{host}:{remote_pkg}")
    
    # 上传文件
    if not secure_sftp_upload(
        host=host,
        local_path=local_pkg,
        remote_path=remote_pkg,
        **ssh_kwargs
    ):
        logger.critical("上传失败!熔断部署流程")
        return False, "UPLOAD_FAILED"
    
    # 执行部署命令
    logger.info(f"执行部署命令：{deploy_cmd}")
    stdout, stderr, code = ssh_execute(
        host=host,
        command=deploy_cmd,
        **ssh_kwargs
    )
    
    # 检查执行结果
    if code == 0 and "OK" in stdout:
        logger.info(f"部署成功 ! 输出摘要:\n{stdout[:100]}")
        return True, stdout
    else:
        logger.error(f"部署异常！| 退出码:{code} | 错误:{stderr[:80]}")
        return False, "DEPLOY_FAILED"

if __name__ == "__main__":
    # 测试部署
    result, message = safe_deploy(
        host="192.168.1.100",
        local_pkg="./test.txt",
        remote_pkg="/tmp/test.txt",
        deploy_cmd="echo 'OK'",
        username="root",
        key_file="~/.ssh/id_rsa"
    )
    
    if result:
        print("部署成功！")
    else:
        print(f"部署失败：{message}")