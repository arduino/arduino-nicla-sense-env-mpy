"""
This example shows how to control the RGB LED on the Nicla Sense Env board.
"""

from arduino_nicla_sense_env import NiclaSenseEnv, IndoorAirQualitySensorMode
from time import sleep_ms

def pulse_led(led):
    """
    Pulses the LED from off to full brightness and back to off.
    """
    print(f"🌈 RGB values: {rgb_led.color}")

    for i in range(0, 256):
        led.brightness = i
        sleep_ms(2)
    for i in range(255, -1, -1):
        led.brightness = i
        sleep_ms(2)

def pulse_colors(led):
    """
    Pulses the LED through the colors red, green, blue and white.
    """
    # Brightness can also be set via 4th tuple element
    led.color = (255, 0, 0, 255)
    pulse_led(led)
    led.color = (0, 255, 0)
    pulse_led(led)
    led.color = (0, 0, 255)
    pulse_led(led)
    led.color = (255, 255, 255)
    pulse_led(led)

device = NiclaSenseEnv()

if device.connected:
    rgb_led = device.rgb_led
    
    print(f"💡 RGB LED brightness: {rgb_led.brightness}")
    pulse_colors(rgb_led)

    # Re-enable indoor air quality indication on RGB LED
    iaq_mode = device.indoor_air_quality_sensor.mode
    if iaq_mode == IndoorAirQualitySensorMode.INDOOR_AIR_QUALITY or iaq_mode == IndoorAirQualitySensorMode.INDOOR_AIR_QUALITY_LOW_POWER:
        print("🏠 Enabling indoor air quality indication on RGB LED")
        # Set indoor air quality LED to full brightness
        rgb_led.enable_indoor_air_quality_status(255)
else:
    print("🤷 Device could not be found. Please double check the wiring.")
