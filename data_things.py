import csv
import os


CSV_doc="mobile_products.csv"  #csv with data
SALES_doc="sale_list.csv"   #new csv

# Load data from CSV
def load_data():
    try:
        with open (CSV_doc) as file:
            reader= csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:  #if there is no csv file, inform user about it
        print("\n" + f"  ❌ Warning: {CSV_doc} not found. Starting with empty dataset.")
        return[] #return with empty list to continue program
    
    except Exception as e: #any other errors 
        print("\n" + f"  ❌ Error reading {CSV_doc}: {e}") #will show saved error as e
        return[]
    
# save data in csv with ticket informations

def save_data(data):
    try:
        with open(CSV_doc, "w", newline="") as file:
            writer=csv.DictWriter(file,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(" <<>><<>><<>><<>><<>> ✔️ Data saved successfully! <<>><<>><<>><<>><<>> ")
    except Exceptions as e:
        print("\n" + f"  ❌ Error saving {CSV_doc}: {e}") #showig saved error like e


# save data in new csv to see sold tickets        
def save_sale(category, age_group, price):
    file_exist = os.path.isfile(SALES_doc)
    
    try:
        with open(SALES_doc, "a", newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["category", "age_group", "price"])

            if not file_exist:
                writer.writegheader()
        
            writer.writerow({
                "category": category,
                "age_group": age_group,
                "price": price
                })
    except Exceptions as e:
        print("\n" + "  ❌ Error saving sale to {SALES_doc}:{e}") #showing error message
        return []
