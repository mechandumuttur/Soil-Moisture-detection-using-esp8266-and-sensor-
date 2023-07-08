import machine
import time

# Set up ADC pin
adc = machine.ADC(0)

# Define soil moisture threshold
threshold = 100
# Loop forever
while True:
    # Read soil moisture level
    soil_moisture = adc.read()
    print(soil_moisture)
    # Check soil moisture level
    if soil_moisture < threshold:
        print('Soil is dry!')
    else:
        print('Soil is moist.')

    # Wait for 1 second
    time.sleep(1)
   

