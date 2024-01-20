while True:
    print("___________________________________________________")
    print("Введите строку формата ((число)(знак)(число)): 2/3")
    print("Знаки: + , - , * , / , **")

    expression = str(input())
    razdeliteli = ['/', '+','**','*','-']
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