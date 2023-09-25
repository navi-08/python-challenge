import csv

# Define the file path where your CSV data is located
file_path = r'C:\Users\navje\OneDrive\Desktop\data_analysis\python-challenge\budget_data.csv'

# Initialize variables to keep track of financial data
total_months = 0
net_profit_loss = 0
changes = []

# Open and read the CSV file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    header = next(csv_reader)

    # Loop through each row in the CSV
    for row in csv_reader:
        # Count the total number of months
        total_months += 1

        # Calculate the net profit/loss
        net_profit_loss += int(row[1])

        # Save the monthly changes in a list
        changes.append(int(row[1]))

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding months for the increase and decrease
greatest_increase_month = header[0]
greatest_decrease_month = header[0]

# Display the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Optionally, you can save the results to a text file
with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_profit_loss}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")



    
