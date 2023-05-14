import network, json, time
#import urequests as ureq


#==============================================================================
# Establishing a WiFi-connection from the ESP32 to the internet
#==============================================================================

# Read config file from FS and deserialise it as an object
with open('configsnoddis.json', 'r') as f:
    config = json.load(f)

# Check config.json has updated credentials
if config['ssid'] == 'Enter SSID':
    assert False, ("config.json has not been updated with your unique keys and data")

# Create WiFi connection and turn it on
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to WiFi router
print ("Connecting to WiFi: {}".format(config['ssid']))
wlan.connect(config['ssid'], config['ssid_password'])

# Wait until connection is established
while not wlan.isconnected():
    pass


#==============================================================================
# Implementing the OV API Seb has created
#==============================================================================

