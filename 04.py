import datetime

def get_upcoming_birthdays(users):
    today = datetime.datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        if (birthday.month < today.month) or (birthday.month == today.month and birthday.day < today.day):
            birthday = birthday.replace(year=today.year + 1)
            print(birthday)
        else:
            birthday = birthday.replace(year=today.year)

        if birthday.weekday() >= 5:
            days_to_monday = 7 - birthday.weekday()
            birthday = birthday + datetime.timedelta(days=days_to_monday)

        if today <= birthday <= today + datetime.timedelta(days=7):
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "Phibie", "birthday": "1985.12.06"},
    {"name": "Marilyn Monroe", "birthday": "1985.12.08"},
    {"name": "Ringo Star", "birthday": "1985.12.05"},
    {"name": "John Poe", "birthday": "1985.12.05"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
