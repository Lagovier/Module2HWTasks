def get_num_list(number):
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    return numbers

while True:
    q_number = int(input("Введите число от 3 до 20: "))
    if q_number >= 3 and q_number <= 20:
        num_list = get_num_list(q_number)
        answer = []
        for i in range(1, q_number + 1):
            for j in num_list:
                if q_number % (i + j) == 0 and i < j:
                    answer.append(i)
                    answer.append(j)
        result = str()
        for k in answer:
            result += (str(k))
        print("Пароль:", result)
        continue
    else:
        print("Внимательнее! Введённое число вне заданного диапазона!")
        continue