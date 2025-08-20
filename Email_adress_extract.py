import re

input_file = "general.txt"

# Step 2: Read the file content
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Step 3: Find all email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Step 4: Save emails to another file
with open("emails.txt", "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print(f"✅ Found {len(emails)} emails and saved them to emails.txt")
