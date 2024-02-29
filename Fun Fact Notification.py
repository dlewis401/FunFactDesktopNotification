# Importing requests to pull the random fact API & winonify for the notifications
import requests
from winotify import Notification

# This is the API configuration.
limit = 1 # Limit is needed in order to avoid overloading the API (to avoid being blocked from using it)
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit) # This is the URL to the API, and replaces the placeholder {} with the limit variable
fact_data = requests.get(api_url, headers={'X-Api-Key': 'rWHIMKCgoTlTLEMyUoqdOw==Zia23Xi8sOBtFPL3'}).text # This actually "grabs" the data of the API, with the API key 
fact_split = fact_data.split(":") # This splits the data into "Fact" and the fact
fact = fact_split[1].split('"') # This puts it as the fact alone, without the speech marks

# This setups the notification, with the app id, title, and message (being the fact), as the duration
factNotification = Notification(app_id="Fun Fact", title="Fun Fact:", msg=fact[1], duration="long")
factNotification.show() # This calls the notification so it shows up