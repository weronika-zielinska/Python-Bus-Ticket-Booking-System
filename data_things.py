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
