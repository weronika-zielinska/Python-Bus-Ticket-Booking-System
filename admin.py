from data_things import save_data
from sales import show_sales_report

# Admin interface program

def admin_interface(data): #admin interface menu after log in
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
                print("  ❌ Invalid choice. Please try one more time.") #invalid choice
    
        if answer == "1":  #show all ticket options to change prices
            for i, row in enumerate(data):
                print("\n" + f"{i}. {row['topup_title']} - {row['topup_price_in_pence']} pence")

            while True:  # choice ticket to change price
                try:
                    idx = int(input("\n" + "Please choose ticket number to edit: "))

                    if idx < 0 or idx >= len(data): #if its out of range (count postitions from excel)
                        print(f"  ❌ Ticket number out of the range. Please select again (0-{len(data)-1}).")
                        continue
                        #new price setting
                    new_price_pounds = float(input("\n" + "Enter new price in pounds (£ - Use a number with a dot for decimal):")) #creating new price
                    break 
                
                except ValueError: #any diffrent answer than number
                    print(f"  ❌ Invalid choice. Please select number (0-{len(data)-1}).") #wrong choice message
                    continue

            new_price_pence = int(new_price_pounds * 100) # convert new price from pound to pence

            data[idx]["topup_price_in_pence"] = str(new_price_pence)
            print("\n" + "=" * 80)
            print("<<>><<>><<>><<>><<>> ✔️ Pice updated! <<>><<>><<>><<>><<>>" + "\n")
            save_data(data)

        elif answer == "2": # go to show sales function
            show_sales_report()

        elif answer == "3": #return to main menu interface
            return

        else:
            print("  ❌ Invalid choice. Please try one more time.") #if wrong choice
