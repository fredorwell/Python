inp_equation = ''
result = 0
list_equation = []


def get_equation():
    global inp_equation
    return inp_equation


def set_equation(string):
    global inp_equation
    inp_equation = string


def get_result():
    global result
    return result


def get_list_equation():
    global list_equation
    return list_equation


def parse_equation():
    global inp_equation
    global list_equation
    norm_str = inp_equation.replace(" ", "")
    temp_var = ''
    for i in range(len(norm_str)):
        if norm_str[i].isdigit():
            temp_var += norm_str[i]
        else:
            list_equation.append(int(temp_var))
            list_equation.append(norm_str[i])
            temp_var = ''
        if i == len(norm_str) - 1:
            list_equation.append(int(temp_var))
            temp_var = ''


def solution_equation():
    global inp_equation
    global list_equation
    global result
    parse_equation()
    while len(list_equation) != 1:
        i = 0
        while ('*' in list_equation or '/' in list_equation) and i < len(list_equation):
            if list_equation[i] == '*':
                result = list_equation[i - 1] * list_equation[i + 1]
                list_equation.pop(i)
                list_equation.pop(i)
                list_equation[i - 1] = result

            elif list_equation[i] == '/':
                result = list_equation[i - 1] / list_equation[i + 1]
                list_equation.pop(i)
                list_equation.pop(i)
                list_equation[i - 1] = result
            else:
                i += 1

        while ('+' in list_equation or '-' in list_equation) and i < len(list_equation):
            if list_equation[i] == '+':
                result = list_equation[i - 1] + list_equation[i + 1]
                list_equation.pop(i)
                list_equation.pop(i)
                list_equation[i - 1] = result

            elif list_equation[i] == '-':
                result = list_equation[i - 1] - list_equation[i + 1]
                list_equation.pop(i)
                list_equation.pop(i)
                list_equation[i - 1] = result
            else:
                i += 1
    result = round(result, 2)
