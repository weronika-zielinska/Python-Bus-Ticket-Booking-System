import csv
import os



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
    print("                Data saved successfully!")


#write headings in new csv - can use to manual clear csv doc, but dont need it anymore, becouse this one clear my csv everytime when i close program. 
# def init_sales():
  #  with open("sale_list.csv","w", newline="") as file:
   #     writer = csv.DictWriter(file, fieldnames = ["category", "age_group", "price"])
    #    writer.writeheader()

# save data in new csv to see sold tickets        
def save_sale(category, age_group, price):
    file_exist = os.path.isfile(SALES_doc)
    
    with open(SALES_doc, "a", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["category", "age_group", "price"])

        if not file_exist:
            writer.writegheader()
        
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

    BAR_CHAR = "█"
  
    print("\n" + "=" * 80)
    print("       ~*~*~*~*~*~*~*~*~*~ SALES REPORT ~*~*~*~*~*~*~*~*~*~")
    print("=" * 80 + "\n")
    
    report = {}

    for row in sales_data:
        key = (row["category"], row ["age_group"])
        report[key] = report.get(key, 0) +1

    total = 0

    LABEL_WIDTH = 60 #to control where bar its starting
    

    for (cat,age), count in report.items():
        label ="\n" + f"{cat} - {age}: sold {count} tickets"
        bar = BAR_CHAR * count
        print(f"{label:<{LABEL_WIDTH}} | {bar}")

        total += count

    print("\n" + "\n" + f"<<>><<>><<>><<>><<>>  TOTAL SOLD: {total} TICKETS <<>><<>><<>><<>><<>> ")


#Visual functions to future use

#def title(text):
 #   print("\n" + "=" * 80)
  #  print(text.center(80))
   # print("=" * 80 + "\n")
    


# Customer interface program

def customer_interface(data):
    while True:
        print("\n" + "=" * 80)
        print("      ~*~*~*~*~*~*~*~*~*~ CUSTOMER TICKET PURCHASE ~*~*~*~*~*~*~*~*~*~")
        print("=" * 80 + "\n")

#Choosing tickets by category
        categories={}
        for row in data:
              title = row["category_title"]
              desc = row["category_description"]
              if title not in categories:
                  categories[title]=desc
          
        print("Available ticket options:" + "\n")
        category_list=list(categories.keys())

        for i, cat in enumerate(category_list):
              print(f"{i}.{cat}")
              print(f"   {categories[cat]}")
              print()
        while True:
            try:
                choice_cat = int(input("Choose category number: ")) #user input1
                selected_category = category_list [choice_cat] #showing available options
                break
            except:
                print("\n" + "❌ Invalid choice. Please try one more time." + "\n") #wrong choice answer
            
        print("\n" + f"You selected: {selected_category}" + "\n") #showing which category choose

# Choose age type of ticket

        age_groups = set()
        for row in data:
            if row["category_title"] == selected_category:
                   age_groups.add(row["topup_passenger_class_name"])

        age_groups = sorted(list(age_groups))

        print("Please select passenger type:") #age options form csv
        for i, ag in enumerate(age_groups):
               print(f"{i}. {ag}")
        while True:
            try:
                choice_age = int(input("\n" + "Choose passenger type numer: "))  #user input age option
                selected_age = age_groups[choice_age]
                break
            except:
                print("\n" + "❌ Invalid choice. Please try one more time." + "\n") #invalid input answer
                
        print("\n" + f"You selected: {selected_age}" + "\n")  #showing selected option


# Choosing specyfic option of ticket

        ticket_options= [] #storage options
        for row in data:
            if row["category_title"] ==  selected_category and row["topup_passenger_class_name"] == selected_age:
             ticket_options.append(row)

        if not ticket_options: #wrong choice answer
            print("Sorry, no tickets available for this category and passenger type.")
            return

        print("Available ticket options:" + "\n")

        for i, row in enumerate(ticket_options): #printing options
            print(f"{i}.{row['topup_title']}")  
        
            if "topup_description" in row and row["topup_description"]:
                print(f"       {row['topup_description']}") #printing option descriptions
            print()
            
        while True:
            try:
                choice_ticket = int(input("Choose ticket numer:")) #user input2
                selected_ticket=ticket_options[choice_ticket]
                break
            except:
                print("\n" + "❌ Invalid choice. Please try one more time." + "\n") #wrong choice answer
                
    
#show price of choosen ticket in pounds
        price_pence = int(selected_ticket["topup_price_in_pence"])
        price_pounds = price_pence/100

        print("\n" + "=" * 80)
        print("      ~*~*~*~*~*~*~*~*~*~ FINAL TICKET SUMMARY ~*~*~*~*~*~*~*~*~*~")
        print("=" * 80 + "\n")
        print(f"Category: {selected_category}")
        print(f"Passenger type: {selected_age}")
        print(f"Ticket: {selected_ticket['topup_title']}")
        print(f"Price: £{price_pounds:.2f}")
        print("\n" + "=" * 80)
        print("                ~*~*~*~*~*~*~*~*~*~***~*~*~*~*~*~*~*~*~*~*~")
        print("=" * 80 + "\n")

