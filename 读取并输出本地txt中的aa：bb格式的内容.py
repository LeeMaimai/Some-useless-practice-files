# def bruteFTPLogin(hostname,passwordFile):
    
#     p = open(passwordFile,'r')
#     print("Now trying bruteforce ataack...")
    
#     for line in p.readlines():
#         print(line)

#         userName = line.split(":")[0]
#         passWord = line.split(":")[1]
        
#         print("Trying:\t" + userName + "/" + passWord)
#         print("ftpcrackProcess")


# if __name__=="__main__":
    
#     host = "127.0.0.1"
#     passwordFile = "c:\\testpwd.txt"
#     bruteFTPLogin(host,passwordFile)

def bruteFTPLogin(hostname,passwordFile):
    p = open(passwordFile,'r')
    print("Now trying bruteforce ataack...")
    for line in p.readlines():
        print(line)
        lineParts=line.split(":")
        username=lineParts[0]
        password=lineParts[1]
        print("Trying:\t" + username + "/" +password)
        print("ftp_crack_Process")

if __name__=="__main__":
    host = "127.0.0.1"
    passwordFile = "C:\\testpwd.txt"
    bruteFTPLogin(host,passwordFile)
