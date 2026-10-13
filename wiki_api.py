import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

print("Привет, это моя не первая попытка сделать что либо с использованием API, но первая поптыка с API Википедии!")

req = requests.Session()
req.headers.update({
    "User-Agent": "wiki_api"
})

req.mount('https://', HTTPAdapter(max_retries=10))

print("Введи имя станицы которую хочешь получить из википедии: ")
requests_title = input()
try:
    response = req.get(f'https://ru.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&format=json&titles={requests_title}')

    data = response.json()
    pages = data["query"]["pages"]
    for page in pages:
        actual_page =pages[f"{page}"]
        print(f"{actual_page['title']}")
        html = actual_page['extract']
        soup = BeautifulSoup(html, "html.parser")
        print(soup.get_text(" ", strip=True))
except Exception as e:
    print(f"Произошла ошибка: {e}.")