#Buying or cancel

        print("1. Buy ticket")
        print("2. Cancel")

        end_choice = input("Choose option: ")

        if end_choice == "1":
            save_sale(selected_category,selected_age,price_pounds)
            print("\n" + "=" * 80)
            print("~*~*~ Ticket purchased successfully! Thank You! ~*~*~")
            print("=" * 80)
            print(r"""
+----------------------+
|     BUS TICKET       |
|----------------------|
|     NOTTINGHAM       |
|   HAVE A NICE TRIP!  |
+----------------------+
""")
        else:
            print("\n" + "❌ ❌ ❌ Purchase cancelled ❌ ❌ ❌" + "\n")

        again = input ("Do you want to buy another ticket? (y/n): ").lower()

        if again == "y":
            continue
        else:
            print(r"""

  _____                                    ___
    |   |   |    /\    |\   | | /   \   / |   | |   | |
    |   |___|   /  \   | \  | |/     \ /  |   | |   | |
    |   |   |  /----\  |  \ | |\      |   |   | |   | |
    |   |   | /      \ |   \| | \     |   |___| |___| O
""")   

            print(" Returning to main menu...")
        return
        


        
# Admin interface program

def admin_interface(data):
    while True:
        print("\n" + "=" * 80)
        print("         ~*~*~*~*~*~*~*~*~*~ ADMIN PANEL ~*~*~*~*~*~*~*~*~*~")
        print("=" * 80 + "\n")
        print("1. Edit ticket price")
        print("2. Show sales report")
        print("3. Return to main menu")

        while True:
            answer = input("\n" + "Choose option: ")
            if answer in ("1", "2", "3"):
                break
            else:
                print("❌ Invalid choice. Please try one more time.")
    
        if answer == "1":
            for i, row in enumerate(data):
                print("\n" + f"{i}. {row['topup_title']} - {row['topup_price_in_pence']} pence")

            try:
                idx = int(input("\n" + "Please choose ticket number to edit: "))
                new_price_pounds = float(input("\n" + "Enter new price in pounds(£): ")) #creating new price
            except:
                print("❌ Invalid choice. Please try one more time.") #wrong choice message
                continue

            new_price_pence = int(new_price_pounds * 100) # convert new price from pound to pence

            data[idx]["topup_price_in_pence"] = str(new_price_pence)
            print("\n" + "=" * 80)
            print("<<>><<>><<>><<>><<>> ✔️ Pice updated! <<>><<>><<>><<>><<>>" + "\n")
            save_data(data)

        elif answer == "2":
            show_sales_report()

        elif answer == "3":
            return

        else:
            print("❌ Invalid choice. Please try one more time.")

        

#Main menu

def main():
    data = load_data()
   # init_sales() - probably dont need it anymore 

    while True:  #how menu looks
        print("\n" + "=" * 80)
        print("      ~*~*~*~*~*~*~*~*~*~ NOTTINGHAM CITY COUNCIL TICKETS ~*~*~*~*~*~*~*~*~*~")
        print("=" * 80)
        print(r"""                            _______________________
                           |   |  |  |  |  |   |   |
                           |___|__|__|__|__|___|___|
                           |  _     CITY BUS    _  |
                           | | |   _________   | | |_
                           | |_|  |         |  |_|   |
                           |_____|_|_______|_|_______|
                              O                 O
""")
        print("1. CUSTOMER - buy ticket")
        print("2. ADMIN - log in")
        print("3. Exit")

        while True:
            choice = input("Select option:")

            if choice in("1", "2", "3"):
                break
            else:
                print("\n" + "❌ Invalid choice. Please try one more time.")

        if choice == "1":
            customer_interface(data)  #go to customer interface
            
        elif choice == "2": #go to admin interface
            while True:
                password = input("\n" + "Enter admin password (or X for cancel):")
                
                if  password == "admin123":  #admin password
                    admin_interface(data)
                    break
                elif password.lower() == "x":
                    print(r"""

  _____                                    ___
    |   |   |    /\    |\   | | /   \   / |   | |   | |
    |   |___|   /  \   | \  | |/     \ /  |   | |   | |
    |   |   |  /----\  |  \ | |\      |   |   | |   | |
    |   |   | /      \ |   \| | \     |   |___| |___| O
""")   

                    print("Returning to main menu...")
                    break
                else: 
                    print("\n" + "❌ Invalid password. Please try one more time.") # invalid password

        elif choice =="3":
            print("\n" + " ============  ***  Goodbye!!  ***  =========== ")

            break
        

if __name__ == "__main__":
    main()
        
