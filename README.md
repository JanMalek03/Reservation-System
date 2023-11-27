# Reservation-System

This Reservation System is a networked application that allows users to make and manage mealtime reservations. It features a server that handles incoming connections and a client interface for users to interact with the reservation database.

## Table of Contents

- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Learnings and Takeaways](#learning-and-takeaways)
- [Contributing](#contributing)


## Getting Started
To get the system up and running, ensure Python is installed on your machine by downloading it from the [the official website](https://www.python.org/downloads/). Start the server by navigating to the project directory and running:

python server.py

For the client interface, execute:

python client.py

in a separate command line window.


## How To Use
The client application provides a menu-driven interface. Once connected to the server, follow the prompts to perform actions like creating a reservation, viewing all reservations, or checking reservations for a particular day.


## Learnings and Takeaways
Building this system allowed me to delve into various technical areas, including:

- **Threading in Python**: Python's threading capabilities to manage concurrent client connections.
- **Socket Programming**: Network communication using Python's socket programming.
- **Regular Expressions**: Applying regular expressions for stringent input validation.
- **SQLite**: Implementing SQLite database operations for persistent data storage.
- **Code Organization**: Organizing a Python project across multiple files to maintain a clean and modular codebase.

This project is a testament to the application of these concepts in a working software system, though it remains a work in progress with room for further development and refinement.


## Contributing

Contributions to this project are welcome. If you want to improve the game or add new features, feel free to fork this repository and submit a pull request.

Enjoy playing the game!
