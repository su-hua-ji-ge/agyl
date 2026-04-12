import  os #使用系统功能
import shutil #导入shut il功能模块这里使用shutil.copy2复制文件并保留元数据
from typing import Dict #这个是从typing 中提取dict

def backup_config(source:str,backup_dir:str) -> Dict:
    #在这里的-> Dict的意思是函数返回值类型为字典
    #source:源配置文件路径，backup_dir:备份目录路径
    if not os.path.isfile(source): #这里是判断原文件是否存在，且为普通文件
        return {  #
            "输出":False,
            "数字":404,
            "状态":"源文件不存在或非普通文件",
            "目标":{"source":source}
        }
    os.makedirs(backup_dir,exist_ok=True)
    #解释为makedirs保存，会创建目录及其所有缺失的父目录,exit_ok=True避免目录已存在时抛出异常，保证代码健壮性
    filename = os.path.basename(source)
    #os.path.basename()提取文件名(从路径中)
    backup_path = os.path.join(backup_dir,filename)
    #这里已经将原来的要求备份的路径和名称拼在一起
    #将备份文件和文件名拼接成完整路径
    #backup_dir为保存的路径
    try:
        shutil.copy2(source,backup_path)
        #可以将原文件复制到目标目录，并尽量保留原来的数据
        #这里如果目标已存在，会直接覆盖
        return {
            "输出":True,
            "数字":200,
            "状态":"备份成功",
            "目标":{"source":source,
                     "backup_path":backup_path
                #这里要输出备份完成之后的名字
                }
        }
    except PermissionError as e: #这里代表如果发现权限不足的话，会收拢到这里，防止程序崩溃
        return {
            "输出":False,
            "数字":403,
            "状态":f"权限不足:{e}",
            "目标":{"source":source,
                    "backup_dir":backup_dir
                }
        }
    except Exception as e: #别的意外的异常将会输出到这里，显示备份失败，同时也要防止程序崩溃
        return  {
            "输出":False,
            "数字":500,
            "状态":f"备份失败:{e}",
            "目标":{"source":source,
                    "backup_dir":backup_dir
                }
        }

if __name__ == "__main__":
    with open("test.txt","w") as f:
        f.write("hello world")
    a = backup_config("test.txt","./backup")
    print(a)