#  The data we need to retrieve.
#  1. The total number of votes cast
#  2. a complete list of candidates who received votes
#  3. the percentage of votes each candidate won
#  4. the total number of votes each candidate won
#  5.  the winner of the election based on popular vote

count = 7

while count < 1:
    print("Hello")

### Datetime module

# Import the datetime class from the date time module

import datetime

# use the now() attribute on the datetime class to get the present time.

now = datetime.datetime.now()

# Print the present time.

print("The time right now is  ", now)

##### abbreviated alias for the datetime module

# Import the datetime class from the date time module

import datetime as dt

# use the now() attribute on the datetime class to get the present time.

now = datetime.datetime.now()

# Print the present time.

print("The time right now is  ", now)

# Assign a variable for the file to load and the path.

file_to_load = "Resources/election_results.csv"

# Open the election results and read the file.

election_data = open(file_to_load, "r")

# To do: perform analysis.

# Close the file.

election_data.close()



    