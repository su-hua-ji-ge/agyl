password = ["123","admin123","pass","SecurePass9996"]
for index,password in enumerate(password):
    if len(password) >=8:
        print("合格")
    elif len(password) <8:
             print("不合格")
