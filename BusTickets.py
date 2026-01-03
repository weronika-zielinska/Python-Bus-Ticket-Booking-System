from data_things import load_data, save_data, save_sale
from sales import show_sales_report
from customer import customer_interface
from admin import admin_interface



#Main menu

def main():
    data = load_data()

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
                print("\n" + "  ❌ Invalid choice. Please try one more time.")

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
                    print("\n" + "  ❌ Invalid password. Please try one more time.") # invalid password

        elif choice =="3":
            print("\n" + " ============  ***  Goodbye!!  ***  =========== ")

            break
        

if __name__ == "__main__":
    main()
        
