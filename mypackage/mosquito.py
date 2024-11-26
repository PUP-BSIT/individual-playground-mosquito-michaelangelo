from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from beautiful_date import D

def date_function():
    date_now = date.today()
    next_day = D.tomorrow()
    last_day = D.yesterday()

    print(date_now)

    print(next_day)

    print(last_day)