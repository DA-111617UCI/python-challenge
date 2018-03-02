# Import required packages
import csv
import datetime

# Files to load and output (Remember to change these)
file_to_load = "raw_data/employee_data2.csv"
file_to_output = "analysis/employee_data_reformatted2.csv"

# Dictionary of states with abbreviations
us_states = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
employee_ids = []
employee_first_names = []
employee_last_names = []
employee_dobs = []
employee_ssns = []
employee_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.DictReader(emp_data)

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:

        # Grab emp_ids and store it into a list
        employee_ids = employee_ids + [row["Emp ID"]]

        # Grab names, split them, and store them in a temporary variable
        split_name = row["Name"].split(" ")

        # Then save first and last name in separate lists
        employee_first_names = employee_first_names + [split_name[0]]
        employee_last_names = employee_last_names + [split_name[1]]

        # Grab DOB and reformat it
        reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")

        # Then store it into a list
        employee_dobs = employee_dobs + [reformatted_dob]

        # Grab SSN and reformat it
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        # Then store it into a list
        employee_ssns = employee_ssns + [joined_ssn]

        # Grab the states and use the dictionary to find the replacement
        state_abbrev = us_states[row["State"]]

        # Then store the abbreviation into a list
        employee_states = employee_states + [state_abbrev]

# Zip all of the new lists together
empdb = zip(employee_ids, employee_first_names, employee_last_names,
            employee_dobs, employee_ssns, employee_states)

# Write all of the election data to csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)