print_calc ="*" * 7, "Привет калькулятор! V 1.0", "*" * 7    #как убрать кавычки
print_number = 'Введите число: '
print_operation = 'Введите знак действия (+, -, *, **, /, //, ==, !=, >, <, >=, <=): '
print_result = 'Результат: '
print_cntn = 'Продолжить вычисление с этим числом? '
print_error = 'Не коректное значение!'
print_exit = 'Выйти? '
print_yes_exit = 'Пока калькулятор!'

operators = ['+', '-', '*','**', '/', '//', '==', '!=', '>', '<', '>=', '<=']
answer_for_continue = ['yes', 'y', 'Yes', 'да', 'Y', 'Да', 'Д', 'д']

def main():
    prev_result = 0

    while True:
        print (print_calc)
        try:
            num1, operator, num2 = get_expression(prev_result)
        except ValueError:
            continue
        except KeyboardInterrupt:
            break
        except TypeError:
            continue

        result = choose_action(num1, operator, num2)

        print(print_result, result)
        cntn = input(print_cntn)
        if cntn in answer_for_continue:
            prev_result = result

        else:
            prev_result = 0
            close = input(print_exit)
            if close in answer_for_continue:
                print(print_yes_exit)
                break

def choose_action(num1, operator, num2):
    if operator == '+':
        return addition(num1, num2)
    if operator == '-':
        return subtraction(num1, num2)
    if operator == '*':
        return multiplication(num1, num2)
    if operator =='**':
        return exponentiation(num1, num2)
    if operator == '/':
        return division(num1, num2)
    if operator == '//':
        return floordivision(num1, num2)
    if operator == '==':
        return true(num1, num2)
    if operator == '!=':
        return false (num1, num2)
    if operator == '>':
        return greater (num1, num2)
    if operator == '<':
        return less(num1, num2)
    if operator == '>=':
        return greater_or_equal(num1, num2)
    if operator == '<=':
        return lessorequal(num1, num2)

def get_expression(prev_result):
    try:
        if prev_result == 0:
            num1 = int(input(print_number))
        else:
            num1 = prev_result
        operator = input(print_operation)
        if operator not in operators:
            raise ValueError
        num2 = int(input(print_number))
        if operator == '/' and num2 == 0:
            raise ValueError
        return num1, operator, num2
    except ValueError:
        print(print_error)

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def floordivision(num1, num2):
    return num1 // num2

def exponentiation(num1, num2):
    return num1 ** num2

def true(num1, num2):
    return num1 == num2

def false(num1, num2):
    return num1 != num2

def greater(num1, num2):
    return num1 > num2

def less(num1, num2):
    return num1 < num2

def greater_or_equal(num1, num2):
    return num1 >= num2

def lessorequal(num1, num2):
    return num1 <= num2

if __name__ == '__main__':
    main()








