# 导入函数
from 自动部署2 import safe_deployA

# 执行部署
result, message = safe_deployA(
    host="目标服务器IP",
    local_pkg="本地文件路径",
    remote_pkg="远程文件路径",
    deploy_cmd="部署命令",
    username="用户名",
    key_file="密钥文件路径"  # 或 password="密码"
)

# 检查部署结果
if result:
    print("部署成功！")
else:
    print(f"部署失败：{message}")