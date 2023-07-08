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
    time.sleep(1

               #If the sensor value is 1000 or more than that then the sensor is not in the soil or sensor is disconnected. 
               #If the sensor value is more than 600 but less than 1000 then the soil is dry. 
               #If the sensor value is 370 to 600 then the soil is humid.
   #If the sensor value is less than 370 then the sensor in the water.
   

