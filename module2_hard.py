import random
question = range(3,21)
q_number = random.choice(question)

print("Число в первой вставке: ", q_number)

def get_num_list(number):
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    return numbers
num_list = get_num_list(q_number)
answer = []
for i in range(1, q_number + 1):
    for j in num_list:
        if q_number % (i + j) == 0 and i < j:
            answer.append(i)
            answer.append(j)
password = str()
for k in answer:
    password += (str(k))
print("Пароль:", password)