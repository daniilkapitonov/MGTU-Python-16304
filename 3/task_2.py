# Дан список, состябщий из натуральный чисел. Длинна спика неизвесна
# Надо найти сумму списка, найти наиболее, наименьшее значения

mass = [1,2,6,4,43,3,-234,2,234,5436,4567,2,2345,2345]

print(min(mass), max(mass), sum(mass)) #так нельзя

summ = 0
mmax = 0
mmin = 0

for i in range(0,len(mass)):
    summ += mass[i]
    
print(summ)
mmax = mass[0]
for i in range(0,len(mass)):
    if mass[i] > mmax:
        mmax = mass[i]
        
print(mmax)

mmin = mass[0]
for i in range(0,len(mass)):
    if mass[i] < mmin:
        mmin = mass[i]
        
print(mmin)

