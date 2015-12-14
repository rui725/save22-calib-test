def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1, num2):
    return  num1 * num2

def divide(num1, num2):
    return float(num1) / float(num2)

def inputOne(input = raw_input):
    return int(input("First number: "))

def inputTwo(input = raw_input):
    return int(input("Second number: "))

def input_operator(input = raw_input):
    return input("Operator:")

def operator(op, num1 ,num2):
    functions = { '+': add,
                  '-': subtract,
                  '*': multiply,
                  '/': divide }
    funcs = functions.get(op, None)
    if funcs:
        return funcs(num1, num2)
    return None

def output(op, num1, num2, ans):
    return '{} {} {} = {}'.format(num1,op,num2,ans)

def main():
    print("---CALCULATOR---")
    num1 = inputOne()
    op = input_operator()
    num2 = inputTwo()
    ans = operator(op, num1 ,num2)
    print output(op,num1,num2,ans)

if __name__ == '__main__':
    main()
