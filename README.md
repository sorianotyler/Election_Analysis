# Election_Analysis
Python program to analyze election data

## Overview of Project
 The objective of this project was to summarize all of the election data using python   
### Purpose
    The purpose of this challenge was to practive importing CSV files using python, to extract the nessisary data for the election audit. We wanted to determine the winner of the election as well as some voter data (by county)

 
## Results 
### Election results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)

    -------------------------
    Largest county Turnout: Denver
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------
   


## Summary 

### Proposal to use this code for future elections
    This script can be used for any election with a few changes. We would simply change the file to upload path whatever CSV file holds our new election data. However, this might take awhile if the dataset is much larger. The way we do things now, we loop through the dataset more than once.I would also propose that we collect the data through one passing counting for county and for candidate. This would speed up the progam making it an even better to use for future elections. 
