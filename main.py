# %%
#End output should look like this 
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# %%
#import libraries
from pathlib import Path
import csv

# %%
#Set file path
csv_path = Path('budget_data.csv')

#initialize variables
total_months = 0
total_pnl = 0
max_increase = 0
max_decrease = 0
max_incr_month = ''
max_dcr_month = ''


# %%

#Read CSV
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

#set header 
    csv_header = next(csv_reader)

#iterate through the csv to calculate metrics
    
    for row in csv_reader:
        total_months += 1
        total_pnl += int(row[1])

        if int(row[1]) > max_increase and int(row[1]) > 0:
            max_increase = int(row[1])  
            max_incr_month = row[0]
        elif int(row[1]) < max_decrease and int(row[1]) < 0:
            max_decrease = int(row[1])
            max_dcr_month = row[0]

    average = total_pnl / total_months
    rounded_avg = round(average, 2)
            


# %%
#Print Results to terminal
print('Financial Analysis')
print('----------------------')   
print(f'Total Months: {total_months}')
print(f'Total Profit/Loss: ${total_pnl}')
print(f'Average  Change: ${rounded_avg}')
print(f'Greatest Increase in Profits: {max_incr_month} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_dcr_month} (${max_decrease})')

# %%
#Write results to .txt file
with open('calculated_metrics.txt', 'w') as results:
    results.write('Financial Analysis\n')
    results.write('----------------------\n')   
    results.write(f'Total Months: {total_months}\n')
    results.write(f'Total Profit/Loss: ${total_pnl}\n')
    results.write(f'Average  Change: ${rounded_avg}\n')
    results.write(f'Greatest Increase in Profits: {max_incr_month} (${max_increase})\n')
    results.write(f'Greatest Decrease in Profits: {max_dcr_month} (${max_decrease})\n')


