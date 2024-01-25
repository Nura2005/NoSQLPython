import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

while True:
    print("\nВыберите действие:")
    print("1. Вставить данные")
    print("2. Получить данные")
    print("3. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        city = input("Введите город: ")

        data = {'name': name, 'age': age, 'city': city}
        inserted_data = collection.insert_one(data)
        print(f"Inserted document ID: {inserted_data.inserted_id}")

    elif choice == "2":
        name_to_query = input("Введите имя для поиска: ")

        result = collection.find_one({'name': name_to_query})
        if result:
            print(f"Data retrieved: {result}")
        else:
            print("Данные не найдены.")

    elif choice == "3":
        break

    else:
        print("Неверный ввод. Пожалуйста, выберите корректное действие.")

client.close()
