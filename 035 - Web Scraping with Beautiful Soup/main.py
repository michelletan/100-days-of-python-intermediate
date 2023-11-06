from bs4 import BeautifulSoup
import requests

TARGET_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
TARGET_FILEPATH = "./movies.txt"

try:
    response = requests.get(TARGET_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    title_tags = soup.find_all(name="h3", class_="title")

    title_text = [t.getText() for t in title_tags]
    title_text.reverse()

    with open(TARGET_FILEPATH, "w") as f:
        f.writelines(s + "\n" for s in title_text)

except requests.exceptions.RequestException as e:
    raise SystemExit(e)
