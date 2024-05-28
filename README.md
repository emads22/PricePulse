# Product Price Tracker

## Overview
The Product Price Tracker Application is a versatile tool designed to track price fluctuations of any product on a website. Offering flexibility and convenience, users can select their desired product by providing its URL and XPath for the price element, enabling them to monitor prices with ease. The application conducts hourly price checks, ensuring timely updates, and notifies users via email and SMS according to their preferences.

## Features
- **Web Scraping Options**: Users can choose between using BeautifulSoup and Selenium for web scraping, allowing flexibility based on website requirements.
- **Customizable Product Selection**: Users can select any product by providing its URL and either XPath or CSS selector (functionality must be modified for CSS selector usage) for the price element.
- **Default Product**: The application showcases its functionality with the **`Bose Home Speaker 500 - Luxe Silver`**, available at [Antaki](https://www.antaki.com.lb/product/bose-home-speaker-500-luxe-silver/).
- **Hourly Price Checks**: The application checks for price changes hourly, ensuring timely notifications.
- **Email and SMS Notifications**: Users can configure email and SMS settings to receive notifications about price changes.
- **Receiver Customization**: Users can specify receiver email addresses and phone numbers for notifications.
- **SMS Service**: By default, the application uses Nexmo (Vonage) for sending SMS notifications, but users are free to choose other SMS service providers as per their preference.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as email credentials, SMS API key, product URL, and either XPath or CSS selector in `constants.py`.
5. Ensure the ChromeDriver executable is downloaded and placed in the appropriate directory (`chromedriver-win64`).
6. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. The application will periodically check for price updates based on the specified time interval and notify users via email and SMS.
3. Customize product selection, receiver details, scraping options, and selector type as needed in the `constants.py` file.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.