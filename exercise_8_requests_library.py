
# Exercise: Using the Requests Library

import requests

# URL to fetch
url = "http://www.tcpipguide.com/"

# Send GET request
response = requests.get(url)

# Print content
print(response.content.decode())
