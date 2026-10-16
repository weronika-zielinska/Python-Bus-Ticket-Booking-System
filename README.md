# Bus Ticket Booking System – Python

## Project Overview

The Bus Ticket Booking System is a console-based Python application developed as part of my BSc (Hons) Software Engineering degree at Nottingham Trent University.

The application simulates a ticket sales system for NCTX bus services. Customers can browse available ticket options, select passenger categories, review prices and purchase tickets. An administrator interface provides functionality for managing ticket prices and reviewing sales records.

The project focuses on data handling, input validation, modular programming and persistent storage using CSV files.

## Features

### Customer Interface

- Browse available ticket categories and their descriptions.
- Select a passenger group, including adults, students and younger passengers.
- View available ticket options and descriptions.
- Review a ticket summary showing the selected category, passenger type, ticket type and price.
- Confirm or cancel a purchase.
- Purchase multiple tickets during one session.
- Receive a purchase confirmation message.

### Administrator Interface

- Access the administration menu using password authentication.
- View available ticket options and their current prices.
- Update ticket prices using amounts entered in pounds.
- Convert prices between pounds and pence for accurate price handling.
- View a sales report containing recorded ticket sales.

### Data Management and Reporting

- Load ticket information from CSV files.
- Save updated ticket prices to a data file.
- Record completed purchases in `sale_list.csv`.
- Retain sales records between program sessions.
- Display recorded sales or indicate when no tickets have been sold.

### User Experience and Validation

- Provide a menu-driven interface with clear instructions.
- Validate user input and handle invalid selections.
- Allow users to retry incorrect inputs without unnecessarily restarting the purchase process.
- Display prices in pounds to two decimal places.
- Use spacing and simple text-based graphics to improve readability.

## Technologies and Concepts

- **Language:** Python
- **Data storage:** CSV files
- **File handling:** Reading and writing structured data
- **Programming concepts:** Functions, conditional statements, loops, input validation and error handling
- **Code organisation:** Modular programming with separate files for customer operations, administration, data management and sales reporting

## Project Structure

The application is organised into separate modules to improve readability, maintainability and separation of responsibilities.

| Module | Responsibility |
|---|---|
| `BusTickets.py` | Main entry point and menu navigation |
| `customer.py` | Customer interface and ticket purchasing |
| `admin.py` | Administrator interface and price management |
| `data_things.py` | Loading and saving data |
| `sales.py` | Sales reporting |

The application uses CSV files to store ticket information and maintain a record of completed purchases.

## Learning Outcomes

Developing this project helped me strengthen my Python programming skills and gain practical experience in building a multi-functional console application.

Key areas of learning included:

- Designing interactive user interfaces using menus and input validation.
- Reading, processing and updating structured data stored in CSV files.
- Implementing persistent data storage for sales records.
- Separating program functionality into reusable modules.
- Testing different user input scenarios and correcting issues.
- Improving code readability through comments and structured program design.

## How to Run

1. Clone or download this repository.
2. Open the project in a Python-compatible development environment, such as Visual Studio Code.
3. Ensure the required Python files and ticket data CSV file are present.
4. Run `BusTickets.py` to launch the application.
5. Follow the on-screen instructions to access the customer or administrator interface.

## Academic Project

Developed as part of the BSc (Hons) Software Engineering course at Nottingham Trent University.


----------------------------------------------------------------------------------------------
 
# Work Plan/ Module diagram/ class diagrams
work plan:
- Project Work Plan -
Bus Tickets Sales Program

1. Project Overview

The aim of this project is to design and implement a console-based ticket sales system for NCTX bus services. The system will allow customers to purchase tickets and administrators to manage ticket prices and view sales reports. The project will be developed using Python and CSV files for data storage.

2. Development Methodology

The project will be developed using an incremental and modular approach.
Each functionality will be implemented and tested separately, then integrated into the main system. This approach allows easier debugging, better organisation of the code, and clearer separation of responsibilities between system components.

3. Planned System Structure

The system will be divided into separate modules, each responsible for a specific part of the program logic:
* main.py – program entry point and main menu
* customer.py – customer ticket purchasing interface
* admin.py – administrator interface
* data_things.py – data loading and saving functions
* sales.py – sales reporting functionality
This modular structure will improve maintainability and readability of the code.

4. Functional Work Plan
4.1 Main Menu (Program Entry Point)

Display a welcome message and main menu.
Provide the user with three options:
* Customer – buy a ticket
* Admin – log in to the administration panel
* Exit – close the program
Validate user input and prevent invalid menu selections.

4.2 Customer Interface – Ticket Purchase Flow
4.2.1 Ticket Category Selection

