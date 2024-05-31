"""
This example shows how to control the white LED on the Nicla Sense Env board.
"""

from arduino_nicla_sense_env import NiclaSenseEnv, IndoorAirQualitySensorMode
from time import sleep_ms

def pulse_led(led):
    """
    Pulses the LED.    
    """
    # Fade in
    for i in range(0, 64):
        led.brightness = i
        sleep_ms(10)
    
    # Fade out
    for i in range(63, -1, -1):
        led.brightness = i
        sleep_ms(10)

device = NiclaSenseEnv()

if device.connected:
    white_led = device.white_led

    print(f"🔢 White LED error status enabled: {white_led.error_status_enabled}")
    print(f"💡 White LED brightness: {white_led.brightness}")
    pulse_led(white_led)

    # Enable sensor error indication on white LED (LED should turn off if sensors are okay)
    white_led.error_status_enabled = True
else:
    print("🤷 Device could not be found. Please double check the wiring.")
