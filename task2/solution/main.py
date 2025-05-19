from bs4 import BeautifulSoup
import requests
import csv

alphabet = [chr(i) for i in range(ord("А"), ord("Я") + 1)]

def parse_animals_by_letter(alphabet=alphabet, url=None):
    count_category = {s: 0 for s in alphabet}
    
    for s in alphabet:
        url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from={s}"
        page = requests.get(url, timeout=2)
        soup = BeautifulSoup(page.text, "html.parser")

        while True:
            animals = (
                soup.find("div", id="mw-content-text", class_="mw-body-content")
                .find("div", class_="mw-category mw-category-columns")
                .find("div", class_="mw-category-group")
                .find_all("li")
            )
            if animals[0].string[0] != s:
                break

            count_category[s] += len(animals)

            href_next_page = (
                soup.find("div", id="mw-content-text", class_="mw-body-content")
                .find("div", id="mw-pages")
                .find("a", string="Следующая страница")
            )
            if href_next_page is None:
                break
            url_next_page = f"https://ru.wikipedia.org/{str(href_next_page['href'])}"
            page = requests.get(url_next_page, timeout=2)
            soup = BeautifulSoup(page.text, "html.parser")

    return count_category

with open("beasts.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    animals = parse_animals_by_letter()
    for letter, amount in animals.items():
        writer.writerow([letter, amount])
