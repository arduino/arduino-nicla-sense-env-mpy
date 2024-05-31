"""
This example demonstrates how to clean the sensors of the Nicla Sense Env after unboxing / assembly.

The cleaning mode performs a thermal cleaning cycle of the MOx element. It can eliminate some light pollution 
residues from production and packaging and improves the stabilization processes in the sensor. 
The function heats up the sensor to allow thermal desorption and catalytic combustion of the residues. 
The cleaning cycle can be executed only once in the sensor lifetime and shall be started after product assembly. 
Please ensure cleaning was completed before power-off/reset and do not interrupt while cleaning.
The cleaning procedure takes 1 minute (blocking).
"""

from arduino_nicla_sense_env import NiclaSenseEnv
from arduino_nicla_sense_env import IndoorAirQualitySensorMode, OutdoorAirQualitySensorMode
import time

device = NiclaSenseEnv()

if device.connected:
    print("🔌 Device is connected")
    indoor_air_quality_sensor = device.indoor_air_quality_sensor
    outdoor_air_quality_sensor = device.outdoor_air_quality_sensor

    print("🧹 Cleaning indoor air quality sensor, do not interrupt or power off!")
    indoor_air_quality_sensor.mode = IndoorAirQualitySensorMode.CLEANING
    time.sleep(90) # Cleaning takes 60 seconds but we add some extra time for safety
    print("🧹 Cleaning outdoor air quality sensor, do not interrupt or power off!")
    outdoor_air_quality_sensor.mode = OutdoorAirQualitySensorMode.CLEANING
    time.sleep(90) # Cleaning takes 60 seconds but we add some extra time for safety
    print("✅ Cleaning completed. Device will reset in 10 seconds.")
    print("🔄 Resetting in ", end="")

    for i in range(10, 0, -1):
        print(f"{i}...", end="")
        time.sleep(1)
    
    device.reset()
else:
    print("🤷 Device could not be found. Please double check the wiring.")