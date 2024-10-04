from playwright.sync_api import sync_playwright
import os
import yaml
import time
from scripts.infoBarManager import closeInfoBar

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


def login():
    print("Logging in with the username and password")
    username = config['login']['username']
    password = config['login']['password']

    page.get_by_label("Email").fill(username)
    page.get_by_label("Password").fill(password)

    page.click('text="Log in"')

    time.sleep(5)

    # If I get a email verification
    if (page.url == 'https://etseclipse.monday.com/auth/login_monday/new_login_detected'):
        newLogin()


# https://etseclipse.monday.com/auth/login_monday/new_login_detected
# This methods ask for the link sent by email
# TODO Test me
def newLogin():
    # Need to check the link to make a if to reach here
    link = input("Please paste the new login link")
    page.goto(link)

# This methods repeat the closing process of the InfoBar
def closeTheInfoBar():
    while True:
        try: 
            closeInfoBar()
            break
        except Exception as e:
            print('Image not found retrying')
            print(e)
            time.sleep(5)

with sync_playwright() as p:
    # Local data for cache preservation
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path, "MondayDash\\User Data\\Default")

    context = p.chromium.launch_persistent_context(user_data_path, headless=False, args=["--start-fullscreen", "--force-dark-mode", "--hide-crash-restore-bubble"], no_viewport=True)

    page = context.pages[0]
    page.goto(config['url']['dashboard'])

    # Get the title of the page
    title = page.url

    # Check if user is already logged in
    if (title == "https://etseclipse.monday.com/auth/login_monday/email_password"):
        print(title)
        print(page.title())
        login()

    time.sleep(5)
        
    div_element = page.query_selector('div.ncYkm W6y9_ mLsJc')
    if div_element:
        # Get the 'style' attribute of the div
        style_attr = div_element.get_attribute('style')
        if style_attr and 'width: 255px' in style_attr:
            page.keyboard.press('Control+.')
    

    time.sleep(1)

    closeTheInfoBar()


    # Keep the window open
    input("Press Enter to close the browser...")