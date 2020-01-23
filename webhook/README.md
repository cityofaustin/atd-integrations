# Security Note

**IMPORTANT: Do not push code with passwords, access keys, api tokens or any other sensitive information.**


# Webhook Integration (Effort Level: Low)

Basically what a webhook does, it takes a json document and submits it to another website. Our webhook integrator will consist of a list of HTTP endpoints and HTTP methods, and the webhook will submit the payload to that list of webhooks. This python script should use the [requests http library](https://realpython.com/python-requests/). You must write the code in Python 3.6 or greater.

Example webhook configuration:

```json
{
    "webhooks": [
        {
            "description": "This is our webhook test 1",
            "endpoint": "https://myendpoint.com/",
            "method": "POST"
        },
        {
            "description": "This is different webhook",
            "endpoint": "https://myendpoint.com/",
            "method": "GET"
        }
	]
}
```

Our webhook will iterate through each of the two webhooks and:

1. Checks or assumes the endpoint is a valid HTTP URL.
2. Validates the method, it has to be either `POST` or `GET` and nothing else.
3. Allows to add custom HTTP Headers
4. Sends a json payload to each of those endpoints.
5. Reports problems via a helper function called `report_error`


## Example Payload:

You can assume this function will provide the payload as a python dictionary:

   ```python
   def get_payload():
       """
       Returns a python dictionary object with the parsed payload
       :return: dict - the parsed content of the file
       """
       return requests.get("https://raw.githubusercontent.com/cityofaustin/atd-integrations/master/sample.json").json()
   ```
   ** Please note that you are going to have to install the requests library for python: https://requests.readthedocs.io/en/master/



## Error Reporting

You can assume there will be a function called `report_error`, while it is not implemented as shown here, you can use this function to output errors to the terminal.

```python
def report_error(message):
    """
        This function prints unto the terminal a message
        param message: string - The message we want to display in the terminal
    """ 
        print(f"There is a problem submitting to a webhook: {message}")
```



## Example Guide

The following script was taken from the requests library:

```python
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
```
