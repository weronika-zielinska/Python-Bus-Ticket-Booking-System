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
 


