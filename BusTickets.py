import csv

CSV_doc="mobile_products.csv"  #csv with data
SALES_doc="sale_list.csv"   #new csv

# Load data from CSV
def load_data():
    with open (CSV_doc) as file:
        reader= csv.DictReader(file)
        return list(reader)
    
# save data in csv with ticket informations

def save_data(data):
    with open(CSV_doc, "w", newline="") as file:
        writer=csv.DictWriter(file,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print("Data saved successfully!")


#write headings in new csv
def init_sales():
    with open("sale_list.csv","w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = ["category", "age_group", "price"])
        writer.writeheader()

# save data in new csv to see sold tickets        
def save_sale(category, age_group, price):
    with open(SALES_doc, "a", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["category", "age_group", "price"])
        writer.writerow({
            "category": category,
            "age_group": age_group,
            "price": price
            })

#Showing sales report

def show_sales_report():
    with open(SALES_doc, newline="") as file:
            reader=csv.DictReader(file)
            sales_data = list(reader)
            
    if not sales_data:
        print("No sales recorded yet!")
        return
  

    print("~*~*~*~*~ SALES REPORT ~*~*~*~*~")
    
    report = {}

    for row in sales_data:
        key = (row["category"], row ["age_group"])
        report[key] = report.get(key, 0) +1

    total=0

    for (cat,age), count in report.items():
        print(f"{cat} -{age}: sold {count} tickets!")
        total += count

    print("~*~*~ TOTAL SOLD: {total} TICKETS ~*~*~")
    


# Customer interface program

def customer_interface(data):
    print("~*~*~*~*~ CUSTOMER TICKET PURCHASE ~*~*~*~*~")

#Choosing tickets by category
    categories={}
    for row in data:
          title = row["category_title"]
          desc = row["category_description"]
          if title not in categories:
              categories[title]=desc
          
    print("Available ticket options:")
    category_list=list(categories.keys())

    for i, cat in enumerate(category_list):
          print(f"{i}.{cat}")
          print(f"   {categories[cat]}")
          print()
    try:
        choice_cat = int(input("Choose category number: ")) #user input1
        selected_category = category_list [choice_cat] #showing available options
    except:
        print("Invalid choice. Please try one more time.") #wrong choice answer
        return
    print(f"You selected: {selected_category}") #showing which category choose

# Choose age type of ticket

    age_groups = set()
    for row in data:
        if row["category_title"] == selected_category:
               age_groups.add(row["topup_passenger_class_name"])

    age_groups = sorted(list(age_groups))

    print("selected passenger type:") #age options form csv
    for i, ag in enumerate(age_groups):
               print(f"{i}. {ag}")
    try:
        choice_age = int(input("Choose passenger type numer: "))  #user input age option
        selected_age = age_groups[choice_age]
    except:
        print("Invalid choice. Try one more time") #invalid input answer
        return

    print(f"You selected: {selected_age}")  #showing selected option


# Choosing specyfic option of ticket

    ticket_options= [] #storage options
    for row in data:
        if row["category_title"] ==  selected_category and row["topup_passenger_class_name"] == selected_age:
         ticket_options.append(row)

    if not ticket_options: #wrong choice answer
        print("Sorry, no tickets available for this category and passenger type.")
        return

    print("Available ticket options:")

    for i, row in enumerate(ticket_options): #printing options
        print(f"{i}.{row['topup_title']}")  
        
        if "topup_description" in row and row["topup_description"]:
            print(f"       {row['topup_description']}") #printing option descriptions
        print()
            
    try:
        choice_ticket = int(input("Choose ticket numer:")) #user input2
        selected_ticket=ticket_options[choice_ticket]
    except:
        print("Invalid choice.") #wrong choice answer
        return
    
#show price of choosen ticket in pounds
    price_pence = int(selected_ticket["topup_price_in_pence"])
    price_pounds = price_pence/100

    print("~*~*~*~*~ FINAL TICKET SUMMARY~*~*~*~*~")
    print(f"Category: {selected_category}")
    print(f"Passenger type: {selected_age}")
    print(f"Ticket: {selected_ticket['topup_title']}")
    print(f"Price: £{price_pounds:2f}")
    print("~*~*~*~*~*~**~*~*~*~*~*~*~*~*~*~*~")

#Buying or cancel

    print("1. Buy ticket")
    print("2. Cancel")

    end_choice = input("Choose option: ")

    if end_choice == "1":
        save_sale(selected_category,selected_age,price_pounds)
        print("Ticket purchased successfully! Thank You!")
    else:
        print("Purchase cancelled")
        


        
# Admin interface program

def admin_interface(data):
    while True:
        print("~*~*~*~*~ ADMIN PANEL ~*~*~*~*~")
        print("1. Edit ticket price")
        print("2. Show sales report")
        print("3. Return to main menu")

        answer = input("Choose option: ")

    
        if answer == "1":
            for i, row in enumerate(data):
                print(f"{i}. {row['topup_title']} - {row['topup_price_in_pence']} pence")

            try:
                idx = int(input("Choose ticket number to edit: "))
                new_price_pounds = float(input("Enter new price in pounds(£): ")) #creating new price
            except:
                print("Invalid choice. Please try one more time.") #wrong choice message
                continue

            new_price_pence = int(new_price_pounds * 100) # convert new price from pound to pence

            data[idx]["topup_price_in_pence"] = str(new_price_pence)
            print("Pice updated!")
            save_data(data)

        elif answer == "2":
            show_sales_report()

        elif answer == "3":
            return

        else:
            print("Invalid option.")

        

#Main menu

def main():
    data = load_data()
    init_sales() 

    while True:  #how menu looks
        print("~*~*~*~*~~*~*~*~*~\n~*~*~*~*~ NOTTINGHAM CITY COUNCIL TICKETS ~*~*~*~*~\n~*~*~*~*~~*~*~*~*~")
        print("1. CUSTOMER - buy ticket")
        print("2. ADMIN - log in")
        print("3. Exit")

        choice = input("Select option:")

        if choice == "1":
            customer_interface(data)  #go to customer interface
        elif choice == "2": #go to admin interface
            password = input("Ender admin passwors: ")
            if  password == "admin123":  #admn password
                admin_interface(data)
            else: 
                print("Invalid password.") # invalid password
        elif choice =="3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Try one more time")

if __name__ == "__main__":
    main()
        
