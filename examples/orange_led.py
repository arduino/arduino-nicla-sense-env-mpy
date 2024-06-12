"""
This example shows how to control the orange LED on the Nicla Sense Env board.
"""

from arduino_nicla_sense_env import NiclaSenseEnv, IndoorAirQualitySensorMode
from time import sleep_ms

def pulse_led(led):
    """
    Pulses the LED.    
    """
    # Fade in
    for i in range(0, 255):
        led.brightness = i
        sleep_ms(10)
    
    # Fade out
    for i in range(255, -1, -1):
        led.brightness = i
        sleep_ms(10)

device = NiclaSenseEnv()

if device.connected:
    orange_led = device.orange_led

    print(f"🔢 Orange LED error status enabled: {orange_led.error_status_enabled}")
    print(f"💡 Orange LED brightness: {orange_led.brightness}")
    pulse_led(orange_led)

    # Enable sensor error indication on orange LED (LED should turn off if sensors are okay)
    orange_led.error_status_enabled = True
else:
    print("🤷 Device could not be found. Please double check the wiring.")
