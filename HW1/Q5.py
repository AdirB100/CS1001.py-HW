#Question 5
def calc(expression):
    lst_expr = expression.split()
    if len(lst_expr) == 1:
        return int(expression)
    while True:
        if lst_expr[1] == '+':
            value = int(lst_expr[0]) + int(lst_expr[2])
        elif lst_expr[1] == '-':
            value = int(lst_expr[0]) - int(lst_expr[2])
        elif lst_expr[1] == '*':
            value = int(lst_expr[0]) * int(lst_expr[2])
        elif lst_expr[1] == '**':
            value = int(lst_expr[0]) ** int(lst_expr[2])
        else:
            value = int(lst_expr[0]) // int(lst_expr[2])
        if len(lst_expr) == 3:
            return value
        else:
            lst_expr[2] = value
            lst_expr = lst_expr[2:]