import os
import hashlib
from collections import defaultdict

def get_file_hash(file_path):
    """计算文件的MD5哈希值"""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            # 分块读取文件以处理大文件
            for byte_block in iter(lambda: f.read(4096), b''):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return None

def find_duplicate_files(directory):
    """查找目录下的重复文件"""
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在")
        return
    
    # 存储文件哈希值和对应的文件路径
    hash_to_files = defaultdict(list)
    
    # 遍历目录及其子目录
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = get_file_hash(file_path)
            if file_hash:
                hash_to_files[file_hash].append(file_path)
    
    # 找出重复的文件
    duplicates = {hash_val: files for hash_val, files in hash_to_files.items() if len(files) > 1}
    
    # 输出重复文件信息
    if duplicates:
        print("找到以下重复文件:")
        print("-" * 80)
        for hash_val, files in duplicates.items():
            print(f"哈希值: {hash_val}")
            print("重复文件:")
            for file_path in files:
                print(f"  - {file_path}")
            print("-" * 80)
    else:
        print("未找到重复文件")

if __name__ == "__main__":
    # 示例用法：检查当前目录
    current_dir = os.getcwd()
    print(f"正在检查目录: {current_dir}")
    find_duplicate_files(current_dir)
    
    # 或者指定其他目录
    # target_dir = "D:\\资料"
    # find_duplicate_files(target_dir)
