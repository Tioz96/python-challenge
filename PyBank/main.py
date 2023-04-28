import csv

# Read .cvs file
with open('Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

#create variables
    total_months = 0
    net_total = 0
    prev_profit = 0
    changes = []
    max_increase = 0
    max_decrease = 0

#for each row in csv file do:
    for row in csvreader:
        #add 1 to months total for each row
        total_months += 1
        #add the actual value to sum or rest depends on profit/losses
        net_total += int(row[1])
        #compare with last row to get max increase and decrease
        if prev_profit != 0:
            change = int(row[1]) - prev_profit
            changes.append(change)
        #get same row for max increase and max decrease
            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]
            elif change < max_decrease:
                max_decrease = change
                max_decrease_month = row[0]

        prev_profit = int(row[1])
        #set average
    avg_change = sum(changes) / len(changes)
#print in terminal
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")
#print in txt file
with open('analysis/financial_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${round(avg_change, 2)}\n")
    textfile.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

