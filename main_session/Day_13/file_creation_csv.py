import csv

products = [["Product Name","Product code","order details"],
            ["Tooth paste","001","order_87686"],
            ["Tooth brush","001","order_87686"],
            ["soap","001","order_87686"]]

file_path = "output.csv"
try:
    with open(file_path, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in products:
            csvwriter.writerow(row)
        print("File created")
except IOError:
    print("I/O error")


