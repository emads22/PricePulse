import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


# Retrieve sender's email and password and receiver email from environment variables
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

GMAIL_HOST = "smtp.gmail.com"
GMAIL_PORT = 587

# Retrieve Nexmo API credentials and phone numbers from environment variables
NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')
SMS_SENDER = os.getenv('SMS_SENDER')
SMS_RECEIVER = os.getenv('SMS_RECEIVER')

# Specify the path to the ChromeDriver executable
# Make sure to download the appropriate ChromeDriver version matching existing Chrome version
CHROMEDRIVER_PATH = Path("./chromedriver-win64") / "chromedriver.exe"

# base url for Zagreb Stock Exchange, Inc. in Croatia
AMAZON_PS5_URL = """https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_5?dib=eyJ2IjoiMSJ9.IBzp2a7hJYOBBKGDpX2BCBZIe10lLXszNLfnztCx6bAq0UShs9DXhtmLQjoKISKsm7JrXtSWVwMBPPKEWGvz-B7JZIuROeCaoWtJL72JD246bfMqlyvN5lLVD0_e0IPrTEw6uEpo2vCQVBhSjdXNOt3J1nhtxz9LwyWCCOiO4xBDv76iIBgFazV82hxiQJUjXwW-hD4zbazuj_-F_sPgTcDxoHvZvekjYGmhrPLuciE.Ngo1tZgGSthRL7xZ6mrAdJ-np77QxaZwXnfGrYplVBQ&dib_tag=se&keywords=ps5&qid=1716817428&sr=8-5&th=1"""

PS5_PRICE_SELECTOR = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole"
