import csv
from data_things import SALES_doc

#Showing sales report in admin menu

def show_sales_report():
    with open(SALES_doc, newline="") as file:
            reader=csv.DictReader(file) #reading file 
            sales_data = list(reader)
            
    if not sales_data: #if there is no sales data
        print("No sales recorded yet!")
        return

    BAR_CHAR = "█" #setting bar to showing sale progress
  
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
