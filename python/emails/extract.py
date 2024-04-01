import csv

# Replace 'your_input_file.csv' with the path to your actual CSV file
input_file = 'members.csv'
output_file = 'result.csv'

emails = []

# Read the CSV and extract emails
with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 2:  # Ensure the row has enough columns
            emails.append(row[2])  # Append the email which is in the third column

# Write the emails to a new file
with open(output_file, 'w', newline='') as outfile:
    outfile.write(', '.join(emails))

print(f'Extracted emails have been written to {output_file}')

