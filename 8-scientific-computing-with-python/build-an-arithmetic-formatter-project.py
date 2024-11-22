def arithmetic_arranger(problems, show_answers=False):
    n_problems = len(problems)
    if n_problems > 5:
        return 'Error: Too many problems.'

    left_operands = []
    right_operands = []
    dashes = []
    answers = []

    for problem in problems:
        splited_problem = problem.split(' ')

        left_operand = splited_problem[0]
        operator = splited_problem[1]
        right_operand = splited_problem[2]

        if not (left_operand + right_operand).isnumeric():
            return 'Error: Numbers must only contain digits.'

        n_max = max(len(left_operand), len(right_operand))
        if n_max > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if operator == '+':
            answer = int(left_operand) + int(right_operand)
        elif operator == '-':
            answer = int(left_operand) - int(right_operand)
        else:
            return "Error: Operator must be '+' or '-'."

        left_operands.append(left_operand.rjust(n_max+2))
        right_operands.append(operator + right_operand.rjust(n_max+1))
        dashes.append('-'*(n_max+2))
        answers.append(str(answer).rjust(n_max+2))

    formated_problems = '    '.join(left_operands)
    formated_problems += '\n' + '    '.join(right_operands)
    formated_problems += '\n' + '    '.join(dashes)
    if show_answers:
        formated_problems += '\n' + '    '.join(answers)

    return formated_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')