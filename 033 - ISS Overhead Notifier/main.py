import datetime as dt
import requests
import mt_email
import credentials
from pytz import utc

ISS_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_URL = "https://api.sunrise-sunset.org/json"
SUNRISE_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"

MY_LOCATION = {
    "lat": 1.357107,
    "lng": 103.8194992
}
LOCATION_THRESHOLD = 5.0

sender_email = credentials.EMAIL
sender_password = credentials.APP_PASSWORD


def get_iss_position() -> dict:
    response = requests.get(url=ISS_URL)
    response.raise_for_status()

    data = response.json()["iss_position"]
    return {
        "lat": float(data["latitude"]),
        "lng": float(data["longitude"])
    }


def get_sun_data(position: tuple) -> dict:

    parameters = {
        "lat": position["lat"],
        "lng": position["lng"],
        "formatted": 0
    }

    response = requests.get(url=SUNRISE_URL, params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_time = dt.datetime.strptime(sunrise, SUNRISE_DATE_FORMAT)
    sunset_time = dt.datetime.strptime(sunset, SUNRISE_DATE_FORMAT)

    return {
        "sunrise": sunrise_time,
        "sunset": sunset_time
    }


def is_position_near_me(position) -> bool:
    is_lat_in_range = (position["lat"] - LOCATION_THRESHOLD) < position["lat"] < (
        position["lat"] + LOCATION_THRESHOLD)
    is_lng_in_range = (position["lat"] - LOCATION_THRESHOLD) < position["lat"] < (
        position["lat"] + LOCATION_THRESHOLD)
    return is_lat_in_range and is_lng_in_range


def is_night_at(position: dict) -> bool:
    sun_data = get_sun_data(position)
    # Compare using next day's sunrise
    sunrise = sun_data["sunrise"] + dt.timedelta(days=1)
    time_now = utc.localize(dt.datetime.now())
    return sun_data["sunset"] > time_now > sunrise


def main():
    iss_position = get_iss_position()
    if is_position_near_me(iss_position):
        if is_night_at(iss_position):
            subject = "The ISS is above you!"
            message = "The ISS is currently above you in the night sky, look up!"
            mt_email.send_email(sender_email=sender_email, sender_password=sender_password,
                                receiver_email=sender_email, subject=subject, message=message)
        else:
            print("It's not night yet, the ISS is not visible.")


main()
