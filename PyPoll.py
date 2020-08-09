import os
import csv

totalvotes = 0
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0


csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')


with open(csvpath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvfile)

    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Votes Cast
        totalvotes += 1
        
        # Calculate Total Number Of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khanvotes += 1
        elif (row[2] == "Correy"):
            correyvotes += 1
        elif (row[2] == "Li"):
            livotes += 1
        else:
            otooleyvotes += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    kahnpercent = khanvotes / totalvotes
    correypercent = correyvotes / totalvotes
    lipercent = livotes / totalvotes
    otooleypercent = otooleyvotes / totalvotes
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(khanvotes, correyvotes, livotes, otooleyvotes)

    if winner == khanvotes:
        winner_name = "Khan"
    elif winner == correyvotes:
        winner_name = "Correy"
    elif winner == livotes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {totalvotes}")
print(f"---------------------------")
print(f"Kahn: {kahnpercent:.3%}({khanvotes})")
print(f"Correy: {correypercent:.3%}({correyvotes})")
print(f"Li: {lipercent:.3%}({livotes})")
print(f"O'Tooley: {otooleypercent:.3%}({otooleyvotes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahnpercent:.3%}({khanvotes})\n")
    txtfile.write(f"Correy: {correypercent:.3%}({correyvotes})\n")
    txtfile.write(f"Li: {lipercent:.3%}({livotes})\n")
    txtfile.write(f"O'Tooley: {otooleypercent:.3%}({otooleyvotes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
