def ChaoZuoYe(num,*words):
    for word in words:
        ChaoZuoYeCiShu=1
        while ChaoZuoYeCiShu<=num:
            print (word)
            ChaoZuoYeCiShu=ChaoZuoYeCiShu+1
    return print("True")


#print__name__

if __name__ =="__main__":
    words=["guo","ren","zhi"]
    isFinished=ChaoZuoYe(2,*words)
    print ("isFinished")
