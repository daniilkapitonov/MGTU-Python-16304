food = []
item = ""
while True:
    menu=input("Выберите действие. 1 - Добавить, 2 - Удалить, 3 - Выйти")
    if menu=="1":
        item = input("Введите название продукта - ").lower()
        food.append(item)
        print(food)
    elif menu == "2":
        item = input("Введите название продукта для удаления - ").lower()
        food.remove(item)
        print(food)
    elif menu == "3":
        print("Итоговый список продуктов", food)
        break
    else:
        print("Нет такой команды")