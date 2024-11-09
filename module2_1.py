num1 = int(input("Введите число 1:"))
num2 = int(input("Введите число 2:"))
num3 = int(input("Введите число 3:"))
if num1 == num2 and num2 == num3:
    print("3 числа равны")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("2 числа равны")
else:
    print("0 равных чисел")