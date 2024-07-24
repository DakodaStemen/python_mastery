def arithmetic_arranger(problems, show_answers=False):

#1 check length of the parameter
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
#2 check the op
    operators = []
    for problem in problems:
        array = problem.split()
        operators.append(array[1])

    for operator in operators:
        if operator in ['*','/']:
            return "Error: Operator must be '+' or '-'."
        
#3 check non-digit
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])

    for number in numbers:
        if not number.isdigit():
            return 'Error: Numbers must only contain digits.'
        
#4 check op length        
        elif len(number) > 4:
             return 'Error: Numbers cannot be more than four digits.'

#5 eval 
    answers = []
    top_row = ''
    bottom_row = ''
    answer_row = ''
    dashes = ''
    
    for i in range(0, len(numbers), 2):
        pass
        n1 = int(numbers[i])
        n2 = int(numbers[i + 1])
        operator = operators[i // 2]

        if operator == '+':
            result = n1 + n2
        else:
            result = n1 - n2
        answers.append(result)

#6 format rows
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2

        top_row += numbers[i].rjust(space_width)
        bottom_row += operator + numbers[i + 1].rjust(space_width - 1) 
        dashes += '-' * space_width

#7 spacing of probs
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4

#8 format ans
    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(answers[i]).rjust(space_width)

#9 spacing between
        if i != len(answers) - 1:
            answer_row += ' ' * 4

#10 return
    if show_answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, answer_row))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')