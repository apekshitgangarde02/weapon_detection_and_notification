import geocoder

import datetime #for reading present date
from playsound import playsound
import time
from plyer import notification #for getting notification on your PC

import requests
import winsound



# ------------Location ----------
g = geocoder.ip('me')
g = g.latlng
lat = g[0]
lon = g[1]
print(lat, " " , lon)

# --------------Send SMS -------------


url = "https://www.fast2sms.com/dev/bulkV2"

mob_number = "9867103671"
querystring = {"authorization":"iEXqmu7POV8MwgbFzCHj0xQUIBTnL6eKGv9yAWNJh2fRDpSoZ1PDFfqyde1TU3Ci2nmkHS6GO9bYjgrp","message":"Weapon detected!\nFollowing are aproximate location cordinates: \nLatitude = " + str(lat) + " Longitude = " + str(lon) + "\nTime: " + str(time.ctime()),"language":"english","route":"q","numbers": mob_number}
headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# ------------------- Desktop Alert ---------------



notification.notify(
    title = "Threat Detected!",
    message = str(time.ctime()),  
    app_icon = "danger.ico",
    timeout  = 20
)


# Play Sound 
# playsound('Alert.wav)

filename = 'alert.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)



