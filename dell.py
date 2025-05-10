import requests
from bs4 import BeautifulSoup

# URL for top MBA colleges in India
url = "https://collegedunia.com/top-mba-colleges-in-india"

def fetch_college_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        colleges = soup.find_all("h2")  # Extracting college names
        return [college.text for college in colleges[:10]]  # Fetch top 10 colleges
    return "Failed to retrieve data."

# Fetch and display top MBA colleges
top_colleges = fetch_college_info(url)
print("Top MBA Colleges in India:")
for idx, college in enumerate(top_colleges, 1):
    print(f"{idx}. {college}")
