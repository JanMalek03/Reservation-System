import socket
import communication
import services

SERVER_PORT = 5050
SERVER = "127.0.0.1"

DISCONNECT_MESSAGE = "!DISCONNECT"

SERVICES = ["Meal time reservation", "List all occupied spaces",
            "List occupied places on a certain day", "End communication"]


def print_services():
    print("\nMENU:")
    print("Choose from the range of services:")
    for index, service in enumerate(SERVICES, start=1):
        print(f"    {index}. {service}")


def run_client():
    server = socket.socket()
    server.connect((SERVER, SERVER_PORT))
    print("You have successfully connected to the server\n")

    actions = {
        "1": lambda: services.reserve_meal_time(server),
        "2": lambda: services.list_all_reservations(server),
        "3": lambda: services.list_reservations_for_day(server)
    }

    while True:
        print_services()
        number = input("\nWrite the number of the service: ")
        if int(number) == len(SERVICES):
            print("Have a nice rest of the day")
            break

        action = actions.get(number)
        if action:
            action()
            input("\nPress Enter to continue to the menu...")
        else:
            print("Invalid input, try again")

    communication.send_to(server, DISCONNECT_MESSAGE)
    server.close


if __name__ == "__main__":
    run_client()
