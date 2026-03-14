from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_google():
    # Setup driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # run headless for automation environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # SeleniumManager auto-resolves compatible driver for installed Chrome.
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.google.com")

        assert "Google" in driver.title

        # Additional check: ensure search box exists
        search_box = driver.find_element(By.NAME, "q")
        assert search_box is not None

    finally:
        driver.quit()


if __name__ == "__main__":
    test_open_google()
    print("Google open validation passed")
