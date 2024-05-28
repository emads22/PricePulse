import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from the '.env' file into the environment
load_dotenv()

# Retrieve sender's email, password, and receiver's email from environment variables
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

# Define Gmail SMTP server details
GMAIL_HOST = "smtp.gmail.com"
GMAIL_PORT = 587

# Retrieve Nexmo API credentials and phone numbers from environment variables
NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')
SMS_SENDER = os.getenv('SMS_SENDER')
SMS_RECEIVER = os.getenv('SMS_RECEIVER')

# Specify the path to the ChromeDriver executable
# Make sure to download the appropriate ChromeDriver version matching the existing Chrome version
CHROMEDRIVER_PATH = Path("./chromedriver-win64") / "chromedriver.exe"

# List of user agent strings for different browsers and operating systems
# Adding a user-agent in web scraping helps mimic the behavior of a real user's web browser, reducing the chances of being blocked by websites and improving the success rate of scraping operations.
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
]

# Define the product name, URL, XPath, and CSS selector
PRODUCT_NAME = 'Bose Home Speaker 500 - Luxe Silver'
PRODUCT_URL = 'https://www.antaki.com.lb/product/bose-home-speaker-500-luxe-silver/'
PRODUCT_XPATH = '//*[@id="col-248923422"]/div/div/div/div[2]/p/ins/span/bdi'
PRODUCT_SELECTOR = '#col-248923422 > div > div > div > div.price-wrapper > p > ins > span > bdi'

# Define the pattern to extract the product price from the webpage
PRODUCT_PRICE_PATTERN = r'\b\d+(?:\.\d+)?\b'
