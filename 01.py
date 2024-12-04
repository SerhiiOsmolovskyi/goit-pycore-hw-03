from datetime import datetime

def get_days_from_today(date: str) -> int:
    try: 
        input_date = datetime.strptime(date, "%Y-%m-%d").date()

        today_date = datetime.today().date()

        delta_days = (today_date - input_date).days

        return delta_days
    except ValueError:
        raise ValueError ("Помилка! Введіть дату у форматі 'РРРР-ММ-ДД'")

try:
    user_date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
    days = get_days_from_today(user_date)
    print(f"Кількість днів: {days}")
    print(get_days_from_today("2021-10-09"))

except ValueError as e:
    print(e)