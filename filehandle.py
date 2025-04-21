favorite_subjects = {
    "Aryan Colst": "Science",
    "Harold Das": "Mathematics",
    "Leo Das": "English",
    "Antony Das": "History",
    "Roy James": "Geography",
}

# Open and read file
file = open("Codingal.txt", "r")
lines = file.readlines()
file.close()

# Update the favorite subject directly
for i in range(1, len(lines)):  # Skip the header line
    parts = lines[i].strip().split(",")
    if parts[0] in favorite_subjects:
        parts[3] = favorite_subjects[parts[0]]  # Set the favorite subject
    lines[i] = ",".join(parts)  # Join the parts back into a line

# Open the file again and write the updated lines
file = open("students.csv", "w")
file.writelines(lines)
file.close()

print("Favorite subjects updated successfully!")
