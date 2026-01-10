# BusTicketsProject
the user interface for NCTX bus tickets

# main - Introduce
Create welcome message, and choosing interface- main menu
User will have a choice: 
1. customer ( to buy ticket)
2. admin ( to login and change a price of tickets)
3. exit

 # case 1 - user interface

# part 1 of case 1 - choose ticket category 
 Create user interface which appear after choosing 1st option in main menu. 
 After choose 1. Client will recive options from excel document - from category_title column. Also i will add description for each of categories from column category_description. Its 6 options available so customer must choose number between 1-6. If he will put wrong input will recive answer "invalid choice, try one more time".
 After customer choice program will print his choice. 

 # part 2 of case 1 - choose age group
 Customer will recive options from excel column topup_passenger_class_name to choice age group. There is 4 available groups: adult, student, under 19, and under 22. Client must choose again numer 1-4 to go ahead. If input its wrong then customer will recive message about it. 

 # part 3 of case 1 - choose specyfic option of ticket
 Client will recive next options to choose from excel column topup_passenger_class_name with description from topup_description. Programm will show all available optins like bulks options for tickets. Customer must choice one option by puting number. If input its wrong then customer will recive message about it. 

 # part 4 of case 1 - price of ticket

 After all choices customer will recive FINAL TICKET SUMMARY which will contain category, passanger type,type of choosen ticket and price in pounds. 
 They will chooce 2 options - buy or cancel. 

 # part 5 of case 1 - finish
 after bought ticket customer will recive message @ ticket purchased successfully! thank you! and will back to start - main menu. 
 

 # Case 2 - admin interface

 # Part 1 of case 2 - create admin interface to change a price
 On the start user will have options to choose between client and admin. 
 If he ask about admin then will need provide password. 
 Password is 'admin123' - will create new document with this password and add it to my github, to be able to open and check the password. 
 Admin will recive opion to change a ticket prices. This changes will save in excel data document. 
 He need provide price in pounds so i will create function to calculate it in pence and add to document. 
 After admin will recive message "Price is change! thank you". 

# Part 2 of case 2 
Create a csv file sale_list.csv, and def save_data to save informations about sold ticket. 
I dont want make it in a loop and check first if file exist so create two separate def. One to create headings in new document, and second one to write data there. 
 
 # Part 3 of case 2

Create new function to showing sales report. If admin ask for it and csv will be empty he will recive "No tickets sold" in other case program will print informations about sold tickets. 
also caled function in admin menu as a option "2" to show sales report. The function must not only save the data to a new CSV file, but also ensure that it is retained there for a longer period of time, and not deleted each time the program is closed.

# Case 3 - improvements

# part 1 of case 3
Improve the way prices are displayed in pounds - by creating the *100 function, the displayed amounts often look wrong.

# part 2 of case 3
option to purchase a second and subsequent ticket by the same customer.

# part 3 of case 3 
Improve the visual aspects of the program - add more blank lines to separate text. Some "graphic" like bus, ticket or thank you. 

# Case 4 - separate modules 
Create new modules for each function and only call them in the main document - this will help organize the program and make it easier to work with 

# Case 5 - testing
Test the program in every possible way and eliminate any problems that may occur. 
Adding comments to explain all code elements.
Fixed issues found, such as returning to the main menu after entering the wrong input instead of giving another chance to respond.
 
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


