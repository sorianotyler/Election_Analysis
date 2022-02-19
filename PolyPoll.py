# The data we need to retrive 
# 1. Total number of votes casted
# 2. A complete list of Candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each cadidate won 
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
#import datetime as dt
#from distutils import text_file
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes= {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count.
            candidate_votes[candidate_name] += 1
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:   

        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        winning_count = float(0)
        winning_percentage = float(0)
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]

            vote_percentage = float(votes) / float(total_votes) * 100

            format_percentage = "{:.2f}".format(vote_percentage) # code taken from https://pythonguides.com/python-print-2-decimal-places/#:~:text=In%20Python%2C%20to%20print%202,float%20with%202%20decimal%20places.

            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            # Print the winning candidate's results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
        

    # Close the file.
    election_data.close()