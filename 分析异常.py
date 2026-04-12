
#!/usr/bin/env python3
# ids_analyzer.py - 智能威胁分析引擎（Python版）
# 价值：模式识别 + 风险评分 + 关联分析

import re
import sys
from collections import Counter
from datetime import datetime, timedelta

def analyze_secure_log(hours=1):
    """分析secure日志，识别暴力破解模式"""
    try:
        with open('/var/log/secure', 'r') as f:
            lines = f.readlines()[-500:]  # 仅分析最近500行（性能优化）
    except FileNotFoundError:
        return {"status": "error", "msg": "/var/log/secure not found"}
    
    cutoff = datetime.now() - timedelta(hours=hours)
    attacks = []
    ip_counter = Counter()
    
    for line in lines:
        # 提取时间戳（格式：Jun 25 10:30:45）
        time_match = re.search(r'^(\w{3}\s+\d+\s+\d+:\d+:\d+)', line)
        if not time_match: continue
        
        try:
            log_time = datetime.strptime(f"{datetime.now().year} {time_match.group(1)}", "%Y %b %d %H:%M:%S")
            if log_time < cutoff: continue
        except: continue
        
        # 检测失败登录
        if "Failed password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                ip_counter[ip] += 1
                # 高级特征：检测"无效用户"试探
                if "invalid user" in line.lower():
                    attacks.append({"ip": ip, "type": "user_probing", "time": log_time})
        
        # 检测root登录（高危！）
        elif "Accepted" in line and "for root" in line:
            attacks.append({"ip": re.search(r'from (\d+\.\d+\.\d+\.\d+)', line).group(1), 
                           "type": "root_login", "time": log_time})
    
    # 风险评分（企业级逻辑）
    risk_score = 0
    alerts = []
    
    for ip, count in ip_counter.items():
        if count >= 15:
            risk_score += min(count, 50)  # 每次尝试+1分，上限50
            alerts.append(f"⚠️ 暴力破解: {ip} 尝试{count}次")
    
    for attack in attacks:
        if attack["type"] == "root_login":
            risk_score += 100  # root登录=致命风险
            alerts.append(f"🔥 高危: root从{attack['ip']}登录！")
        elif attack["type"] == "user_probing":
            risk_score += 10
            alerts.append(f"🔍 试探攻击: {attack['ip']} 尝试无效用户")
    
    # 生成报告
    severity = "CRITICAL" if risk_score >= 100 else "HIGH" if risk_score >= 50 else "MEDIUM" if risk_score > 0 else "LOW"
    return {
        "risk_score": risk_score,
        "severity": severity,
        "alerts": alerts if alerts else ["✅ 无异常活动"],
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    result = analyze_secure_log(hours=1)
    print(f"\n🤖 Python智能分析报告 | 风险评分: {result['risk_score']},({result['severity']})")
    for alert in result["alerts"]:
        print(alert)
    sys.exit(0 if result["severity"] == "LOW" else 1)

