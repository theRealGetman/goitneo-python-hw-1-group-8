from collections import defaultdict
from datetime import datetime


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Bill Gates 2", "birthday": datetime(1955, 2, 25)},
    {"name": "Bill Gates 6", "birthday": datetime(1955, 3, 2)},
    {"name": "Bill Gates 3", "birthday": datetime(1955, 2, 26)},
    {"name": "Bill Gates 4", "birthday": datetime(1955, 2, 27)},
    {"name": "Bill Gates 5", "birthday": datetime(1955, 3, 1)},
    {"name": "Bill Gates 18", "birthday": datetime(1955, 3, 5)},
    {"name": "Bill Gates 28", "birthday": datetime(1955, 3, 6)},
    {"name": "Bill Gates 7", "birthday": datetime(1955, 3, 3)},
    {"name": "Bill Gates 8", "birthday": datetime(1955, 3, 4)},
]

weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


def get_birthdays_per_week(users):
    birthdays_by_weekday = defaultdict(list)
    today = datetime.now().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)
        if today > birthday_this_year:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            weekday = weekdays[birthday_this_year.weekday()]
            if weekday == 'Saturday' or weekday == 'Sunday':
                if delta_days > 5:
                    birthdays_by_weekday['Next Monday'].append(
                        {'name': name, 'days_delta': delta_days})
                else:
                    birthdays_by_weekday['Monday'].append(
                        {'name': name, 'days_delta': delta_days})
            else:
                birthdays_by_weekday[weekday].append(
                    {'name': name, 'days_delta': delta_days})

    sorted_items = {k: v for k, v in sorted(
        birthdays_by_weekday.items(), key=lambda item: item[1][0]['days_delta'])}

    for weekday, users in sorted_items.items():
        print('{}: {}'.format(weekday, ', '.join(
            [user['name'] for user in users])))


get_birthdays_per_week(users)
