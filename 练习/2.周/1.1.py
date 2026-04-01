import os
def safe_delete_temp(file_path):
    try:
        os.remove(file_path)
        print(f"已删除文件: {file_path}")
    except FileNotFoundError as e:
        print(f"文件不存在，跳过: {e}")
    except PermissionError as e:
        print(f"拒绝访问: {file_path} (需sudo权限)")
    except Exception as e:
        print(f"删除文件时出错: {e}")
with open("test.txt", "w") as f:
    f.write("这是一个测试文件")
safe_delete_temp("test.txt")