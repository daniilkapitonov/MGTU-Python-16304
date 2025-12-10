import os

path = os.getcwd()
print(path)
parent = os.path.join(path, os.pardir)
print(os.path.abspath(parent))

print(os.listdir(path))
if not os.path.exists(path+'/TESTFOLDER'):
    os.mkdir(path+'/TESTFOLDER')
else:
    os.rmdir(path+'/TESTFOLDER')

# Программа генерирует номера комнат в отеле 
# кол-во (случайно от 10 до 70)
# (от 100 до 999 номер комнаты), 
# находит "счастливые" номера и красиво их оформляет
# Счастливый номер это - 111,222,333 и тд.
# 100,200,300 итд и делимое на 7
