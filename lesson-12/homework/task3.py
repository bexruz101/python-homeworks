import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.demoblaze.com")
time.sleep(3)


laptops_category = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_category.click()
time.sleep(3)

laptops_data = []


def scrape_laptops():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    laptop_items = soup.find_all("div", class_="card-block")

    for item in laptop_items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()

        laptops_data.append({"name": name, "price": price, "description": description})


scrape_laptops()


while True:
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)
        scrape_laptops()
    except:
        break


driver.quit()


with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops_data, f, indent=2, ensure_ascii=False)

print("Laptop data has been successfully saved to laptops.json!")
