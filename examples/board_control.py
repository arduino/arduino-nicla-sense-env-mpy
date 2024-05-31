"""
This example shows how to print the device information of the Nicla Sense Env, 
how to disable all sensors and how to reset the device or put it to sleep.
"""

from arduino_nicla_sense_env import NiclaSenseEnv
from time import sleep

device = NiclaSenseEnv()

if device.connected:
    print(f"🔌 Device (0x{device.device_address:x}) connected.")
    print(f"🔢 Serial number: {device.serial_number}")
    print(f"🔢 Product ID: {device.product_id}")
    print(f"🔢 Software revision: {device.software_revision}")
    print(f"🔢 Baud rate: {device.uart_baud_rate}")
    print(f"🔢 CSV delimiter: {device.csv_delimiter}")    
    print(f"🔧 Debugging enabled: {device.debugging_enabled}")
    print(f"🔧 CSV output enabled: {device.uart_csv_output_enabled}")

    # Enable debugging and CSV output if desired
    # device.debugging_enabled = True
    # device.uart_csv_output_enabled = True

    # Disable all sensors
    print("🙅 Disabling all sensors...")
    device.temperature_humidity_sensor.enabled = False
    device.indoor_air_quality_sensor.enabled = False
    device.outdoor_air_quality_sensor.enabled = False

    print(f"🔧 Temperature sensor enabled: {device.temperature_humidity_sensor.enabled}")
    print(f"🔧 Indoor air quality sensor enabled: {device.indoor_air_quality_sensor.enabled}")
    print(f"🔧 Outdoor air quality sensor enabled: {device.outdoor_air_quality_sensor.enabled}")
    
    # Reset sensors to default state by resetting the device
    print("🔄 Resetting device...")
    device.reset()
    sleep(2)

    print(f"🔧 Temperature sensor enabled: {device.temperature_humidity_sensor.enabled}")
    print(f"🔧 Indoor air quality sensor enabled: {device.indoor_air_quality_sensor.enabled}")
    print(f"🔧 Outdoor air quality sensor enabled: {device.outdoor_air_quality_sensor.enabled}")

    # Go to sleep. Device can only be woken up by pressing the reset button
    print("💤 Going to sleep...")
    device.deep_sleep()
else:
    print("🤷 Device could not be found. Please double check the wiring.")
    