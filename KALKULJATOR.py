while True:
    number_1 = float(input("Введите первое число\n"))
    number_2 = float(input("Введите второе число\n"))
    number_3 = 0.0


    action = str(input("Введите действие с числом, либо exit\n"))

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