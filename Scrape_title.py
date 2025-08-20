import requests
from bs4 import BeautifulSoup

# Step 1: URL of the webpage
url = "https://www.python.org/"

# Step 2: Send a request to get the webpage content
response = requests.get(url)

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Get the title tag
title = soup.title.string

# Step 5: Save the title to a file
with open("webpage_title.txt", "w", encoding="utf-8") as file:
    file.write(title)

print(f"✅ Title saved: {title}")
