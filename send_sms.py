import vonage
from constants import NEXMO_API_KEY, NEXMO_API_SECRET, SMS_SENDER, SMS_RECEIVER


def send_sms_nexmo(message, sender=SMS_SENDER, receiver=SMS_RECEIVER,
                   key=NEXMO_API_KEY, secret=NEXMO_API_SECRET):
    """
    Send an SMS message using the Nexmo (Vonage) API.

    Args:
        message (str): The text message to send.
        sender (str, optional): The sender ID or phone number. Defaults to SMS_SENDER.
        receiver (str, optional): The recipient's phone number. Defaults to SMS_RECEIVER.
        key (str, optional): The Nexmo API key. Defaults to NEXMO_API_KEY.
        secret (str, optional): The Nexmo API secret. Defaults to NEXMO_API_SECRET.

    Returns:
        str: The status of the message delivery.
    """
    # Initialize the Nexmo client with the API credentials
    client = vonage.Client(key=key, secret=secret)

    # Create an Sms object to send messages
    sms = vonage.Sms(client)

    # Send the SMS message
    responseData = sms.send_message(
        {
            "from": sender,    # Sender ID or phone number
            "to": receiver,    # Recipient's phone number
            "text": message,   # Text message content
        }
    )

    # Check the response status
    if responseData["messages"][0]["status"] == "0":
        send_status = "Message sent successfully."
    else:
        send_status = f"Message failed with error: {
            responseData['messages'][0]['error-text']}"

    return send_status
