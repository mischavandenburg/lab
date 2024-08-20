import requests
import os

# from rich import print

token = os.getenv("OURA_TOKEN")

# Sleep

# url = "https://api.ouraring.com/v2/usercollection/sleep"
# params = {"start_date": "2024-08-18", "end_date": "2024-08-20"}
# headers = {"Authorization": f"Bearer {token}"}
# response = requests.request("GET", url, headers=headers, params=params)
# print(response.text)


url = "https://api.ouraring.com/v2/usercollection/heartrate"
params = {"start_date": "2024-08-18", "end_date": "2024-08-20"}
headers = {"Authorization": f"Bearer {token}"}
response = requests.request("GET", url, headers=headers, params=params)
print(response.text)
