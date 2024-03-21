import requests
from twilio.rest import Client

OWM_Endpoint = "api.openweathermap.org/data/2.5/forecast"
api_key = "df2f52da78306b0f5ca285739505d6b6"
account_sid = "ACa7df06f8034a0ddc8fa2d35e5be3d41f"
auth_token = "0a5c3dd099e26327beb77d456dc1cb38"

weather_params = {
    "lat": 24.05,
    "lon": 81.3833,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?"
                        "lat=44.34&lon=10.99&appid=df2f52da78306b0f5ca285739505d6b6",
                        params=weather_params)
response.raise_for_status()

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
# Check the code you are getting from open weather api, and if the code is less than 700 than bring an umbrella
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "It's going to rain today. Remember to bring an ☂️",
        from_= '+5642161321',
        to= "Your verified number"
    )
    print(message.status)


