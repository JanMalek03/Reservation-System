import json
import user_input
import communication

RESERVATION_MESSAGE = "!MAKE_RESERVATION"
LIST_ALL_MESSAGE = "!LIST_ALL_RESERVATIONS"
LIST_FOR_DAY_MESSAGE = "!LIST_RESERVATIONS_FOR_DAY"


def print_all_reservations(data):
    if not data:
        print("There are no reservations.")
        return

    reservations = data.split(';')
    for reservation in reservations:
        date, start, end = reservation.split(',')
        print(f"    Date: {date}, Start: {start}, End: {end}")


def print_reservations_for_date(data):
    if not data:
        print("There are no reservations.")
        return

    reservations = data.split(';')
    for reservation in reservations:
        start, end = reservation.split(',')
        print(f"    Start: {start}, End: {end}")


def list_all_reservations(server):
    communication.send_to(server, LIST_ALL_MESSAGE)
    reservations = communication.recv_from(server)

    print("All reservations:")
    print_all_reservations(reservations)


def list_reservations_for_day(server):
    date = user_input.get_date()
    communication.send_to(server, LIST_FOR_DAY_MESSAGE)
    communication.send_to(server, date)

    reservations = communication.recv_from(server)
    print(f"Reservations for {date}:")
    print_reservations_for_date(reservations)


def reserve_meal_time(server):
    print("\nSo let's make a reservation")

    while True:
        start_time, end_time, date = user_input.get_informations()

        json_data = {
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
        }

        json_string = json.dumps(json_data)
        communication.send_to(server, RESERVATION_MESSAGE)
        communication.send_to(server, json_string)

        message = communication.recv_from(server)
        if message == "SUCCESS":
            print("Your reservation was successful. "\
                  f"So we look forward to seeing you at {start_time} on {date}")
            break

        if message == "TAKEN":
            print("Unfortunately, we do not have any free space at "\
                  "the requested time. Let's try again.")
            break
        else:
            print("Sorry, but something went wrong. Let's try again.")
