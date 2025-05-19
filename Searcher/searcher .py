from typing import List
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/articles/"

def get_articles():
    response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        print(f"Ошибка подключения [{response.status_code}]")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')  # все статьи на странице

    # список статей 
    result: List[str] = []

    for article in articles:
        title_tag = article.find('h2')  # Заголовок
        title = title_tag.text.strip() if title_tag else 'Без названия'
        preview = article.find(class_='article-formatted-body').get_text(strip=True).lower() if article.find(class_='article-formatted-body') else ''
        date = article.find('time')['datetime'] if article.find('time') else 'Неизвестно'
        link_tag = article.find('a', class_='tm-article-snippet__title-link')  # Ссылка
        link = f"https://habr.com{link_tag['href']}" if link_tag else 'Ссылка отсутствует'

        # создание списка по ттегам
        if any(keyword in preview for keyword in KEYWORDS) or any(keyword in title.lower() for keyword in KEYWORDS):
            result.append(f"{date} – {title} – {link}")

    if result:
        print("Найденные статьи:")
        for item in result:
            print(item)
    else:
        print("По вашему запросу стать и не найдены.")

if __name__ == "__main__":
    get_articles()
