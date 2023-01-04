first_num = 0
second_num = 0
operation = ''
result = 0


def get_first():
    global first_num
    return first_num


def get_second():
    global second_num
    return second_num


def get_operation():
    global operation
    return operation


def get_result():
    global result
    return result


def set_first(value):
    global first_num
    first_num = value


def set_second(value):
    global second_num
    second_num = value


def set_operation(oper):
    global operation
    operation = oper


def addition():
    global first_num
    global second_num
    global result
    result = first_num + second_num


def difference():
    global first_num
    global second_num
    global result
    result = first_num - second_num


def multiplication():
    global first_num
    global second_num
    global result
    result = first_num * second_num


def division():
    global first_num
    global second_num
    global result
    result = first_num / second_num
    if result == int(result):
        result = int(result)

