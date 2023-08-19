from datetime import datetime, timedelta


def get_celebrators(users, now):
    # Определяем, у кого день рождения был вчера и в ближайшие 6 дней
    celebrators = []
    for user in users:
        if now - timedelta(days=1) <= user['birthday'].date() <= now + timedelta(days=6):
            celebrate_user = {}
            celebrate_user['name'] = user['name']
            celebrate_user['birthday'] = user['birthday']
            celebrators.append(celebrate_user)

    return celebrators


def get_celebrate_per_week(users, now):
    # Определяем, у кого день рождения в воскресенье и увеличиваем ему дату поздравления на 1 день
    # остальным убираем проверку на вчера
    celebrate_users = []
    for user in users:
        celebrate_user = {}
        if user['birthday'].weekday() == 6:
            celebrate_user['name'] = user['name']
            celebrate_user['birthday'] = user['birthday'] + timedelta(days=1)
            celebrate_users.append(celebrate_user)
        else:
            if now <= user['birthday'].date() <= now + timedelta(days=6):
                celebrate_user['name'] = user['name']
                celebrate_user['birthday'] = user['birthday']
                celebrate_users.append(celebrate_user)

    return celebrate_users


def get_birthdays_per_week(users, now):
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
        day_of_week = (start_of_week + timedelta(days=(birthday.weekday() - start_of_week.weekday()) % 7)).strftime('%A')
        
        # Добавляем пользователя в словарь по дням недели
        birthdays_per_week[day_of_week].append(name)
    
    # Выводим именинников на печать
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


def start(test_users):
    # Определяем текущий день
    now = datetime.now().date()
    # Определяем, у кого день рождения в ближайшие 7 дней
    celebrators = get_celebrators(test_users, now)
    # Определяем, у кого день рождения в воскресенье и увеличиваем ему дату поздравления на 1 день
    celebrate_users = get_celebrate_per_week(celebrators, now)
    # Сортируем пользователей и выводим на печать именинников
    get_birthdays_per_week(celebrate_users, now)





# Тестовый список пользователей
test_users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 27)},
    {'name': 'Jill', 'birthday': datetime(2023, 8, 22)},
    {'name': 'Kim', 'birthday': datetime(2023, 8, 25)},
    {'name': 'Jan', 'birthday': datetime(2023, 8, 25)},
    {'name': 'Kate', 'birthday': datetime(2023, 8, 20)},
]



if __name__ == '__main__':

    start(test_users)

