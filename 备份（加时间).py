import os
from datetime import datetime #导入datetime模块，用于获取当前时间
from typing import Dict 

def backup_config(source, backup_dir):
    """
    安全备份配置文件（今日练习核心）
    要求：
    1. 校验source存在且为文件
    2. backup_dir不存在则自动创建
    3. 备份名格式: 原文件名_时间戳.bak (例: nginx.conf_20240601_1430.bak)
    4. 用with open安全读写 + 指定encoding
    5. 返回: {"success": bool, "backup_path": str}
    """
    # 1. 路径安全校验（防../攻击）
    # 2. 检查source是否存在
    if not os.path.isfile(source):
        return {"success": False, "backup_path": "", "message": "源文件不存在或非普通文件"}
    
    try:
        # 3. 创建backup_dir
        os.makedirs(backup_dir, exist_ok=True) #如果目录已存在，不会抛出异常
        
        # 4. 生成带时间戳的备份文件名
        name = os.path.basename(source)
        today = datetime.now().strftime("%Y%m%d_%H%M%S") #获取当前时间，格式化为YYYYMMDD_HHMMSS
        #这里是为了在备份文件名中包含时间戳，避免覆盖
        #backup_name为备份文件名，包含时间戳
        backup_name = f"{name}_{today}.bak" #备份文件名格式为 原文件名_时间戳.bak
        #这里是为了在备份文件名中包含时间戳，避免覆盖
        #backup_name为备份文件名，包含时间戳
        backup_path = os.path.join(backup_dir, backup_name) #将备份文件和文件名拼接成完整路径
        
        # 5. 用with open读取source → 写入备份文件
        with open(source, "r", encoding="utf-8") as src:
            content = src.read() #read()方法读取文件内容，返回一个字符串,赋值给content
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(content) #write()方法将字符串写入文件，这里将content写入备份文件
            #f为备份文件对象 content为源文件内容，写入备份文件
        
        # 6. 返回结构化结果
        return {"success": True, "backup_path": backup_path}
        
    except PermissionError as e:
        return {"success": False, "backup_path": "", "message": f"权限不足: {e}"}
    except Exception as e:
        return {"success": False, "backup_path": "", "message": f"备份失败: {e}"}

# 创建测试配置
with open("app.conf", "w", encoding="utf-8") as f:
    f.write("# 安全测试配置\nport=8080\n") #这里w 是写入模式，会覆盖原文件内容

# 执行备份
result = backup_config("app.conf", "backups") #调用备份函数，备份app.conf文件到backups目录
print(f"📌 备份结果: {result}")

# 验证文件存在
if result.get("success") and os.path.exists(result.get("backup_path", "")): 
    #解释为如果备份成功，且备份文件存在 ，则打印备份文件路径
    #os.path.exists()方法判断文件是否存在，返回值为布尔值，True表示存在，False表示不存在
    #result.get("backup_path", "")获取备份文件路径，默认值为空字符串
    #backup_path为备份文件路径
    #result.get方法获取字典中的值，如果键不存在，返回默认值（这里为获取success的值）
    # ，如果键存在，返回对应的值
    print(f"✅ 验证通过: {result['backup_path']}")
else:
    print("❌ 备份失败，请检查")