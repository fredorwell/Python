# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# с помощью математических формул нахождения корней квадратного уравнения

def EquationConvertToDict(equation):
    equation = equation.replace(' ', '')
    equation = equation[:-2].split('+')
    new_equation = {}
    for i in range(len(equation)):
        new_equation[len(equation) - i - 1] = equation[i].split('*x')[0]
    return new_equation

pol: str = '45*x**5+34*x**4+23*x**3+123*x**2+7*x+5=0'
my_dict = EquationConvertToDict(pol)
print(f'Изначальное уравнение: {pol}')
print(f'Словарь из уравнения: {my_dict}')




