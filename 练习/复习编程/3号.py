import sys
try:
    methods = ["GET" , "POST" , "GET" , "PUT" , "GET" , "POST"]
    高危 = ["POST","PUT"]
    if any(ff in methods for ff in 高危):
        print("高危方法存在")
    else:
        print("无高危方法")
    高危_count = sum(1 for ff in methods if ff in 高危)
    print(f"高危方法数量为：{高危_count}")
    可通过 = len(methods) - 高危_count
    print(f"可通过方法数量为：{可通过}")
    print(f"由此得出结论：该方法中存在{高危_count}个高危方法，可通过{可通过}个方法")
    aum = sum(1 for method in methods if method == "GET")
    sum = sum(1 for method in methods if method == "POST")
    xum = len([method for method in methods if method == "PUT"])
    print(f"可通过的类型有：{aum}个方法，不可通过的类型有：{sum}个方法（POST)加{xum}个方法（PUT）")
except ValueError as e:
    print(f"{e}，方法格式错误")






