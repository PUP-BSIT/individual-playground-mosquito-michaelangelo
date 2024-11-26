from datetime import date
from beautiful_date import D
from dateutil.relativedelta import relativedelta

def date_function():
    date_now = date.today()
    next_day = D.tomorrow()
    last_day = D.yesterday()
    days_7_from_now = D.today() + relativedelta(days=7)

    print("This is the date today:",date_now)   

    print("This is the date tomorrow:",next_day)

    print("This is the date yesterday:", last_day)

    print("This is the date 7 days from now:", days_7_from_now)