from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.amazon.in/product-reviews/B07MZG27XK"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

# wait until reviews load
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-hook='review']")))

reviews_data = []

reviews = driver.find_elements(By.CSS_SELECTOR, "div[data-hook='review']")

print(f"Reviews found: {len(reviews)}")  # DEBUG LINE

for review in reviews:
    try:
        rating = review.find_element(By.CSS_SELECTOR, "i[data-hook='review-star-rating']").text
    except:
        rating = None

    try:
        title = review.find_element(By.CSS_SELECTOR, "a[data-hook='review-title']").text
    except:
        title = None

    try:
        body = review.find_element(By.CSS_SELECTOR, "span[data-hook='review-body']").text
    except:
        body = None

    try:
        date = review.find_element(By.CSS_SELECTOR, "span[data-hook='review-date']").text
    except:
        date = None

    reviews_data.append({
        "rating": rating,
        "title": title,
        "body": body,
        "date": date
    })

driver.quit()

for i, r in enumerate(reviews_data, 1):
    print(f"\nReview {i}")
    for k, v in r.items():
        print(f"{k}: {v}")
