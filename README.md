# Library Management System

A command-line Library Management System developed in Python to practise object-oriented programming principles and basic application logic.

## Overview

The application allows users to manage books and library members, track borrowing status and perform basic library operations through a command-line interface.

The project was developed as a practical exercise in Python OOP, with a focus on abstraction, inheritance, encapsulation and interaction between multiple classes.

## Features

* Add books to the library
* Register library members
* Display all books
* Display available books
* Display borrowed books
* Borrow books using a member ID and ISBN
* Return books using a member ID and ISBN
* Search for books by ISBN
* Search for members by member ID
* Track the borrowing status of books
* Display information about library items

## Object-Oriented Design

The project uses several classes to model the library system:

* **`LibraryItem`** – an abstract base class containing common properties and behaviour for library items.
* **`Book`** – inherits from `LibraryItem` and adds book-specific attributes such as author and page count.
* **`Magazines`** – inherits from `LibraryItem` and demonstrates how another type of library item can extend the base class.
* **`Member`** – represents a library member and manages their borrowed books.
* **`Library`** – manages books and members and controls borrowing and returning operations.

### OOP Concepts Demonstrated

* **Abstraction** – `LibraryItem` is implemented as an abstract base class using `ABC` and `@abstractmethod`.
* **Inheritance** – `Book` and `Magazines` inherit common functionality from `LibraryItem`.
* **Method overriding** – each library item type provides its own implementation of `display_info()`.
* **Encapsulation** – object attributes and methods are organised within classes to manage application state and behaviour.
* **Composition** – the `Library` class manages collections of books and members, while `Member` objects maintain their borrowed books.

## Technologies

* Python
* Object-Oriented Programming
* Abstract Base Classes
* Command-Line Interface

## How It Works

The program starts with an empty library and presents a menu of available operations.

For example, when borrowing a book, the user provides a member ID and ISBN. The application searches for the corresponding member and book, checks whether the book is available, updates the borrowing status and adds the book to the member's borrowed book list.

When a book is returned, the application removes it from the member's borrowed book list and updates its availability status.

## Project Structure

The project is currently implemented as a Python application with the main classes and command-line interface contained in the source code.

## Future Improvements

Possible future improvements include:

* Adding persistent data storage using SQLite
* Adding full magazine management through the command-line interface
* Adding stronger input validation and error handling
* Preventing duplicate member IDs and ISBNs
* Separating the command-line interface from the application logic
* Adding automated tests
