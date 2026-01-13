# Logistics Console Application

## Table of Contents

* [Project Overview](#-project-overview)
* [Key Features](#-key-features)
* [Architectural Design](#-architectural-design)
* [Project Structure](#-project-structure)
* [Business Logic Highlights](#-business-logic-highlights)
* [Testing](#-testing)
* [Technologies Used](#-technologies-used)
* [Learning Outcomes](#-learning-outcomes)
* [Future Improvements](#-future-improvements)

---

## Project Overview

**Logistics App** is a console-based logistics management system written in **Python**, designed following **Object-Oriented Programming (OOP)** principles.
The application simulates the internal system of a logistics company operating delivery routes between major Australian cities.

Employees can:

* Register customers and packages
* Create and manage delivery routes
* Assign packages to routes and trucks
* Track delivery status and ETA (Estimated Time of Arrival)
* Persist and restore application state

This project was developed as a **course assignment**, but its architecture and scope go beyond basic requirements and demonstrate real-world software design practices.

---

## Key Features

* **Package Management**
  Create, assign, and track delivery packages

* **Route Management**
  Define delivery routes between multiple hubs

* **Truck & Capacity Management**
  Automatic capacity checks and availability tracking

* **ETA Calculation**
  Delivery time is calculated dynamically based on distance and average speed

* **Persistence**
  Save and load the full application state

* **Clean Architecture**
  Strong separation of concerns using OOP patterns

---

## Architectural Design

The application is structured around **domain-driven design** and **Command Pattern**.

### Core Components

* **Engine**
  Entry point of the application, responsible for command execution

* **ApplicationData**
  Central storage of application state (customers, packages, routes, trucks)

* **Models**
  Core domain entities such as `Package`, `Route`, `Truck`, and `Customer`

* **Commands**
  Each user action is encapsulated in a separate command class

* **Factories**
  Responsible for controlled object creation and ID management

---

## Project Structure

```
logistics_app/
│
├── core/
│   ├── engine.py
│   ├── application_data.py
│
├── commands/
│   ├── create_package.py
│   ├── create_route.py
│   ├── assign_package.py
│   └── ...
│
├── models/
│   ├── package.py
│   ├── route.py
│   ├── truck.py
│   └── customer.py
│
├── factories/
│   └── models_factory.py
│
├── utils/
│   ├── validation_helpers.py
│   └── city_distances.py
│
└── main.py
```

---

## Business Logic Highlights

* Trucks become unavailable once a route starts and are released after completion
* Packages can only be assigned if capacity allows
* Routes can include multiple delivery hubs
* ETA is calculated using:

```
ETA = distance / average_speed
```

* Package delivery status updates automatically when the destination is reached

---

## Testing

The project includes **unit tests** covering core business logic, domain models, and command execution.

### Covered Areas

* **ApplicationData**

  * Initialization and default state
  * User, customer, package, and route management
  * Route discovery and assignment validation

* **Commands**

  * `CreatePackage` command validation and execution logic

* **Domain Models**

  * `Customer` – input validation and constraints
  * `Package` – status transitions, ETA logic, and string representation

### Test Structure

```
tests/
│
├── application_data_test.py
├── create_package_test.py
├── customer_test.py
├── package_test.py
└── test_data.py
```

### Testing Techniques Used

* `unittest` framework
* `unittest.mock` for dependency isolation
* Boundary and negative test cases
* Subtests for parameterized validation

These tests ensure **test isolation**, **deterministic behavior**, and confidence in the core business rules.

---

## How to Use the Application

The application is operated entirely through **console commands**. Each command represents a specific user action and follows a clear and consistent syntax.

---

## Authentication Commands

```text
Login <email> <password>
Logout
```

**Example:**

```text
Login manager1@telerikacademy.com 123456
Logout
```

---

## User & Customer Management

### Create User (Manager only)

```text
CreateUser <email> <first_name> <last_name> <password> <role>
```

**Example:**

```text
CreateUser regular1@telerikacademy.com Gosho Goshev 123456 Regular
```

### Create Customer

```text
CreateCustomer <first_name> <last_name> <email>
```

**Examples:**

```text
CreateCustomer John Doe john_doe@gmail.com
CreateCustomer Petar Petrov p_petrov@gmail.com
```

---

## Package Management

### Create Package

```text
CreatePackage <start_city> <end_city> <weight> <customer_email>
```

**Examples:**

```text
CreatePackage Brisbane Sydney 500 john_doe@gmail.com
CreatePackage Brisbane Melbourne 5000 p_petrov@gmail.com
CreatePackage Sydney Melbourne 45 john_doe@gmail.com
```

### Find Package

```text
FindPackage <package_id>
```

---

## Route & Truck Management

### Create Route

```text
CreateRoute <city1> <city2> [city3 ...]
```

**Example:**

```text
CreateRoute Brisbane Sydney Melbourne
```

### Find Truck

```text
FindTruck <truck_id>
```

### Assign Truck to Route

```text
AssignTruck <route_id> <truck_id>
```

---

## Assignment & Tracking

### View Unassigned Packages at Location

```text
ViewUnassignedPackagesAtLocation <city>
```

### Bulk Assign Packages at Location

```text
BulkAssignAtLocation <route_id> <city>
```

### Find Suitable Route for Package

```text
FindSuitableRoute <package_id>
```

### Add Package to Route

```text
AddPackage <package_id> <route_id>
```

---

## Monitoring

### View Delivery Routes

```text
ViewDeliveryRoutes
```

---

## Full Example Workflow

```text
Login manager1@telerikacademy.com 123456
CreateUser regular1@telerikacademy.com Gosho Goshev 123456 Regular
Logout

Login regular1@telerikacademy.com 123456
CreateCustomer John Doe john_doe@gmail.com
CreateCustomer Petar Petrov p_petrov@gmail.com

CreatePackage Brisbane Sydney 500 john_doe@gmail.com
CreatePackage Brisbane Melbourne 5000 p_petrov@gmail.com

ViewUnassignedPackagesAtLocation Brisbane

CreateRoute Brisbane Sydney Melbourne
FindTruck 1
AssignTruck 1001 1
BulkAssignAtLocation 1 Brisbane

CreatePackage Sydney Melbourne 45 john_doe@gmail.com
FindSuitableRoute 3
AddPackage 3 1

CreatePackage Brisbane Melbourne 10000 p_petrov@gmail.com

FindPackage 1
FindPackage 2
FindPackage 3
FindPackage 4

ViewDeliveryRoutes

Logout
Login manager1@telerikacademy.com 123456
ViewDeliveryRoutes
```

---

## Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Command Pattern
* Enumerations (Enum)
* File-based persistence

---

## Learning Outcomes

Through this project I practiced:

* Designing scalable OOP architectures
* Applying design patterns in real scenarios
* Writing clean, maintainable Python code
* Modeling real-world business logic
* Separating domain logic from application flow

---

## Future Improvements

* Add full unit test coverage
* Introduce logging instead of print statements
* Add database persistence (SQLite)
* Build a REST API or GUI frontend

