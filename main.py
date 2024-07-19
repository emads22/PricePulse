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
from send_sms import send_sms
from app_utils import get_random_user_agent, generate_price_update_email, generate_price_update_sms
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

        # Introduce a delay before sending the request
        time.sleep(5)

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


def notify_price_change_email(product_url, product_name, new_price):
    """
    Generate email content for a price update and send the email.

    Args:
        product_url (str): The URL of the product.
        product_name (str): The name of the product.
        new_price (float): The new price of the product.

    Returns:
        None
    """
    # Generate the email subject and content with the price update information
    subject, content = generate_price_update_email(
        product_url, product_name, new_price)

    # Send the email with the price update information
    email_sending, error_message = send_email(subject, content)

    # Check if the email was sent successfully and print appropriate message
    if email_sending:
        print(f"\n--- Email notification sent successfully! ---\n")
    else:
        print(f"\n--- {error_message} ---\n")


def notify_price_change_sms(product_name, new_price):
    """
    Generate message content for a price update and send the SMS.

    Args:
        product_name (str): The name of the product.
        new_price (float): The new price of the product.

    Returns:
        None
    """
    # Generate the message content with the price update information
    content = generate_price_update_sms(product_name, new_price)

    # Send the SMS with the price update information
    sms_sending_status = send_sms(content)

    # Print the status of the SMS sending process
    print(f"\n--- {sms_sending_status} ---\n")


def main():
    """
    Main function to get product price and send notification whether via email or sms
    """

    # Initialize a dictionary to store old and new product prices
    product_price = {
        'old': 0,
        'new': 0
    }

    # Display logo or ASCII art
    print("\n\n\n\n", ASCII_ART, "\n\n")

    # Run this main function in a loop, pausing for 1 hour between each iteration
    while True:

        try:
            # Retrieve the product price using BeautifulSoup
            product_price['new'] = get_product_price_bs4()

            # Uncomment this if you want to use Selenium instead
            # product_price['new'] = get_product_price_selenium()

            # Print the new price for debugging purposes (optional)
            # print(product_price)

            # Check if the new price is different from the old price
            if product_price['new'] != product_price['old']:
                # Update the old price with the new price
                product_price['old'] = product_price['new']

                # Notify the user about the price change via email
                notify_price_change_email(
                    PRODUCT_URL, PRODUCT_NAME, product_price['new'])

                # Notify the user about the price change via sms
                notify_price_change_sms(PRODUCT_NAME, product_price['new'])

            else:
                print("\n--- Price has not changed. ---\n")

        except Exception as e:
            # Handle any exceptions that may occur during the process and print error message
            print(f"\n--- An error occurred:  {e} ---\n")

        print("\n\n--- Waiting for the next price check in 1 hour... ---\n\n")
        time.sleep(3600)


if __name__ == "__main__":
    main()
