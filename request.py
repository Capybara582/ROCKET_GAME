import requests
from bs4 import BeautifulSoup


def req(url):
    response = requests.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        },
    )

    soup_parse = BeautifulSoup(response.content, "html.parser")

    text = soup_parse.get_text(strip=False)

    return text
