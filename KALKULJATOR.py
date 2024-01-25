import re
import math

while True:
    print("**************************************************************************")
    print("* Введите строку формата: 2/3 или 3+3                                   **")
    print("* Знаки: + , - , * , / , **, %                                          **")
    print("* Введите строку формата: log10 или sin45                               **")
    print("* Знаки: log, sin, cos, tan, ctg, sqrt, arcsin, arccos, arctan, arcctan **")
    print("**************************************************************************")
    
    razdeliteli = ['/', '+','**','*','-','%','log','sin','cos','tan','ctg','sqrt','arcsin','arccos','arctan','arcctan']
    expression = str(input())
    if expression == "exit":
        break

    pattern = re.compile(r'^\b(sin|cos|tan|ctg|log|sqrt|arcsin|arccos|arctan|arcctan)\d+|\d+(\+|\-|\'|\*|\/|\*\*|\%)\d+$')
    if not pattern.match(expression):
        print("Некорректный формат строки. Повторите ввод.")
        continue

    else:
        for razdelitel in razdeliteli:
            if razdelitel in expression:
                expression = expression.split(razdelitel)
                action = razdelitel
            

    if expression[0].isdigit():
        number_1 = float(expression[0])

    if expression[1].isdigit():
        number_2 = float(expression[1])

    else:
        print("error")
    number_3 = 0.0


    
    if action == 'sin':
        number_3 = math.sin(number_2)
        print("sin",number_2,"=", number_3)
        continue

    elif action == 'arcsin':
        number_3 = math.arcsin(number_2)
        print("arcsin",number_2,"=", number_3)
        continue 

    elif action == 'arccos':
        number_3 = math.arccos(number_2)
        print("cos",number_2,"=", number_3)
        continue

    elif action == 'arctan':
        number_3 = math.arctan(number_2)
        print("arctg",number_2,"=", number_3)
        continue
    
    elif action == 'arcctan':
        number_3 = math.arctg(number_2)
        print("arctg",number_2,"=", number_3)
        continue

    elif action == 'cos':
        number_3 = math.cos(number_2)
        print("cos",number_2,"=", number_3)
        continue

    elif action == 'tan':
        number_3 = math.tan(number_2)
        print("tg",number_2,"=", number_3)
        continue

    elif action == 'ctg':
        number_3 = 1/math.tan(number_2)
        print("ctg",number_2,"=", number_3)
        continue

    elif action == 'log':
        number_3 = math.log(number_2)
        print("log",number_2,"=", number_3)
        continue

    elif action == 'sqrt':
        number_3 = math.sqrt(number_2)
        print("sqrt",number_2,"=", number_3)
        continue

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
    
    elif action == "%":
        number_3 = number_1 % number_2
        print(number_1, "%", number_2, "=", number_3)
        continue

    else:
        print("Введенный символ не подходит")
        continue



