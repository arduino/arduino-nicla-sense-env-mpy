"""
Example of reading various sensor properties from the Nicla Sense Env's outdoor air quality sensor ZMOD4510.
"""

from arduino_nicla_sense_env import NiclaSenseEnv, OutdoorAirQualitySensorMode

def display_sensor_data(sensor):    

    if sensor.enabled:
        print(f"🔧 Outdoor air quality sensor mode: {sensor.mode_string}")
        print(f"🌳 Outdoor air quality value: {sensor.air_quality_index}")
        print(f"🌳 Outdoor air quality: {sensor.air_quality_index_interpreted}")
        print(f"🌳 Fast outdoor air quality index: {sensor.fast_air_quality_index}")
        print(f"🌳 NO2 (ppb): {sensor.no2:.2f}")
        print(f"🌳 O3 (ppb): {sensor.o3:.2f}")
    else:
        print("🙅 Outdoor air quality sensor is disabled")

device = NiclaSenseEnv()

if device.connected:
    print("🔌 Device is connected")
    outdoor_air_quality_sensor = device.outdoor_air_quality_sensor

    # Enable outdoor air quality sensor (disabled by default)
    # Please note that it may take some time for the sensor to deliver the first data
    # Use set_enabled(True, persist=True) make the change persistent
    outdoor_air_quality_sensor.enabled = True
    display_sensor_data(outdoor_air_quality_sensor)

else:
    print("🤷 Device could not be found. Please double check the wiring.")