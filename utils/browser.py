from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-logging')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=1280,720')
    options.add_argument('--log-level=3')
    
    try:
        service = Service()
        return webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Error setting up WebDriver: {str(e)}")
        return None