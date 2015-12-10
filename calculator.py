def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
import pdb
def main():
    first_num = input('Please enter the first number: ')
    #operator = input('Please enter the operator: ')
    second_num  = input ('Please enter the second number: ')
    operator = raw_input('Please enter the operator: ')
    #pdb.set_trace()
    print '{} {} {} = {}'.format(first_num,operator,second_num,
           {"+": add(first_num,second_num),
                 
            "-": subtract(first_num,second_num),
                 
            "*": multiply(first_num,second_num),
                 
            "/": divide(float(first_num),float(second_num)),
                 
            }.get(operator, 'Sorry Wrong value Please try again later'))
main()
