import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request

url = "https://glovoapp.com/ng/en/lagos/food_1/"
response = requests.get(url)

# Check the response status code
print("Response Status Code:", response.status_code)



# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Print the prettified HTML
print(soup.prettify())


# Find all <h3> tags with specified attributes and extract their texts
links = soup.find_all("h3", attrs={"data-test-id": True, "class":"store-card__footer__title"})

for link in links:
    print("Link:", link.get_text(strip=True))
