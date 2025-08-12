import requests
from datetime import datetime
    
my_lat = 51.507351
my_long = -0.127758

res = requests.get("http://api.open-notify.org/iss-now.json")
res.raise_for_status()
data = res.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

def isNear():
    if abs(my_lat - iss_lat) < 5 and abs(my_long - iss_long) < 5:
        return True
    
# sunrise = data["sunrise"]
# sunset = data["sunset"]

# time = datetime.now()

# sunrise = sunrise.split("T")[1].split(":")[0]
# print(sunrise)
# print(time)
