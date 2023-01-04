import model
import view
import logger

def input_equation():
    equ_str = view.input_equation()
    model.set_equation(equ_str)


def start():
    input_equation()
    model.solution_equation()
    view.print_to_console(f'{model.get_equation()} = {model.get_result()}')
    logger.add_log(f'{model.get_equation()} = {model.get_result()}')


