"""
Example of reading various sensor properties from the Nicla Sense Env's indoor air quality sensor ZMOD4410.
To read sulfur odor and odor intensity, the sensor mode must be changed.
"""

from arduino_nicla_sense_env import NiclaSenseEnv, IndoorAirQualitySensorMode

def display_sensor_data(sensor):    

    if sensor.enabled:
        iaq_mode = sensor.mode
        print(f"🔧 Indoor air quality sensor mode: {sensor.mode_string}")

        if iaq_mode == IndoorAirQualitySensorMode.SULFUR:
            print(f"👃 Sulfur odor: {sensor.sulfur_odor}")
            if sensor.sulfur_odor:
                print(f"👃 Odor intensity: {sensor.odor_intensity:.2f}")    

        if iaq_mode == IndoorAirQualitySensorMode.INDOOR_AIR_QUALITY or iaq_mode == IndoorAirQualitySensorMode.INDOOR_AIR_QUALITY_LOW_POWER:
            print(f"🏠 Indoor air quality value: {sensor.air_quality:.2f}")
            print(f"🏠 Indoor air quality: {sensor.air_quality_interpreted}")
            print(f"🏠 Relative indoor air quality: {sensor.relative_air_quality:.2f}")        
            print(f"🌬 CO2 (ppm): {sensor.co2:.2f}")
            print(f"🌬 TVOC (mg/m3): {sensor.tvoc:.2f}")
            print(f"🍺 Ethanol (ppm): {sensor.ethanol:.2f}")
    else:
        print("🙅 Indoor air quality sensor is disabled")

device = NiclaSenseEnv()

if device.connected:
    print("🔌 Device is connected")
    indoor_air_quality_sensor = device.indoor_air_quality_sensor

    # Please note that it may take some time for the sensor to deliver the first data.
    indoor_air_quality_sensor.mode = IndoorAirQualitySensorMode.INDOOR_AIR_QUALITY
    display_sensor_data(indoor_air_quality_sensor)

    # Set indoor air quality sensor mode to sulfur odor (default is indoor air quality)    
    # After switching modes you may need to wait some time before the sensor delivers the first data.
    # indoor_air_quality_sensor.mode = IndoorAirQualitySensorMode.SULFUR
    # display_sensor_data(indoor_air_quality_sensor)

    # Optionally disable the sensor
    # indoor_air_quality_sensor.enabled = False
else:
    print("🤷 Device could not be found. Please double check the wiring.")