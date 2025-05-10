import requests
from bs4 import BeautifulSoup

# URLs for defense system and aircraft information
urls = [
    "https://www.jagranjosh.com/general-knowledge/complete-list-of-indian-air-defence-system-1746352839-1",
    "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft",
    "https://www.defencexp.com/full-list-of-indian-air-defence-systems/"
]

def fetch_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join([p.text for p in paragraphs[:5]])  # Fetch first 5 paragraphs
    return "Failed to retrieve data."

# Fetch information from each source
for url in urls:
    print(f"Information from {url}:\n")
    print(fetch_info(url))
    print("\n" + "-"*50 + "\n")

# Image sources
image_urls = [
    "https://www.iadb.in/2021/12/29/made-in-india-aerospace-capabilities/",
    "https://www.indiatimes.com/news/india/combat-aircraft-of-indian-air-force-362948.html"
]

print("Images related to India's defense system and aircraft:")
for img_url in image_urls:
    print(img_url)
