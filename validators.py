import datetime
import re


def time_valid(time):
    time_format = re.compile(r'^([0-2][0-9]:[0-5][0-9])-([0-2][0-9]:[0-5][0-9])$')
    if not (time_format.match(time)):
        return False

    start_time_str, end_time_str = time.split('-')
    start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
    end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
    return start_time < end_time


def date_valid(date):
    date_format = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
    if not (date_format.match(date)):
        return False

    input_date = datetime.datetime.strptime(date, "%d.%m.%Y")
    current_date = datetime.datetime.now()

    input_date = input_date.replace(hour=0, minute=0, second=0, microsecond=0)
    current_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)

    return input_date >= current_date
