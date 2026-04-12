import paramiko
import logging
from pathlib import Path
import subprocess
from sys import executable

#首先，第一步，创建个函数
if not safe_deployA(host,local_pkg,remote_pkg,deploy_cmd,**ssh_kwargs):#这里为基础格式
    #是默认有两个函数吗？（应该是有两个默认函数，直接传到那两个默认函数里）
    #local_pkg:本地要上传的文件或包路径
    #**ssh_kwargs:可变关键字参数 用于传递给默认的函数
    logger.info(f"启动部署：{local_pkg}→{host}:{remote_pkg}")
    if not secure_sftp_upload(
        host=host,
        local_path=local_pkg,
        remote_path=remote_pkg,
        **ssh_kwargs
    ):
         #这里应该是判断是否正常的输入格式
         logger.critical("上传失败!熔断部署流程")
         return False, "UPLOAD_FAILED"
    logger.info(f"执行部署命令：{deploy_cmd}")
    stdout,stderr,code = ssh_execute(
        host=host,
        command=deploy_cmd,  #这里默认执行的命令是?
        **ssh_kwargs
    )#code:是退出码，下面是先确定退出码是否为0（正确）
#然后确定上传操作格式中deploy_cmd位置的执行命令是否正确并返回正确的如："OK"才会通过
    #stdout:为正确输出
    #stderr:为错误输出
if code==0 and "OK" in stdout:
    logger.success(f"部署成功 ! 输出摘要:\n{stdout:[:100]}")
    return True,stdout
else:
    logger.error(f"部署异常！| 退出码:{code} | 错误:{stderr:80}")
    return False, stderr
