from data_things import save_sale


# Customer interface program

def customer_interface(data): #customer interface menu
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
                print("\n" + "  ❌ Invalid choice. Please try one more time." + "\n") #wrong choice answer
            
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
                print("\n" + "  ❌ Invalid choice. Please try one more time." + "\n") #invalid input answer
                
        print("\n" + f"You selected: {selected_age}" + "\n")  #showing selected option


# Choosing specyfic option of ticket like bundles/ single trip/ 24h etc.

        ticket_options= [] #storage options
        for row in data:
            if row["category_title"] ==  selected_category and row["topup_passenger_class_name"] == selected_age:
             ticket_options.append(row)

        if not ticket_options: #answer if there is no options for choosen category
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
                print("\n" + "  ❌ Invalid choice. Please try one more time." + "\n") #wrong choice answer
                
    
#show price of choosen ticket in pounds
        price_pence = int(selected_ticket["topup_price_in_pence"])
        price_pounds = price_pence/100

        print("\n" + "=" * 80)
        print("      ~*~*~*~*~*~*~*~*~*~ FINAL TICKET SUMMARY ~*~*~*~*~*~*~*~*~*~")
        print("=" * 80 + "\n")
        print(f"Category: {selected_category}") #print type of ticket
        print(f"Passenger type: {selected_age}") #print age category
        print(f"Ticket: {selected_ticket['topup_title']}") #print details of ticket
        print(f"Price: £{price_pounds:.2f}") #.2f for two places after decimal
        print("\n" + "=" * 80)
        print("                ~*~*~*~*~*~*~*~*~*~***~*~*~*~*~*~*~*~*~*~*~")
        print("=" * 80 + "\n")

#Buying or cancel

        print("1. Buy ticket")
        print("2. Cancel")

        end_choice = input("Choose option: ")

        if end_choice == "1": #if customer buy the ticket
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
            print("\n" + "❌ ❌ ❌ Purchase cancelled ❌ ❌ ❌" + "\n") #if cancelled

        again = input ("Do you want to buy another ticket? (y/n): ").lower()

        if again == "y": #chance to buy another ticket
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
        