Load ticket data from a CSV file.
Display available ticket categories based on the category_title field.
Display category descriptions from the category_description field.
Allow the customer to select a category using a numeric option.
Validate input and display an error message if the input is invalid.

4.2.2 Passenger Type Selection

Display available passenger types based on the topup_passenger_class_name field.
Allow the customer to select a passenger type using numeric input.
Validate input and handle incorrect values appropriately.

4.2.3 Ticket Type Selection

Display all available ticket options for the selected category and passenger type.
Show ticket descriptions using the topup_description field.
Allow the customer to select a specific ticket option.
Validate input to prevent invalid selections.

4.2.4 Ticket Summary and Price Display

Display a final ticket summary including:
* Ticket category
* Passenger type
* Selected ticket type
* Ticket price converted from pence to pounds
Provide options to either confirm or cancel the purchase.

4.2.5 Purchase Completion

If the purchase is confirmed:
* Display a confirmation message and a visual ticket graphic.
* Save the sale details to a CSV file.
* Allow the customer to purchase another ticket or return to the main menu.
* Ensure incorrect inputs do not automatically exit the ticket purchase flow.

5. Admin Interface
5.1 Admin Authentication

Require a password to access the admin interface.
* Allow the admin to cancel and return to the main menu.
* Prevent unauthorised access through input validation.
Create separate document with admin password.

5.2 Ticket Price Management

Display all available tickets and their current prices.
Allow the admin to select a ticket and enter a new price in pounds.
Convert the price to pence before saving.
Save updated ticket data back to the CSV file.
Display a confirmation message after a successful update.

5.3 Sales Reporting

Create a persistent CSV file to store ticket sales data.
Save each completed sale with:
* Ticket category
* Passenger type
* Ticket price
Implement a function to display a sales report:
* Show a message if no tickets have been sold.
* Display all recorded sales if data exists.
* Ensure sales data is retained between program runs.

6. Planned Improvements and Enhancements
6.1 Price Formatting

Improve price display by ensuring correct conversion from pence to pounds.
Format prices to two decimal places for clarity.

6.2 Multiple Ticket Purchases

Add functionality allowing customers to purchase multiple tickets in one session.
Validate user input when confirming additional purchases.

6.3 User Interface Improvements

Improve readability of the console output using spacing and separators.
Add simple ASCII graphics (bus, ticket, confirmation messages) to enhance user experience.

7. Code Organisation and Refactoring

Separate the program into clearly defined modules.
Ensure each function has a single responsibility.
Add comments to explain the purpose of functions and key code sections.

8. Testing Plan

Test all menu options and user input paths.
Verify correct handling of invalid input at each stage.
Test ticket purchase, cancellation, and repeated purchases.
Test admin functions including price updates and sales reporting.
Fix any issues identified during testing.

9. Documentation and Diagrams

Prepare a module diagram showing relationships between system components.
Prepare a conceptual class diagram to illustrate logical system design.
Ensure the README file clearly explains how the system works.

Module diagram: 

+--------------------+
|    BusTickets.py   |
|--------------------|
| main()             |
| - main menu        |
| - navigation       |
+---------+----------+
          |
          | calls
          v
+--------------------+        +--------------------+
|    customer.py     |        |     admin.py       |
|--------------------|        |--------------------|
| customer_interface |        | admin_interface()  |
| - ticket purchase  |        | - price editing    |
| - user input       |        | - admin menu       |
|                    |        | - sale report      |
+---------+----------+        +---------+----------+
          |                               |
          | uses                          | uses
          v                               v
+--------------------------------------------------+
|                data_things.py                    |
|--------------------------------------------------|
| load_data()                                      |
| save_data()                                      |
| save_sale()                                      |
+----------------------+---------------------------+
                       |
                       | reads / writes
                       v
               CSV files (mobile_products.csv,
                          sale_list.csv)

+--------------------+
|    sales.py        |
|--------------------|
| show_sales_report()|
| - sales summary    |
+--------------------+



Class diagrams: 

+----------------------+
|      Ticket          |
|----------------------|
| category             |
| passenger_type       |
| title                |
| price                |
+----------------------+

+----------------------+
|   CustomerInterface  |
|----------------------|
| customer_interface() |
|----------------------|
| select_ticket()      |
| buy_ticket()         |
+----------------------+

+----------------------+
|     AdminInterface   |
|----------------------|
| admin_interface()    |
|----------------------|
| edit_price()         |
| view_sales()         |
+----------------------+

+----------------------+
|     DataManager      |
|----------------------|
| load_data()          |
| save_data()          |
| save_sale()          |
+----------------------+

+----------------------+
|    SalesReport       |
|----------------------|
| show_sales_report()  |
+----------------------+


