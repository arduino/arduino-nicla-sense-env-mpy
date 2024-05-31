"""
Example of reading temperature and humidity from the Nicla Sense Env's HS4001 sensor.
"""

from arduino_nicla_sense_env import NiclaSenseEnv

def display_sensor_data(sensor):    

    if sensor.enabled:
        temperature = sensor.temperature
        if temperature is None:
            print("🌡 Temperature: N/A")
        else:
            print(f"🌡 Temperature: {temperature:.2f}°C")
        print(f"💧 Relative Humidity: {sensor.humidity:.2f}")
    else:
        print("🙅 Temperature sensor is disabled")

device = NiclaSenseEnv()

if device.connected:
    print("🔌 Device is connected")
    temperature_sensor = device.temperature_humidity_sensor
    display_sensor_data(temperature_sensor)
    # Optionally disable the sensor
    # temperature_sensor.enabled = False
else:
    print("🤷 Device could not be found. Please double check the wiring.")