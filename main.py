import requests
import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_driver import chrome_web_driver
from bs4 import BeautifulSoup
from lxml import etree
from send_email import send_email
from app_utils import get_random_user_agent, generate_price_update_email
from constants import *


def get_product_price_selenium():
    """
    Function to scrape product price using Selenium WebDriver.

    Returns:
        float: The price of the product.

    Raises:
        Exception: If any error occurs during the process.
    """
    try:
        # Create Chrome WebDriver instance
        chrome = chrome_web_driver(url=PRODUCT_URL)

        # Wait for the page to load completely
        # Initialize WebDriverWait with a timeout of 10 seconds (maximum time limit to wait for the page to load completely or for the desired element to be located before 'TimeoutException')
        wait = WebDriverWait(chrome, 10)
        # Wait until the presence of the price element is located on the webpage using XPath
        # EC.presence_of_element_located() waits until the element is present in the DOM of the page
        # The By.XPATH argument specifies that we are locating the element using XPath
        price_element = wait.until(
            EC.presence_of_element_located((By.XPATH, PRODUCT_XPATH)))

        # Check if the price element is found
        if price_element is None:
            raise Exception("\n-- Product price element not found. --\n\n")

        # Get the text content of the price element
        price_text = price_element.text.strip()

        # Compile the regular expression pattern PRODUCT_PRICE_PATTERN and find all matches in the price_text
        # Extract the first match using [0], assuming there is at least one match
        cleaned_price = re.compile(
            PRODUCT_PRICE_PATTERN).findall(price_text)[0]

        # Convert the clean price text to float
        price = float(cleaned_price)

        # Close the web driver session
        chrome.quit()

        return price

    except Exception as e:
        # Handle any unexpected errors
        raise Exception(f"\n-- Error occurred: {e} --\n\n")


def get_product_price_bs4():
    """
    Function to scrape product price from a web page using Beautiful Soup.

    Returns:
        float: The price of the product.

    Raises:
        Exception: If any error occurs during the process.
    """
    try:
        # Prepare headers for the HTTP request
        headers = {
            'user-agent': get_random_user_agent(),
            'accept-language': 'en-US,en;q=0.9'
        }

        # Send HTTP GET request to the API
        response = requests.get(PRODUCT_URL, headers=headers)

        # Check if the response is successful
        response.raise_for_status()

        # Introduce a delay before parsing the HTML
        time.sleep(5)

        # Extract the HTML content from the response
        html_source = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')

        # Convert the BeautifulSoup object to an lxml etree object
        dom = etree.HTML(str(soup))

        # Use the XPath to find the price element
        price_element = dom.xpath(PRODUCT_XPATH)

        # Check if the price element is found
        if not price_element:
            raise Exception("\n-- Product price element not found. --\n\n")

        # Get the text content of the price element
        price_text = price_element[0].text.strip()

        # Compile the regular expression pattern PRODUCT_PRICE_PATTERN and find all matches in the price_text
        # Extract the first match using [0], assuming there is at least one match
        cleaned_price = re.compile(
            PRODUCT_PRICE_PATTERN).findall(price_text)[0]

        # Convert the clean price text to float
        price = float(cleaned_price)

        return price

    except requests.RequestException as e:
        # Handle errors related to HTTP request
        raise Exception(f"\n-- Error during HTTP request: {e} --\n\n")

    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"\n-- Error occurred: {e} --\n\n")


def main():

    try:
        product_price = get_product_price_bs4()

        # product_price = get_product_price_selenium()

        # print(product_price)

        subject, content = generate_price_update_email(PRODUCT_URL, PRODUCT_NAME, product_price)

        email_sending, message = send_email(subject, content)

        if email_sending:
            print("\n\n--- Email sent successfully. ---\n\n")
        else:
            print(f"\n\n--- {message} ---\n\n")


    except Exception as e:
        print(f"\n--- An error occured:  {e}---\n\n")


if __name__ == "__main__":
    main()
