SMS Gateway API Client
=====================

This Python script sends an SMS using the SMS Gateway Hub API.

**Prerequisites**

* An API key from SMS Gateway Hub
* A sender ID from SMS Gateway Hub
* A mobile number to send the SMS to

**Usage**

1. Replace `YourAPIkey` with your actual API key from SMS Gateway Hub.
2. Replace `TESTIN` with your actual sender ID from SMS Gateway Hub.
3. Replace `YOUR MESSAGE HERE` with the message you want to send.
4. Replace `91989xxxxxxx` with the mobile number you want to send the SMS to. You can add multiple numbers separated by commas.
5. Run the script using Python (e.g., `python script.py`).

**Script Explanation**

The script uses the `requests` library to send a POST request to the SMS Gateway Hub API. The API endpoint is constructed using the `urllib.parse` library to encode the message content.

The script disables SSL verification using `verify=False` to avoid SSL certificate issues.

The response from the API is printed to the console.

**Note**

* Make sure to replace the placeholders with your actual values.
* This script assumes that you have a valid API key and sender ID from SMS Gateway Hub.
* This script sends a single SMS to a single mobile number. If you want to send SMS to multiple numbers, you'll need to modify the script accordingly.
