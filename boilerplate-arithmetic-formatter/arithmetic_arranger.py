import re


def arithmetic_arranger(problems, solve=False):
    first = ''
    second = ''
    lines = ''
    sumf = ''
    string = ''

    # turn this ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    # into this "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +
    # 40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNumber = problem.split()[0]
        secondNumber = problem.split()[2]
        sign = problem.split()[1]

        if len(firstNumber) > 4 or len(secondNumber) > 4:
            return "Error: Numbers cannot be more than four digits."

        if sign == '-':
            sum = int(firstNumber) - int(secondNumber)
        elif sign == '+':
            sum = int(firstNumber) + int(secondNumber)

        length = max(len(firstNumber) + 2, len(secondNumber) + 2)
        top = firstNumber.rjust(length)
        bottom = sign + secondNumber.rjust(length - 1)
        line = "-" * length
        sumi = str(sum).rjust(length)

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumf += sumi + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumf += sumi

    if solve == True:
        string = first + '\n' + second + '\n' + lines + '\n' + sumf
    else:
        string = first + '\n' + second + '\n' + lines
    return string
