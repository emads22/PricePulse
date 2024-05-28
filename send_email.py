import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from constants import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, GMAIL_HOST, GMAIL_PORT


def send_email(subject, body,
               sender=EMAIL_SENDER, password=EMAIL_PASSWORD, receiver=EMAIL_RECEIVER,
               host=GMAIL_HOST, port=GMAIL_PORT):
    """
    Send an email using the SMTP protocol with Gmail's SMTP server.

    Args:
        subject (str): The subject line of the email.
        body (str): The HTML-formatted body of the email.
        sender (str, optional): The sender's email address. Defaults to EMAIL_SENDER.
        password (str, optional): The sender's email account password. Defaults to EMAIL_PASSWORD.
        receiver (str, optional): The recipient's email address. Defaults to EMAIL_RECEIVER.
        host (str, optional): The SMTP server host. Defaults to GMAIL_HOST.
        port (int, optional): The SMTP server port. Defaults to GMAIL_PORT.

    Returns:
        tuple: A tuple containing a boolean indicating success or failure and an optional error message.
    """
    # Create a MIMEMultipart message (Multipurpose Internet Mail Extensions)
    message = MIMEMultipart()

    # Set the sender, receiver, and subject of the email
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    # Create a MIMEText object to represent the email body
    mimetext = MIMEText(body, 'html')

    # Attach the MIMEText object to the MIMEMultipart message
    message.attach(mimetext)

    try:
        # Establish connection with Gmail SMTP server using 'with' statement
        with smtplib.SMTP(host, port) as server:
            # Initiate connection with the server
            server.ehlo()

            # Initiate TLS encryption
            server.starttls()

            # Log in to the sender's email account
            server.login(sender, password)

            # Send the email after converting the message MIMEMultipart object to string
            server.sendmail(sender, receiver, message.as_string())

            # Return success with no error message
            return True, None
    except Exception as err:
        # Return failure along with the error message
        error_message = f"An error occurred while sending the email: {err}"
        return False, error_message
