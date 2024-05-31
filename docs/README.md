# 📖 Documentation

## ✨ Features

This library supports the complete API exposed by the Nicla Sense Env sensor board over I2C.

- 🌈 RGB LED control
- ⚪️ White LED control
- 💤 Board control (sleep, reset, factory reset)
- 🔧 Board configuration (e.g. changing the I2C address)
- 🏠 Indoor Air Quality Sensor control
    - Change mode (Power down, cleaning, Indoor Air quality, sulfur detection)
    - Detect sulfur
    - Measure odor intensity
    - Measure ethanol level
    - Measure TVOC
    - Measure CO2
    - Measure air quality
- 🌳 Outdoor Air Quality Sensor control
    - Change mode (Power down, cleaning, Outdoor Air quality)
    - Measure NO2
    - Measure O3
    - Measure air quality
- 🌡 Temperature/Humidity Sensor Control
    - Change mode (Power down, temperature/humidity)
    - Read temperature
    - Read humidity
- 📄 UART CSV output

## 💻 Usage

To use this library you can import the `arduino_nicla_sense_env` module along with the desired classes which give you access to the different sensor and actuator objects:

```python
from arduino_nicla_sense_env import NiclaSenseEnv

device = NiclaSenseEnv()

if device.connected:
    print("🔌 Device is connected")
    indoor_air_quality_sensor = device.indoor_air_quality_sensor
    # ...
    outdoor_air_quality_sensor = device.outdoor_air_quality_sensor
    # ...
    temperature_sensor = device.temperature_humidity_sensor
    # ...
    rgb_led = device.rgb_led
    # ...
    white_led = device.white_led
    # ...
```
Once the desired object is obtained you can call functions and query properties on these objects such as `temperature_sensor.temperature`.

## 👀 Examples

The following scripts are examples of how to use the Nicla Sense Env board with Python:

- [board_control.py](../examples/board_control.py): Shows how to print the device information of the Nicla Sense Env, how to disable sensors and how to reset the device or put it to sleep.
- [change_i2c_address.py](../examples/change_i2c_address.py): Demonstrates how to change the board's I2C address.
- [clean_sensors.py](../examples/clean_sensors.py): Shows how to clean the sensors of the Nicla Sense Env after unboxing / assembly.
- [data_logging.py](../examples/data_logging.py): Demonstrates how to log sensor data to a file.
- [factory_reset.py](../examples/factory_reset.py): Demonstrates how to perform a factory reset on the board.
- [indoor_air_quality.py](../examples/indoor_air_quality.py): Demonstrates how to read the indoor air quality data from the board's sensors.
- [outdoor_air_quality.py](../examples/outdoor_air_quality.py): Demonstrates how to read the outdoor air quality data from the board's sensors.
- [rgb_led.py](../examples/rgb_led.py): Demonstrates how to control the board's RGB LED.
- [temperature_humidity.py](../examples/temperature_humidity.py): Demonstrates how to read the temperature and humidity data from the board's sensors.
- [uart_read.py](../examples/uart_read.py): Shows how to read data from the UART port on the board when not connecting to it over I2C.
- [white_led.py](../examples/white_led.py): Demonstrates how to control the board's white LED.