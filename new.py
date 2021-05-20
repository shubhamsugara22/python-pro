import requests
import json
# response = requests.get(
#     "https://cdn-api.co-vin.in/api/v2/admin/location/districts/09")
# print(response.status_code)

# print(response.json())


response = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=150&date=06-05-2021")
print(response.json())
