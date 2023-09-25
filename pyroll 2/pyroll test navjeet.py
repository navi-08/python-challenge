import csv
import os

# Define the file path
file_path = r'C:\Users\navje\OneDrive\Desktop\data_analysis\Starter_Code\PyPoll\Resources\election_data.csv'

#open and read the file, handle FileNotFoundError if it occurs
try:
    with open(file_path, 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

# Correctly define the path to the CSV file
election_data = file_path

#lists and counters
# List to store candidate names
candidates = []      
 # List to store the number of votes each candidate receives
num_votes = []      
# List to store the percentage of total votes each candidate garners
percent_votes = []   
 # Counter for the total number of votes
total_votes = 0     

# Open and read the CSV file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   # Read and store the CSV header
    csv_header = next(csvreader)  

    # Iterate through each row of the CSV
    for row in csvreader:
     # Increment the total votes counter
        total_votes += 1  

        # Check if the candidate is not in the list of candidates
        if row[2] not in candidates:
             # Add the candidate to the list
            candidates.append(row[2]) 
            index = candidates.index(row[2])
            # Initialize their vote count to 1
            num_votes.append(1)  
        else:
            index = candidates.index(row[2])
            # Increment the candidate's vote count

            num_votes[index] += 1  
# Calculate and add the percentage of votes for each candidate
for votes in num_votes:
    percentage = (votes / total_votes) * 100
# Round to 3 decimal places
    percentage = round(percentage, 3) 
# Format as a string with 3 decimal places 
    percentage = "{:.3f}%".format(percentage)  
    percent_votes.append(percentage)

# Find the winning candidate
max_votes = max(num_votes)
index = num_votes.index(max_votes)
winning_candidate = candidates[index]

# Display results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")

#candidates and display their names, percentages, and vote counts
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})")

    print("--------------------------")
    print(f"Winner: {winning_candidate}")
    print("--------------------------")

# Export results to a .txt file
output_path = os.path.join("output.txt")

with open(output_path, "w") as output:
    lines = [
        "Election Results",
        "--------------------------",
        f"Total Votes: {total_votes}",
        "--------------------------"
    ]
    output.write('\n'.join(lines) + '\n')

    #candidates and write their information to the file
    for i in range(len(candidates)):
        line = f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})"
        output.write(line + '\n')

    lines = [
        "--------------------------",
        f"Winner: {winning_candidate}",
        "--------------------------"
    ]
    output.write('\n'.join(lines) + '\n')

print(f"Results exported to {output_path}")
