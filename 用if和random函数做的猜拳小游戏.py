import random

print ("-"*100)

you = int(input("请出拳(剪刀:0)\t\t\t(石头:1)\t\t\t(布:2)\n\n请输入:)"))

computer = random.randint(0,2)

print(f'电脑的出拳是{computer}')

#你胜利的情况
if ((you == 0) and (computer == 2)) or ((you == 1) and (computer == 0)) or ((you == 2) and (computer == 1)):
    print ("-"*70)
    print("you win")   
    print ("-"*70)
#你失败的情况
elif ((you == 1) and (computer == 2))  or  ((you == 0) and (computer) == 1)  or  ((you == 2) and (computer == 0)):
    print ("-"*70)
    print("computer win")
    print ("-"*70)
#平局
else :
    print ("-"*70)
    print("draw")
    print ("-"*70)

print("↓↓↓new game↓↓↓")
print ("-"*100)
