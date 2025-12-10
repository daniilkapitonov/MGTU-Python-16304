    
# Пользователь вводит число. Программа считает сумму чисел
# от 1 до введённого числа

num = int(input('Num 1 - '))
cash = 0
for i in range(1,num+1):
    cash+=i
print(cash)