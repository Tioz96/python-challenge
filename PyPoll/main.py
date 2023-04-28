'PyPoll'

import csv
#create variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0
#read csv file
with open('Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  
    #for each row
    for row in csvreader:
        #sum votes
        total_votes += 1
        #set candidate form row 2
        candidate = row[2]
        # if candidate not exist dont count the vote
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1
#print in terminal
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
for candidate in candidates:
    vote_percentage = candidates[candidate] / total_votes * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({candidates[candidate]})")
    if candidates[candidate] > winner_votes:
        winner = candidate
        winner_votes = candidates[candidate]
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")
#print in txt file
with open('analysis/election_results.txt', 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("----------------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("----------------------------------------\n")
    for candidate in candidates:
        # Calculate the percentage of votes each candidate won
        vote_percentage = candidates[candidate] / total_votes * 100
        textfile.write(f"{candidate}: {vote_percentage:.3f}% ({candidates[candidate]})\n")
        # Determine the winner based on popular vote
        if candidates[candidate] > winner_votes:
            winner = candidate
            winner_votes = candidates[candidate]
    textfile.write("----------------------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("----------------------------------------\n")