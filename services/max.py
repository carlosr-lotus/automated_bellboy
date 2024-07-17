from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def access(user_email: str, user_password: str):
    # User credentials
    USER_EMAIL = user_email 
    USER_PASSWORD = user_password 

    # Open link using Firefox browser
    driver = webdriver.Firefox()
    driver.get("https://www.max.com/br/pt")

    # Access Max index page
    assert "Max" in driver.title
    login_link = driver.find_element(By.CSS_SELECTOR, 'div.d-none:nth-child(3) > div:nth-child(1) > a:nth-child(1)')
    login_link.send_keys(Keys.ENTER)

    # Click on 'accept all cookies' button
    try:
        cookies_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))
        )

        cookies_option.click()
    finally:
        print('Cookies accepted.')
        
    # Fetch input tag for email
    user_email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of(
            (driver.execute_script
                ("return document.querySelector('gi-login-username-and-mvpd').shadowRoot.querySelector('gi-login-username').shadowRoot.querySelector('gi-track-analytics-events').querySelector('#login-username-input')")
            )
        )
    )

    # Add user EMAIL to input field
    user_email_input.send_keys(USER_EMAIL)

    # Fetch input tag for password
    user_password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of(
            (driver.execute_script
                ("return document.querySelector('gi-login-username-and-mvpd').shadowRoot.querySelector('gi-login-username').shadowRoot.querySelector('gi-track-analytics-events').querySelector('#login-password-input')")
            )
        )
    )

    # Add user PASSWORD to input field
    user_password_input.send_keys(USER_PASSWORD)

    # Find button to log in to website
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of(
            (driver.execute_script
                ("return document.querySelector('gi-login-username-and-mvpd').shadowRoot.querySelector('gi-login-username').shadowRoot.querySelector('gi-track-analytics-events').querySelector('.button')")
            )
        )
    )

    # Click login button
    login_button.click()

    print('Success!')

    assert "No results found." not in driver.page_source