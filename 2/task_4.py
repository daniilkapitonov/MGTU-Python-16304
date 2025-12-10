#calculator

num1 = int(input('Num 1 - '))
num2 = int(input('Num 2 - '))

operator = input('+-/* ')

if operator == '+':
    print(f'{num1}{operator}{num2}={num1+num2}')
elif operator == '-':
    print(f'{num1}{operator}{num2}={num1-num2}')
elif operator == '*':
    print(f'{num1}{operator}{num2}={num1*num2}')
elif operator == '/' and num2!=0:
    print(f'{num1}{operator}{num2}={num1/num2}')
else:
    print('Err, проверьте написание или деление на 0')
    