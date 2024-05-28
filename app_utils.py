import random
from constants import USER_AGENT_LIST


def construct_proxy_string(proxy_address, proxy_port):
    """
    Function to construct a proxy string.

    Args:
        proxy_address (str): The proxy address.
        proxy_port (str): The proxy port.

    Returns:
        str: The constructed proxy string.
    """
    proxy = f'{proxy_address}:{proxy_port}'
    return proxy


def get_random_user_agent():
    """
    Function to generate a random user agent from a list of user agent strings.

    Returns:
        str: A randomly selected user agent string.
    """
    return random.choice(USER_AGENT_LIST)


def generate_price_update_email(product_url, product_name, product_price):
    """
    Generate an email content for notifying price update of a product.

    Args:
        product_url (str): The URL of the product.
        product_name (str): The name of the product.
        product_price (str): The updated price of the product.

    Returns:
        str: The email content.
    """
    product_name = product_name.title()

    subject = f"{product_name} price has changed!"

    content = f"""<h2><em>{product_name}</em> price update</h2>
    <p>The price of <strong>{product_name}</strong>, has been updated.</p>
    <p>It currently stands at <strong>${product_price}</strong>.</p>
    <p>As per the data available at <span style="text-decoration: underline;">{product_url}</span></p>"""

    return subject, content


def generate_price_update_sms(product_name, product_price):
    """
    Generate an SMS content for notifying the price update of a product.

    Args:
        product_name (str): The name of the product.
        product_price (str): The updated price of the product.

    Returns:
        str: The SMS content.
    """
    # Format the SMS content
    content = f'"{product_name.title()}" price update. It currently stands at "${
        product_price}".'

    return content
