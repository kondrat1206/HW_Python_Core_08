from datetime import datetime, timedelta


now = datetime.now().date()


def get_celebrate_per_week(users):
    # Переносим празднование ДР на следующий понедельник, если ДР в субботу, или воскресенье
    celebrate_users = []
    for user in users:
        celebrate_user = {}
        if user['birthday'].weekday() == 6:
            celebrate_user['name'] = user['name']
            celebrate_user['birthday'] = user['birthday'] + timedelta(days=1)
            celebrate_users.append(celebrate_user)
        elif user['birthday'].weekday() == 5:
            celebrate_user['name'] = user['name']
            celebrate_user['birthday'] = user['birthday'] + timedelta(days=2)
            celebrate_users.append(celebrate_user)
        else:
                celebrate_user['name'] = user['name']
                celebrate_user['birthday'] = user['birthday']
                celebrate_users.append(celebrate_user)

    return celebrate_users


def get_celebrators(users, now=now):
    # Определяем, у кого празднуем день рождения в ближайшие 7 дней
    celebrate_users = get_celebrate_per_week(users)
    celebrators = []
    for user in celebrate_users:
        if now  < user['birthday'].date() <= now + timedelta(days=7):
            celebrate_user = {}
            celebrate_user['name'] = user['name']
            celebrate_user['birthday'] = user['birthday']
            celebrators.append(celebrate_user)

    return celebrators


def get_birthdays_per_week(users, now=now):
    #получаем пользователей, которых надо поздравить в ближайшие 7 дней
    users = get_celebrators(users)
    # находим первый понедельник на этой неделе
    start_of_week = now - timedelta(days=now.weekday())
    # Создаем словарь для сохранения поздравлений по дням недели
    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    
    # Для каждого пользователя из списка
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        # Определяем день недели для его поздравления
        day_of_week = birthday.strftime('%A')
        # Добавляем пользователя в словарь по дням недели
        birthdays_per_week[day_of_week].append(name)
    
    # Выводим именинников на печать
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 19)}, # сб
    {'name': 'Jill', 'birthday': datetime(2023, 8, 20)}, # вс
    {'name': 'Kim', 'birthday': datetime(2023, 8, 21)}, # пн
    {'name': 'Jan', 'birthday': datetime(2023, 8, 22)}, # вт
    {'name': 'Kate', 'birthday': datetime(2023, 8, 23)}, # ср
    {'name': 'Ane', 'birthday': datetime(2023, 8, 24)}, # чт
    {'name': 'Serg', 'birthday': datetime(2023, 8, 25)}, # пт
    {'name': 'Natali', 'birthday': datetime(2023, 8, 26)}, # сб
    {'name': 'Petr', 'birthday': datetime(2023, 8, 27)}, # вс
    {'name': 'Evgen', 'birthday': datetime(2023, 8, 28)}, # пн
    {'name': 'Mary', 'birthday': datetime(2023, 8, 29)}, # вт
    {'name': 'Nik', 'birthday': datetime(2023, 8, 30)}, # ср
    {'name': 'Andry', 'birthday': datetime(2023, 8, 31)}, # чт

]


get_birthdays_per_week(users)