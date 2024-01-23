import re
def has_letters(str_input):
    for simw in str_input:
        if simw.isalpha():
            return True
    return False


while True:
    print("________55___________________________________________")
    print("Введите строку формата: 2/3 или 3+3")
    print("Знаки: + , - , * , / , **")
    razdeliteli = ['/', '+','**','*','-']
    expression = str(input())

    # Проверка на корректность введенной строки
    pattern = re.compile(r'^\d+(\+|\-|\*|\/|\*\*)\d+$')
    if not pattern.match(expression):
        print("Некорректный формат строки. Повторите ввод.")
        continue

    # Проверка на наличие букв
    if has_letters(expression):
        print("Строка содержит буквы. Повторите ввод.")
        continue

    # Остальная часть вашего кода...

    else:
        print("zalup net")
        for razdelitel in razdeliteli:
            if razdelitel in expression:
                expression = expression.split(razdelitel)
                action = razdelitel
    
    
    number_1 = float(expression[0])
    number_2 = float(expression[1])
    number_3 = 0.0

    # print(action)
    # print(expression)
    # print(number_1)
    # print(number_2)

    if action == "exit":
        break

    elif action == "+":
        number_3 = number_1 + number_2
        print(number_1, "+", number_2, "=", number_3) 
        continue
    
    elif action == "-":
        number_3 = number_1 - number_2
        print(number_1, "-", number_2, "=", number_3)
        continue 
        
    elif action == "*":
        number_3 = number_1 * number_2
        print(number_1, "*", number_2, "=", number_3)
        continue

    elif action == "/":
        if number_2 == 0:
            print("На 0 делить нельзя/n")
            continue
                    
        else:
            number_3 = number_1 / number_2
            print(number_1, "/", number_2, "=", number_3)
            continue

    elif action == "**":
        number_3 = number_1 ** number_2
        print(number_1, "**", number_2, "=", number_3)
        continue

    else:
        print("Введенный символ не подходит")
        continue



