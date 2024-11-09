number1 = int(input("Введите число 1:"))
number2 = int(input("Введите число 2:"))
number3 = int(input("Введите число 3:"))
if number1 == number2 and number2 == number3:
    print("3 числа равны")
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("2 числа равны")
else:
    print("0 равных чисел")