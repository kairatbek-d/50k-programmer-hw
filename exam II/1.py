keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
    'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield']

special_characters = "\"!№@#$%^&*()-+?=,<>/\""

special_numbers = "0123456789"

def check_symbols(value):
    if any(c in special_characters for c in value):
        return False
    else:
        return True

def check_keywords(value):
    if any(c == value for c in keywords):
        return False
    else:
        return True

def check_first_symbol(value):
    if value[0] in special_numbers:
        return False
    else:
        return True

def check_name(*args):
    thisdict = {}

    print(args)

    for arg in args:
        if not isinstance(arg, str):
            raise Exception('Введите только строку')
        thisdict[arg] = check_symbols(arg) and check_keywords(arg) and check_first_symbol(arg)

    return thisdict

result = check_name('global', '1my_num', 'item_1', 'item_№_2')
print(result)