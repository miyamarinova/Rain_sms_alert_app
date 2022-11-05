import requests
from twilio.rest import Client

account_sid = "AC8cc0f7e59903545250d78e940fb2de58"
account_token = "50e1343af70d6bc84e1767d580d48e07"

weather_id_list = []
api_key = "f2beaf96c1f5256c98d3980f037c9f87"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 51.759050,
    "lon": 19.458600,
    "appid": api_key
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather_id in weather_data['list'][0:12]:
    if int(weather_id['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, account_token)
    message = client.messages \
                .create(
                     body="Looks like you'll need an umbrella if you are going to London ☔️💋",
                     from_='+19804009361',
                     to='+12025107305'
                 )




