import os #导入os,是用文件系统操作
#（如删除创建重命名权限管理，路径处理等）
from typing import Dict, Any  #从Python的typing 模块中导入Dict和Any类型注解

def safe_delete_temp(file_path:str)-> Dict[str,Any]:
    """
    该函数为安全运维标准函数，作用为安全删除文件
    data:显示错误的文件
    success:False(错误，假)，True(真，正确)
    message:显示错误的原因
    code:显示错误的简称
    """
    #Dict[str, Any] 表示函数返回一个字典，键是字符串（str），值可以是任意类型（Any）。这能让IDE和静态检查工具更好地理解代码。#file_path:str表示
 #def定义函数，file_path是函数形参接受要删除的文件路线
#frg:bool=True(真)时开启测试模式，反之False真实运行
    try:
        if not os.path.isfile(file_path):
              #在，设置结构化字典.要把对与错两种结果或多种结局都写出来
             return{  #条件满足则返回这些字典
                 "success":False,
                  "code":404,
                  "message":"错误，文件不存在",
                  "data":{"file_path":file_path}
                  }
                    
        os.remove(file_path)
        return{
               "success":True,
                "code":200,
                "message":"已删除目标文件",
                "data":{file_path}
        }
    except FileNotFoundError as e:
        return {"success":False,"code":404,"message":f"文件不存在，跳过: {e}","data":{"错误":file_path}}
    except PermissionError as e: #权限不足
        return {
        "success":False,
        "code":403,
        "message":f"权限不足:{e}",
        "data":{"错误":file_path}}
    except Exception as e: #未知错误
        return {
        "success":False,
        "code":500,
        "message":f"未知错误！:{e}"}
    finally:
            print("清理清理流程结束")

# 1. 先创建并写入文件，with语句会确保文件在使用后正确关闭
with open("test.txt", "w",encoding="utf-8") as f:
    f.write("这是一个测试文件")

# 2. 文件已关闭，现在可以安全地删除它
help(safe_delete_temp)
ss = safe_delete_temp("test.txt")
print("返回值:",ss)
