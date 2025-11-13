import csv

print("Welcome to the NCTX Bus Ticket Application")

filename ='mobile_products.csv'

header= []
rows= []

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header=next(csv_reader)
    for row in csv_reader:
        rows.append(row)


print("The columns are:")
for i in range(len(header)):
    print(f"{i}: ", header[i])

userChoice = input("Pick a field: ")

for i in range(len(header)):
     if userChoice == header[i]:
         print("You have to choosen: ",header[i])
