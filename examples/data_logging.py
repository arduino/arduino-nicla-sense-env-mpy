"""
This example shows how to log sensor data to a file.
It prints the temperature to the console and writes it to a file.
It uses the RTC to add a (UTC/GMT) timestamp to the data which is updated from an NTP server.
"""

import errno
from time import sleep, gmtime
from ntptime import settime
from machine import Pin
from arduino_nicla_sense_env import NiclaSenseEnv

LOGGING_INTERVAL = 60 # seconds
LOG_FILE_NAME = "data.txt"
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Please note that this example uses LED.value(0) to turn on the LED.
# If your board's LED is not active LOW, you will need to change this to LED.value(1)
ACTIVITY_LED = Pin("LED_BLUE", Pin.OUT) # Adjust pin to match your board's LED pin
ACTIVITY_LED.value(1) # turn off LED
ERROR_LED = Pin("LED_RED", Pin.OUT) # Adjust pin to match your board's LED pin
ERROR_LED.value(1) # turn off LED

def connect_wifi(ssid, password):
	import network
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		print('Connecting to network...')
		sta_if.active(True)
		sta_if.connect(ssid, password)
		while not sta_if.isconnected():
			print(".", end="")
			sleep(1)
		print("")
	print('Network config:', sta_if.ifconfig())

def current_time():
    now = gmtime()
    return f"{now[2]}.{now[1]}.{now[0]} {now[3]:02d}:{now[4]:02d}:{now[5]:02d}"

def blink_led(led, times=1, delay=0.2):
    for i in range(times):
        led.value(0)
        sleep(delay)
        led.value(1)
        sleep(delay)

def read_data(filename):    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        if e.errno == errno.ENOENT:
            print("No existing data file found.")
        else:
            print(f"Error reading file: {filename}. Error: {e}")
        return None

def log_data(filename, data):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
    except:
        print('Error writing to file: ' + filename)
        ERROR_LED.value(0) # turn on LED to indicate error
        while True:
            pass

print("Reading data from file...")
data = read_data(LOG_FILE_NAME)
if data is not None:
    print(data)

# Update RTC from NTP server
ACTIVITY_LED.value(0) # turn on LED to indicate activity
connect_wifi(WIFI_SSID, WIFI_PASSWORD)
settime() # Update RTC from NTP server
ACTIVITY_LED.value(1) # turn off LED

device = NiclaSenseEnv()
if not device.connected:
    print("Not connected")
    ERROR_LED.value(0) # turn on LED to indicate error
else:
    print("Logging data...")
    log_data(LOG_FILE_NAME, f"Logging started at {current_time()}")

    while True:
        blink_led(ACTIVITY_LED, 3)
        temperature = device.temperature_humidity_sensor.temperature
        if temperature is not None:
            timestamp = current_time()
            formatted_temperature = f"{timestamp} 🌡️ {temperature:.2f} °C"
            print(formatted_temperature)
            log_data(LOG_FILE_NAME, formatted_temperature)
        sleep(LOGGING_INTERVAL)