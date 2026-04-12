import subprocess
import platform

def linux_a():
    cmd = """
    echo "系统基础信息"
    echo "操作系统类型:"; uname -s
    echo "主机名:"; hostname
    echo "内核版本:"; uname -r
    echo "========== 硬件资源 =========="
    echo "CPU信息:"; lscpu | grep -E "Model name|Socket|Core|Thread"
    echo "内存信息:"; free -h
    echo "磁盘信息:"; df -h

    echo "========== 网络配置 =========="
    ip addr show | grep -E "^[0-9]+:|inet "

    echo "========== 用户和进程信息 =========="
    echo "当前登录用户:"; who
    echo "进程TOP10 (按内存):"; ps aux --sort=-%mem | head -11
    """
    
    #这里分别查看操作系统类型和版本，主机名，内核版本
    try:
        linux9 = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )
        with open("D:/py/linux9存.txt", "w", encoding="utf-8") as f:
            f.write(linux9.stdout)
            print("Linux扫描信息已存入linux9存.txt")
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败:{e}")
        print(f"错误输出:{e.stderr}")

def windows_a():
    cmd = """
    echo "系统基础信息"
    echo "操作系统类型:"; ver
    echo "主机名:"; hostname
    echo "内核版本:"; systeminfo | findstr /C:"OS Version"
    echo ========== 硬件资源 ==========
    echo CPU信息: & wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors
    echo 内存信息: & systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"
    echo 磁盘信息: & wmic logicaldisk where drivetype=3 get deviceid,size,freespace

    echo ========== 网络配置 ==========
    ipconfig | findstr "IPv4 地址"

    echo ========== 用户和进程信息 ==========
    echo 当前登录用户: & query user
    echo 进程TOP10 (按内存): & tasklist /nh /fi "memusage gt 0" | sort /R /+68 | more +3 | findstr /v "==="
    """
    try:
        wiwindows11 = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )
        with open("D:/py/windows11存.txt", "w", encoding="utf-8") as f:
            f.write(wiwindows11.stdout)
            print("Windows扫描信息已存入windows11存.txt")
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败:{e}")
        print(f"错误输出:{e.stderr}")
    

try:
    sysdd = platform.system() #获取操作系统类型
    if sysdd == 'Linux':
        linux_a()
    elif sysdd == 'Windows':
        windows_a()
except Exception as e:
    print({
        "success": False,
        "code": 404,
        "message": f"错误{e}",
    })
finally:
    pass