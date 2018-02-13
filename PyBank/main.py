# PyBank
# Revenue
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The total amount of revenue gained over the entire period

# The average change in revenue between months over the entire period

# The greatest increase in revenue (date and amount) over the entire period

# The greatest decrease in revenue (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dependencies
import os
import csv
import pandas as pd
import moment
from datetime import datetime
import random


# Create output file name
file_output_name = "budget_data_output.csv"
file_input_name = input("Enter file name: " ) + ".csv"
bank_csvpath = os.path.join(file_input_name)

# Create DF from Pandas
df = pd.read_csv(bank_csvpath)

# Find the range of Revenue [lowest, highest]

# Maximum Values
max_revenue = max(df.iloc[:,1])
max_index = df.loc[df['Revenue']==max_revenue].index
max_date = df.iloc[max_index, 0]

# Minimum Values
min_revenue = min(df.iloc[:,1])
min_index = df.loc[df['Revenue']==min_revenue].index
min_date = df.iloc[min_index, 0]

# Total Revenue
tot_revenue = sum(df.iloc[:,1])
# List to store change in revenues over the period
Avg_Range = []
# Open the file
with open(bank_csvpath, newline = "", encoding = 'utf-8') as bankfile:
    bank_reader = csv.reader(bankfile, delimiter = ",")
    neg_counter = 0
    # Skip header line
    next(bank_reader, None)

# Calculate average rate of change in Revenue
    tot_months = len(list(bank_reader)) + 1
    for i  in range(1,tot_months-2):
        Rev_change = (df.iloc[i+1, 1] - df.iloc[i, 1])
        Avg_Range.append(Rev_change)
    Avg_ROC = (sum(Avg_Range))/(tot_months-1)
    ChangeInRevenue = Avg_ROC

# Range of profits or losses (Chane as needed)
range_revenue = [int(min_revenue), int(max_revenue)]

print("FINANCIAL ANALYSIS")
print("-----------------------------------")
print("Total Months: " + str(tot_months))
print("Total Revenue: " + "${:.2f}".format(tot_revenue))
print("Average Revenue Change: " + "${:.2f}".format(ChangeInRevenue))
print("Greatest Increase in Revenue: " + max_date + " " + "${:,}".format(max_revenue))
print("Greatest Decrease in Revenue: " + min_date + " " + "${:,}".format(min_revenue))
print("--------------------------------------------------------")
# print(max_revenue)
# print(min_revenue)
# print(min_date)
# print(max_date)
# print(Avg_Range)

with open("Output.txt", "w") as text_file:
    print("FINANCIAL ANALYSIS\n -----------------------------------\nTotal Months: " + str(tot_months) + "\nTotal Revenue: " + "${:.2f}".format(tot_revenue) + "\nAverage Revenue Change: " + "${:.2f}".format(ChangeInRevenue) + "\nGreatest Increase in Revenue: " + max_date + " " + "${:,}".format(max_revenue) + "\nGreatest Decrease in Revenue: " + min_date + " " + "${:,}".format(min_revenue) + "\n--------------------------------------------------------\n"    , file=text_file)