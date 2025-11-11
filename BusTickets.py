import csv

print("Welcome to the NCTX Bus Ticket Application")

filename ='mobile_products.csv'

fields= []
rows= []

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    fields=next(csv_reader)
    for row in csv_reader:
        rows.append(row)


print("The columns are:")
for i in range(len(fields)):
    print(f"{i}: ", fields[i])

userChoice = input("Pick a field: ")

for i in range(len(fields)):
     if userChoice == fields[i]:
         print("You have to choosen: ",field[i])
