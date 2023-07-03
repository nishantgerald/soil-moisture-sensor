from machine import ADC
import json
import time
import urequests
import ujson

# Initialize the ADC
adc = ADC(0)

url = "http://sensor.nishantgerald.com/api/sensor"

def map_value(value, in_min, in_max, out_min, out_max):
    # Map a value from one range to another
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    # Read the value from the ADC
    moisture_value = adc.read()

    # Map the value to a moisture percentage and invert it
    moisture_percentage = map_value(moisture_value, 400, 850, 100, 0)
    
    data = {
        "value": moisture_percentage
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    
    print(response.text)
    
    # print("Soil moisture level (%): ", moisture_percentage)
    print("Soil moisture level (%): ", moisture_percentage)
    time.sleep(2)