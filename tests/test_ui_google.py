from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("SDET job")
    search_box.submit()
    assert "SDET" in driver.title
    driver.quit()
