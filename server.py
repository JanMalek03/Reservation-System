import socket
import threading
import database_manager
import communication

PORT = 5050
MAX_CONNECTIONS = 5

DISCONNECT_MESSAGE = "!DISCONNECT"
RESERVATION_MESSAGE = "!MAKE_RESERVATION"
LIST_ALL_MESSAGE = "!LIST_ALL_RESERVATIONS"
LIST_FOR_DAY_MESSAGE = "!LIST_RESERVATIONS_FOR_DAY"


def handle_client(client, address):
    while True:
        message = communication.recv_from(client)
        if message == None or message == DISCONNECT_MESSAGE:
            break

        if message == LIST_ALL_MESSAGE:
            print(f"Listing all reservations for a client: {address}")
            reservations = database_manager.get_all_reservations()
            communication.send_to(client, reservations)

        if message == LIST_FOR_DAY_MESSAGE:
            date = communication.recv_from(client)
            print(f"Listing reservations for the day {date} for a client: {address}")
            reservations = database_manager.get_reservations_for_date(date)
            communication.send_to(client, reservations)

        if message == RESERVATION_MESSAGE:
            print(f"Making a reservation for a client: {address}")
            message = communication.recv_from(client)
            response = database_manager.make_reservation(message)
            communication.send_to(client, response)

    client.close
    print(f"Client {address} disconnected")


def run_server():
    database_manager.init_db()
    database_manager.delete_past_reservations()

    s = socket.socket()
    s.bind(('', PORT))
    s.listen(MAX_CONNECTIONS)
    print("Server is listening")

    while True:
        client, address = s.accept()
        print(f"\nClient connected from: {address}")

        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()


if __name__ == "__main__":
    run_server()
