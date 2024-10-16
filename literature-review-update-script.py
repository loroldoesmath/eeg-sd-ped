import csv
import requests

# Google Sheets CSV export URL
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSOl0G8Ad01Jn8nxF1VuEl0_Xivzw0GvPMVKZTHnDmGK9X-u6OS3-gdIQx736sFXRvNUoUXj1nUxYai/pub?output=csv"
response = requests.get(url)
data = response.text.splitlines()

# Read CSV
reader = csv.reader(data)
markdown_table = "| Paper | Author(s) or Institution | Key Takeaways | Status |\n"
markdown_table += "|-------|--------------------------|---------------|--------|\n"

for row in reader:
    markdown_table += f"| {' | '.join(row)} |\n"

# Write the markdown to literature-review
with open("literature-review", "w") as file:
    file.write(markdown_table)

print("literature-review has been updated with the latest table from Google Sheets.")