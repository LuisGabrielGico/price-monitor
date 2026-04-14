from selenium import webdriver
from selenium.webdriver.common.by import By

def start_browser():
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=options)
    return driver

def get_books():
    driver=start_browser()
    driver.get("https://books.toscrape.com")
    books=driver.find_elements(By.CLASS_NAME, "product_pod")

    data=[]
    for book in books:
        title=book.find_element(By.TAG_NAME, "h3").text
        price=book.find_element(By.CLASS_NAME, "price_color").text
        link=book.find_element(By.TAG_NAME, "a").get_attribute("href")

        data.append({
            "title": title,
            "price": price,
            "link": link
        })

    driver.quit()
    
    return data