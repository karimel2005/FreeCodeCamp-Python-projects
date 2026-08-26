def arithmetic_arranger(problems, show_answers=False):
    # check problems number
    if len(problems) > 5:
       return 'Error: Too many problems.'
    else:
        first_row = ''
        second_row = '' 
        dashes = ''
        answers = '' 
        # Go through each Operation
        for operation in problems:
         # Then:
            # check operator
            if '+' in operation:
                operator = '+'
            elif '-' in operation:
                operator = '-'
            else: return "Error: Operator must be '+' or '-'."

        # Operands
            fir_operand = operation.split(' ')[0]
            sec_operand = operation.split(' ')[2] 
            # check digits
            if not fir_operand.isdigit() or not sec_operand.isdigit():
               return 'Error: Numbers must only contain digits.'
                 
            # check max digits
            splitted_op = operation.split(operator)
            for num in splitted_op:
                if len(num) > 5:
                  return 'Error: Numbers cannot be more than four digits.'

            # No errors == format the operations 

            # width
            width = max(len(fir_operand), len(sec_operand)) + 2

            # calculating the result
            if operator == '+':
                summed = int(fir_operand) + int(sec_operand)
            elif operator == '-':
                summed = int(fir_operand) - int(sec_operand)
            
            # tune each row
            top = str(fir_operand).rjust(width)
            bottom = operator + str(sec_operand).rjust(width - 1)
            line = ''
            answer = str(summed).rjust(width)

            # costum dashes for each operation
            for _ in range(width):
                line += '-'
            
            # leaving 5 spaces between each two operations
            if operation == problems[-1]:
                first_row += top
                second_row += bottom
                dashes += line
                answers += answer
            else:
                first_row += top + '    '
                second_row += bottom + '    '
                dashes += line + '    '
                answers += answer + '    '
           





        if show_answers:
          here_you_go = first_row + '\n' + second_row + '\n' + dashes + '\n' + answers 
        else: here_you_go = first_row + '\n' + second_row + '\n' + dashes

    return here_you_go
            

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

