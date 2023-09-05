import csv

user_list = [
    {"first_name": "Анна", "last_name": "Иванова", "email": "anna@example.com", "gender": "Женский", "balance": "1200.25"},
    {"first_name": "Иван", "last_name": "Петров", "email": "ivan@example.com", "gender": "Мужской", "balance": "850.75"},
    {"first_name": "Екатерина", "last_name": "Смирнова", "email": "kate@example.com", "gender": "Женский", "balance": "3500.50"},
    {"first_name": "Алексей", "last_name": "Сидоров", "email": "alex@example.com", "gender": "Мужской", "balance": "670.80"},
    {"first_name": "Ольга", "last_name": "Козлова", "email": "olga@example.com", "gender": "Женский", "balance": "2100.60"},
    {"first_name": "Дмитрий", "last_name": "Морозов", "email": "dmitry@example.com", "gender": "Мужской", "balance": "430.90"},
    {"first_name": "Мария", "last_name": "Васильева", "email": "maria@example.com", "gender": "Женский", "balance": "1800.45"},
    {"first_name": "Сергей", "last_name": "Павлов", "email": "sergey@example.com", "gender": "Мужской", "balance": "990.30"},
    {"first_name": "Анна", "last_name": "Михайлова", "email": "anna2@example.com", "gender": "Женский", "balance": "2900.15"},
    {"first_name": "Владимир", "last_name": "Кузнецов", "email": "vladimir@example.com", "gender": "Мужской", "balance": "1500.70"},
    {"first_name": "Елена", "last_name": "Новикова", "email": "elena@example.com", "gender": "Женский", "balance": "750.40"},
    {"first_name": "Александр", "last_name": "Федоров", "email": "alexander@example.com", "gender": "Мужской", "balance": "120.99"},
    {"first_name": "Наталья", "last_name": "Соколова", "email": "natalia@example.com", "gender": "Женский", "balance": "2800.33"},
    {"first_name": "Павел", "last_name": "Лебедев", "email": "pavel@example.com", "gender": "Мужской", "balance": "410.67"},
    {"first_name": "Юлия", "last_name": "Ковалева", "email": "yulia@example.com", "gender": "Женский", "balance": "2150.87"},
    {"first_name": "Максим", "last_name": "Медведев", "email": "maxim@example.com", "gender": "Мужской", "balance": "690.21"},
    {"first_name": "Александра", "last_name": "Андреева", "email": "alexandra@example.com", "gender": "Женский", "balance": "1800.12"},
    {"first_name": "Антон", "last_name": "Соловьев", "email": "anton@example.com", "gender": "Мужской", "balance": "520.43"},
    {"first_name": "Евгения", "last_name": "Тихонова", "email": "evgenia@example.com", "gender": "Женский", "balance": "3200.75"},
    {"first_name": "Игорь", "last_name": "Орлов", "email": "igor@example.com", "gender": "Мужской", "balance": "980.65"}
]


with open('data_users_l-3.csv', 'w', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)
   