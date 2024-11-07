inputNumber = input("Tell me a number:")

try:
    inputNumber = float(inputNumber)
    imputNumber = inputNumber / 0 #故意制造除0错误，练习try except语法
except ValueError:
    print("It is not a number...")
except Exception as e:
    print("Exception here")
    print("e")
finally:
    print("Double value is {0}.".format(inputNumber * 3))
