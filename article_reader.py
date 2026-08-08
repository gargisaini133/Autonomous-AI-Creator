import requests
from bs4 import BeautifulSoup


def read_article(url):
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        article_text = " ".join(
            paragraph.get_text(" ", strip=True)
            for paragraph in paragraphs
        )

        return article_text[:6000]

    except Exception:
        return ""   