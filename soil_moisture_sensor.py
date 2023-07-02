from machine import ADC
import time

# Initialize the ADC
adc = ADC(0)

def map_value(value, in_min, in_max, out_min, out_max):
    # Map a value from one range to another
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    # Read the value from the ADC
    moisture_value = adc.read()

    # Map the value to a moisture percentage and invert it
    moisture_percentage = map_value(moisture_value, 450, 850, 100, 0)
    
    print("Soil moisture level (%): ", moisture_percentage)
    time.sleep(1)
