import validators


def get_time_range():
    while True:
        time = input("\nEnter preferred time range (HH:MM-HH:MM): ")
        if validators.time_valid(time):
            return time
        print("Invalid input. Please enter the time in HH:MM-HH:MM " \
              "format within the range 00:00 to 23:59.")


def get_date():
    while True:
        date = input("\nEnter the date (DD.MM.YYYY): ")
        if validators.date_valid(date):
            return date
        print("Invalid input. Please enter the time in DD.MM.YYYY format. " 
              "Dates in the past are also not allowed.")


def get_answer(time, date):
    start_time, end_time = time.split('-')
    while True:
        response = input(f"\nSo you want reservation from {start_time} " \
                         f"to {end_time} on {date}? (y/n): ").lower()
        if response != "y" and response != "n":
            print("Invalid input. Please enter the yes or no answer.")
            continue
        return response


def get_informations():
    date = ""
    time_range = ""

    while True:
        date = get_date()
        time_range = get_time_range()

        confirmation = get_answer(time_range, date)
        if confirmation == "y":
            break
        print("So lets go again")

    start_time, end_time = time_range.split('-')
    return (start_time, end_time, date)
