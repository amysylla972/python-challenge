import os
import csv

totalmonths = 0
netamount = 0
monthlychange = []
monthcount = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0




csvpath = os.path.join("..", "Resources",'budget_data.csv')



with open(csvpath, newline='') as csvfile:
    

   with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    row = next(csvreader)
    

    p_row = int(row[1])
    totalmonths += 1
    netamount += int(row[1])
    greatestincrease = int(row[1])
    greatestincrease_month = row[0]
    
    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Months Included In Dataset
        totalmonths += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        netamount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenuechange = int(row[1]) - p_row
        monthlychange.append(revenuechange)
        p_row = int(row[1])
        monthcount.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthlychange)/ len(monthlychange)
    
    highest = max(monthlychange)
    lowest = min(monthlychange)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${netamount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify File To Write To
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${netamount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
